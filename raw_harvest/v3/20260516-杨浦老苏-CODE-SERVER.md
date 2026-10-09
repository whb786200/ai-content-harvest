---
title: "杨浦老苏-CODE-SERVER私有AI工作站"
source: "杨浦老苏"
date: 2026-04-09
url: "https://mp.weixin.qq.com/s/BXiULxIVMyAfkR5ujR_FXg"
tags: [开发环境, Code-Server, HAPI]
---
# 基于CODE-SERVER打造私有AI编程工作站

## Code Server
运行在远程服务器的VS Code，浏览器即开发环境。

## HAPI
AI编程助手远程控制工具，支持6款AI CLI（Claude Code/Gemini/OpenAI Codex/OpenCode/iFlow/Qwen Code）。

## 核心优势
- 浏览器即开发环境（iPad/手机也能写代码）
- 远程控制AI（手机点点让AI写代码）
- 数据本地化（群晖存储）
- AFK审批（离开电脑手机一键审批）

## Docker Compose关键配置
端口：3196（code-server）、3197（HAPI）
内置setup-code.sh一键安装Node.js和6个AI CLI。
