---
title: Tailscale自建DERP中继 — 5分钟部署
source: AI前沿短裤哥 公众号
date: 2026-05-16
tags: [网络, Tailscale, DERP, VPS, Docker]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/6YjXWf0yVNHqYIOLsqvKjw
---

# Tailscale自建DERP中继蒸馏

## 核心主题
Tailscale官方DERP在国内无节点导致P2P失败时绕道海外速度极慢。Docker自建DERP中继，5分钟部署，最低VPS月费10-20元解决国内节点问题。

## 操作流

**5步部署流程**
1. 安装Tailscale客户端
2. Docker运行DERP服务器（`deepfal/tailscale-derp:latest`）
3. 配置防火墙（TCP 59443 + UDP 3478）
4. 配置Tailscale ACL的derpMap（RegionID=900）
5. `tailscale netcheck` 验证

**关键参数**
| 参数 | 作用 |
|------|------|
| `--verify-clients` | 防止被白嫖 |
| `-certmode manual` | 无需SSL证书（Tailscale自身端到端加密） |
| `OmitDefaultRegions: false` | 保留官方节点作备份 |

## 成本
最低配VPS月费10-20元

## 适用场景
- 国内Tailscale用户：解决官方DERP无国内节点的痛点
- 异地组网加速：P2P直连失败时的低延迟中继
- 小团队远程协作：低成本的网络加速方案

## 文章摘要
Tailscale官方DERP在国内无节点，自建方案：Docker运行deepfal/tailscale-derp镜像，配置防火墙（TCP 59443+UDP 3478）、ACL derpMap，5分钟完成。关键参数：--verify-clients防白嫖、certmode manual免SSL（Tailscale自带端到端加密）。最低VPS月费10-20元。

---
*蒸馏自 AI前沿短裤哥 公众号，2026-05-16*
