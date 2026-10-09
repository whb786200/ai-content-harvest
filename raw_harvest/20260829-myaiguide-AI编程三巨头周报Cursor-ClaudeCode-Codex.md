---
source: My AI Guide - Builders Weekly
url: https://myaiguide.co/news/builders-weekly-20260828
published: 2026-08-28
harvested_at: 2026-08-29
harvest_method: web_fetch
model_selection: hunyuan-turbo
tags: [Cursor, Claude Code, OpenAI Codex, AI编程, Agent, 周报]
---

# Cursor / Claude Code / Codex 周报 (2026-08-17 ~ 2026-08-28)

> 三大 AI 编程工具本周合计 **95 项更新**（Cursor 10 + Claude Code 43 + Codex 42），主线"从对话到可调度的行动"。本资料综合 My AI Guide 周报整理。

## 1. Cursor (10 项，本周无明确版本号)

最重要的 3 个新功能：

- **Google Workspace 插件**：Marketplace 插件让 Agent 在编码会话内**读取 Drive 文件、起草 Gmail、更新 Calendar 事件**——减少上下文切换。
- **Cursor Origin 代码托管 (Beta)**：内置托管，**GitHub 双向同步 + Vercel 发布 + Buildkite 集成**，Agent 无需外部 SCM 登录即可管理 repo。
- **预构建环境 / Background Builds**：后台预装依赖，**Cloud Agent 启动快 10x、首 token 快 3x**（对比冷启动）。

其他：Cloud Agents 订阅 PR/Slack 事件、隔离 VM 子代理、`/goal` 持久命令；iPad 多窗口 + Pencil，移动端 Inbox + Bitbucket/Azure DevOps。

## 2. Claude Code (43 个版本：2.1.234 → 2.1.241)

最重要的 5 个新功能：

- **`/permissions` Auto mode 标签页**：显示分类器规则；**通配符 Bash 白名单子命令执行前警告**。
- **SendFeedback 工具 + `/claude-api cost-optimize`**：一键起草会话报告；Sonnet 5 压缩时可用完整 1M 上下文。
- **Restricted mode + per-agent prompt cache TTL frontmatter**：跨供应商防缓存失效。
- **Linux glibc 2.44 启动崩溃修复 (2.1.239)**：Arch / CachyOS / Fedora Rawhide。
- **美国数据驻留费用估算 (2.1.239)**：预算跟踪纳入 residency 溢价；`/claude-api upgrade` 辅助 Python SDK v1 迁移。

其他：`/usage` 新增 loops 拆解；modelPicker 自定义；免密 Console 登录；GitLab MR 徽章 + 限额重置自动续跑 (2.1.234)；`ANTHROPIC_DEFAULT_MODEL` + `notify_when_idle` 跨会话消息；Concise 输出风格；zstd 压缩；Admin API 扩展覆盖 CMEK。

## 3. OpenAI Codex (42 项更新：CLI 0.149.0 → 0.150.1)

最重要的 3 个新功能：

- **Agents Dashboard + 队列命令 (CLI 0.149.0)**：TUI 交互式仪表盘，`/cd` `/pwd` 目录命令，`codex queue` 队列。
- **@任务提及 + Interrupt hooks (CLI 0.150.0)**：可自定义中断钩子。
- **事件触发的计划任务**：**Gmail 过滤器 / Slack 频道 / GitHub PR 活动**自动触发 Codex 任务。

其他：Linux 桌面 App 预览版（.deb/.rpm），内置**从 Claude Code / Cursor 导入工具**；Daybreak Blue / Red 网络安全分层 GPT-5.6 Sol / GPT-5.6 Cyber；GitLab 集成 Beta；Apple Messages 插件；Computer History 扩至 EEA/瑞士/英国 Pro 用户；浏览器扩展 +4（Edge/Brave/Opera/Vivaldi）；⚠️ **`mcp-server` 命令弃用**（迁移至 Codex app server 或 Claude Code 插件）。

## 4. 整体趋势：Agents 走出终端 → 渗入工作流界面

> 原文判断：*"moving coding agents from chat to **scheduled actions** with concrete workspace and cloud ties"*

| 工具 | 触达 Surface |
|------|--------------|
| Cursor | Google Drive / Gmail / Calendar / Slack / PR 事件 / iPad/移动端 |
| Claude Code | GitLab MR / 跨会话消息 / 终端稳定性 |
| Codex | Gmail / Slack / GitHub 事件 / Apple Messages / 4 浏览器 / Linux 桌面 / iOS |

**作者观点**：Agent 自主性如今取决于**权限与数据访问能力，而非模型原始规模**；重度集成可能造成 vendor lock-in；团队需管理多个 agent runtime + 跨供应商数据驻留规则；建议本周在单个非关键项目试点一项集成后推广。

## 5. 关键洞察

- **三家都在做"集成而非模型"**：本周三家的版本号合计 95 项更新，但没有任何一家发布全新基础模型——全部是产品/集成/工作流侧。
- **agent lock-in 风险初现**：Cursor Origin vs GitHub、Codex queue vs Claude Code SendMessage、自建 marketplace——跨供应商数据/工作流迁移成本上升。
- **运维/成本细节成主战场**：auto-mode 警告、cache TTL frontmatter、数据驻留溢价计入、SendFeedback、Admin API——意味着客户已从 PoC 进入生产化。
- **`mcp-server` 弃用**：Codex 弃用自己的 mcp-server 命令，要求用户迁移至 Codex app server 或 Claude Code 插件——MCP 生态治理中心正从多端向单一稳定端收敛。
