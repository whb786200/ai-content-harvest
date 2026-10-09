---
title: "微信CLI开源工具"
source: "拂晓AI数字人"
date: 2026-04-10
url: "https://mp.weixin.qq.com/s/4PkqM3yvqipPJyUnySLeog"
tags: [微信, CLI, Agent]
---
# wechat-cli：微信命令行工具

## 核心价值
本地操作微信数据，JSON输出，Agent友好，零封号风险。

## 11个命令
| 命令 | 功能 |
|------|------|
| init | 初始化环境，提取数据库密钥 |
| sessions | 最近聊天会话 |
| history | 指定聊天记录（分页+时间过滤） |
| search | 全局搜索消息 |
| contacts | 联系人搜索和详情 |
| members | 群成员信息 |
| stats | 聊天统计分析 |
| export | 导出为Markdown/纯文本 |
| favorites | 查看微信收藏 |
| unread | 查看未读会话 |
| new-messages | 增量拉取新消息 |

## 安装
```bash
npm install -g wechat-cli
```

GitHub: https://github.com/freestylefly/wechat-cli
