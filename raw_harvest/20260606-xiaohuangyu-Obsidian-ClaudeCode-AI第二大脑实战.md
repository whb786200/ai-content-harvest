---
title: Obsidian + Claude Code 构建 AI 第二大脑实战指南
source: blog.xiaohuangyu.space
date: 2026-06-06
tags: [Obsidian, Claude Code, 第二大脑, MCP, AI工作流, 知识管理]
type: harvested
url: https://blog.xiaohuangyu.space/p/obsidian-claude-code-ai-second-brain-guide/
harvested_at: 2026-06-06T10:01:00
---

# Obsidian + Claude Code 构建 AI 第二大脑实战指南

## 核心优势
Obsidian 笔记全是 Markdown，Claude Code 原生理解 Markdown。
无需复制粘贴、无需切换窗口，Claude Code 直接读写 vault 文件。

## 三种集成方案

### 方案一：Claude Code Integration 插件（推荐）
- **来源**: deivid11/obsidian-claude-code-plugin
- **特点**: 完整UI交互——标签页、会话管理、流式输出、变更预览、Diff对比
- **安装**: 通过BRAT安装 → 配置Backend/Model/API Key
- **使用**: 侧边栏图标 → 输入需求 → 实时输出 → 预览变更

### 方案二：Claude Sidebar
- **来源**: derek-larson14/obsidian-claude-sidebar
- **特点**: 简洁原生，侧边栏嵌入终端体验，无额外UI
- **适合**: 已熟悉Claude Code命令行的用户

### 方案三：Terminal 插件
- **来源**: Polyware Terminal
- **特点**: 最灵活，Obsidian内嵌完整终端直接运行claude
- **适合**: 追求灵活性的高级用户

## 方案对比

| 方案 | 适合人群 | 特点 |
|------|----------|------|
| Integration插件 | 新手推荐 | 功能最全，UI体验最好 |
| Sidebar | 命令行老手 | 简洁原生，侧边栏终端 |
| Terminal插件 | 追求灵活性 | 最灵活，需自行折腾 |

## 进阶：让Claude更懂你的Vault
在 vault 根目录创建 `CLAUDE.md`，定义：
- Front matter 格式要求
- 图片管理规则
- 部署流程说明

## 配置要点
- Backend: Claude Code
- Model: Sonnet(均衡)/Opus(最强)/Haiku(最快最便宜)
- Allow Vault Access: 建议开启
- 国内用户可配置GLM等第三方模型

## Vibe Writing 工作流
一边在 Obsidian 写笔记，一边让 AI 在终端实时辅助——"写作像呼吸一样自然"。
