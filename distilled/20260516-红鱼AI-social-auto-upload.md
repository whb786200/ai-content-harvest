---
title: social-auto-upload — 7平台自动发布
source: 红鱼AI 公众号
date: 2026-05-16
tags: [自媒体, 自动发布, 开源, Playwright, Cookie管理]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/JveoZRwCsRKgg-pblfkBQA
---

# social-auto-upload — 多平台自动发布蒸馏

## 核心主题
social-auto-upload：7平台（抖音/B站/小红书/快手/视频号/百家号/TikTok）自动发布系统，支持定时上传/Cookie智能管理/Proxy代理，3人工作→1人定时发布，效率提升300%。

## 工具链

**支持平台（7个）**
抖音 / Bilibili / 小红书 / 快手 / 视频号 / 百家号 / TikTok

**技术栈**
| 组件 | 技术 |
|------|------|
| 后端 | Python + Playwright（Chromium/Firefox） |
| 前端 | Node.js + Vite（端口5173） |
| 数据库 | Python createTable.py |
| Cookie管理 | get_xxx_cookie.py 自动获取 |

## 操作流

**8步部署**
```bash
git clone https://github.com/dreammis/social-auto-upload.git
conda create -n social-auto-upload python=3.10
pip install -r requirements.txt
playwright install chromium firefox
cp conf.example.py conf.py  # 配置Chrome路径
cd db && python createTable.py
python examples/get_xxx_cookie.py  # 获取Cookie
python sau_backend.py  # 后端端口5409
npm run dev  # 前端端口5173
```

## 核心功能
- 定时上传（Cron Job）
- Cookie智能管理（自动刷新）
- 国外平台Proxy代理
- Web前端管理界面
- RESTful API封装

## 对1052-OS的参考价值
- **7平台发布**：与1052-OS的social-auto-upload/目录直接对应
- **Cookie智能管理**：可借鉴到1052-OS的自动化发布管线
- **效率提升300%**：工程化管理思维

## 适用场景
- 短视频矩阵运营：7平台一键发布
- 团队协作：1人替代3人上传工作
- 跨平台内容分发：统一管理多平台账号

## 文章摘要
social-auto-upload是7平台自动发布系统（抖音/B站/小红书/快手/视频号/百家号/TikTok）。Python+Playwright后端，Node.js前端，支持定时上传/Cookie智能管理/Proxy代理。8步部署，3人工作→1人定时发布，效率提升300%。

---
*蒸馏自 红鱼AI，2026-05-16*
