---
Created date: 2026-01-14 14:52
Modified date: 2026-02-20 18:21
---

# agency-tools

## 内核

- [mihomo](https://github.com/MetaCubeX/mihomo)
	- 介绍： MetaCubeX 维护的 Mihomo 内核（Clash Meta 内核的社区延续版），兼容 Clash 配置，支持更多协议（如 Hysteria2、TUIC、Reality 等）、高级分流规则、性能优化，是当前最主流的 Clash 替代内核，更新活跃、社区支持强大。
	- 使用教程： [文档教程](https://wiki.metacubex.one/)
	- 标签： #Mihomo #ClashMeta #MetaCubeX #高级分流 #多协议支持
- [sing-box - SagerNet](https://github.com/SagerNet/sing-box)
	- 介绍： SagerNet 官方维护的 sing-box 内核，通用代理平台，支持 Shadowsocks、VMess、Trojan、Hysteria、TUIC、Reality 等丰富协议，配置简洁、性能优异、跨平台兼容性强，是 sing-box 生态的主要分支。
	- 使用教程： [文档教程 - sing-box](https://sing-box.sagernet.org/)
	- 标签： #sing-box #SagerNet #通用代理 #多协议 #跨平台
- [sing-box - PuerNya](https://github.com/PuerNya/sing-box)
	- 介绍： sing-box 的 PuerNya 分支，通用代理平台内核，支持 Shadowsocks、VMess、Trojan、Hysteria、TUIC 等多种协议，配置简洁、性能出色、社区活跃，常用于自定义优化与实验。
	- 使用教程： [文档教程 - sing-box](https://sing-box.sagernet.org/)
	- 标签： #sing-box #PuerNya #通用代理 #多协议 #轻量内核
- [v2ray-core](https://github.com/v2fly/v2ray-core)
	- 介绍： V2Ray 官方核心项目，提供 VMess、VLESS、Shadowsocks、Trojan 等协议支持，是经典代理工具的基础内核，支持插件扩展、传输方式自定义、路由规则等，稳定可靠。
	- 使用教程： [文档教程 - V2Fly.org](https://www.v2fly.org/)
	- 标签： #V2Ray #v2fly #VMess #VLESS #经典代理内核
- [Xray-core](https://github.com/XTLS/Xray-core)
	- 介绍： XTLS 团队维护的 Xray 内核，是 V2Ray 的增强版，支持 XTLS、REALITY、Vision 等高级传输方式，更高性能、更强抗检测能力、更多协议兼容，是目前最推荐的 V2Ray 系核心。
	- 使用教程： [文档教程 Project X](https://xtls.github.io/)
	- 标签： #Xray #XTLS #REALITY #抗检测 #高性能内核

## GUI

- [YumeBox](https://github.com/YumeLira/YumeBox)
	- 介绍：an ordinary box, as ordinary as it can possibly be
	- 标签：
	- 其他：
- [clash_for_android](https://github.com/clashbk/clash_for_android)
	- 介绍： Clash for Android 的最后版本备份下载仓库，提供官方 Clash for Android 的历史版本、汉化补丁、APK 直链下载，适合需要使用旧版或汉化版的用户。
	- 内核： clash
	- 使用教程： 
	- 标签： #ClashForAndroid #备份下载 #汉化补丁 #安卓客户端 #Clash
- [clash-for-flutter](https://github.com/mapleafgo/clash-for-flutter)
	- 介绍： 使用 Flutter 开发的 Clash 桌面客户端，支持 Windows、Linux、macOS 平台，提供图形化界面、节点管理、规则编辑、订阅导入等功能，跨平台体验一致。
	- 内核： clash
	- 使用教程： 
	- 标签： #ClashFlutter #桌面客户端 #跨平台 #图形界面 #Clash
- [ClashMetaForAndroid](https://github.com/MetaCubeX/ClashMetaForAndroid)
	- 介绍： 基于 Clash Meta（mihomo）内核的 Android 客户端，支持更高级的分流规则、协议兼容、性能优化、Meta 特性（如 Hysteria2、TUIC、Reality 等），功能强大、更新活跃。
	- 内核： mihomo
	- 使用教程： 
	- 标签： #ClashMeta #Meta内核 #安卓客户端 #高级分流 #MetaCubeX
- [Exclave](https://github.com/dyhkwong/Exclave)
	- 介绍： Android 平台的 V2Ray 客户端，支持 V2Ray 核心，提供节点管理、订阅导入、规则分流、流量统计等功能，界面简洁、稳定可靠。
	- 内核： v2ray-core
	- 使用教程： 
	- 标签： #Exclave #V2Ray客户端 #安卓V2Ray #节点管理 #协议支持
- [FlClash](https://github.com/chen08209/FlClash)
	- 介绍： 基于 Clash Meta 内核的多平台代理客户端，简单易用、开源无广告，支持节点订阅、分流规则、策略组、Tun 模式等，界面现代化、性能优秀。
	- 内核： mihomo
	- 使用教程： 
	- 标签： #FlClash #ClashMeta #多平台 #无广告 #简单易用
- [FlyClash-Android](https://github.com/GtxFury/FlyClash-Android)
	- 介绍： FlyClash 的 Android 版本，基于 mihomo 内核，提供轻量级代理功能，支持订阅、规则、分流、Tun 模式等，适合追求极简体验的用户。
	- 内核： mihomo
	- 使用教程： 
	- 标签： #FlyClash #安卓轻量 #mihomo客户端 #极简代理 #订阅支持
- [hiddify-app](https://github.com/hiddify/hiddify-app)
	- 介绍： Hiddify 多平台自动代理客户端，支持 Sing-box、X-ray、TUIC、Hysteria、Reality、Trojan、SSH 等多种协议，开源、安全、无广告，提供节点管理、订阅导入、规则分流等功能。
	- 内核： Sing-box
	- 使用教程： 
	- 标签： #Hiddify #多协议支持 #Sing-box #开源代理 #无广告
- [husi](https://github.com/xchacha20-poly1305/husi)
	- 介绍： Husi（虎兕）是一款非专业、娱乐向的代理工具集成模块，支持多种协议与内核，提供简单配置、趣味化界面、自定义规则等，适合轻度用户与实验玩机。
	- 内核： Sing-Box
	- 使用教程： 
	- 标签： #Husi #娱乐代理 #Sing-box #自定义规则 #趣味工具
- [karing](https://github.com/KaringX/karing)
	- 介绍： Karing 是一款简单而强大的代理工具，支持 Clash 与 Sing-box 路由规则，提供图形化界面、节点管理、规则编辑、Tun 模式、流量统计等功能，兼容性强、更新活跃。
	- 内核： Sing-Box
	- 使用教程： https://karing.app/
	- 标签： #Karing #Sing-box客户端 #图形化代理 #规则支持 #简单强大
- [MikuBoxForAndroid](https://github.com/HatsuneMikuUwU/MikuBoxForAndroid)
	- 介绍： MikuBox for Android，基于 Sing-box 内核的通用代理工具链，提供节点订阅、分流规则、Tun 模式、性能优化等功能，界面可爱、功能齐全。
	- 内核： Sing-Box
	- 使用教程： 
	- 标签： #MikuBox #Sing-box #安卓代理 #通用工具链 #可爱界面
- [NekoBoxForAndroid](https://github.com/MatsuriDayo/NekoBoxForAndroid)
	- 介绍： NekoBox for Android，基于 Sing-box 的通用代理工具链，支持多种协议、节点订阅、分流规则、Tun 模式、插件扩展等，功能丰富、更新频繁、社区活跃。
	- 内核： Sing-Box
	- 使用教程： https://matsuridayo.github.io/
	- 标签： #NekoBox #Sing-box #MatsuriDayo #多协议支持 #安卓代理
- [ShadowsocksR-Android](https://github.com/HMBSbige/ShadowsocksR-Android)
	- 介绍： ShadowsocksR（SSR）Android 客户端，使用 Kotlin 开发，支持 SSR 协议、节点管理、订阅导入、插件扩展等功能，稳定可靠、界面简洁。
	- 内核： ssr
	- 使用教程： 
	- 标签： #ShadowsocksR #SSR客户端 #安卓SSR #Kotlin开发 #协议支持
- [surfboard](https://github.com/getsurfboard/surfboard)
	- 介绍： Surfboard 是一款基于 V2Ray 的代理客户端，支持多种协议、节点订阅、规则分流、Tun 模式等功能，界面现代化、配置灵活。
	- 内核： surfboard
	- 使用教程： 
	- 标签： #Surfboard #V2Ray客户端 #安卓代理 #规则分流 #Tun模式
- [v2rayNG](https://github.com/2dust/v2rayNG)
	- 介绍： v2rayNG 是最流行的 V2Ray Android 客户端，支持 Xray 核心与 v2fly 核心，提供节点订阅、规则分流、Tun 模式、插件支持等功能，界面简洁、更新频繁、社区活跃。
	- 内核： Xray core， v2fly core
	- 使用教程： 
	- 标签： #v2rayNG #V2Ray客户端 #Xray支持 #安卓代理 #订阅管理
- [Xray](https://github.com/SaeedDev94/Xray)
	- 介绍： Xray GUI Client For Android，基于 Xray 核心的图形化客户端，提供节点管理、订阅导入、分流规则、Tun 模式等功能，界面简洁、性能优秀。
	- 内核： Xray-core
	- 使用教程： 
	- 标签： #Xray客户端 #安卓Xray #图形界面 #Tun模式 #代理工具
- [Neko-ray](https://github.com/yixuan66/Neko-ray)
	- 介绍： Neko-ray 是基于 Xray 核心与 v2fly 核心的 V2Ray Android 客户端，采用 UWU 团队的美观 UI 风格，提供节点订阅、分流规则、Tun 模式等功能，界面可爱、体验优秀。
	- 内核：  Xray, v2fly
	- 使用教程： 
	- 标签： #Neko-ray #UWU风格 #V2Ray客户端 #美观UI #安卓代理
- [Exclave](https://github.com/dyhkwong/Exclave)
	- 介绍： Exclave 是一款代理客户端，支持多种协议与配置，提供节点管理、订阅导入、分流规则等功能，界面简洁、稳定可靠。
	- 内核： 
	- 使用教程： 
	- 标签： #Exclave #代理客户端 #节点管理 #订阅支持 #安卓工具

### 自带节点

- [shadowrocket](https://shadowrocket.v2cross.com/)
	- 介绍： 支持 Trojan、Socks、shadowsocks、vmess、VLESS 等协议,内置海量免费节点，可供导出使用。同时也是一个完全免费使用的节点池类型 app
	- 内核： 
	- 使用教程： 
	- 标签： 

## webui

- [yacd](https://yacd.haishan.me/)
- [zashboard](https://github.com/Zephyruso/zashboard)
- [metacubexd](https://github.com/MetaCubeX/metacubexd)
	- 介绍： Mihomo Dashboard, The Official One, XD
	- 标签： 
- [Clash](https://clash.razord.top/#/proxies)
