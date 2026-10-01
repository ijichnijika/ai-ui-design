# AI UI Design Intelligence (`ai-ui-design`) 🎨

> **Anti-Mediocrity UI Design Intelligence System for AI Coding Assistants**  
> 突破大模型“下一个 Token 陷阱”，通过外部熵种子注入、无状态 Critic 视觉审查闭环、人机共创小样试玩、风格对比页与残忍删减，产出具辨识度与克制感的顶级界面。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Compatible with Antigravity & Claude Code](https://img.shields.io/badge/Compatible-Antigravity%20%7C%20Claude%20Code%20%7C%20Cursor-brightgreen.svg)](#-installation)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/ijichnijika/ai-ui-design/pulls)

---

## 💡 核心设计理念

大语言模型（LLM）叠加 RLHF 后天然寻找“符合最多人偏好的安全公约数”，在没有外部推力时必然输出蓝紫渐变、圆角卡片嵌套与通用图标等平庸的“委员会设计”。

本 Skill 旨在**强行将模型推离其统计可预测区间**，建立一套对抗统计平均、追求真实质感与克制美学的完整工程协议。

```text
[新需求启动]
  │
  ▼
[阶段一：头脑风暴与方向共创 (Pattern 3)]  <──【强制人机协同，严禁 AI 单向启动全站重构】
  ├─ Turn 1: 提出 6-8 个极端概念隐喻（故意省略细节）
  ├─ Turn 2: 引导人类注入触觉、材质偏好并排查雷区
  ├─ Turn 3: 产出轻量候选小样并通过内置对比页 (Pattern 7) 并排交付
  └─ Turn 4: 人类在浏览器真实试玩对比，跨方案拼装优势 ──> 锁定终版生产级 POC
  │
  ▼
[阶段二：工程实现与双智能体审查闭环]
  ├─ 注入外部随机种子 (Pattern 1) + 正式编写生产级组件代码
  ├─ 自动调用内置生图 (Pattern 4) 或索取 API Key 隔离于 .env.agents 生成核心资产
  ├─ 捕获浏览器全保真渲染截图 + 准备 Moodboard 参考基准
  ├─ 【主动询问用户】确认评审模式：
  │    ├─ 选项 A：严格 ≥9 分模式（门禁隔离，最多 3 轮迭代直至达标）
  │    └─ 选项 B：单轮诊断模式（1 轮全面体检，快速吸收修改建议）
  └─ 调起独立无状态 Critic 子智能体 (Pattern 2)
       ├─ [严格模式] 评分 < 9 ──> 输出整改指令 ──> Worker 修复代码 ──> 重新提审 (上限 3 轮)
       ├─ [严格模式] 评分 >= 9 ─> 进入 Deliver 阶段
       └─ [单轮模式] 采纳 3-5 条关键建议修正 ──> 进入 Deliver 阶段
  │
  ▼
[阶段三：残忍删减与最终交付]
  ├─ 排查消除 7 大“AI 味”沉疴
  ├─ 复杂动效/材质替换为多模态资产 (Pattern 5 & 6)
  └─ 原生规范化，向人类交付终稿
```

---

## ✨ 核心能力与实操模式

### 1. 外部熵种子注入 (External Entropy)
大模型无法自发产生真正的随机性。通过系统外部高熵种子（`openssl rand -hex 16`）注入 Prompt，强制模型将字符节奏映射为独特的色彩跨度、网格律动与视觉隐喻，阻断概率收敛。

### 2. 双智能体无状态 Critic 审查闭环 (Stateless Critic)
编写代码的智能体受沉没成本与自我解释偏见影响，无法客观评判自身设计。
- **物理隔离**：通过 `invoke_subagent` 调起独立审查智能体，仅接收真实渲染截图与行业顶级参考图（Moodboard），严禁透传代码与对话历史。
- **主动询问模式**：评审前主动向用户确认采用 **严格 ≥9 分门禁（上限 3 轮）** 还是 **单轮快速诊断**。
- **门禁隔离原则**：及格门槛绝不向 Critic 泄露，多轮迭代复用统一提示词，杜绝打分通胀。

### 3. 人机共创与多方向验证 (Human-in-the-Loop)
在正式工程编码前，严禁 AI 单向闭门编写全站代码。通过发散 6–8 个极端视觉隐喻并引导用户注入触觉/材质偏好，快速产出候选小样，由人类在浏览器中真实上手试玩与决策。

### 4. 离线风格对比页工具 (Style Explorer)
内置 Python 自动化构建脚本（[`scripts/build_explorer.py`](skills/ai-ui-design/scripts/build_explorer.py)），可根据 `manifest.json` 将各候选方案、本地 dev server 或截图打包为单个高便携离线 HTML：
- 桌面（1280×900）与手机（390×844）同屏并排比对；
- 真实尺寸 100% 验收；
- 键盘快捷键（`←` / `→` / `Esc` / `P`）盲切与即点即选；
- DOM 元素点选高亮与浮动批注卡片，自动复制标注指令回传 Agent；
- 具备严格 CSP 沙箱与内存级 `localStorage` 隔离垫片。

### 5. 残忍删减与去容器化 (Ruthless Subtraction & De-containering)
- **去容器化**：坚决摒弃把每个模块、条目逐层套成圆角卡片的恶习（容器嵌套层级深度严格 $\le 1$），依靠字阶差、严格网格与留白建立空间秩序。
- **根治 7 大 AI 视觉异味**：坚决清除蓝紫弥散渐变、多层卡片嵌套、随机占位小图标、全屏文本偷懒居中、空洞套话文案、浮夸大字号、粗糙纯 CSS 3D 旋转。

### 6. 多模态资产融合与凭据隔离
杜绝纯 CSS 粗劣模拟复杂高光与拟物。主动调用内置多模态工具（如 `generate_image`）产出高精 3D 实体与真实物理材质；若需外部 API，强制隔离于 `.env.agents`（加入 `.gitignore`），严禁凭据泄露。

---

## 📁 目录架构

```text
ai-ui-design/
├── plugin.json                                 # Agent 插件清单
├── LICENSE                                     # MIT 开源协议
├── README.md                                   # 项目全景说明
└── skills/
    └── ai-ui-design/
        ├── SKILL.md                            # 核心执行规范与阶段指引
        ├── patterns.md                         # 7 大落地设计模式库
        ├── cheatsheet.md                       # 决策树、异味排查表与度量基准
        ├── glossary.md                         # 核心专业术语词典
        ├── assets/
        │   └── style-explorer.html             # 风格对比页离线容器模板
        ├── scripts/
        │   └── build_explorer.py               # 风格对比页自动化生成脚本
        └── references/
            ├── design-direction.md             # 调性刻度、生成引擎与首屏骨架
            ├── visual-language.md              # 焦点、空间、字体排版与图标选型
            ├── visual-review.md                # 独立评审协议、交接清单与模板
            ├── style-explorer.md               # 风格对比页使用规范与 manifest 说明
            ├── imagery.md                      # 配图生成 7 步公式与融边接力
            ├── motion.md                       # 动效手感、物理参数映射与时长规范
            └── layout-and-viewport.md          # 截图精准还原与视口安全区验证
```

---

## 🚀 安装与使用

### 在 Google Antigravity 中使用

将本技能目录克隆或放入 Antigravity 全局技能目录：

```bash
# 全局安装
git clone https://github.com/ijichnijika/ai-ui-design.git ~/.gemini/config/skills/ai-ui-design-repo
cp -r ~/.gemini/config/skills/ai-ui-design-repo/skills/ai-ui-design ~/.gemini/config/skills/
```

或直接在项目中通过自然语言或命令触发：
```text
/ai-ui-design 请为我们的开发者分析平台设计首屏视觉
```

### 在 Claude Code / Cursor / Amp 中使用

将 `skills/ai-ui-design/SKILL.md` 及相关引用放入项目 `.claude/skills/` 或工作区规则即可原生兼容。

---

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源。
