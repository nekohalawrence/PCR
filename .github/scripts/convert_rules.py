import os
import yaml
import datetime
import re

# 配置
SOURCE_DIR = 'agency-resource/rule/yaml'
TARGET_DIR = 'agency-resource/rule/list'
REPO_NAME = os.environ.get('GITHUB_REPOSITORY', 'nekohalawrence/PCR') # 默认值用于本地测试
BRANCH_NAME = 'main' # 假设主分支为 main

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"创建目录: {directory}")

def get_stats(payload):
    """统计规则类型数量"""
    stats = {}
    for rule in payload:
        # 假设规则格式为 "TYPE,Value,..."
        parts = rule.split(',')
        if parts:
            rule_type = parts[0].strip()
            stats[rule_type] = stats.get(rule_type, 0) + 1
    return stats

def generate_header(original_content, filename_no_ext, stats):
    """生成新的文件头"""
    today = datetime.datetime.now().strftime('%Y%m%d')
    
    # 提取原始头部注释（保留 name, content, repo 等信息）
    # 我们不仅要提取，还要更新其中的 update_date 和 update_url
    lines = original_content.splitlines()
    new_header_lines = []
    
    # 定义需要动态生成的统计部分标记
    in_stats_block = False
    
    # 基础头部处理
    has_update_date = False
    has_update_url = False
    
    for line in lines:
        stripped = line.strip()
        
        # 停止读取到 yaml payload 的位置
        if stripped.startswith('payload:'):
            break
            
        # 跳过旧的统计块（我们稍后会重新生成）
        if stripped == '# 规则计数':
            in_stats_block = True
            continue
        if in_stats_block and stripped.startswith('#') and ':' in stripped and not stripped.startswith('# name') and not stripped.startswith('# content'):
            # 这是一个简单的启发式方法来跳过旧的统计行
            continue
        else:
            in_stats_block = False

        # 更新日期
        if stripped.startswith('# update_date:'):
            new_header_lines.append(f'# update_date: {today}')
            has_update_date = True
            continue
            
        # 更新 URL
        if stripped.startswith('# update_url:'):
            new_url = f'https://raw.githubusercontent.com/{REPO_NAME}/{BRANCH_NAME}/agency-resource/rule/list/{filename_no_ext}.list'
            new_header_lines.append(f'# update_url: {new_url}')
            has_update_url = True
            continue

        # 保留其他注释行
        if stripped.startswith('#'):
            new_header_lines.append(line)

    # 如果原文件没有这些字段，追加上去（可选）
    if not has_update_date:
        new_header_lines.append(f'# update_date: {today}')
    if not has_update_url:
        new_url = f'https://raw.githubusercontent.com/{REPO_NAME}/{BRANCH_NAME}/agency-resource/rule/list/{filename_no_ext}.list'
        new_header_lines.append(f'# update_url: {new_url}')

    # 插入新的统计块
    new_header_lines.append('')
    new_header_lines.append('# 规则计数')
    for r_type, count in sorted(stats.items()):
        new_header_lines.append(f'# {r_type}: {count}')
    new_header_lines.append('')

    return "\n".join(new_header_lines)

def process_file(filename):
    source_path = os.path.join(SOURCE_DIR, filename)
    target_filename = os.path.splitext(filename)[0] + '.list'
    target_path = os.path.join(TARGET_DIR, target_filename)

    print(f"正在处理: {filename} -> {target_filename}")

    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content_str = f.read()
            
        # 解析 YAML payload
        # 为了避免头部注释干扰 yaml 解析，我们可以只解析 payload 部分，或者忽略 parse 错误
        # 这里使用一种简单的方法：找到 payload: 并解析其后的内容
        if 'payload:' not in content_str:
            print(f"警告: {filename} 中未找到 payload，跳过。")
            return

        # 使用 PyYAML 安全加载
        try:
            yaml_content = yaml.safe_load(content_str)
        except yaml.YAMLError:
            # 如果文件包含非标准注释导致解析失败，尝试只截取 payload 部分
            split_content = content_str.split('payload:')
            yaml_payload_str = 'payload:' + split_content[1]
            yaml_content = yaml.safe_load(yaml_payload_str)

        payload = yaml_content.get('payload', [])
        if not payload:
            print(f"信息: {filename} payload 为空。")
            payload = []

        # 1. 计算统计
        stats = get_stats(payload)

        # 2. 生成头部
        header_text = generate_header(content_str, os.path.splitext(filename)[0], stats)

        # 3. 组合最终内容
        final_content = header_text + "\n" + "\n".join(payload) + "\n"

        # 4. 检查内容变更 (幂等性检查)
        if os.path.exists(target_path):
            with open(target_path, 'r', encoding='utf-8') as f_existing:
                existing_content = f_existing.read()
            
            # 如果内容（忽略两端空白）一样，则不写入
            if existing_content.strip() == final_content.strip():
                print(f"跳过: {target_filename} 内容未变更。")
                return

        # 5. 写入文件
        with open(target_path, 'w', encoding='utf-8') as f_out:
            f_out.write(final_content)
        print(f"成功写入: {target_path}")

    except Exception as e:
        print(f"错误: 处理 {filename} 时失败: {e}")

def main():
    # 检查源目录是否存在
    if not os.path.exists(SOURCE_DIR):
        print(f"错误: 源目录 {SOURCE_DIR} 不存在。")
        exit(1)

    ensure_dir(TARGET_DIR)

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(('.yaml', '.yml'))]
    
    if not files:
        print("未找到 YAML 文件。")
        return

    for file in files:
        process_file(file)

if __name__ == '__main__':
    main()
