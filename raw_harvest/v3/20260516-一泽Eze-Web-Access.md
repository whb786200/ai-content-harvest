---
title: "一泽Eze-Web Access Skill"
source: "一泽Eze"
date: 2026-04-10
url: "https://mp.weixin.qq.com/s/rps5YVB6TchT9npAaIWKCw"
tags: [AI-Skills, 浏览器, Agent]
---
# Web Access：拉满Agent联网和浏览器能力

## 理想Agent联网5大能力
1. 灵活分配策略（遇障碍换工具）
2. 复用登录态（不为每站点维护身份）
3. 强泛化能力（适应不同联网任务）
4. 支持并发（Sub-Agent分治）
5. 经验沉淀（下次访问不复蹈前辙）

## Skill设计哲学
`Skill = Agent策略哲学 + 最小完备工具集 + 必要的事实说明`

## 四步思考循环
```
① 定义成功标准 → ② 选起点验证 → ③ 过程校验 → ④ 对照标准停止
```

## 最小完备工具集
| 行为 | 工具 |
|------|------|
| 搜 | Search |
| 看 | Fetch/Curl / 浏览器打开 |
| 做 | 浏览器自动化（点击/填表/上传）|

GitHub: https://github.com/eze-is/web-access
