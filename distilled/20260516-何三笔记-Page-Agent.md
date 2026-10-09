---
title: Page Agent — 一行JS让网页变AI Agent
source: 何三笔记 公众号
date: 2026-05-16
tags: [AI-Agent, GUI, 阿里巴巴, 浏览器自动化]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/zj1pWBBpHjAQiJhj7v5RmQ
---

# Page Agent — 网页变AI Agent蒸馏

## 核心主题
阿里巴巴开源Page Agent：一行JS即可让任意网页具备AI Agent能力。核心创新是"文本化DOM"（无需截图和多模态模型），以及"inside-out"设计（AI住进应用，天然继承登录态）。

## 方法论/认知框架

**核心创新：文本化DOM**
```
遍历DOM树 → 提取可交互元素 → 生成文本描述 → 发给LLM决策
（无需截图 + 无需多模态模型）
```

**"inside-out"设计哲学**
> 让AI住进应用，而非外部控制应用

天然继承登录态，无需为每个站点单独维护身份信息。

## 操作流

**快速接入（一行HTML）**
```html
<script src="https://cdn.jsdelivr.net/npm/page-agent/dist/index.global.js"></script>
```

**初始化调用**
```javascript
const agent = new PageAgent({
    model: 'qwen-plus',
    baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    apiKey: 'YOUR_API_KEY',
    language: 'zh-CN',
})
await agent.execute('点击登录按钮')
```

## 注意事项
- 仍处于早期阶段（highly experimental）
- 复杂页面（Shadow DOM、Canvas）可能表现不佳
- GitHub: github.com/alibaba/page-agent

## 适用场景
- 网页快速AI化：一行JS接入Agent能力
- 内部工具增强：给现有Web应用添加AI操作能力
- 替代浏览器自动化：比Playwright更轻量

## 文章摘要
阿里巴巴开源Page Agent，一行JS让网页变AI Agent。核心创新：文本化DOM（遍历DOM提取可交互元素生成文本描述，无需截图和多模态模型）；"inside-out"设计（AI住进应用，天然继承登录态）。仍早期阶段，复杂页面支持有限。

---
*蒸馏自 何三笔记 公众号，2026-05-16*
