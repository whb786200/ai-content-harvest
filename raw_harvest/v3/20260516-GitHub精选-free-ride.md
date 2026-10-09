---
title: "GitHub精选-free-ride免费AI"
source: "GitHub精选"
date: 2026-04-01
url: "https://mp.weixin.qq.com/s/WP7olmRKMUY2qohwR8ckrA"
tags: [AI-Skills, 免费, OpenRouter]
---
# free-ride：免费用AI的正确姿势

## 核心价值
自动配置OpenRouter免费模型，遇到限速自动降级切换。

## 工具栈
| 工具 | 作用 |
|------|------|
| free-ride | 自动配置免费模型+降级策略 |
| OpenRouter | 30+免费模型聚合 |
| OpenClaw | AI助手框架 |
| freeride-watcher | 守护进程，持续监控轮换模型 |

## 安装
```bash
freeride auto
openclaw gateway restart
freeride-watcher --daemon  # 持续监控
```

## 模型列表示例
主力：openrouter/nvidia/nemotron-3-nano-30b:free (256K)
备选：qwen3-coder、step-3.5、deepseek、mistral
