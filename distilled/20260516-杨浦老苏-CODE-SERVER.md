---
title: CODE-SERVER — 私有AI编程工作站
source: 杨浦老苏 公众号
date: 2026-05-16
tags: [开发环境, Code-Server, HAIP, AI-CLI]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/BXiULxIVMyAfkR5ujR_FXg
---

# CODE-SERVER — 私有AI工作站蒸馏

## 核心主题
基于VS Code Server + HAIP协议打造私有AI编程工作站：浏览器即开发环境（iPad/手机也能写代码），AI编程助手远程控制，数据本地化（群晖存储），AFK手机一键审批。

## 工具链

**技术栈**
| 组件 | 作用 |
|------|------|
| code-server | VS Code远程版，浏览器即IDE |
| HAIP | AI编程助手远程控制工具，支持6款AI CLI |
| 群晖NAS | 数据存储，本地化 |
| Docker Compose | 容器编排 |

**HAIP支持的6款AI CLI**
Claude Code / Gemini CLI / OpenAI Codex / OpenCode / iFlow / Qwen Code

## 操作流

**Docker Compose关键配置**
```
端口：3196（code-server）、3197（HAIP）
内置setup-code.sh一键安装Node.js和6个AI CLI
```

**核心优势**
1. 浏览器即开发环境（iPad/手机也能写代码）
2. 远程控制AI（手机点点让AI写代码）
3. 数据本地化（群晖存储）
4. AFK审批（离开电脑手机一键审批）

## 适用场景
- 移动办公：iPad/手机写代码
- 私有化部署：数据不离开本地
- AI辅助编程：远程让AI写代码+手机审批

## 文章摘要
基于code-server + HAIP打造AI私有编程工作站。code-server让浏览器成为IDE（iPad/手机通用），HAIP支持6款AI CLI（Claude Code/Gemini/Codex等）远程控制。Docker Compose一键部署（端口3196/3197），数据存群晖NAS，支持AFK手机审批。核心优势：移动办公+数据本地化+AI远程控制。

---
*蒸馏自 杨浦老苏，2026-05-16*
