---
title: "social-auto-upload多平台自动发布"
source: "红鱼AI"
date: 2026-04-03
url: "https://mp.weixin.qq.com/s/JveoZRwCsRKgg-pblfkBQA"
tags: [自媒体, 自动发布, 开源]
---
# social-auto-upload：7平台自动发布

## 支持平台
抖音、Bilibili、小红书、快手、视频号、百家号、TikTok

## 核心功能
- 定时上传（Cron Job）
- Cookie智能管理
- 国外平台Proxy代理
- Web前端管理界面
- RESTful API封装

## 8步部署
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

## 效率提升
3人上传工作→1人定时发布，效率提升300%
