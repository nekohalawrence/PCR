import os
import yaml
import datetime
import re

# --- 配置区域 ---
SOURCE_DIR = 'rule/yaml'
TARGET_DIR = 'rule/list'

# 动态获取仓库信息
REPO_NAME = os.environ.get('GITHUB_REPOSITORY', 'User/proxy-resource')
BRANCH_NAME = os.environ.get('GITHUB_REF_NAME', 'main')

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_stats(payload):
    """统计规则类型数量"""
    stats = {}
    for line in payload:
        # 跳过注释行
        if isinstance(line, str) and line.strip().startswith('#'):
            continue
        
        # 处理规则行
        rule = line if isinstance(line, str) else str(line)
        parts = rule.split(',')
        if parts and len(parts) > 0:
            rule_type = parts[0].strip()
            # 简单的验证，确保是有效的规则类型（大写字母开头）
            if rule_type and rule_type[0].isupper() and '-' in rule_type or rule_type.isupper():
                 stats[rule_type] = stats.get(rule_type, 0) + 1
    return stats

def extract_payload_categories(payload_str):
    """从 payload 字符串中提取注释作为类别 (例如 # OpenAI)"""
    categories = []
    lines = payload_str.splitlines()
    for line in lines:
        stripped = line.strip()
        # 匹配 payload 中的注释行 (以 - # 开头 或者 直接 # 开头，但在 yaml list 中通常是直接 #)
        # 假设格式为: "  # OpenAI"
        if stripped.startswith('#'):
            # 排除掉可能的规则注释 (如 # DOMAIN...)，只保留纯文本描述
            comment = stripped.lstrip('#').strip()
            # 过滤掉元数据标记
            if comment and not any(k in comment for k in ['DOMAIN', 'IP-', '规则计数', 'update_', 'name:', 'content:', 'repo:']):
                if comment not in categories:
                    categories.append(comment)
    return categories

def generate_header(original_header_lines, filename, ext, stats, categories):
    """生成标准化的文件头"""
    today = datetime.datetime.now().strftime('%Y%m%d')
    new_header = []
    
    # 标记状态
    skip_block = False

    # 基础字段处理
    has_date = False
    has_url = False
    has_repo = False
    
    # 构建当前文件的目标路径 (用于 update_url)
    if ext == '.yaml':
        relative_path = f"{SOURCE_DIR}/{filename}{ext}"
    else:
        relative_path = f"{TARGET_DIR}/{filename}{ext}"

    for line in original_header_lines:
        stripped = line.strip()
        
        # 遇到 payload 停止
        if stripped.startswith('payload:'):
            break

        # --- 过滤掉旧的自动生成块 ---
        if stripped == '# 包含的规则' or stripped == '# 规则计数':
            skip_block = True
            continue
        
        # 如果在跳过块模式下，遇到空行或非键值对注释，继续跳过
        if skip_block:
            if stripped == '' or (stripped.startswith('#') and ':' in stripped and not any(x in stripped for x in ['name:', 'content:', 'repo:', 'update_'])):
                continue
            # 遇到可能是正常注释的内容，结束跳过
            if stripped.startswith('#') and ':' not in stripped:
                pass # 可能是包含的规则的具体项，继续跳过
            else:
                skip_block = False

        if skip_block:
            continue

        # --- 更新动态字段 ---
        if stripped.startswith('# update_date:'):
            new_header.append(f'# update_date: {today}')
            has_date = True
            continue
            
        if stripped.startswith('# update_url:'):
            new_url = f'https://raw.githubusercontent.com/{REPO_NAME}/{BRANCH_NAME}/{relative_path}'
            new_header.append(f'# update_url: {new_url}')
            has_url = True
            continue

        if stripped.startswith('# repo:'):
            # repo 指向包含该文件的目录树
            repo_url = f'https://github.com/{REPO_NAME}/tree/{BRANCH_NAME}/{os.path.dirname(relative_path)}'
            new_header.append(f'# repo: {repo_url}')
            has_repo = True
            continue

        # 保留其他原有行
        new_header.append(line)

    # --- 补全缺失字段 ---
    if not has_date:
        new_header.append(f'# update_date: {today}')
    if not has_url:
        new_url = f'https://raw.githubusercontent.com/{REPO_NAME}/{BRANCH_NAME}/{relative_path}'
        new_header.append(f'# update_url: {new_url}')
    if not has_repo:
        repo_url = f'https://github.com/{REPO_NAME}/tree/{BRANCH_NAME}/{os.path.dirname(relative_path)}'
        new_header.append(f'# repo: {repo_url}')

    # --- 插入自动生成块 ---
    
    # 1. 包含的规则
    if categories:
        new_header.append('')
        new_header.append('# 包含的规则')
        for cat in categories:
            new_header.append(f'# {cat}')
    
    # 2. 规则计数
    if stats:
        new_header.append('')
        new_header.append('# 规则计数')
        for r_type, count in sorted(stats.items()):
            new_header.append(f'# {r_type}: {count}')
            
    new_header.append('') # 结尾空行
    return "\n".join(new_header)

