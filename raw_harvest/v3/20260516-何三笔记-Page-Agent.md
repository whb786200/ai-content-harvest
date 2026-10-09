---
title: "何三笔记-Page Agent"
source: "何三笔记"
date: 2026-04-08
url: "https://mp.weixin.qq.com/s/zj1pWBBpHjAQiJhj7v5RmQ"
tags: [AI-Agent, GUI, 阿里巴巴]
---
# Page Agent：一行JS让网页变AI Agent

## 核心创新
**文本化DOM** — 遍历DOM树，提取可交互元素生成文本描述发给LLM，无需截图和多模态模型。

## "inside-out"设计
让AI住进应用，而非外部控制应用。天然继承登录态。

## 快速体验
```html
<script src="https://cdn.jsdelivr.net/npm/page-agent/dist/index.global.js"></script>
```

## 初始化
```javascript
const agent = new PageAgent({
    model: 'qwen-plus',
    baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    apiKey: 'YOUR_API_KEY',
    language: 'zh-CN',
})
await agent.execute('点击登录按钮')
```

## 注意
- 仍处于早期阶段（highly experimental）
- 复杂页面（Shadow DOM、Canvas）可能表现不佳
- GitHub: https://github.com/alibaba/page-agent
