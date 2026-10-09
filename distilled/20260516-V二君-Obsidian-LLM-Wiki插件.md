---
title: Obsidian LLM Wiki插件 — 零配置知识生成
source: V二君 公众号
date: 2026-05-16
tags: [Obsidian, LLM-Wiki, 插件, 知识管理, 零配置]
type: distilled
distilled_at: 2026-05-30
original_url: https://mp.weixin.qq.com/s/vKamXXBWbg4CIXWGrAre7g
---

# Obsidian LLM Wiki插件蒸馏

## 核心主题
lite-llm-wiki：Obsidian零配置AI知识生成插件，右键文件/目录即可自动生成Wiki词条，内置免费模型+自动降级，提示词可视化编辑。

## 工具信息
| 属性 | 值 |
|------|-----|
| GitHub | github.com/kinaito/lite-llm-wiki |
| 安装方式 | 手动下载→解压→Obsidian插件目录→启用 |
| 定价 | 免费（公共API模式）/ 自备Key（私有模式） |

## 核心功能
1. **零配置开箱即用**：安装后右键文件/目录即可生成，无需改脚本配环境
2. **内置模型+自动降级**：内置大语言模型，一个挂了自动切换下一个
3. **双模式数据安全**：公共API模式（免费）/ 私有API模式（自己的Key）
4. **提示词可视化编辑**：设置页直接修改，改完即时生效，可一键恢复默认
5. **快捷右键菜单**：标记LLW，支持单文件/多文件/目录

## 与 1052-OS 关联
- 1052-OS 已有 Obsidian 同步机制（pipeline_config.obsidian_sync）
- LLM-Wiki 的"零配置右键生成"思路可与 1052-OS 蒸馏管线结合：在 Obsidian 中直接触发蒸馏操作
- 自动降级策略启示：蒸馏管线也可实现多模型 fallback

## 金句
> "最好的效率工具，从来不是功能最多的那个，而是让你感觉不到它存在的那个"

## 适用场景
- Obsidian 重度用户：快速生成笔记词条和知识图谱
- 知识管理：自动化Wiki生成减少手动整理
- 个人知识库构建：右键即生成，零心智负担

## 文章摘要
lite-llm-wiki 是 Obsidian 零配置 AI 知识生成插件。核心特性：右键文件/目录自动生成 Wiki 词条、内置免费模型并支持自动降级切换、双模式数据安全（公共/私有API）、提示词可视化编辑即时生效。安装简单，无门槛上手。

---
*蒸馏自 V二君 公众号，2026-05-16*
