---
title: "Tailscale DERP自建中继"
source: "AI前沿短裤哥"
date: 2026-03-28
url: "https://mp.weixin.qq.com/s/6YjXWf0yVNHqYIOLsqvKjw"
tags: [网络, Tailscale, VPS]
---
# Tailscale自建DERP中继（5分钟部署）

## 为什么自建
官方DERP在国内无节点，P2P失败时绕道海外，速度极慢。

## 部署步骤
1. 安装Tailscale客户端
2. Docker运行DERP服务器（deepfal/tailscale-derp:latest）
3. 配置防火墙（TCP 59443 + UDP 3478）
4. 配置Tailscale ACL的derpMap（RegionID=900）
5. `tailscale netcheck` 验证

## 关键参数
- `--verify-clients`：防止被白嫖
- `-certmode manual`：无需SSL证书（Tailscale自身端到端加密）
- `OmitDefaultRegions: false`：保留官方节点作备份

## 成本
最低配VPS月费10-20元
