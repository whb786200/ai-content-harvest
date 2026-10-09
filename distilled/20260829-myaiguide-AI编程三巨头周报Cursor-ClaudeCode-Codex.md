# AI编程三巨头周报：Cursor+Claude Code+Codex合计95项更新，从对话到可调度行动

> 来源：My AI Guide - Builders Weekly · 2026-08-28 · https://myaiguide.co/news/builders-weekly-20260828

---

## 核心主题

2026年8月17-28日，Cursor（10项）+Claude Code（43项）+Codex（42项）合计95项更新，主线"从对话到可调度的行动"（from chat to scheduled actions）。三家都在做"集成而非模型"——无一家发布全新基础模型，全部是产品/集成/工作流侧。Agent自主性如今取决于权限与数据访问能力而非模型原始规模。agent lock-in风险初现：跨供应商数据/工作流迁移成本上升。

---

## 方法论框架

### 三家更新量级分布

| 工具 | 更新数 | 版本范围 | 重点方向 |
|------|--------|---------|---------|
| Cursor | 10项 | 无明确版本号 | Google Workspace插件+代码托管+预构建环境 |
| Claude Code | 43项 | 2.1.234→2.1.241 | 权限管理+成本优化+数据驻留+稳定性 |
| Codex | 42项 | CLI 0.149.0→0.150.1 | 仪表盘+事件触发任务+多平台扩展 |

### Cursor三大关键更新

| 功能 | 价值 | 信号 |
|------|------|------|
| Google Workspace插件 | Agent在编码会话内读Drive/起草Gmail/更新Calendar | 减少上下文切换，Agent渗入办公工作流 |
| Cursor Origin代码托管(Beta) | 内置托管+GitHub双向同步+Vercel发布+Buildkite集成 | Agent无需外部SCM登录即可管理repo |
| 预构建环境/Background Builds | 后台预装依赖，Cloud Agent启动快10x、首token快3x | 对比冷启动的效率革命 |

### Claude Code五大关键更新

| 功能 | 版本 | 价值 |
|------|------|------|
| /permissions Auto mode标签页 | — | 显示分类器规则，通配符Bash白名单子命令执行前警告 |
| SendFeedback+/claude-api cost-optimize | — | 一键起草会话报告；Sonnet 5压缩时用完整1M上下文 |
| Restricted mode+per-agent prompt cache TTL | — | 跨供应商防缓存失效 |
| Linux glibc 2.44启动崩溃修复 | 2.1.239 | Arch/CachyOS/Fedora Rawhide |
| 美国数据驻留费用估算 | 2.1.239 | 预算跟踪纳入residency溢价 |

### Codex三大关键更新

| 功能 | 版本 | 价值 |
|------|------|------|
| Agents Dashboard+队列命令 | CLI 0.149.0 | TUI交互式仪表盘，/cd /pwd目录命令，codex queue队列 |
| @任务提及+Interrupt hooks | CLI 0.150.0 | 可自定义中断钩子 |
| 事件触发计划任务 | — | Gmail过滤器/Slack频道/GitHub PR活动自动触发Codex任务 |

### Agent触达Surface对比

| 工具 | 触达Surface |
|------|------------|
| Cursor | Google Drive/Gmail/Calendar/Slack/PR事件/iPad/移动端 |
| Claude Code | GitLab MR/跨会话消息/终端稳定性 |
| Codex | Gmail/Slack/GitHub事件/Apple Messages/4浏览器/Linux桌面/iOS |

### 四条趋势主线

1. **集成而非模型**：95项更新无一家发布全新基础模型，全部产品/集成/工作流侧
2. **agent lock-in风险初现**：Cursor Origin vs GitHub、Codex queue vs Claude Code SendMessage、自建marketplace——跨供应商迁移成本上升
3. **运维/成本细节成主战场**：auto-mode警告/cache TTL frontmatter/数据驻留溢价/SendFeedback/Admin API——客户从PoC进入生产化
4. **mcp-server命令弃用**：Codex弃用自己的mcp-server，要求迁移至Codex app server或Claude Code插件——MCP生态治理中心收敛

---

## 工具链

| 类别 | 工具/平台 | 说明 |
|------|----------|------|
| AI编程-Cursor | Cursor + Origin + Cloud Agents | Google Workspace集成+预构建环境 |
| AI编程-Claude Code | Claude Code 2.1.241 | 权限管理+成本优化+数据驻留 |
| AI编程-Codex | Codex CLI 0.150.1 | 仪表盘+事件触发+多平台 |
| 代码托管 | Cursor Origin (Beta) | 内置托管+GitHub双向同步+Vercel发布 |
| 事件触发 | Codex计划任务 | Gmail/Slack/GitHub PR自动触发 |
| MCP治理 | mcp-server→Codex app server/Claude Code插件 | 生态治理中心收敛 |

---

## 关键洞察

1. **三家都在做"集成而非模型"**：95项更新无一家发布全新基础模型——Agent自主性取决于权限与数据访问能力而非模型原始规模
2. **agent lock-in风险初现**：Cursor Origin vs GitHub、Codex queue vs Claude Code SendMessage、自建marketplace——跨供应商数据/工作流迁移成本上升
3. **运维/成本细节成主战场**意味着客户已从PoC进入生产化：auto-mode警告/cache TTL/数据驻留溢价/SendFeedback/Admin API
4. **mcp-server弃用是MCP生态治理收敛信号**：Codex弃用自己的mcp-server命令，迁移至Codex app server或Claude Code插件
5. **Agent走 出终端渗入工作流界面**：从chat到scheduled actions with concrete workspace and cloud ties
6. **建议本周在单个非关键项目试点一项集成后推广**

---

## 金句

> "moving coding agents from chat to scheduled actions with concrete workspace and cloud ties."

> "Agent自主性如今取决于权限与数据访问能力，而非模型原始规模。"

> "三家都在做'集成而非模型'——95项更新无一家发布全新基础模型。"

---

## 适用场景

- **AI编程工具选型**：三家触达Surface对比+更新量级分布
- **Agent工作流集成**：Cursor Google Workspace/Codex事件触发/Claude Code GitLab MR
- **生产化成本管理**：Claude Code数据驻留溢价/cache TTL/SendFeedback
- **agent lock-in风险评估**：跨供应商数据/工作流迁移成本
- **MCP生态治理**：mcp-server弃用→Codex app server/Claude Code插件迁移

---

## 文章摘要

My AI Guide发布Builders Weekly（8/17-28）。Cursor 10项（Google Workspace插件读Drive/起草Gmail/更新Calendar；Cursor Origin代码托管Beta内置GitHub双向同步+Vercel发布；预构建环境启动快10x）。Claude Code 43项（2.1.234→2.1.241：/permissions Auto mode；SendFeedback+/claude-api cost-optimize Sonnet 5用1M上下文；Restricted mode+prompt cache TTL；Linux glibc 2.44修复；美国数据驻留费用估算）。Codex 42项（CLI 0.149.0→0.150.1：Agents Dashboard+队列命令；@任务提及+Interrupt hooks；Gmail/Slack/GitHub PR事件触发计划任务；⚠️mcp-server命令弃用）。四条趋势：集成而非模型/agent lock-in风险/运维成本成主战场/mcp-server弃用。Agent从chat到scheduled actions。

蒸馏自：My AI Guide·Cursor/Claude Code/Codex周报(2026-08-28)
