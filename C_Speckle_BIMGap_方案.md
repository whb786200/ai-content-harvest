# C. Speckle 集成方案 + BIMGap 分析

> 阶段：P3 长期探索（不需要立即执行，产出设计方案）

---

## 一、Speckle 是什么

| 属性 | 说明 |
|------|------|
| 定位 | AEC 行业开源数据协作平台（类似 Figma 之于设计） |
| 核心功能 | BIM 数据实时同步、版本管理、Web 可视化、API 访问 |
| 支持格式 | IFC, Revit, Rhino, Blender, Tekla 等 |
| 部署方式 | 自托管（Docker）或 Speckle Cloud |
| Python SDK | `specklepy`（官方，但 PyPI 包可能不完整，推荐从 GitHub 安装） |

---

## 二、1052-OS × Speckle 集成架构

### 2.1 目标
将 **1052-OS 认知蒸馏流水线** 与 **Speckle BIM 数据** 打通，实现：
1. Speckle 模型变更 → 自动触发认知蒸馏
2. 蒸馏结果 → 写回 Speckle Comments/Issues
3. BIM 模型中的规范条文引用 → 自动关联 PDF 规范库

### 2.2 架构图

```
Speckle Server (自托管 / Cloud)
    │
    │  Webhook (模型更新事件)
    ▼
n8n 工作流 (或 WorkBuddy 定时任务)
    │
    ├──→ 拉取模型数据 (Speckle API / GraphQL)
    ├──→ 解析 IFC 数据 (ifc-quantity-extractor Skill)
    ├──→ 对照规范条文 (pdf-spec-extractor Skill)
    └──→ 推送结果到 Speckle (Comment / Issue / BIM Counter)
            │
            ▼
    项目团队（在 Speckle Viewer 中直接看到规范符合性报告）
```

### 2.3 技术栈

| 组件 | 选型 | 说明 |
|------|------|------|
| Speckle Server | Docker 自托管 | `speckle/server` 镜像 |
| Python SDK | `specklepy` (GitHub main 分支) | `pip install git+https://github.com/specklesystems/specklepy.git` |
| Webhook | n8n HTTP Request | 监听 `commit.create` 事件 |
| 数据写入 | Speckle GraphQL API | 创建 Comment / Issue |
| 可视化 | Speckle Viewer (JS) | 在浏览器展示 BIM + 标注 |

---

## 三、实施步骤（3 阶段）

### 阶段 1：基础连接（1 周）

```bash
# 1. 安装 specklepy（从 GitHub）
python -m pip install git+https://github.com/specklesystems/specklepy.git

# 2. 验证连接
python -c "
from specklepy.api.client import SpeckleClient
from specklepy.transports.server import ServerTransport
client = SpeckleClient(host='http://localhost:3000')
# 需要 token
"

# 3. 部署 Speckle Server（Docker）
docker run -d -p 3000:3000 speckle/speckle-server:latest
```

### 阶段 2：工作流集成（2 周）

- n8n 工作流增加 Speckle Trigger（Webhook）
- 模型更新 → 触发 `ifc-quantity-extractor`
- 提取工程量 → 对照 `pdf-spec-extractor` 规范条文
- 结果通过 Speckle API 写回 Comment

### 阶段 3：双向协同（4 周）

- Speckle Viewer 中选中构件 → WorkBuddy 返回规范条文 + 历史案例
- 规范更新（PDF 新版本）→ 推送到 Speckle Project as Issue
- 移动端（微信/飞书）接收 Speckle 通知

---

## 四、BIMGap 分析：1052-OS vs DDC

### 4.1 能力对比矩阵

| 维度 | 1052-OS | DDC Skills (221个) | Gap |
|------|----------|---------------------|-----|
| **知识蒸馏** | ✅ 完整（v11.0，152模块） | ❌ 无 | 1052 领先 |
| **IFC 解析** | ❌ 依赖外部 | ✅ ifc-to-excel（IfcOpenShell） | **需补齐** |
| **规范结构化** | ❌ 无 | ✅ pdf-spec-extractor（本阶段已创建） | 已补齐 |
| **BIM 可视化** | ❌ 无 | ❌ 无（但 DDC 引用 xeokit） | 共同缺口 |
| **实时协作** | ❌ 无 | ❌ 无（Speckle 可补齐） | **共同缺口** |
| **成本分析** | ✅ cost-management (升级版) | ✅ budget-variance-analyzer | 持平 |
| **安全管理** | ✅ safety-management (升级版) | ✅ safety-inspection-checklist | 持平 |
| **会议纪要** | ✅ meeting-minutes-generator | ❌ 无 | 1052 领先 |
| **n8n 自动化** | ✅ 本阶段已部署 | ❌ 无 | 1052 领先 |
| **缺陷检测** | ✅ defect-detection (轻量版) | ❌ 无 | 1052 领先 |
| **Speckle 集成** | ❌ 无（本方案设计） | ❌ 无 | **共同缺口** |

### 4.2 推荐补齐顺序

| 优先级 | 能力 | 预计工作量 |
|--------|------|------------|
| **P0** | IFC 解析完整化（修 bugs + 支持几何输出） | 3 天 |
| **P1** | Speckle 基础连接（阶段 1） | 1 周 |
| **P2** | BIM 可视化（xeokit-sdk + 规范标注叠加） | 2 周 |
| **P3** | 移动端协同（微信/飞书 + Speckle 通知） | 3 周 |

### 4.3 最终能力蓝图

```
1052-OS 完整能力版图：

知识层（已有）    工具层（已有）      协同层（规划）
─────────────    ──────────────      ──────────────
认知蒸馏 v11.0  →  IFC解析          →  Speckle 实时协作
152个模块        →  规范结构化        →  微信/飞书通知
公众号运营       →  缺陷检测          →  移动端查看 BIM
n8n 自动化      →  成本/安全管理     →  现场拍照→AI识别→推送到 BIM
```

---

## 五、下一步行动

- [ ] **立即**：安装 `specklepy` 从 GitHub（当前 PyPI 版本不完整）
- [ ] **本周**：Docker 部署 Speckle Server（localhost:3000）
- [ ] **下周**：写 `speckle-integration.py`（连接测试 + 创建第一个 Comment）
- [ ] **长期**：xeokit-sdk 集成（Web 端 BIM 查看器 + 规范标注叠加）

---

*创建时间：2026-05-23 13:30*
*作者：WorkBuddy AI*
