---
title: Obsidian + Claude Code AI第二大脑实战 — 三种集成方案+Vibe Writing
source: blog.xiaohuangyu.space
date: 2026-06-06
tags: [Obsidian, Claude Code, 第二大脑, MCP, AI工作流, Vibe Writing, BRAT]
type: distilled
distilled_at: 2026-06-06
original_url: https://blog.xiaohuangyu.space/p/obsidian-claude-code-ai-second-brain-guide/
---

# Obsidian + Claude Code AI第二大脑实战 — 蒸馏

## 核心主题
Obsidian笔记全是Markdown，Claude Code原生理解Markdown——无需复制粘贴、无需切换窗口，Claude Code直接读写vault文件。三种集成方案从新手到高级，核心是CLAUDE.md配置+Vibe Writing工作流。

## 方法论/认知框架

**Obsidian+Claude Code集成的核心逻辑**
```
Markdown原生优势 → Claude Code原生理解.md
→ 无需复制粘贴 → 无需切换窗口
→ 直接读写vault → AI成为写作的一部分
```

**CLAUDE.md配置法（让Claude更懂你的Vault）**
```
在vault根目录创建 CLAUDE.md，定义：
1. Front matter格式要求
2. 图片管理规则
3. 部署流程说明
→ Claude自动遵守项目约定
```

**Vibe Writing工作流**
```
一边在Obsidian写笔记
一边让AI在终端实时辅助
→ "写作像呼吸一样自然"
```

## 工具链

### 三种集成方案对比
| 方案 | 来源 | 适合人群 | 核心特点 |
|------|------|----------|---------|
| **Integration插件**（推荐） | deivid11/obsidian-claude-code-plugin | 新手 | 功能最全：标签页+会话管理+流式输出+变更预览+Diff对比 |
| **Sidebar** | derek-larson14/obsidian-claude-sidebar | 命令行老手 | 简洁原生，侧边栏嵌入终端体验 |
| **Terminal插件** | Polyware Terminal | 追求灵活性 | 最灵活，Obsidian内嵌完整终端 |

### 配置要点
- **Backend**: Claude Code
- **Model选择**: Sonnet（均衡）/ Opus（最强）/ Haiku（最快最便宜）
- **Allow Vault Access**: 建议开启
- **国内用户**: 可配置GLM等第三方模型
- **安装方式**: BRAT插件安装器

## 关键洞察

1. **Integration插件是最佳入门选择**：UI交互完整（标签页/会话管理/流式输出/变更预览/Diff对比），BRAT一键安装
2. **CLAUDE.md是关键配置**：在vault根目录定义规则，让Claude自动遵守项目约定
3. **Vibe Writing=AI辅助写作的终极形态**：写和AI辅助同步进行，无切换成本
4. **国内可配置GLM**：绕过Claude API限制，用国产模型替代
5. **三种方案梯度适配**：新手→Integration，老手→Sidebar，极客→Terminal

## 金句
> "写作像呼吸一样自然。"

## 适用场景
- Obsidian+Claude Code集成入门：三种方案对比选择
- Vibe Writing工作流：AI辅助写作无缝集成
- CLAUDE.md配置：让AI自动理解项目约定
- 国内用户Obsidian+AI：GLM等国产模型替代方案
- BRAT插件安装流程：社区插件快速部署

## 文章摘要
Obsidian+Claude Code AI第二大脑实战：三种集成方案（Integration插件推荐：标签页+会话+流式输出+Diff对比；Sidebar：命令行老手简洁原生；Terminal：极客内嵌终端），CLAUDE.md配置法（Front matter/图片管理/部署规则），Vibe Writing工作流（写作+AI辅助同步进行），模型选择（Sonnet均衡/Opus最强/Haiku最便宜），国内GLM替代，BRAT安装。

---
*蒸馏自 blog.xiaohuangyu.space，2026-06-06*
