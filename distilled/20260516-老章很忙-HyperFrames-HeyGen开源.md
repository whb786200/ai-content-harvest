---
title: HyperFrames — HeyGen开源HTML视频渲染框架
source: 老章很忙 + 空格的键盘 公众号
date: 2026-05-16
tags: [HyperFrames, HeyGen, HTML视频, Skills, Claude-Code, FFmpeg, 视频生产]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/CBEqkDH-Q8Z2j1iuvg6K5Q
---

# HyperFrames — HTML视频渲染框架蒸馏

## 核心主题
HeyGen开源的HTML视频渲染框架：以HTML编写视频，GSAP做动画，headless Chrome逐帧抓取+FFmpeg编码生成MP4。5个Skills模块覆盖从编写到渲染的全流程，Apache 2.0完全开源可商用。

## 核心方法论

**"视频即代码"范式**
```
每个场景 = HTML页面
动画 = GSAP时间线
音轨 = HTML audio标签
渲染 = headless Chrome逐帧 + FFmpeg编码 → MP4
```

**为什么HTML路线优于React**
> HTML生成的准确率远高于生成完整React项目，无构建步骤，反馈链路极短，对AI Agent更友好

## 工具链

### 5个 Skills 模块
| Skill | 功能 |
|-------|------|
| hyperframes | HTML composition编写、字幕、TTS、转场 |
| hyperframes-cli | CLI命令：init/lint/preview/render/transcribe/tts |
| hyperframes-registry | 通过add安装区块和组件 |
| website-to-hyperframes | 抓取URL直接转视频 |
| gsap | GSAP动画API、时间轴、ScrollTrigger |

### 与 Remotion 对比
| 维度 | HyperFrames | Remotion |
|------|------------|----------|
| 许可 | Apache 2.0 完全开源 | source-available（大团队需付费） |
| 技术路线 | HTML原生（Agent友好） | React路由 |
| 构建 | 无构建步骤 | 需要构建 |
| 分布式渲染 | 无 | Lambda分布式渲染 |

## 操作流

```bash
# Claude Code 安装
npx skills add heygen-com/hyperframes

# 手动安装使用
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

## 对 1052-OS 的参考价值
- Skills模块架构：5个skill模块化拆分，与1052-OS的skill体系一致
- "HTML原生 = Agent友好"：AI生成HTML的成功率可作为1052-OS自动排版的技术选型参考
- 视频生产新范式：网页→视频的路径可替代传统剪辑流程

## 文章摘要
HeyGen开源HyperFrames HTML视频渲染框架（Apache 2.0）。核心理念"视频即代码"：每个场景是HTML页面，动画用GSAP时间线，音轨用HTML audio标签，通过headless Chrome逐帧抓取+FFmpeg编码生成MP4。提供5个Skills模块（编写/CLI/组件注册/URL转视频/GSAP动画）。6类高适配场景，与Remotion对比在开源许可和Agent友好度上占优。环境要求Node.js≥22+FFmpeg。

---
*蒸馏自 老章很忙 公众号，2026-05-16*
