---
title: tech-radar — Agent的科技情报中心
source: 01fish 公众号
date: 2026-05-16
tags: [AI-Skills, 科技情报, tech-radar, 信息采集, 日报]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/Ky_jodFHfcCkhwioERZuwA
---

# tech-radar — 科技情报中心蒸馏

## 核心主题
tech-radar：Agent驱动的科技情报系统，7个Node.js脚本并行采集7个主流科技信息源，三层架构（采集→AI分析→主编综合）输出含行动建议的日报，支持飞书推送和交互式工作台。

## 方法论/认知框架

**三层架构设计**
```
脚本采集层 → 7个Node.js并行采集，不消耗AI token，10秒完成
AI分析层 → 4个独立分析师并行研判，互不依赖，精准聚焦
主编综合层 → 汇总所有报告，跨源关联，捕捉多源共振强信号
```

**信息源覆盖**
GitHub / Product Hunt / Hacker News / Reddit AI / X平台AI builder / Polymarket

## 核心亮点
- **交互式工作台**：日报中插入 `fish点评:指令` 自动触发动作
- **定时推送**：每天固定时间自动运行 + 飞书通知
- **高度可定制**：Markdown文件存储配置，可直接修改

## 金句
> "脚本采集不消耗AI token，AI只做分析决策——精准分层，降本增效"

## 适用场景
- 科技从业者：每日AI/科技情报追踪
- 团队情报同步：飞书自动推送日报
- 可定制化情报系统：Markdown配置即改即用

## 文章摘要
tech-radar是Agent驱动的科技情报中心。7个Node.js脚本并行采集GitHub/Product Hunt/Hacker News等7大信息源（10秒完成，不消耗AI token），经4个独立AI分析师并行研判后由主编综合交叉关联，输出附带行动建议的日报。支持飞书定时推送和交互式工作台。

---
*蒸馏自 01fish 公众号，2026-05-16*
