---
title: wechat-cli — 微信命令行工具
source: 拂晓AI数字人 公众号
date: 2026-05-16
tags: [微信, CLI, Agent, 开源, 数据分析]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/4PkqM3yvqipPJyUnySLeog
---

# wechat-cli — 微信CLI蒸馏

## 核心主题
wechat-cli：本地操作微信数据的命令行工具，JSON输出，Agent友好，零封号风险。11个命令覆盖会话/消息/联系人/统计/导出全链路。

## 工具链

**11个命令全览**
| 命令 | 功能 |
|------|------|
| `init` | 初始化环境，提取数据库密钥 |
| `sessions` | 最近聊天会话 |
| `history` | 指定聊天记录（分页+时间过滤） |
| `search` | 全局搜索消息 |
| `contacts` | 联系人搜索和详情 |
| `members` | 群成员信息 |
| `stats` | 聊天统计分析 |
| `export` | 导出为Markdown/纯文本 |
| `favorites` | 查看微信收藏 |
| `unread` | 查看未读会话 |
| `new-messages` | 增量拉取新消息 |

## 核心优势
- **本地操作**：直接读取微信本地数据库，零封号风险
- **JSON输出**：Agent友好，可直接解析
- **数据分析**：stats命令支持聊天统计分析

## 安装
```bash
npm install -g wechat-cli
```

GitHub: github.com/freestylefly/wechat-cli

## 对1052-OS的参考价值
- **微信数据本地读取**：可作为1052-OS公众号运营的数据分析工具
- **JSON输出Agent友好**：与1052-OS的自动化管线对接成本低
- **零封号风险**：比网页版微信API更安全

## 适用场景
- 微信聊天记录分析：导出+统计分析
- Agent集成：通过CLI操作微信数据
- 聊天记录备份：Markdown格式导出

## 文章摘要
wechat-cli是本地操作微信数据的命令行工具（GitHub开源）。11个命令：init/sessions/history/search/contacts/members/stats/export/favorites/unread/new-messages。核心优势：本地读取零封号风险、JSON输出Agent友好。npm一键安装。

---
*蒸馏自 拂晓AI数字人 公众号，2026-05-16*