def write_file_if_changed(path, content):
    """仅当内容变化时写入"""
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            old_content = f.read()
        if old_content.strip() == content.strip():
            print(f"  -> 内容无变化，跳过写入: {os.path.basename(path)}")
            return
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  -> 已更新: {path}")

def process_file(filename):
    print(f"正在处理: {filename}")
    source_path = os.path.join(SOURCE_DIR, filename)
    filename_no_ext = os.path.splitext(filename)[0]
    
    with open(source_path, 'r', encoding='utf-8') as f:
        full_content = f.read()

    # --- 分离 Header 和 Payload ---
    # 我们不使用 yaml.load 来完全解析，因为要保留 Payload 部分的原始注释和格式
    if 'payload:' not in full_content:
        print(f"警告: {filename} 缺少 payload，跳过")
        return

    parts = full_content.split('payload:', 1)
    header_raw = parts[0]
    payload_raw = parts[1] # 这是原始字符串，包含注释和缩进

    # --- 解析数据用于统计 ---
    # 使用 yaml safe_load 解析 payload 部分以获取纯数据进行统计
    try:
        # 构造一个合法的 yaml 字符串来解析列表
        temp_payload = yaml.safe_load('payload:' + payload_raw)
        payload_list_clean = temp_payload.get('payload', [])
        if payload_list_clean is None: payload_list_clean = []
    except Exception as e:
        print(f"解析 YAML 结构失败: {e}")
        return

    # 1. 获取统计数据
    stats = get_stats(payload_list_clean)
    
    # 2. 获取包含的规则类别 (从 payload 原始字符串中提取注释)
    categories = extract_payload_categories(payload_raw)

    # --- 生成新的 YAML 内容 ---
    new_yaml_header = generate_header(header_raw.splitlines(), filename_no_ext, '.yaml', stats, categories)
    # 拼接：新头 + "payload:" + 原始payload部分 (保留了注释)
    new_yaml_content = new_yaml_header + "payload:" + payload_raw

    # --- 生成新的 LIST 内容 ---
    new_list_header = generate_header(header_raw.splitlines(), filename_no_ext, '.list', stats, categories)
    # List 文件通常不需要缩进，我们清理一下格式，但保留注释行以便阅读
    list_body_lines = []
    for line in payload_raw.splitlines():
        stripped = line.strip()
        if not stripped: continue
        
        # 如果是列表项 "- DOMAIN,xxx" -> "DOMAIN,xxx"
        if stripped.startswith('- '):
            list_body_lines.append(stripped[2:])
        # 如果是注释 "# OpenAI" -> 保留
        elif stripped.startswith('#'):
            list_body_lines.append(stripped)
    
    new_list_content = new_list_header + "\n".join(list_body_lines) + "\n"

    # --- 写入文件 ---
    # 1. 更新源 YAML 文件
    write_file_if_changed(source_path, new_yaml_content)
    
    # 2. 生成/更新 List 文件
    target_path = os.path.join(TARGET_DIR, filename_no_ext + '.list')
    write_file_if_changed(target_path, new_list_content)

def main():
    if not os.path.exists(SOURCE_DIR):
        print(f"错误: 源目录 {SOURCE_DIR} 不存在")
        exit(1)
    ensure_dir(TARGET_DIR)

    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(('.yaml', '.yml'))]
    for file in files:
        process_file(file)

if __name__ == '__main__':
    main()
