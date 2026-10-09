---
source: CloudPro Consulting
url: https://cloudproinc.com.au/index.php/2026/08/28/microsoft-agent-framework-production-guide-for-a2a-mcp-governance
published: 2026-08-28
harvested_at: 2026-08-28
harvest_method: web_fetch
model_selection: hunyuan-turbo
tags: [Microsoft Agent Framework, A2A, MCP, 生产化, 治理, 中间件, 长运行]
---

# Microsoft Agent Framework Production Guide for A2A MCP Governance

面向把 AI agent 推向生产的企业的指南：最新发布改了什么、新风险在哪、技术负责人现在该审什么。

## 框架定位与版本
Microsoft Agent Framework 是构建运行 AI agent 的开源基座，给模型套上结构：用审批工具、记住工作、遵循流程、与其他 agent 协作。
- 2026 年 4 月达 .NET/Python 1.0 GA（稳定核心）。
- **截至 2026/8/27 发布列车：.NET 1.19.0 / Python 1.15.0**。
- 近期改进聚焦运维细节（决定 agent 能否在真实业务被信任），而非聊天花活：
  - 更可靠的状态/会话持久化（重启后继续）
  - 更好的长运行可恢复 hosted agent 支持
  - A2A 跨 agent 通信更新
  - 支持最新 MCP 长任务方案
  - 更强中间件/拦截以强制策略
  - 改进 agent 与 workflow 活动监控

## A2A 正在成为实用的服务边界
A2A 是让独立 agent 发现彼此、交换消息、协调工作的开放通信标准（跨团队/跨技术平台的"数字工人通用语言"）。
- .NET 新版修复 A2A 流式 artifact 更新：agent 在另一 agent 仍工作时可靠接收文件/结构化结果/部分输出。
- 例：合规 agent 渐进把发现返回给采购 agent，而非让整个流程等一个最终响应。
- **何时不该用 A2A**：两 agent 同应用同团队 → 直接内部 workflow 更简单、更快、更便宜。
- 用 A2A 的时机：跨越系统/团队/编程语言/组织间真实边界。

## MCP 现在能处理不立即完成的工作
MCP 是 agent 连业务工具/数据的标准；7 月规范引入 **Tasks 扩展**处理可能耗时数分至数时的操作——不再长连接赌不超时，而是建可查/可更新/可恢复的长久任务。
- Microsoft Agent Framework .NET 1.19.0 把长运行 MCP 支持迁移到新 Tasks 模型——**破坏性变更**，现有实现应测试而非自动升级。
-  upside：文档分析、批报、审批流、安全调查的更可靠自动化。
-  risk：长任务在原始用户离开后仍可能持续消耗资金/访问系统 → 身份、时限、成本限额、取消控制必须进设计。

## 治理进入 agent 运行时
书面 AI 政策无法阻止 agent 凌晨 2 点未授权工具调用；生产治理需在 agent 真正决策与行动的运行时内加控制。
- Agent Framework 支持 **middleware**（检查点）：请求放行前可校验输入、拦截工具、请求人审、强制花费限额、记审计事件。
- 新方向：通用 **agent-hooks 契约**跨模型调用/工具使用/最终输出应用控制（部分仍实验，作方向而非立即替换既证实控制）。
- 简单生产控制契约示例：
```
Agent: Supplier Invoice Review
Can read: 发票邮箱与采购单
Can propose: 不匹配标记与编码建议
Needs approval: 银行信息变更与付款释放
Cannot access: 薪酬或客户身份记录
Must log: 每次工具调用、A2A 交接、审批
Stop conditions: 成本限额、超时或策略失败
```
- 业务结果=可问责：出事时可定哪个 agent 行动、用谁身份、访问何信息、何策略允许。

## 持久化与恢复已成董事会级议题
- 会话持久化改进（状态可存 Azure Blob Storage），hosted agent 恢复增强——基础设施故障后恢复工作而不重来或重复已完成动作。
- 减少浪费 AI 用量、防重复业务事务；但 agent 存储状态可能含客户详情/内部文档/商业敏感推理史 → 新数据管理责任（保留期/存储地/可取回者）。

## 200 人企业场景
发票审核 agent 用 MCP 读发票与采购单 → 用 A2A 问独立管理的合规 agent 查异常供应商变更；准备异常报告但银行信息变更/付款须财务人审；会话存储可恢复，每次工具调用与 agent 交接记录备查。
价值不在 AI 能读发票，而在更快异常处理、更少重复检查、清晰审批链，且不给单一大 agent 整个财务环境的无限制访问。

## 技术负责人下一步
1. 盘点每个 agent 与 MCP 连接（owner/用途/数据访问/模型/托管地/业务影响）。
2. 锁定并测试框架版本（协议与依赖快速变化，勿自动生产升级）。
3. 区分 A2A 与 MCP 用例（agent 间通信用 A2A，工具/数据受控访问用 MCP）。
4. 测试失败与恢复（超时/重复消息/权限撤销/部分结果/基础设施重启）。
5. 加可执行控制（受限身份、中间件、人审、预算、明确停止条件）。
6. 监控业务结果（处理时长/错误率/审批延迟/AI 消耗/事件）而非数对话数。

> 真正的生产里程碑是**控制**：A2A/MCP/长运行 agent 更有用，也更能深入业务运营，抬高了弱身份/不清所有权/弱监控的代价。
