---
title: HyperFrames — HeyGen开源HTML视频渲染框架
author: 老章很忙 + 空格的键盘
date: 2026-04-27 / 2026-05-08
source: https://mp.weixin.qq.com/s/CBEqkDH-Q8Z2j1iuvg6K5Q
tags: [HyperFrames, HeyGen, HTML视频, Skills, Claude-Code, FFmpeg]
category: AI视频
---

# HyperFrames — Write HTML, Render Video, Built for Agents

## 项目信息
- **GitHub**: github.com/heygen-com/hyperframes
- **许可证**: Apache 2.0（完全开源，商用无限制）
- **环境**: Node.js >= 22 + FFmpeg

## 核心理念
将视频作为代码编写——每个场景是HTML页面，动画是GSAP时间线，音轨是HTML audio标签，最终通过headless Chrome逐帧抓取+FFmpeg编码生成MP4。

## 5个Skills模块
| Skill | 功能 |
|-------|------|
| hyperframes | HTML composition编写、字幕、TTS、转场 |
| hyperframes-cli | CLI命令：init/lint/preview/render/transcribe/tts |
| hyperframes-registry | 通过add安装区块和组件 |
| website-to-hyperframes | 抓取URL直接转视频 |
| gsap | GSAP动画API、时间轴、ScrollTrigger |

## 安装
```bash
# Claude Code
npx skills add heygen-com/hyperframes

# 手动
npx hyperframes init my-video
cd my-video && npx hyperframes preview
npx hyperframes render
```

## 6类高适配场景
1. 网站/PPT转产品宣传片
2. 文章配视频
3. 产品发布片
4. 知识科普切片
5. Brief转方案展示
6. 教程演示视频

## vs Remotion
- HyperFrames: Apache 2.0开源 / HTML原生（Agent友好） / 无构建步骤
- Remotion: source-available（大团队需付费） / React路由 / 有Lambda分布式渲染

## 关键洞察
> HTML路线比React更适合Agent——大模型生成HTML准确率远高于生成完整React项目，无构建步骤，反馈链路极短
