---
Created date: 2025-02-07 00:41
Modified date: 2025-12-02 13:16
---
# 了解什么是 DNS 以及相关的协议

> [浅谈在代理环境中的 DNS 解析行为](https://blog.skk.moe/post/what-happend-to-dns-in-proxy/#Ru-Guo-Cao-Zuo-Xi-Tong-Huo-Zhe-Liu-Lan-Qi-Huan-Cun-Liao-DNS-Jie-Xi-Jie-Guo)

- 如果你不想折腾（DNS 分流），用默认配置就可以了，使用运营商的 DNS 服务最快，如果 DNS 污染非常严重时再换公共 DNS。

## DNS(Domain Name System/域名系统) 

- 将人们易于记忆的域名（如 www.example.com）转换为计算机能够理解的 IP 地址（如 192.0.2.1）。这就像是互联网的“电话簿”，帮助浏览器找到你要访问的网站。

## DNS 协议

### 传统 DNS (UDP/TCP over port 53)

- 传统的 DNS 使用 UDP 端口 53 进行查询和响应。对于较大的查询响应（超过 512 字节），可能会使用 TCP 端口 53。
- 优点：简单、快速，适用于大多数查询。
- 缺点：缺乏安全性，容易受到中间人攻击和缓存投毒攻击。

### [DNS over QUIC (DoQ)](https://zh.wikipedia.org/wiki/DNS_over_QUIC)

- QUIC 协议本身使得队头堵塞问题得以解决，能使其在更为苛刻的网络环境中表现得更好。速度更快，是 DNS over TLS 协议速度的两倍。
- 优点：提供加密和隐私保护；相较于 TCP，QUIC 可以减少连接建立的延迟，提高性能。
- 缺点：仍在发展和标准化过程中，支持的服务器和客户端较少。

### DNS over TLS (DoT)

- DoT 使用 TLS（传输层安全协议）加密 DNS 查询和响应，通常通过 TCP 端口 853 进行通信。
- 优点：提高了安全性，通过加密防止中间人攻击和窥探；保持 DNS 查询的完整性和隐私性。
- 缺点: 相较于传统的 DNS，DoT 可能会增加一些延迟，因为建立 TLS 连接需要更多的时间。

### DNS over HTTPS (DoH)

- DoH 使用 HTTPS（HTTP over TLS）协议通过标准的 HTTPS 端口（443）传输 DNS 查询和响应。查询和响应被封装在 HTTPS 请求和响应中。
- 优点：与 DoT 一样提供加密，防止中间人攻击和窥探；通过使用 HTTPS 端口，可以绕过一些网络过滤和审查机制；利用现有的 HTTP/2 和 HTTP/3 连接优化，可能提供更高的性能。
- 缺点：实现和配置相对复杂，可能增加客户端和服务器的处理负担。

## reference

- [Cloudflare](https://www.cloudflare-cn.com/learning/dns/what-is-a-dns-server/)
- [百度百科](https://baike.baidu.com/item/%E5%9F%9F%E5%90%8D%E7%B3%BB%E7%BB%9F/2251573)
