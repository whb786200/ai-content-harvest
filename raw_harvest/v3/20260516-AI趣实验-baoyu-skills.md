---
title: "baoyu-skills内容自动化工作流"
source: "AI趣实验"
date: 2026-03-31
url: "https://mp.weixin.qq.com/s/z6Flju_7VgDuFqUybszP-w"
tags: [AI-Skills, 内容创作, baoyu-skills]
---
# baoyu-skills：内容生产自动化工作流

## 核心原则
`Script > Skill > Agent` — 固定动作脚本化、重复规则技能化、高价值判断工作交给AI。

## 四层链路
1. **素材采集层**：baoyu-url-to-markdown / baoyu-youtube-transcript / baoyu-danger-x-to-markdown
2. **成稿整理层**：baoyu-translate / baoyu-format-markdown
3. **视觉表达层**：baoyu-cover-image / baoyu-article-illustrator / baoyu-infographic / baoyu-xhs-images / baoyu-slide-deck
4. **发布分发层**：baoyu-post-to-wechat / baoyu-post-to-x / baoyu-post-to-weibo

## 安装
```bash
npx skills add jimliu/baoyu-skills
```

## 最小闭环
先装5个核心技能跑通素材→成稿→发布的基础流程，再逐步扩展。
