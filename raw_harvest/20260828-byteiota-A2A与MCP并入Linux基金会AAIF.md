---
source: byteiota
url: https://byteiota.com/a2a-and-mcp-are-now-under-one-roof-what-aaif-means?ref=feedbagel.com
published: 2026-08-25
harvested_at: 2026-08-28
harvest_method: web_fetch
model_selection: hunyuan-turbo
tags: [A2A, MCP, Agentic AI Foundation, Linux Foundation, 多智能体, 协议标准]
---

# A2A and MCP Are Now Under One Roof: What AAIF Means

Google's A2A joined Anthropic's MCP under the Linux Foundation-directed AAIF on August 20, 2026. 这是多智能体系统构建者等待已久的消息：协议之战结束，两层协议栈成为参考架构，由 AWS、Anthropic、Google、Microsoft、OpenAI 及 250+ 组织共同背书。

## Stop Confusing These Two Protocols
MCP 与 A2A 从不竞争，分属协议栈不同层；混淆二者导致糟糕的架构决策。
- **MCP 是垂直的（vertical）**：标准化 agent 如何连接工具——数据库、API、文件系统、搜索结果。模型调用函数，函数返回结果。无状态、事务性、快。查询 Postgres、读文件、调 SaaS API 属于 MCP 领地。
- **A2A 是水平的（horizontal）**：处理一个 agent 如何与另一个 agent 对话——任务委托、能力发现、身份交换、跨组织边界的长运行状态。编排 agent 把工作交给不同系统的专家 agent 时，是 A2A 的活。
- 最清晰的比喻：**MCP 给 agent 手（hands），A2A 给 agent 同事（colleagues）**。

## The Reference Architecture（三层 agent 栈）
在 AAIF 治理下，三层栈成为官方架构：
1. **WebMCP** — agent 结构化 web 访问
2. **MCP** — agent-to-tool 连接（数据库、API、服务）
3. **A2A** — agent-to-agent 编排（任务委托、协调）

具体工作流：编排 agent 用 A2A 把数据校验任务委托给专家 agent；专家用 MCP 从 Snowflake 拉记录并跑质检；结果经 A2A 返回编排者。两层各司其职，互不越界。Google 在 A2A 原公告中演示的招聘 agent 即此模式：A2A 协调候选人搜寻/排期/背调专家，各专家用 MCP 连自身数据源。

## Why Governance Is the Actual News
技术架构早被关注团队理解；AAIF 改变的是**治理**——这比多数开发者意识到的更重要。
- 8/20 前，两协议均有"单厂商问题"：Anthropic 降优先级则 MCP 前途未卜，Google 转移焦点则 A2A 同理。企业押注于公司战略稳定并非安全赌注。
- AAIF 下，任一方协议变更需 RFC + 技术指导委员会评审 + 公开评议期——同 OpenAPI/GraphQL 流程。Linux 基金会治理下的项目不会因支持者转向而消失。
- LangChain 联合创始人 Harrison Chase：AAIF 把协作从" goodwill 临时态"变为"结构永久态"。

## The Numbers（确认这不是实验）
- MCP 月 SDK 下载 **1.1 亿**；官方注册 **9,652** 个 server；15,000+ GitHub 仓库标为 MCP server。
- **78%** 企业 AI 团队报告 MCP 已在生产环境。
- 用 MCP 集成一个新 SaaS 工具的时间从约 18 小时自定义代码降至 **4.2 小时**。
- A2A v1.0 已上线；Salesforce Agentforce、ServiceNow Now Assist、Google ADK 均实现。
- Gartner 预测 2026 年底 **40%** 企业应用含任务型 AI agent（2025 年 <5%）。

## What Developers Should Do Now
- 工具访问先用 MCP（生态成熟、SDK 扎实、注册表给集成先手）。
- 系统需跨服务边界协调多个 agent 时再加 A2A。
- 不要自建协议；不要试图让 MCP 覆盖 A2A 职责或反之。
- 锁定协议版本，在 CI 同发布通道测试。
- 企业场景：AAIF 成员资格（250+ 组织含所有主流云与 AI 实验室）已具真实分量。

> 一句话：协议之战结束，栈已定。Build something。
