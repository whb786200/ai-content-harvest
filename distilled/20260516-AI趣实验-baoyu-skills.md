---
title: baoyu-skills — 内容生产自动化工作流
source: AI趣实验 公众号
date: 2026-05-16
tags: [AI-Skills, 内容创作, baoyu-skills, 自动化, 工作流]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/z6Flju_7VgDuFqUybszP-w
---

# baoyu-skills — 内容自动化工作流蒸馏

## 核心主题
baoyu-skills：Jim Liu开源的内容生产自动化Skills体系。核心原则"Script > Skill > Agent"，将内容生产拆解为素材采集→成稿整理→视觉表达→发布分发四层链路。

## 方法论/认知框架

**核心原则：Script > Skill > Agent**
```
固定动作 → 脚本化
重复规则 → 技能化
高价值判断 → 交给AI
```

**四层链路架构**
| 层级 | Skills | 功能 |
|------|--------|------|
| 素材采集层 | url-to-markdown, youtube-transcript, danger-x-to-markdown | 多源素材抓取 |
| 成稿整理层 | translate, format-markdown | 翻译+格式化 |
| 视觉表达层 | cover-image, article-illustrator, infographic, xhs-images, slide-deck | 封面/插图/信息图/小红书图/PPT |
| 发布分发层 | post-to-wechat, post-to-x, post-to-weibo | 微博/微信/X平台发布 |

## 操作流

```bash
npx skills add jimliu/baoyu-skills
# 最小闭环：先装5个核心技能跑通素材→成稿→发布
```

## 对 1052-OS 的参考价值
- **Script > Skill > Agent 原则**与 1052-OS 当前的认知蒸馏管线高度契合
- 四层链路架构可对标 1052-OS 的 harvest→distill→merge→publish 管线
- 最小闭环思路：先跑通核心流程再扩展

## 金句
> "固定动作脚本化、重复规则技能化、高价值判断交给AI"

## 文章摘要
baoyu-skills是Jim Liu开源的内容生产自动化Skills体系。核心原则Script > Skill > Agent，四层链路：素材采集（url/youtube/x平台）、成稿整理（翻译/格式化）、视觉表达（封面/插图/信息图/PPT）、发布分发（微信/x/微博）。npx一键安装，建议先装5个核心技能跑通最小闭环。

---
*蒸馏自 AI趣实验 公众号，2026-05-16*
