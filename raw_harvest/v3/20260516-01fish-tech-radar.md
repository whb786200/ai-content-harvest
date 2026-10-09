---
title: "tech-radar科技情报中心"
source: "01fish"
date: 2026-04-07
url: "https://mp.weixin.qq.com/s/Ky_jodFHfcCkhwioERZuwA"
tags: [AI-Skills, 科技情报, tech-radar]
---
# tech-radar：Agent的科技情报中心

## 核心能力
自动采集7个主流科技信息源，三层架构处理后输出附带行动建议的日报。

## 三层架构
| 层级 | 功能 | 特点 |
|------|------|------|
| 脚本采集层 | 7个Node.js脚本并行采集 | 不消耗AI token，10秒完成 |
| AI分析层 | 4个独立分析师并行研判 | 互不依赖，精准聚焦 |
| 主编综合层 | 汇总所有报告，跨源关联 | 捕捉多源共振强信号 |

## 信息源
Github、Product Hunt、Hacker News、Reddit AI、X平台AI builder、Polymarket等7个

## 特色功能
- **交互式工作台**：日报中插入`fish点评:指令`自动触发动作
- **定时推送**：每天固定时间自动运行+飞书通知
- **高度可定制**：Markdown文件存储配置，可直接修改

## 安装
GitHub: https://github.com/OrangeViolin/tech-radar
