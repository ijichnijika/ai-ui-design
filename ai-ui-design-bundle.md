# AI UI Design Intelligence - Full Knowledge Base Bundle

## Path: `plugin.json`

```json
{
  "name": "ai-ui-design",
  "description": "Antigravity & Claude Code UI design intelligence skill. Breaks LLM mediocrity via external entropy injection, stateless Critic review loops, human-in-the-loop candidate exploration, and ruthless subtraction."
}
```

## Path: `.gitignore`

```text
.DS_Store
*.log
.idea/
.vscode/
__pycache__/
*.pyc
*.pyo
.env*
dist/
build/
```

## Path: `LICENSE`

```text
MIT License

Copyright (c) 2026 nijika

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Path: `README.md`

````markdown
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
[阶段一：头脑风暴与方向共创]  <──【强制人机协同，严禁 AI 单向启动全站重构】
  ├─ Turn 1: 提出 6-8 个极端概念隐喻（故意省略细节）
  ├─ Turn 2: 引导人类注入触觉、材质偏好并排查雷区
  ├─ Turn 3: 产出轻量候选小样并通过内置对比页并排交付
  └─ Turn 4: 人类在浏览器真实试玩对比，跨方案拼装优势 ──> 锁定设计说明
  │
  ▼
[阶段二：工程实现与双智能体审查闭环]
  ├─ 注入外部随机种子 + 正式编写生产级组件代码
  ├─ 自动调用内置生图或索取 API Key 隔离于 .env.agents 生成核心资产
  ├─ 捕获浏览器全保真渲染截图 + 准备 Moodboard 参考基准
  ├─ 【主动询问用户】确认评审模式：
  │    ├─ 选项 A：严格 ≥9 分模式（门禁隔离，最多 3 轮迭代直至达标）
  │    └─ 选项 B：单轮诊断模式（1 轮全面体检，快速吸收修改建议）
  └─ 调起独立无状态 Critic 子智能体
       ├─ [严格模式] 评分 < 9 ──> 输出整改指令 ──> 修复代码 ──> 重新提审 (上限 3 轮)
       ├─ [严格模式] 评分 >= 9 ─> 进入 Deliver 阶段
       └─ [单轮模式] 采纳 3-5 条关键建议修正 ──> 进入 Deliver 阶段
  │
  ▼
[阶段三：残忍删减与最终交付]
  ├─ 排查消除 AI 味清单
  ├─ 复杂动效/材质替换为多模态资产
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
- **根治 AI 视觉异味**：坚决清除蓝紫弥散渐变、多层卡片嵌套、随机占位小图标、全屏文本偷懒居中、空洞套话文案、浮夸大字号、粗糙纯 CSS 3D 旋转。

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
        ├── assets/
        │   ├── style-explorer.html             # 风格对比页离线容器模板
        │   └── templates/
        │       └── design-brief.md             # 设计说明沉淀模板
        ├── scripts/
        │   ├── build_explorer.py               # 风格对比页自动化生成脚本
        │   ├── check_contrast.py               # WCAG 2.x 与 OKLCH 相对亮度对比度校验
        │   └── screenshot.py                   # 零依赖 CDP 无头截图与页面体检
        └── references/
            ├── build-and-verify.md             # 制作检查、CDP 截图取证与还原标准
            ├── design-direction.md             # 调性刻度、生成引擎、首屏骨架与方向卡
            ├── media.md                        # 素材选择、提示词公式、图码分工与视频
            ├── mockup-to-production.md         # 小样形态选择与主流框架 Token 平移落地
            ├── motion.md                       # 动效手感、物理参数映射与时长规范
            ├── style-explorer.md               # 风格对比页使用规范与 manifest 说明
            ├── visual-language.md              # 焦点、空间、排版、色彩与 AI 味排查
            └── visual-review.md                # 独立评审协议、交接清单与模板
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
````

## Path: `skills/ai-ui-design/SKILL.md`

````markdown
---
name: ai-ui-design
description: "界面设计与前端页面实现：新界面与多方向探索、风格对比、改版与视觉精修、截图还原、UI/UX 评审、去 AI 味。"
---

模型默认产出"委员会设计"：蓝紫渐变、居中圆角卡片、通用图标。本 Skill 的每一步都是把设计推离这个**可预测区间**的具体推力。以一个**北极星**组织构图、字体、色彩、素材和交互；克制是保留最有力的选择、删掉无贡献的元素，不是磨成中庸。

相对链接与命令里的 `<skill>` 都指本文件所在目录。按当前决策读取参考，不预先全部加载。

## 三条底线

- **用户的要求优先**：用户指定的风格、字体、配色和参考图照做，即使它出现在 AI 味清单里。清单只管用户没有指定的部分。
- **精修保留，改版替换**：精修沿用现有风格、文案和行为，不动范围外的东西。认为方向本身有问题时说出来，由用户决定是否改版。
- **只说看到的**：只使用在项目里读到过、或本轮核实过的组件、类名、Token、字体、图标与链接。只把亲眼看过截图的内容说成"已验证"，其余如实写"未验证"；自己做的判断在交付时列为假设。

## 选择范围

从请求、现有页面和参考资料确定用户、主要任务、真实内容、目标设备与交付形式。只在缺失信息会改变核心方向且无法推断时集中提问；可逆细节自行决定并简述假设。用户要求直接做完时，选方向、选评审模式这类需要用户拍板的环节按你的推荐走，交付时列为假设。

设计说明、小样、对比页、素材和评审记录都放**任务目录**（默认 `<项目根>/design/<主题>/`）。

| 范围 | 路径 |
| --- | --- |
| 单个元素、间距、文案、颜色 | 直接改，在目标视口看改动处和相邻元素，一两句话交付。跳过方向、评审，不产生文档 |
| 新界面，或要求重新探索 | 步骤 1–5 |
| 已有方向的深化或局部优化 | 从步骤 2 进入，只查受影响的区域与状态 |
| 存量项目精修、局部重构 | 先盘点页面、设计变量与共享组件，留基线截图，从步骤 2 进入，从源头改 |
| 存量项目改版 | 同样先盘点、留基线截图，再走步骤 1–5 |
| 截图还原 | 按 [制作与验证](references/build-and-verify.md) 锁定参考视口后进入步骤 2，沿用参考图风格 |
| UI/UX 评审 | 截图取证后只做步骤 4 的诊断，交付证据与建议 |

## 1. 与用户共创方向

读 [设计方向](references/design-direction.md)，按其中的轮次推进，每轮等用户回应。方向由用户的品味决定：每轮附上推荐与理由，请用户说出具体喜欢与排除什么。

完成标志：用户已选定（或拼装出）一个方向，且你按 [模板](assets/templates/design-brief.md) 在任务目录写下了设计说明。此前只做轻量小样，生产代码从这里开始。

## 2. 建立视觉与交互结构

| 要解决的问题 | 参考 |
| --- | --- |
| 层级、字体、色彩、空间、图标、示例数据、AI 味自查 | [视觉语言](references/visual-language.md) |
| 主图与配图、真实材质（玻璃、金属、3D）、生图与密钥、视频 | [素材](references/media.md) |
| 动效手感、过渡、滚动叙事 | [动效](references/motion.md) |

- 交代主要内容的视觉层级和关键操作链，覆盖默认状态以外的状态。营销页可表达情绪，高频工具优先识别效率与操作稳定。
- 页面有主图时先把它定下来，再围绕它的主体、留白与裁切排文字和操作。
- 既有项目复用有效的设计变量、组件和交互习惯；模式妨碍任务时修复其源头。

完成标志：说得出每个主要区块的主角、关键操作链经过哪些状态；主图已经落地，或已写成素材需求。

## 3. 制作并取得实际证据

动手前读 [制作与验证](references/build-and-verify.md)；从选定的小样进入生产代码时，按 [小样到生产](references/mockup-to-production.md) 平移。

- 先做代表性页面或关键操作链，看过再延展。
- 文字、按钮、表单、数据标签保持原生可编辑 DOM；生成素材只放在明确的容器或背景层。
- 示例内容写成真实产品的样子；画面上只出现产品本身会有的文字（"示例""未接入"这类制作说明属于缺陷）。客户评价、合作品牌、业务成果和产品指标没有真实来源时，交付时列为待替换内容。

完成标志：桌面与手机的截图你都打开看过，看到的和截图脚本报告的问题已一批修完。构建成功只证明能构建。

## 4. 独立评审与修正

新页面、整体改版或影响主构图的变更，初版稳定后按 [视觉评审协议](references/visual-review.md) 停下请用户选择模式，等用户回应后再派发**无状态 Critic**；评审已有界面用协议里的"已有界面"模板。局部低风险修改由你自查。

完成标志：所选模式的轮次走完，核实属实的意见都已修，跳过的写明原因。风格开始漂移、意见反复或到达用户预算时，保留当前最合适的版本并说明取舍。

## 5. 减法与交付

检查深度跟着改动走：新页面全查；小改动只看改动处和相邻元素。

- **残忍删减**：一页一个主角，其余安静；逐区块删一轮文字，只放回删了会影响理解的。保留对象名称、判断依据、当前状态和主动作。
- 按 [视觉语言](references/visual-language.md) 的 **AI 味**清单逐项排查，出现即清除。
- 交付范围内的文件或预览，说明选定方向、关键变化、实际看过什么、没验证什么、做了哪些假设。视觉与功能分开报：看过哪些截图，走通了哪些操作。
- **清理提醒**：交付时向用户说明过程产物（验证截图 `shots/` 可直接删除，设计小样与对比页 `design/` 可按需保留或部署时忽略），并主动询问：“这些过程文件是可以删除的，需要我帮你删除吗？”

完成标志：AI 味清单的每一项都对照过；交付说明里每个"已验证"都对应一张你看过的截图或一次走通的操作。

## 能力边界

以当前工具清单里实际存在的工具为准。

- 没有看图能力：可产出设计说明、代码或源码层检查，注明"未验证实际视觉"，不给视觉评分；截图脚本报告的溢出、字号、热区与报错仍算可测项的证据。没有运行环境：不声称交互通过。
- 没有生成能力：用已有素材，或交付素材需求与占位版本。只用任务已授权的服务；密钥处理见 [素材](references/media.md)。
- 没有子 Agent：评审按 [视觉评审协议](references/visual-review.md) 的自评方式进行。
````

## Path: `skills/ai-ui-design/assets/templates/design-brief.md`

````markdown
# 设计说明：<主题>

- **用户与主要任务**：
- **界面类型**：说服 / 操作 / 阅读 / 体验
- **内容与主动作**：
- **选定方向**：选定的方向卡全文；拼装出的方向按拼装结果改写每一项
- **用户的取舍**：明确喜欢的、明确排除的
- **Token**：选定小样的 Token 块，或它所在的文件
- **组件映射**：每个区块落到现有组件、现有组件的新变体，还是必须新建
- **关键状态**：
- **设备与视口**：
- **验收重点**：
- **假设**：自己做的、用户没确认过的判断
````

## Path: `skills/ai-ui-design/assets/style-explorer.html`

```html
<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>风格对比</title><style>
:root{--canvas:#f4f4f4;--surface:#fff;--well:#e8e8e8;--raised:#fff;--line:#e2e2e2;--line-2:#d0d0d0;--text:#161616;--soft:#5c5c5c;--faint:#8c8c8c;--ink:#161616;--hl:#ffe28a;--bar-h:48px;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;--brand:"Helvetica Neue",Helvetica,Arial,sans-serif;color-scheme:light;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;color:var(--text);background:var(--canvas);font-synthesis:none;-webkit-font-smoothing:antialiased;font-variant-numeric:tabular-nums;
 /* 动效：咔嗒用于控件，滑行用于画面与切换，弹出用于确认；弹簧曲线由刚度/阻尼采样 */
 --snap:cubic-bezier(.2,.9,.25,1.04);--snap-d:330ms;--glide:cubic-bezier(.2,.8,.2,1);--glide-d:440ms;--pop:cubic-bezier(.3,1.5,.5,1);--exit:cubic-bezier(.4,0,1,1)}
@supports (transition-timing-function:linear(0,1)){:root{
 --snap:linear(0,.058,.186,.339,.491,.626,.739,.827,.893,.941,.973,.994,1.005,1.011,1.013,1.013,1.012,1.01,1.008,1.006,1);
 --glide:linear(0,.028,.097,.186,.286,.384,.48,.565,.644,.71,.768,.816,.856,.889,.915,.936,.953,.966,.976,.983,.989,.993,1);
 --pop:linear(0,.087,.289,.533,.765,.954,1.084,1.156,1.176,1.161,1.126,1.083,1.042,1.009,.986,.973,.969,.971,.977,.985,.992,.998,1.002,1.005,1.005,1.005,1)}}
*{box-sizing:border-box}body{margin:0;min-width:320px;background:var(--canvas)}h1,h2,p,dl,dd{margin:0}button,textarea,input{font:inherit;color:inherit}button{background:none;border:0;padding:0;cursor:pointer;-webkit-tap-highlight-color:transparent}:focus-visible{outline:2px solid var(--ink);outline-offset:3px}[hidden]{display:none!important}

.bar{position:sticky;top:0;z-index:10;min-height:48px;display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:14px;padding:6px 20px;background:#f4f4f4e6;backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid var(--line);view-transition-name:bar}
.bar-l{display:flex;align-items:center;gap:12px;min-width:0}
.brand{display:flex;align-items:center;gap:8px;flex:none;color:var(--ink);text-decoration:none}.brand img{width:28px;height:28px;display:block;transition:transform .5s var(--snap)}.brand:hover img{transform:rotate(-10deg) scale(1.06)}
.wm{font-family:var(--brand);font-size:19px;line-height:1;font-weight:700;letter-spacing:-.045em;display:flex;align-items:flex-start;gap:3px}.wm b{font-size:9.5px;line-height:1;font-weight:700;letter-spacing:.06em;padding:2px 4px 1.5px;margin-top:-1px;border-radius:4px;background:var(--hl);box-shadow:inset 0 0 0 1.4px var(--ink)}
.sep{width:1px;height:18px;background:var(--line-2);flex:none}.proj{font-size:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.round{font-size:13px;color:var(--faint);white-space:nowrap}
.bar-c{display:flex;gap:8px}.bar-r{display:flex;justify-content:flex-end;align-items:center;gap:12px}
.seg{position:relative;display:flex;padding:2px;border-radius:8px;background:var(--well)}
.seg button{position:relative;z-index:1;font-size:13px;line-height:1.5;padding:4px 11px;border-radius:6px;color:var(--soft);white-space:nowrap;transition:color .2s}.seg button:hover{color:var(--text)}.seg button[aria-pressed=true]{color:var(--text)}
.thumb{position:absolute;left:0;top:0;width:0;border-radius:6px;background:var(--raised);box-shadow:0 1px 2px #0000001f,0 2px 8px -2px #00000014,inset 0 0 0 .5px #0000000f;transition:transform var(--snap-d) var(--snap),width var(--snap-d) var(--snap)}
.toggle{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--soft);cursor:pointer;white-space:nowrap}.toggle input{appearance:none;width:28px;height:16px;margin:0;border-radius:99px;background:var(--line-2);position:relative;cursor:pointer;transition:background .2s}.toggle input::after{content:"";position:absolute;top:2px;left:2px;width:12px;height:12px;border-radius:99px;background:#fff;box-shadow:0 1px 2px #0003;transition:transform var(--snap-d) var(--snap),width .15s}.toggle input:checked{background:var(--ink)}.toggle input:checked::after{transform:translateX(12px)}.toggle:active input::after{width:14px}.toggle:active input:checked::after{transform:translateX(10px)}
.filter{position:relative;font-size:13px}.filter summary{list-style:none;cursor:pointer;color:var(--soft);padding:4px 10px;border-radius:6px;box-shadow:inset 0 0 0 1px var(--line);white-space:nowrap;transition:color .15s,box-shadow .15s}.filter summary::-webkit-details-marker{display:none}.filter summary:hover,.filter[open] summary{color:var(--text);box-shadow:inset 0 0 0 1px var(--line-2)}
.filter-list{position:absolute;right:0;top:calc(100% + 8px);min-width:220px;display:grid;gap:2px;padding:6px;border-radius:10px;background:var(--raised);box-shadow:0 18px 44px -8px #00000026,0 0 0 1px #00000012;transform-origin:top right}.filter[open]>.filter-list{animation:pop-in var(--snap-d) var(--snap) both}
.filter-list label{display:flex;align-items:center;gap:10px;padding:7px 8px;border-radius:6px;cursor:pointer;font-size:14px;transition:background .12s}.filter-list label:hover{background:#0000000a}.filter-list input{accent-color:var(--ink);width:15px;height:15px;margin:0}.filter-list .n{font-family:var(--mono);color:var(--faint);font-size:13px}

.intro{max-width:1840px;margin:0 auto;padding:28px 24px 0}.intro p{font-size:14px;line-height:1.75;color:var(--soft);max-width:68ch}

.grid{max-width:1840px;margin:0 auto;padding:24px 24px 64px;display:grid;grid-template-columns:repeat(var(--cols,3),minmax(0,1fr));gap:48px 28px;align-items:start}
.grid.first .card,.intro.first{animation:rise .7s var(--glide) both;animation-delay:calc(var(--i,0) * 70ms + 60ms)}
.card{min-width:0;display:flex;flex-direction:column}
.cap{display:flex;align-items:center;gap:12px;padding-top:14px}.cap .no{font-family:var(--mono);font-size:13px;color:var(--faint);transition:color .2s}.cap .name{font-size:16px;font-weight:600;line-height:1.4;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.cap .strip-mini{margin:0 auto 0 4px;width:40px;flex:none}.cap .no.base{font-family:inherit;font-size:12px;font-weight:600;line-height:1.6;padding:0 8px;border-radius:99px;background:var(--well);color:var(--soft)}
.lede{margin-top:8px;font-size:13.5px;line-height:1.7;color:var(--soft);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}.grid[data-notes=off] .lede{display:none}
.name{font-size:19px;line-height:1.35;font-weight:600;overflow-wrap:anywhere}.strip-mini{display:flex;height:4px;width:96px;margin-top:9px;border-radius:2px;overflow:hidden;box-shadow:0 0 0 1px #0000001f}.strip-mini i{flex:1}
.frame{position:relative;background:var(--surface);border-radius:4px;box-shadow:0 0 0 1px #00000014,0 24px 48px -30px #00000040;transition:box-shadow .25s,transform .45s var(--glide)}.frame:hover{box-shadow:0 0 0 1px #0000002e,0 36px 64px -30px #00000052;transform:translateY(-3px)}.frame:active{transform:translateY(-1px) scale(.995);transition-duration:.25s,.12s}.frame[data-viewport=mobile]{padding:20px 0;background:var(--well)}
.peek{position:absolute;inset:auto 0 0 0;z-index:2;padding:10px 12px;font-size:12.5px;color:#fff;background:linear-gradient(transparent,#000b);opacity:0;transform:translateY(6px);transition:opacity .18s,transform .3s var(--glide);pointer-events:none;border-radius:0 0 4px 4px}.frame:hover .peek,.hit:focus-visible~.peek{opacity:1;transform:none}
.stage{position:relative;overflow:hidden;margin:0 auto;border-radius:3px;background:#ebebeb}.stage iframe,.stage img{position:absolute;left:0;top:0;border:0;display:block;transform-origin:top left;background:#fff;opacity:0;transition:opacity .4s ease-out}.stage.ready iframe,.stage.ready img{opacity:1}.stage iframe{pointer-events:none}.stage img{object-fit:contain;background:#ebebeb}
.hit{position:absolute;inset:0;width:100%;height:100%;z-index:1;border-radius:4px;cursor:zoom-in}.hit:focus-visible{outline-offset:-2px}
.slide .static{display:none}.static{position:absolute;left:10px;bottom:10px;z-index:2;font-size:12.5px;line-height:1.4;padding:3px 8px;border-radius:4px;background:#000c;color:#ddd;pointer-events:none}
.pick-mark{position:absolute;top:10px;right:10px;z-index:3;display:none;align-items:center;gap:6px;padding:4px 10px 4px 8px;border-radius:99px;background:var(--ink);color:#fff;font-size:13px;font-weight:600;line-height:1.4;box-shadow:0 6px 16px #0000003d;pointer-events:none;transform-origin:85% 50%}.pick-mark::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--hl)}
.is-chosen .pick-mark{display:inline-flex}.is-chosen .frame{box-shadow:0 0 0 2px var(--ink),0 30px 60px -30px #00000052}.is-chosen .cap .no{color:var(--text)}

.spec{display:grid;grid-template-columns:32px minmax(0,1fr);gap:10px 12px;font-size:13px;line-height:1.6}.spec dt{color:var(--faint)}.spec dd{color:var(--soft);min-width:0}
.pick{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-size:14px;line-height:1.5;padding:8px 16px;border-radius:8px;box-shadow:inset 0 0 0 1px var(--line-2);color:var(--text);white-space:nowrap;transition:background .2s,color .2s,box-shadow .2s,transform .35s var(--snap)}.pick:hover{background:#0000000a}.pick:active{transform:scale(.96);transition-duration:.2s,.2s,.2s,.08s}
.pick kbd{font-family:var(--mono);font-size:12px;color:var(--faint);padding:0 5px;border-radius:4px;box-shadow:inset 0 0 0 1px var(--line-2);transition:color .2s,box-shadow .2s}
.pick[data-on]{background:var(--ink);color:#fff;box-shadow:none}.pick[data-on]:hover{background:#333}.pick[data-on] kbd{color:#bdbdbd;box-shadow:inset 0 0 0 1px #ffffff40}
.pick[data-on]::before{content:"";width:9px;height:5px;margin:-3px 1px 0 0;border-left:1.6px solid;border-bottom:1.6px solid;transform:rotate(-45deg)}
.cap .pick{flex:none;font-size:13px;padding:4px 12px;border-radius:6px}

.loupe{position:fixed;top:var(--bar-h);left:0;right:0;bottom:0;display:grid;grid-template-columns:minmax(0,1fr) 300px;grid-template-rows:minmax(0,1fr)}
.view{position:relative;min-width:0;min-height:0;display:flex;flex-direction:column}
.surface{position:relative;flex:1;min-height:0;overflow:hidden}
.track{display:flex;height:100%;transition:transform var(--glide-d) var(--glide)}
.slide{flex:0 0 100%;min-width:0;height:100%;overflow:auto;padding:20px 72px;display:flex;justify-content:center;align-items:center}.slide[data-zoom=actual]{display:block}
.slide .stage{flex:none;box-shadow:0 0 0 1px #00000014,0 40px 80px -40px #00000059;transition:transform var(--glide-d) var(--glide),opacity var(--glide-d) ease-out}.slide:not(.is-current) .stage{transform:scale(.92);opacity:.4}.slide.is-current .stage iframe{pointer-events:auto}
.nav{position:absolute;top:50%;z-index:2;width:44px;height:44px;margin-top:-22px;border-radius:50%;display:grid;place-items:center;font-size:18px;background:#ffffffd9;color:var(--ink);box-shadow:0 0 0 1px #00000014,0 8px 24px -6px #00000033;backdrop-filter:blur(8px);opacity:.85;transition:opacity .2s,transform .35s var(--snap)}.nav:hover{opacity:1}.nav:active{transform:scale(.9);transition-duration:.2s,.08s}.nav.prev{left:14px}.nav.next{right:14px}.nav:disabled{opacity:0;pointer-events:none;transform:scale(.8)}
.info{grid-row:1;grid-column:2;overflow:auto;border-left:1px solid var(--line);background:var(--surface);display:flex;flex-direction:column;view-transition-name:info}
.film{position:relative;display:grid;gap:2px;padding:10px;border-bottom:1px solid var(--line)}
.film-ind{position:absolute;left:0;top:0;width:0;height:0;border-radius:8px;background:#f0f0f0;box-shadow:inset 0 0 0 1px var(--line);transition:transform var(--snap-d) var(--snap),width var(--snap-d) var(--snap),height var(--snap-d) var(--snap)}
.film button{position:relative;z-index:1;display:grid;grid-template-columns:auto minmax(0,1fr);align-items:center;gap:3px 10px;padding:7px 10px;border-radius:8px;color:var(--soft);text-align:left;transition:color .2s,background .15s}.film button:hover{color:var(--text)}.film button:not([aria-current=true]):hover{background:#00000006}.film button[aria-current=true]{color:var(--text)}
.film .fn{font-family:var(--mono);font-size:12.5px;color:var(--faint);grid-row:span 2}.film .ft{font-size:13.5px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.film .strip-mini{margin:0;width:48px;height:3px}
.film .ft.chosen::after{content:"";width:6px;height:6px;border-radius:50%;background:var(--ink);display:inline-block;margin-left:8px;vertical-align:middle}
.info-body{padding:20px 20px 24px;display:flex;flex-direction:column;gap:16px}
.idx{font-size:48px;line-height:.9;font-weight:200;letter-spacing:-.02em;color:var(--faint)}.info .name{font-size:20px;line-height:1.35;margin-top:-6px}.north{font-size:14px;line-height:1.7;color:#2b2b2b}
.big-sw{display:grid;gap:6px}.big-sw div{display:grid;grid-template-columns:32px 1fr;align-items:center;gap:10px;font-family:var(--mono);font-size:12.5px;color:var(--soft)}.big-sw i{height:20px;border-radius:4px;box-shadow:inset 0 0 0 1px #00000017}
.info .pick{align-self:stretch;padding:8px 14px;font-size:13.5px}
.tools{display:flex;gap:10px;flex-wrap:wrap;align-items:center}.tool{font-size:13px;padding:5px 12px;border-radius:6px;color:var(--soft);box-shadow:inset 0 0 0 1px var(--line-2);transition:color .15s,background .2s}.tool:hover{color:var(--text)}.tool[aria-pressed=true]{background:var(--ink);color:#fff;box-shadow:none}
.hint{font-size:12px;line-height:1.9;color:var(--faint)}.hint kbd{font-family:var(--mono);font-size:12px;padding:0 5px;border-radius:4px;box-shadow:inset 0 0 0 1px var(--line-2);color:var(--soft)}
.src{font-size:12px;line-height:1.6;color:var(--faint);overflow-wrap:anywhere}

.picked{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--soft);white-space:nowrap;max-width:220px;padding-left:12px;border-left:1px solid var(--line);overflow:hidden}.picked #decide-name{display:block;overflow:hidden;text-overflow:ellipsis}.picked.on #decide-name{color:var(--text);font-weight:600}
.picked .strip-mini,.choice-empty{flex:none;margin:0;width:22px;height:12px;border-radius:3px}.choice-empty{box-shadow:inset 0 0 0 1px var(--line-2)}
.notes-panel{width:340px;padding:10px}.notes-panel textarea{width:100%;min-height:110px;resize:vertical;padding:10px 12px;border:0;border-radius:6px;background:#f6f6f6;box-shadow:inset 0 0 0 1px var(--line);font-size:14px;line-height:1.7;transition:box-shadow .15s,background .15s}.notes-panel textarea:focus{outline:0;background:#fff;box-shadow:inset 0 0 0 1px var(--faint)}.notes-panel textarea::placeholder{color:var(--faint)}
.state{font-size:12px;line-height:1.6;color:var(--faint);padding:8px 2px 0}.state:empty{display:none}.state[data-warn]{color:#b3401f}

.toast{position:fixed;left:50%;bottom:24px;z-index:40;display:flex;align-items:center;gap:12px;max-width:min(560px,calc(100vw - 32px));padding:10px 16px 10px 12px;border-radius:12px;background:var(--ink);color:#fff;box-shadow:0 18px 44px -10px #00000066;font-size:13.5px;line-height:1.5;opacity:0;transform:translate(-50%,14px) scale(.96);pointer-events:none;transition:opacity .16s var(--exit),transform .2s var(--exit)}
.toast.show{opacity:1;transform:translate(-50%,0);pointer-events:auto;transition:opacity .18s ease-out,transform var(--snap-d) var(--snap)}
.toast .tick{flex:none;width:22px;height:22px;border-radius:50%;background:var(--hl);display:grid;place-items:center}.toast .tick::before{content:"";width:8px;height:4px;margin-top:-2px;border-left:1.6px solid var(--ink);border-bottom:1.6px solid var(--ink);transform:rotate(-45deg)}.toast[data-fail] .tick{background:#c2462e}.toast[data-fail] .tick::before{width:2px;height:9px;margin:0;border:0;background:#fff;transform:none}
.toast b{font-weight:600;white-space:nowrap}.toast code{font-family:var(--mono);font-size:12.5px;color:#a8a8a8;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;user-select:all}.toast[data-fail] code{white-space:pre-wrap}

.none,.empty{max-width:560px;margin:18vh auto;padding:24px;text-align:center;font-size:15px;line-height:1.8;color:var(--soft)}.none button{margin-top:12px;color:var(--text);text-decoration:underline;text-underline-offset:4px}

@keyframes rise{from{opacity:0;transform:translateY(16px)}}
@keyframes pop-in{from{opacity:0;transform:translateY(-4px) scale(.96)}}
@keyframes vt-out{to{opacity:0;transform:scale(.97)}}
@keyframes vt-in{from{opacity:0;transform:scale(.98)}}
@keyframes info-in{from{transform:translateX(100%)}}
@keyframes info-out{to{transform:translateX(100%)}}
/* 并排与单张之间、视口与筛选变化用页面过渡：同一方向的画面从卡片放大到单张，其他卡片淡出，侧栏从右侧滑入 */
::view-transition-group(*){animation-duration:var(--glide-d);animation-timing-function:var(--glide)}
::view-transition-old(*),::view-transition-new(*){height:100%;object-fit:cover;object-position:50% 0}
::view-transition-old(root),::view-transition-new(root){animation-duration:.2s}
::view-transition-old(*):only-child{animation:vt-out .18s var(--exit) both}
::view-transition-new(*):only-child{animation:vt-in .3s .08s ease-out both}
::view-transition-new(info):only-child{animation:info-in var(--glide-d) var(--glide) both}
::view-transition-old(info):only-child{animation:info-out .22s var(--exit) both}
::view-transition-old(bar){display:none}::view-transition-new(bar){animation:none}
/* 视口、筛选、说明开关和缩放只改变形状与位置：外框直接变形，内容不做叠影 */
html[data-vt=reshape]::view-transition-old(*){animation:none;opacity:0}
html[data-vt=reshape]::view-transition-new(*){animation:none}
html[data-vt=reshape]::view-transition-old(*):only-child{animation:vt-out .18s var(--exit) both;opacity:1}
html[data-vt=reshape]::view-transition-new(*):only-child{animation:vt-in .3s .08s ease-out both}

@media(max-width:1180px){.grid{--cols:2!important}.bar{grid-template-columns:minmax(0,1fr) auto;row-gap:10px}.bar-r{grid-column:1/-1;justify-content:flex-start;flex-wrap:wrap}.loupe{grid-template-columns:minmax(0,1fr) 280px}}
@media(max-width:760px){.bar{grid-template-columns:1fr;padding:10px 16px}.bar-c{flex-wrap:wrap}.intro{padding:24px 16px 0}.grid{--cols:1!important;padding:24px 16px 48px;gap:48px}.loupe{position:static;display:flex;flex-direction:column}.surface{flex:none}.track{height:auto;align-items:flex-start}.slide{height:auto;padding:16px 12px}.info{border-left:0;border-top:1px solid var(--line)}.film{display:flex;overflow-x:auto}.film button{flex:none}.info-body{padding:20px 16px}.nav{display:none}.picked{border-left:0;padding-left:0}.notes-panel{width:min(340px,calc(100vw - 32px))}.filter-list{right:auto;left:0;transform-origin:top left}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{transition-duration:0s!important;animation-duration:0s!important;animation-delay:0s!important}.frame:hover{transform:none}}

/* 点选标注功能与实时浮窗 */
.inspect-btn{display:inline-flex;align-items:center;gap:6px;font-size:13px;line-height:1.5;padding:4px 10px;border-radius:6px;box-shadow:inset 0 0 0 1px var(--line);color:var(--soft);background:var(--surface);cursor:pointer;transition:all .2s;white-space:nowrap}
.inspect-btn:hover{color:var(--text);box-shadow:inset 0 0 0 1px var(--line-2)}
.inspect-btn[aria-pressed=true]{background:var(--ink);color:#fff;box-shadow:none}
.inspect-btn[aria-pressed=true] svg{stroke:#ffe28a}
.an-popover{position:fixed;z-index:100;width:380px;max-width:calc(100vw - 32px);background:var(--surface);border-radius:10px;box-shadow:0 20px 48px -12px rgba(0,0,0,0.28),0 0 0 1px rgba(0,0,0,0.12);padding:14px 16px;display:flex;flex-direction:column;gap:10px;font-size:13px;color:var(--text);animation:pop-in var(--snap-d) var(--snap) both}
.an-header{display:flex;align-items:center;justify-content:space-between;gap:8px}
.an-badge{font-family:var(--mono);font-size:12px;font-weight:600;color:var(--ink);background:var(--well);padding:2px 8px;border-radius:4px;max-width:280px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.an-close{font-size:16px;line-height:1;color:var(--faint);padding:2px 6px;border-radius:4px;cursor:pointer}
.an-close:hover{color:var(--text);background:var(--well)}
.an-selector{font-family:var(--mono);font-size:11px;color:var(--faint);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.an-snippet{font-size:12.5px;color:var(--soft);padding:6px 10px;background:var(--well);border-radius:6px;font-style:italic;max-height:48px;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
.an-textarea{width:100%;min-height:72px;resize:vertical;padding:8px 10px;border:0;border-radius:6px;background:#f6f6f6;box-shadow:inset 0 0 0 1px var(--line);font-size:13px;line-height:1.6;color:var(--text);transition:box-shadow .15s,background .15s}
.an-textarea:focus{outline:0;background:#fff;box-shadow:inset 0 0 0 1px var(--ink)}
.an-footer{display:flex;align-items:center;justify-content:space-between;gap:8px;padding-top:4px}
.an-btn{font-size:12.5px;padding:6px 12px;border-radius:6px;cursor:pointer;transition:all .15s;white-space:nowrap}
.an-btn.sub{color:var(--soft);box-shadow:inset 0 0 0 1px var(--line)}
.an-btn.sub:hover{color:var(--text);box-shadow:inset 0 0 0 1px var(--line-2)}
.an-btn.main{background:var(--ink);color:#fff;font-weight:600}
.an-btn.main:hover{background:#333}

</style></head><body>
<header class="bar" id="bar" hidden>
 <div class="bar-l"><span class="brand" title="风格对比"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--ink);flex:none;"><rect x="3" y="3" width="8" height="18" rx="1.5"></rect><rect x="13" y="3" width="8" height="18" rx="1.5"></rect></svg><span class="wm" style="font-size:15px;letter-spacing:-0.02em;">风格<b>对比</b></span></span><span class="sep" aria-hidden="true"></span><span class="proj" id="project"></span><span class="round" id="round"></span></div>
 <div class="bar-c">
  <div class="seg" role="group" aria-label="查看方式"><span class="thumb" aria-hidden="true"></span><button type="button" data-layout="compare" aria-pressed="true">并排</button><button type="button" data-layout="loupe" aria-pressed="false">单张</button></div>
  <div class="seg" role="group" aria-label="预览视口"><span class="thumb" aria-hidden="true"></span><button type="button" data-viewport="desktop" aria-pressed="true">桌面 1280</button><button type="button" data-viewport="mobile" aria-pressed="false">手机 390</button></div>
 </div>
 <div class="bar-r">
  <button type="button" class="inspect-btn" id="inspect-toggle" aria-pressed="false" title="在页面中点选 DOM 元素实时生成位置备注框"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="22" y1="12" x2="18" y2="12"></line><line x1="6" y1="12" x2="2" y2="12"></line><line x1="12" y1="6" x2="12" y2="2"></line><line x1="12" y1="22" x2="12" y2="18"></line></svg><span>点选标注</span></button>
  <label class="toggle"><input id="notes-toggle" type="checkbox" checked>设计说明</label>
  <details class="filter"><summary id="filter-summary"></summary><div id="filter-list" class="filter-list"></div></details>
  <span class="picked" id="picked" title="当前选择的方向"><span id="choice-chip" class="choice-empty"></span><span id="decide-name">未选择方向</span></span>
  <details class="filter"><summary id="notes-open">备注</summary><div class="filter-list notes-panel"><textarea id="notes" aria-label="备注" placeholder="喜欢哪里、要改哪里，可以用编号指明方向。"></textarea><p id="state" class="state"></p></div></details>
 </div>
</header>
<div id="compare-view" hidden>
 <section class="intro"><p id="brief"></p></section>
 <main id="grid" class="grid" aria-label="候选方向"></main>
</div>
<main id="loupe" class="loupe" hidden aria-label="单张查看">
 <div class="view">
  <button type="button" class="nav prev" id="prev" aria-label="上一个方向">←</button>
  <div id="surface" class="surface"><div id="track" class="track"></div></div>
  <button type="button" class="nav next" id="next" aria-label="下一个方向">→</button>
 </div>
 <aside id="info" class="info"><nav id="film" class="film" aria-label="切换方向"></nav><div id="info-body" class="info-body" aria-live="polite"></div></aside>
</main>
<div id="none" class="none" hidden>当前没有要比较的方向。<br><button type="button" id="show-all">显示全部</button></div>
<div id="empty" class="empty" hidden>尚未加入设计小样。按 references/style-explorer.md 准备 manifest 后用生成器组装。</div>

<div id="an-popover" class="an-popover" hidden>
 <div class="an-header">
  <span class="an-badge" id="an-badge">&lt;element&gt;</span>
  <button type="button" class="an-close" id="an-close" aria-label="关闭">×</button>
 </div>
 <div class="an-selector" id="an-selector"></div>
 <div class="an-snippet" id="an-snippet" hidden></div>
 <textarea id="an-text" class="an-textarea" placeholder="输入修改建议或备注，例如：背景加深、加大字号、增加内边距..."></textarea>
 <div class="an-footer">
  <button type="button" class="an-btn sub" id="an-copy-item" title="仅复制此单条元素标注">复制此项</button>
  <div style="display:flex;gap:6px;">
   <button type="button" class="an-btn sub" id="an-cancel">取消</button>
   <button type="button" class="an-btn main" id="an-save">写入备注并复制</button>
  </div>
 </div>
</div>

<div id="toast" class="toast" role="status" aria-live="polite"><span class="tick"></span><b></b><code></code></div>
<script>
const DATA = /*__STYLE_EXPLORER_DATA__*/ null;
(()=>{
 const $=s=>document.querySelector(s),$$=s=>document.querySelectorAll(s);
 if(!DATA?.candidates?.length){$('#empty').hidden=false;return;}
 const C=DATA.candidates,SIZES={desktop:{w:1280,h:900},mobile:{w:390,h:844}},KEY=`oil-ui:${DATA.fingerprint||DATA.project}`;
 const byId=Object.fromEntries(C.map(c=>[c.id,c])),DIRS=C.filter(c=>!c.baseline),no=c=>c.baseline?'现状':String(DIRS.indexOf(c)+1).padStart(2,'0'),vtName=c=>`stage-${C.indexOf(c)}`;
 const root=document.documentElement,calm=matchMedia('(prefers-reduced-motion: reduce)'),narrow=()=>matchMedia('(max-width:760px)').matches;
 const ease=n=>getComputedStyle(root).getPropertyValue(`--${n}`).trim()||'ease-out';
 let st={layout:'compare',viewport:'desktop',notesOn:true,visible:C.map(c=>c.id),current:C[0].id,chosen:null,notes:''},stored=true,zoomActual=false,compareScroll=0,gridKey='',loupeKey='',toastTimer=0;
 try{const saved=JSON.parse(localStorage.getItem(KEY)||'null');if(saved&&typeof saved==='object'){Object.assign(st,saved);st.visible=(Array.isArray(st.visible)?st.visible:[]).filter(id=>byId[id]);if(!byId[st.chosen])st.chosen=null;if(!byId[st.current])st.current=C[0].id;if(!['compare','loupe'].includes(st.layout))st.layout='compare';if(!SIZES[st.viewport])st.viewport='desktop';}}catch{stored=false;}
 function save(){if(!stored)return;try{localStorage.setItem(KEY,JSON.stringify(st));}catch{stored=false;status();}}
 const el=(tag,cls,text)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(text!=null)n.textContent=text;return n;};
 const shown=()=>C.filter(c=>st.visible.includes(c.id));

 // 动效工具：尊重“减少动态效果”，浏览器不支持时直接落到最终状态
 function animate(node,frames,opts){if(calm.matches||!node?.animate)return;try{node.animate(frames,opts);}catch{node.animate(frames,{...opts,easing:'ease-out'});}}
 let vtSeq=0;
 function morph(update,kind){
  if(calm.matches||!document.startViewTransition||document.hidden){update();return;}
  const n=++vtSeq;root.dataset.vt=kind||'';
  try{document.startViewTransition(update).finished.finally(()=>{if(n===vtSeq)delete root.dataset.vt;});}catch{update();}
 }
 function slideTo(ind,target,instant){
  if(!ind||!target||!target.offsetWidth)return;
  if(instant)ind.style.transition='none';
  ind.style.width=`${target.offsetWidth}px`;ind.style.height=`${target.offsetHeight}px`;ind.style.transform=`translate(${target.offsetLeft}px,${target.offsetTop}px)`;
  if(instant){ind.offsetWidth;ind.style.transition='';}
 }
 const placeThumbs=instant=>$$('.seg').forEach(s=>slideTo(s.querySelector('.thumb'),s.querySelector('[aria-pressed=true]'),instant));
 const placeFilm=instant=>{const f=$('#film');slideTo(f.querySelector('.film-ind'),f.querySelector('[aria-current=true]'),instant);};

 document.title=`${DATA.project} · 风格对比`;
 $('#project').textContent=DATA.project;$('#round').textContent=DATA.round||'';
 $('#brief').textContent=DATA.brief||'';

 function stripMini(c){const s=el('span','strip-mini');(c.palette||[]).forEach(h=>{const i=el('i');i.style.background=h;s.append(i);});return s;}
 function stage(c,interactive){
  const s=el('div','stage');s.dataset.id=c.id;
  const m=document.createElement(c.kind==='image'?'img':'iframe');
  if(c.kind==='image'){m.alt=c.name;m.draggable=false;}
  else{m.title=c.name;if(c.kind==='url'){m.setAttribute('sandbox','allow-scripts allow-same-origin allow-forms');}m.referrerPolicy='no-referrer';if(!interactive)m.tabIndex=-1;}
  m.addEventListener('load',()=>{s.classList.add('ready');fit(s);attachInspector(m,c.id);});
  if(c.kind==='image')m.src=c.content;else if(c.kind==='url')m.src=c.content;else m.srcdoc=c.content;
  s.append(m);
  if(c.kind!=='html'||c.interactive)s.append(el('span','static',c.kind==='url'?'本地运行':c.kind==='image'?'静态图':'可操作'));
  return s;
 }
 function fit(s){
  if(!s.isConnected)return;
  const size=SIZES[st.viewport],m=s.querySelector('iframe,img'),box=s.parentElement;let r;
  if(box.classList.contains('slide')){const cs=getComputedStyle(box),w=box.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight),h=narrow()?Infinity:box.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom);r=box.dataset.zoom==='actual'?1:Math.min(w/size.w,h/size.h,1);}
  else r=Math.min(box.clientWidth/size.w,1);
  if(!(r>0))return;
  s.style.width=`${size.w*r}px`;s.style.height=`${size.h*r}px`;m.style.width=`${size.w}px`;m.style.height=`${size.h}px`;m.style.transform=`scale(${r})`;
 }
 const fitAll=()=>$$('.stage').forEach(fit),refit=()=>requestAnimationFrame(fitAll);

 function specList(c){
  const dl=el('dl','spec');const row=(k,v)=>{dl.append(el('dt',null,k),el('dd',null,v));};
  row('字体',c.typography);row('特征',(c.traits||[]).join(' · '));return dl;
 }
 function pickButton(c){const b=el('button','pick');b.type='button';b.dataset.pick=c.id;b.addEventListener('click',()=>choose(c.id));return b;}
 function card(c,i){
  const a=el('article','card');a.dataset.id=c.id;a.style.setProperty('--i',i);a.setAttribute('aria-label',c.name);
  const frame=el('div','frame');frame.style.viewTransitionName=vtName(c);const s=stage(c,false);
  const hit=el('button','hit');hit.type='button';hit.setAttribute('aria-label',`单张查看 ${c.name}`);hit.addEventListener('click',()=>setLayout('loupe',c.id));
  s.append(hit);frame.append(s,el('span','pick-mark','已选择'),el('span','peek','点击单张查看 · 实际尺寸'));
  const cap=el('div','cap');cap.style.viewTransitionName=`cap-${C.indexOf(c)}`;cap.append(el('span',c.baseline?'no base':'no',no(c)),el('h2','name',c.name),stripMini(c),pickButton(c));
  const lede=el('p','lede',c.concept);lede.title=c.concept;lede.style.viewTransitionName=`lede-${C.indexOf(c)}`;
  a.append(frame,cap,lede);return a;
 }
 function syncCompare(){
  const list=shown(),g=$('#grid'),key=list.map(c=>c.id).join();
  if(key!==gridKey){gridKey=key;g.replaceChildren(...list.map(card));}
  g.dataset.notes=st.notesOn?'on':'off';g.style.setProperty('--cols',Math.min(Math.max(list.length,1),st.viewport==='mobile'?4:3));
  $$('.card .frame').forEach(f=>f.dataset.viewport=st.viewport);
 }

 // 单张查看：所有方向预先排成一条横向轨道，切换时整条轨道滑动，不重新加载画面
 function syncLoupe(dir){
  const list=shown(),key=list.map(c=>c.id).join();if(!list.length)return;
  if(key!==loupeKey){
   loupeKey=key;dir=0;
   $('#track').replaceChildren(...list.map(c=>{const sl=el('div','slide');sl.dataset.id=c.id;sl.append(stage(c,true));return sl;}));
   $('#film').replaceChildren(el('span','film-ind'),...list.map(c=>{const b=el('button');b.type='button';b.dataset.id=c.id;b.append(el('span','fn',no(c)),el('span','ft',c.name),stripMini(c));b.addEventListener('click',()=>go(c.id));return b;}));
  }
  if(!list.some(c=>c.id===st.current))st.current=list[0].id;
  const i=list.findIndex(c=>c.id===st.current),track=$('#track');
  if(!dir)track.style.transition='none';
  track.style.transform=`translateX(${-i*100}%)`;
  if(!dir){track.offsetWidth;track.style.transition='';}
  $$('.slide').forEach(sl=>{const on=sl.dataset.id===st.current;sl.classList.toggle('is-current',on);sl.inert=!on;sl.dataset.zoom=on&&zoomActual?'actual':'fit';sl.firstElementChild.style.viewTransitionName=on?vtName(byId[sl.dataset.id]):'none';});
  $('#prev').disabled=i<=0;$('#next').disabled=i>=list.length-1;
  $$('#film button').forEach(b=>b.setAttribute('aria-current',String(b.dataset.id===st.current)));
  renderInfo(dir);placeFilm(!dir);if(inspectOn){const curIfr=$('.slide.is-current iframe');if(curIfr)attachInspector(curIfr,st.current);}
  const cur=$('#film [aria-current=true]'),f=$('#film');
  if(cur&&f.scrollWidth>f.clientWidth)f.scrollTo({left:cur.offsetLeft-16,behavior:calm.matches||!dir?'auto':'smooth'});
 }
 function renderInfo(dir){
  const c=byId[st.current],body=$('#info-body');
  const sw=el('div','big-sw');(c.palette||[]).forEach(h=>{const d=el('div');const x=el('i');x.style.background=h;d.append(x,h.toUpperCase());sw.append(d);});
  const tools=el('div','tools');const z=el('button','tool',zoomActual?'适应窗口':'实际尺寸 100%');z.id='zoom';z.type='button';z.setAttribute('aria-pressed',String(zoomActual));z.addEventListener('click',toggleZoom);tools.append(z);
  const hint=el('p','hint');hint.innerHTML='<kbd>←</kbd> <kbd>→</kbd> 切换方向　<kbd>P</kbd> 选择并复制<br><kbd>Esc</kbd> 回到并排';
  const blocks=[el('span','idx',no(c)),el('h2','name',c.name)];
  if(st.notesOn)blocks.push(el('p','north',c.concept),sw,specList(c));
  blocks.push(pickButton(c),tools,hint,el('p','src',c.kind==='image'?`静态图：${c.sourceLabel}。缩放不代表响应式重排。`:c.kind==='url'?`实时运行 ${c.sourceLabel}。空白时确认开发服务器已启动，且允许被嵌入。`:c.interactive?`单张查看时可以直接操作 ${c.sourceLabel}；无法联网，也不保留浏览器存储。`:`预览禁用脚本与提交；交互请直接打开 ${c.sourceLabel}。`));
  body.replaceChildren(...blocks);paintChoice();
  if(dir)animate(body,[{opacity:0,transform:`translateX(${dir*18}px)`},{opacity:1,transform:'none'}],{duration:420,easing:ease('glide')});
 }
 function toggleZoom(){
  morph(()=>{zoomActual=!zoomActual;const sl=$('.slide.is-current');sl.dataset.zoom=zoomActual?'actual':'fit';fitAll();sl.scrollTo(0,0);const z=$('#zoom');z.textContent=zoomActual?'适应窗口':'实际尺寸 100%';z.setAttribute('aria-pressed',String(zoomActual));},'reshape');
 }

 function render(){
  const list=shown(),loupe=st.layout==='loupe'&&list.length>0;
  $('#compare-view').hidden=st.layout!=='compare'||!list.length;$('#loupe').hidden=!loupe;$('#none').hidden=list.length>0;
  syncCompare();syncLoupe(0);
  $$('[data-layout]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.layout===st.layout)));
  $$('[data-viewport]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.viewport===st.viewport)));
  placeThumbs(false);placeFilm(true);
  $('#notes-toggle').checked=st.notesOn;
  $('#filter-summary').textContent=`比较范围 ${list.length}/${C.length}`;
  $$('#filter-list input').forEach(i=>i.checked=st.visible.includes(i.value));
  paintChoice();fitAll();
 }
 function setLayout(layout,id){
  if(layout===st.layout&&!(id&&id!==st.current))return;
  if(layout==='loupe'&&st.layout==='compare')compareScroll=scrollY;
  if(id)st.current=id;st.layout=layout;zoomActual=false;save();
  morph(()=>{
   render();
   if(layout==='loupe'){window.scrollTo(0,0);return;}
   window.scrollTo(0,compareScroll);
   const a=$(`.card[data-id="${CSS.escape(st.current)}"]`),r=a?.getBoundingClientRect();
   if(r&&(r.top<60||r.bottom>innerHeight))a.scrollIntoView({block:'center'});
  });
 }
 function go(id){
  const list=shown(),from=list.findIndex(c=>c.id===st.current),to=list.findIndex(c=>c.id===id);
  if(to<0||to===from)return;
  st.current=id;zoomActual=false;save();syncLoupe(Math.sign(to-from));fitAll();
 }
 function step(d){const list=shown(),i=list.findIndex(c=>c.id===st.current),n=list[i+d];if(n)go(n.id);else nudge(d);}
 function nudge(d){animate($('.slide.is-current .stage'),[{transform:'none'},{transform:`translateX(${d*14}px)`},{transform:'none'}],{duration:320,easing:'ease-out'});}

 // 选择即复制：再次点击“已选择”会带上最新备注重新复制，不再有单独的复制按钮
 function choose(id){
  const fresh=st.chosen!==id;st.chosen=id;save();paintChoice();
  if(fresh){
   animate($(`.card[data-id="${CSS.escape(id)}"] .pick-mark`),[{opacity:0,transform:'scale(.4)'},{opacity:1,transform:'scale(1)'}],{duration:500,easing:ease('pop')});
   animate($('#decide-name'),[{opacity:0,transform:'translateY(10px)'},{opacity:1,transform:'none'}],{duration:380,easing:ease('glide')});
   animate($('#choice-chip'),[{transform:'scale(.3)'},{transform:'scale(1)'}],{duration:500,easing:ease('pop')});
  }
  copy();
 }
 function paintChoice(){
  $$('.card').forEach(a=>a.classList.toggle('is-chosen',a.dataset.id===st.chosen));
  $$('[data-pick]').forEach(b=>{const on=b.dataset.pick===st.chosen,short=!!b.closest('.cap');b.replaceChildren(document.createTextNode(on?(short?'已选择':'已选择 · 复制'):(short?'选择':'选这个方向')));if(!short)b.append(el('kbd',null,'P'));b.toggleAttribute('data-on',on);b.title=on?'再点一次，带上最新备注重新复制':'选择这个方向，并复制给 Agent';});
  $$('#film button').forEach(b=>b.querySelector('.ft').classList.toggle('chosen',b.dataset.id===st.chosen));
  const c=byId[st.chosen];$('#decide-name').textContent=c?`${no(c)} ${c.name}`:'未选择方向';$('#picked').classList.toggle('on',!!c);
  const chip=$('#choice-chip'),next=c?stripMini(c):el('span','choice-empty');next.id='choice-chip';chip.replaceWith(next);
  status();
 }
 function status(){$('#notes-open').textContent=st.notes?'备注 ·':'备注';const s=$('#state');if(!stored){s.textContent='浏览器存储不可用：关闭页面后选择和备注不会保留。';s.dataset.warn='';}else{s.textContent='备注会和选择一起复制。改完备注，再点一次“已选择”重新复制。';delete s.dataset.warn;}}
 function copyText(){const c=byId[st.chosen];let t=`${DATA.round?DATA.round+'：':''}选 ${no(c)} ${c.name}`;if(st.notes.trim())t+=`\n备注：${st.notes.trim()}`;return t;}
 async function copy(title){
  const t=copyText();let ok=false;
  try{await navigator.clipboard.writeText(t);ok=true;}catch{const a=el('textarea');a.value=t;a.setAttribute('readonly','');a.style.cssText='position:fixed;opacity:0';document.body.append(a);a.select();try{ok=document.execCommand('copy');}catch{}a.remove();}
  toast(ok,t,title);
 }
 function toast(ok,t,title){
  const n=$('#toast');n.toggleAttribute('data-fail',!ok);n.querySelector('b').textContent=title||(ok?'已复制，粘贴给 Agent':'复制失败，请手动复制');n.querySelector('code').textContent=(t||'').replace(/\n/g,' · ');
  n.classList.remove('show');n.offsetWidth;n.classList.add('show');
  clearTimeout(toastTimer);toastTimer=setTimeout(()=>n.classList.remove('show'),ok?2400:8000);
 }

 const fl=$('#filter-list');
 C.forEach(c=>{const l=el('label'),i=el('input');i.type='checkbox';i.value=c.id;i.addEventListener('change',()=>{st.visible=C.map(x=>x.id).filter(id=>id===c.id?i.checked:st.visible.includes(id));save();morph(render,'reshape');});l.append(i,el('span','n',no(c)),c.name);fl.append(l);});
 $('#show-all').addEventListener('click',()=>{st.visible=C.map(c=>c.id);save();morph(render,'reshape');});
 $$('button[data-layout]').forEach(b=>b.addEventListener('click',()=>setLayout(b.dataset.layout)));
 $$('button[data-viewport]').forEach(b=>b.addEventListener('click',()=>{if(st.viewport===b.dataset.viewport)return;st.viewport=b.dataset.viewport;save();morph(render,'reshape');}));
 $('#notes-toggle').addEventListener('change',e=>{st.notesOn=e.target.checked;save();morph(render,'reshape');});
 $('#prev').addEventListener('click',()=>step(-1));$('#next').addEventListener('click',()=>step(1));
 document.addEventListener('keydown',e=>{
  if(e.target.closest?.('textarea,input,summary')||e.metaKey||e.ctrlKey||e.altKey||st.layout!=='loupe')return;
  if(e.key==='ArrowLeft')step(-1);else if(e.key==='ArrowRight')step(1);else if(e.key==='Escape')setLayout('compare');else if(e.key.toLowerCase()==='p')choose(st.current);
 });
 const notes=$('#notes');notes.value=st.notes||'';
 notes.addEventListener('input',()=>{st.notes=notes.value;save();status();});
 $('#notes-open').parentElement.addEventListener('toggle',e=>{if(e.target.open)notes.focus();});
 function syncBars(){root.style.setProperty('--bar-h',`${$('#bar').offsetHeight}px`);placeThumbs(true);placeFilm(true);refit();}
 window.addEventListener('resize',syncBars,{passive:true});
 document.fonts?.ready.then(()=>{placeThumbs(true);placeFilm(true);});
 $('#bar').hidden=false;
 if(st.layout==='compare'){$('#grid').classList.add('first');$('.intro').classList.add('first');setTimeout(()=>{$('#grid').classList.remove('first');$('.intro').classList.remove('first');},1400);}
 
 // ------------------------------------------------------------------
 // 点选标注（DOM 元素选取与实时浮动备注）
 // ------------------------------------------------------------------
 let inspectOn = false;
 let curSelected = null;

 function buildSelector(el, body) {
  const parts = [];
  let cur = el;
  while (cur && cur !== body && cur.tagName) {
   let s = cur.tagName.toLowerCase();
   if (cur.id) {
    parts.unshift('#' + cur.id);
    return parts.join(' > ');
   }
   if (cur.className && typeof cur.className === 'string') {
    const cls = cur.className.split(/\s+/).filter(c => c && !c.startsWith('__ve_'));
    if (cls.length > 0) s += '.' + cls.slice(0, 2).join('.');
   }
   const siblings = Array.from(cur.parentElement?.children || []);
   if (siblings.length > 1) {
    const idx = siblings.indexOf(cur) + 1;
    s += `:nth-child(${idx})`;
   }
   parts.unshift(s);
   cur = cur.parentElement;
  }
  return parts.join(' > ');
 }

 function attachInspector(iframe, candidateId) {
  if (!iframe) return;
  try {
   const doc = iframe.contentDocument || iframe.contentWindow?.document;
   if (!doc || !doc.body) return;
   if (!doc.getElementById('__ve_style__')) {
    const stEl = doc.createElement('style');
    stEl.id = '__ve_style__';
    stEl.textContent = `
     .__ve_hover {
      outline: 2px dashed #0078bf !important;
      outline-offset: 2px !important;
      cursor: crosshair !important;
      box-shadow: 0 0 10px rgba(0,120,191,0.25) !important;
     }
     .__ve_selected {
      outline: 3px solid #ff48b0 !important;
      outline-offset: 2px !important;
      background-color: rgba(255,72,176,0.08) !important;
     }
    `;
    (doc.head || doc.body).appendChild(stEl);
   }

   if (iframe.__ve_attached) return;
   iframe.__ve_attached = true;

   doc.body.addEventListener('mouseover', e => {
    if (!inspectOn) return;
    const t = e.target;
    if (t === doc.body || t === doc.documentElement) return;
    doc.querySelectorAll('.__ve_hover').forEach(x => x.classList.remove('__ve_hover'));
    if (!t.classList.contains('__ve_selected')) t.classList.add('__ve_hover');
    e.stopPropagation();
   }, true);

   doc.body.addEventListener('mouseout', e => {
    if (!inspectOn) return;
    e.target.classList.remove('__ve_hover');
   }, true);

   doc.body.addEventListener('click', e => {
    if (!inspectOn) return;
    const t = e.target;
    if (t === doc.body || t === doc.documentElement) return;
    e.preventDefault();
    e.stopPropagation();

    doc.querySelectorAll('.__ve_selected').forEach(x => x.classList.remove('__ve_selected'));
    doc.querySelectorAll('.__ve_hover').forEach(x => x.classList.remove('__ve_hover'));
    t.classList.add('__ve_selected');

    const cleanCls = Array.from(t.classList).filter(c => !c.startsWith('__ve_')).join('.');
    const tagName = t.tagName.toLowerCase();
    const badge = `<${tagName}${t.id ? '#' + t.id : cleanCls ? '.' + cleanCls : ''}>`;
    const sel = buildSelector(t, doc.body);
    const txt = (t.textContent || '').trim().slice(0, 100);
    const r = t.getBoundingClientRect();

    openAnnotationBox({
     target: t,
     badge,
     selector: sel,
     textContent: txt,
     rect: r,
     iframe,
     candidateId: candidateId || st.current
    });
   }, true);
  } catch (err) {
   console.warn('attachInspector fallback:', err);
  }
 }

 function openAnnotationBox(info) {
  curSelected = info;
  const pop = $('#an-popover');
  if (!pop) return;
  $('#an-badge').textContent = info.badge;
  $('#an-selector').textContent = info.selector;
  const snip = $('#an-snippet');
  if (info.textContent) {
   snip.textContent = `“${info.textContent}”`;
   snip.hidden = false;
  } else {
   snip.hidden = true;
  }
  $('#an-text').value = '';

  const iframeRect = info.iframe.getBoundingClientRect();
  let scale = 1;
  const match = info.iframe.style.transform.match(/scale\(([^)]+)\)/);
  if (match) scale = parseFloat(match[1]);

  let top = iframeRect.top + (info.rect.bottom * scale) + 8;
  let left = iframeRect.left + (info.rect.left * scale);

  if (left + 390 > window.innerWidth) left = window.innerWidth - 400;
  if (left < 16) left = 16;
  if (top + 280 > window.innerHeight) {
   top = iframeRect.top + (info.rect.top * scale) - 270;
   if (top < 60) top = 60;
  }

  pop.style.top = `${top}px`;
  pop.style.left = `${left}px`;
  pop.hidden = false;
  setTimeout(() => $('#an-text')?.focus(), 50);
 }

 function closeAnnotationBox() {
  const pop = $('#an-popover');
  if (pop) pop.hidden = true;
  if (curSelected?.target) {
   try { curSelected.target.classList.remove('__ve_selected'); } catch {}
  }
  curSelected = null;
 }

 function formatAnnotationMarkdown(info, noteText) {
  let md = `【元素标注】${info.badge} (${info.selector})`;
  if (info.textContent) md += `\n- 内容：“${info.textContent}”`;
  md += `\n- 批注：${noteText.trim() || '已选中此元素'}`;
  return md;
 }

 function toggleInspect() {
  inspectOn = !inspectOn;
  const btn = $('#inspect-toggle');
  if (btn) {
   btn.setAttribute('aria-pressed', String(inspectOn));
   const sp = btn.querySelector('span');
   if (sp) sp.textContent = inspectOn ? '退出标注' : '点选标注';
  }
  if (inspectOn) {
   if (st.layout !== 'loupe') {
    setLayout('loupe');
   }
   toast(true, '鼠标悬浮元素高亮，点击即可生成实时备注框', '标注模式已开启');
   $$('iframe').forEach(ifr => {
    const parentStage = ifr.closest('.stage');
    attachInspector(ifr, parentStage?.dataset.id);
   });
  } else {
   closeAnnotationBox();
   $$('iframe').forEach(ifr => {
    try {
     ifr.contentDocument?.querySelectorAll('.__ve_hover, .__ve_selected').forEach(x => {
      x.classList.remove('__ve_hover', '__ve_selected');
     });
    } catch {}
   });
  }
 }

 $('#inspect-toggle')?.addEventListener('click', toggleInspect);
 $('#an-close')?.addEventListener('click', closeAnnotationBox);
 $('#an-cancel')?.addEventListener('click', closeAnnotationBox);

 $('#an-copy-item')?.addEventListener('click', async () => {
  if (!curSelected) return;
  const noteText = $('#an-text').value;
  const md = formatAnnotationMarkdown(curSelected, noteText);
  let ok = false;
  try {
   await navigator.clipboard.writeText(md);
   ok = true;
  } catch {}
  toast(ok, md, ok ? '已复制该元素标注' : '复制失败');
 });

 $('#an-save')?.addEventListener('click', async () => {
  if (!curSelected) return;
  const noteText = $('#an-text').value;
  const md = formatAnnotationMarkdown(curSelected, noteText);
  st.notes = st.notes ? (st.notes.trim() + '\n\n' + md) : md;
  $('#notes').value = st.notes;
  save();
  status();
  closeAnnotationBox();
  await copy('已将标注写入备注并复制');
 });

 $('#an-text')?.addEventListener('keydown', e => {
  if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') {
   $('#an-save')?.click();
  } else if (e.key === 'Escape') {
   closeAnnotationBox();
  }
 });

 render();syncBars();
})();
</script></body></html>
```

## Path: `skills/ai-ui-design/scripts/build_explorer.py`

```python
#!/usr/bin/env python3
"""Build a portable, offline design comparison from a local manifest."""

from __future__ import annotations

import argparse
import base64
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import urlsplit


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL_ROOT / "assets" / "style-explorer.html"
MARKER = "/*__STYLE_EXPLORER_DATA__*/ null"
PREVIEW_CSP = (
    "default-src 'none'; style-src 'unsafe-inline'; img-src data:; "
    "font-src data:; media-src data:; script-src 'none'; "
    "form-action 'none'; base-uri 'none'; object-src 'none'"
)


def text_field(obj: dict, name: str, *, default: str | None = None) -> str:
    value = obj.get(name, default)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} 必须是非空字符串")
    return value.strip()


def text_list(obj: dict, name: str) -> list[str]:
    values = obj.get(name)
    if not isinstance(values, list) or not values:
        raise ValueError(f"{name} 必须是非空字符串数组")
    if any(not isinstance(v, str) or not v.strip() for v in values):
        raise ValueError(f"{name} 的每项必须是非空字符串")
    return [v.strip() for v in values]


class AssetCheck(HTMLParser):
    """Reject resource dependencies; the browser sandbox disables behavior."""

    def __init__(self):
        super().__init__()
        self.styles = []
        self.in_style = False
        self.head_position = None

    def handle_starttag(self, tag: str, attrs: list) -> None:
        attrs = dict(attrs)
        if tag == "head" and self.head_position is None:
            self.head_position = (self.getpos(), self.get_starttag_text())
        if tag in ("iframe", "frame", "object", "embed"):
            raise ValueError("候选 HTML 不支持嵌套文档；请提供静态内容或截图")
        if tag == "style":
            self.in_style = True
        if attrs.get("style"):
            self.styles.append(attrs["style"])
        if tag == "base":
            raise ValueError("候选 HTML 不应包含 base；资源需要内嵌")
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            raise ValueError("候选 HTML 不应自动跳转")
        for key in ("src", "poster", "data", "href", "xlink:href"):
            value = attrs.get(key, "") or ""
            if not value or value.startswith(("#", "data:")):
                continue
            raise ValueError(f"候选 HTML 含未内嵌资源 {tag}.{key}: {value}")
        if attrs.get("srcset"):
            raise ValueError("候选 HTML 请用内嵌 src 代替 srcset")

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self.in_style = False

    def handle_data(self, data: str) -> None:
        if self.in_style:
            self.styles.append(data)


CSS_TOKEN = re.compile(
    r"(?P<comment>/\*.*?\*/)|(?P<string>\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')"
    r"|(?P<ident>(?:[-_a-zA-Z]|\\(?:[0-9a-fA-F]{1,6}\s?|[^\r\n]))"
    r"(?:[-_a-zA-Z0-9]|\\(?:[0-9a-fA-F]{1,6}\s?|[^\r\n]))*)"
    r"|(?P<space>\s+)|(?P<symbol>.)", re.S,
)


def css_unescape(value: str) -> str:
    def replacement(match):
        if match.group(1):
            codepoint = int(match.group(1), 16)
            return chr(codepoint) if 0 < codepoint <= 0x10FFFF else "\ufffd"
        return match.group(2)
    return re.sub(r"\\([0-9a-fA-F]{1,6})(?:\s)?|\\([^\r\n])", replacement, value)


def check_css(css: str, label: str) -> None:
    tokens = [(m.lastgroup, m.group()) for m in CSS_TOKEN.finditer(css)
              if m.lastgroup not in ("comment", "space")]

    def check_resource(value: str):
        if not css_unescape(value).strip().lower().startswith(("data:", "#")):
            raise ValueError(f"{label}: CSS 含未内嵌资源")

    for index, (kind, value) in enumerate(tokens):
        if value == "@" and index + 1 < len(tokens) and tokens[index + 1][0] == "ident" and css_unescape(tokens[index + 1][1]).lower() == "import":
            raise ValueError(f"{label}: 请内嵌 CSS，不使用 @import")
        name = css_unescape(value).lower() if kind == "ident" else ""
        if name not in ("url", "image-set", "-webkit-image-set", "image", "src"):
            continue
        if index + 1 >= len(tokens) or tokens[index + 1][1] != "(":
            continue
        depth, body = 1, []
        for inner_kind, inner_value in tokens[index + 2:]:
            if inner_kind == "symbol" and inner_value == "(":
                depth += 1
            elif inner_kind == "symbol" and inner_value == ")":
                depth -= 1
                if depth == 0:
                    break
            if name == "url":
                body.append(inner_value[1:-1] if inner_kind == "string" else inner_value)
            elif depth == 1 and inner_kind == "string":
                check_resource(inner_value[1:-1])
        if name == "url":
            check_resource("".join(body))


STORAGE_SHIM = (
    "<script>(()=>{const mem=()=>{const m=new Map();return{get length(){return m.size},"
    "key:i=>[...m.keys()][i]??null,getItem:k=>m.has(String(k))?m.get(String(k)):null,"
    "setItem:(k,v)=>{m.set(String(k),String(v))},removeItem:k=>{m.delete(String(k))},clear:()=>m.clear()}};"
    "for(const n of['localStorage','sessionStorage']){try{window[n].length}catch{"
    "Object.defineProperty(window,n,{value:mem(),configurable:true})}}})();</script>"
)


def preview_csp(interactive: bool) -> str:
    return PREVIEW_CSP.replace("script-src 'none'", "script-src 'unsafe-inline'") if interactive else PREVIEW_CSP


EMBEDDABLE = {
    ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp",
    ".gif": "image/gif", ".avif": "image/avif", ".svg": "image/svg+xml",
    ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".otf": "font/otf",
    ".mp4": "video/mp4", ".webm": "video/webm",
}
ATTR_REF = re.compile(r"""(?P<lead>\b(?:src|poster|href|xlink:href)\s*=\s*)(?P<q>["'])(?P<ref>[^"'#][^"']*)(?P=q)""")
CSS_REF = re.compile(r"""url\(\s*(?P<q>["']?)(?P<ref>[^"')\s][^"')]*)(?P=q)\s*\)""")


def embed_local_files(content: str, base: Path, root: Path, used: set[Path]) -> str:
    """Inline images, fonts and videos referenced relative to the candidate, as long as they stay inside the manifest folder."""

    def data_url(ref: str) -> str | None:
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:|^//", ref):
            return None
        target = (base / ref.split("?")[0].split("#")[0]).resolve()
        mime = EMBEDDABLE.get(target.suffix.lower())
        if not mime or not target.is_file() or not target.is_relative_to(root):
            return None
        used.add(target)
        return f"data:{mime};base64," + base64.b64encode(target.read_bytes()).decode("ascii")

    def attr(match):
        url = data_url(match["ref"])
        return match.group(0) if url is None else f'{match["lead"]}{match["q"]}{url}{match["q"]}'

    def css(match):
        url = data_url(match["ref"])
        return match.group(0) if url is None else f'url("{url}")'

    return CSS_REF.sub(css, ATTR_REF.sub(attr, content))


def prepare_html(path: Path, interactive: bool = False, root: Path | None = None, used: set[Path] | None = None) -> str:
    content = path.read_text(encoding="utf-8")
    if root is not None:
        content = embed_local_files(content, path.parent, root, used if used is not None else set())
    parser = AssetCheck()
    parser.feed(content)
    for style in parser.styles:
        check_css(style, path.name)
    if parser.head_position is None:
        raise ValueError(f"{path.name}: 候选 HTML 需要完整的 head 元素")
    (line, column), start_tag = parser.head_position
    head_end = sum(len(part) + 1 for part in content.split('\n')[:line - 1]) + column + len(start_tag)
    meta = f'<meta http-equiv="Content-Security-Policy" content="{preview_csp(interactive)}">'
    return content[:head_end] + meta + (STORAGE_SHIM if interactive else "") + content[head_end:]


def prepare_image(path: Path) -> str:
    data = path.read_bytes()
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        mime = "image/png"
    elif data.startswith(b"\xff\xd8\xff"):
        mime = "image/jpeg"
    elif data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        mime = "image/webp"
    else:
        raise ValueError(f"{path.name}: 静态预览支持 PNG、JPEG 和 WebP")
    return f"data:{mime};base64," + base64.b64encode(data).decode("ascii")


LOOPBACK = {"localhost", "127.0.0.1", "::1"}


def local_url(value: str, identifier: str) -> str:
    """Live candidates only point at a dev server on this machine."""
    parts = urlsplit(value)
    if parts.scheme not in ("http", "https") or (parts.hostname or "").lower() not in LOOPBACK or parts.username or parts.password:
        raise ValueError(f"{identifier}: url 只能是本机开发服务器地址，例如 http://localhost:5173/orders")
    return value


def load_manifest(path: Path) -> tuple[dict, set[Path]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or raw.get("schemaVersion") != 1:
        raise ValueError("manifest.schemaVersion 必须为 1")
    data = {"schemaVersion": 1, "project": text_field(raw, "project"),
            "brief": text_field(raw, "brief"), "round": text_field(raw, "round", default="01")}
    candidates = raw.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("candidates 至少需要一个候选")
    seen = set()
    inputs = {path, TEMPLATE.resolve()}
    output = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            raise ValueError("每个候选必须是对象")
        identifier = text_field(candidate, "id")
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,63}", identifier) or identifier in seen:
            raise ValueError(f"候选 id 无效或重复: {identifier}")
        seen.add(identifier)
        kind = candidate.get("kind", "html")
        if kind not in ("html", "image", "url"):
            raise ValueError(f"未知候选 kind: {kind}")
        baseline = candidate.get("baseline", False)
        interactive = candidate.get("interactive", False)
        if not isinstance(baseline, bool) or not isinstance(interactive, bool):
            raise ValueError(f"{identifier}: baseline 和 interactive 必须是 true 或 false")
        if interactive and kind != "html":
            raise ValueError(f"{identifier}: interactive 只用于 html 候选")
        if kind == "url":
            source = None
            url = local_url(text_field(candidate, "url"), identifier)
        else:
            source = (path.parent / text_field(candidate, "source")).resolve()
            if not source.is_relative_to(path.parent) or not source.is_file():
                raise ValueError(f"候选 source 必须是 manifest 目录内可读文件: {identifier}")
            inputs.add(source)
        colors = text_list(candidate, "palette")
        if any(not re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})", c) for c in colors):
            raise ValueError(f"{identifier}: palette 需要十六进制颜色")
        output.append({
            "id": identifier,
            **{name: text_field(candidate, name) for name in ("name", "concept", "typography")},
            "palette": colors, "traits": text_list(candidate, "traits"), "kind": kind,
            "content": url if kind == "url" else prepare_html(source, interactive, path.parent, inputs) if kind == "html" else prepare_image(source),
            "sourceLabel": url if kind == "url" else source.name,
            "baseline": baseline,
            "interactive": interactive,
        })
    if sum(c["baseline"] for c in output) > 1:
        raise ValueError("最多只能有一个基线候选")
    output.sort(key=lambda c: not c["baseline"])
    data["candidates"] = output
    canonical = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    data["fingerprint"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:24]
    return data, inputs


def build(manifest: Path, output: Path, *, force: bool = False) -> dict:
    manifest, output = manifest.resolve(), output.resolve()
    data, inputs = load_manifest(manifest)
    if output in inputs or output.is_relative_to(SKILL_ROOT):
        raise ValueError("输出不能覆盖输入或写进 Skill 安装目录")
    if output.exists() and not force:
        raise FileExistsError("输出已存在；使用新路径，或明确加 --force 更新")
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count(MARKER) != 1:
        raise ValueError("模板数据入口缺失或重复")
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    page = template.replace(MARKER, payload)
    output.parent.mkdir(parents=True, exist_ok=True)
    if force:
        temp = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=output.parent, delete=False) as handle:
                temp = Path(handle.name)
                handle.write(page)
            temp.replace(output)
        finally:
            if temp and temp.exists():
                temp.unlink()
    else:
        with output.open("x", encoding="utf-8") as handle:
            handle.write(page)
    return {"output": str(output), "candidates": len(data["candidates"]), "fingerprint": data["fingerprint"], "bytes": output.stat().st_size}


def main() -> int:
    if sys.version_info < (3, 9):
        print("需要 Python 3.9 或更新版本", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description="把本地候选与 manifest 组装成独立风格对比 HTML")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--force", action="store_true", help="明确允许原子更新已有输出")
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.manifest, args.output, force=args.force), ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(f"未生成对比页：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
```

## Path: `skills/ai-ui-design/scripts/check_contrast.py`

```python
#!/usr/bin/env python3
"""Compute WCAG 2.x contrast ratios for foreground/background color pairs."""

from __future__ import annotations

import argparse
import math
import re
import sys


HEX = re.compile(r"^#?([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
FUNCTION = re.compile(r"^(rgba?|oklch)\((.*)\)$", re.I)
TOKEN = re.compile(r"[a-zA-Z]+\([^)]*\)|[^\s,/]+")
THRESHOLDS = {"text": 4.5, "large": 3.0}
FORMATS = "#rgb、#rgba、#rrggbb、#rrggbbaa、rgb() 或 oklch()"


def number(token: str, scale: float) -> float:
    """Percentages are fractions of scale; `none` counts as zero."""
    if token.lower() == "none":
        return 0.0
    return float(token[:-1]) / 100 * scale if token.endswith("%") else float(token)


def encode(linear: float) -> float:
    linear = min(max(linear, 0.0), 1.0)
    return linear * 12.92 if linear <= 0.0031308 else 1.055 * linear ** (1 / 2.4) - 0.055


def oklch_to_srgb(lightness: float, chroma: float, hue: float) -> tuple[float, float, float]:
    """OKLCH to gamma-encoded sRGB; out-of-gamut channels are clipped."""
    a, b = chroma * math.cos(math.radians(hue)), chroma * math.sin(math.radians(hue))
    l = (lightness + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (lightness - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (lightness - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (encode(4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s),
            encode(-1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s),
            encode(-0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s))


def parse_color(value: str) -> tuple[float, float, float, float]:
    """Return gamma-encoded sRGB channels and alpha, each in 0–1."""
    text = value.strip()
    match = HEX.match(text)
    if match:
        digits = match.group(1)
        if len(digits) in (3, 4):
            digits = "".join(c * 2 for c in digits)
        channels = [int(digits[i:i + 2], 16) / 255 for i in range(0, len(digits), 2)]
        return (*channels[:3], channels[3] if len(channels) == 4 else 1.0)
    match = FUNCTION.match(text)
    parts = re.split(r"[\s,/]+", match.group(2).strip()) if match else []
    if len(parts) not in (3, 4):
        raise ValueError(f"无法解析色值 {value!r}：需要 {FORMATS}")
    try:
        alpha = number(parts[3], 1) if len(parts) == 4 else 1.0
        if match.group(1).lower() == "oklch":
            rgb = oklch_to_srgb(number(parts[0], 1), number(parts[1], 0.4), number(re.sub(r"deg$", "", parts[2]), 360))
        else:
            rgb = tuple(min(max(number(p, 255) / 255, 0.0), 1.0) for p in parts[:3])
    except ValueError:
        raise ValueError(f"无法解析色值 {value!r}：需要 {FORMATS}") from None
    return (*rgb, min(max(alpha, 0.0), 1.0))


def luminance(rgb: tuple[float, float, float]) -> float:
    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg: str, bg: str) -> float:
    *back, back_alpha = parse_color(bg)
    if back_alpha < 1:
        raise ValueError(f"背景 {bg!r} 带透明度：换成它在页面上实际呈现的不透明色")
    *front, alpha = parse_color(fg)
    shown = tuple(alpha * f + (1 - alpha) * b for f, b in zip(front, back))
    a, b = sorted((luminance(shown), luminance(tuple(back))), reverse=True)
    return (a + 0.05) / (b + 0.05)


def parse_pair(value: str, default_level: str) -> tuple[str, str, str]:
    parts = TOKEN.findall(value)
    level = default_level
    if len(parts) == 3 and parts[2] in THRESHOLDS:
        level = parts.pop()
    if len(parts) != 2:
        raise ValueError(f"{value!r} 需要 \"<前景> <背景> [text|large]\"")
    return parts[0], parts[1], level


def main() -> int:
    parser = argparse.ArgumentParser(description="计算前景/背景色对的 WCAG 对比度；半透明前景先按背景合成再算")
    parser.add_argument("pairs", nargs="+", help=f'色对，如 "#161616 #f4f4f4"；末尾可加 text 或 large 单独指定门槛。色值支持 {FORMATS}')
    parser.add_argument(
        "--level",
        choices=sorted(THRESHOLDS),
        default="text",
        help="未单独指定的色对使用的门槛：text 为正文 4.5:1，large 为大字与 UI 组件 3:1（默认 text）",
    )
    args = parser.parse_args()

    rows = []
    for raw in args.pairs:
        try:
            fg, bg, level = parse_pair(raw, args.level)
            rows.append((fg, bg, level, contrast(fg, bg)))
        except ValueError as exc:
            print(f"错误：{exc}", file=sys.stderr)
            return 2

    width = max(9, *(len(color) for fg, bg, _, _ in rows for color in (fg, bg)))
    failed = 0
    print(f"{'前景':<{width}} {'背景':<{width}} {'对比度':>7}  {'门槛':<5}  结果")
    for fg, bg, level, ratio in rows:
        ok = ratio >= THRESHOLDS[level]
        print(f"{fg:<{width}} {bg:<{width}} {ratio:>6.2f}:1  {level:<5}  {'达标' if ok else '不达标'}（需 {THRESHOLDS[level]}:1）")
        failed += not ok
    if failed:
        print(f"{failed} 对不达标", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## Path: `skills/ai-ui-design/scripts/screenshot.py`

```python
#!/usr/bin/env python3
"""Screenshot pages with an installed Chromium-family browser over CDP, using only the standard library."""

from __future__ import annotations

import argparse
import base64
import glob
import json
import os
from pathlib import Path
import re
import select
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time
from urllib.parse import urlsplit


SKILL_ROOT = Path(__file__).resolve().parents[1]
PRESETS = {"desktop": (1440, 900, 1.0, False), "mobile": (390, 844, 2.0, True)}
KEYS = {"Tab": 9, "Enter": 13, "Escape": 27, "Space": 32, "ArrowLeft": 37, "ArrowUp": 38, "ArrowRight": 39, "ArrowDown": 40}
FLAGS = [
    "--headless=new", "--remote-debugging-port=0", "--no-first-run", "--no-default-browser-check",
    "--disable-extensions", "--disable-sync", "--disable-default-apps", "--disable-component-update",
    "--disable-background-networking", "--disable-background-timer-throttling",
    "--disable-backgrounding-occluded-windows", "--disable-renderer-backgrounding", "--disable-dev-shm-usage",
    "--password-store=basic", "--use-mock-keychain", "--force-color-profile=srgb", "--hide-scrollbars",
    "--mute-audio", "--disable-breakpad", "--disable-features=Translate,MediaRouter,OptimizationHints",
]

# The measurable items of build-and-verify.md, reported with every screenshot.
CHECKS = r"""(() => {
  if (!document.body) return {blank: true};
  // The layout viewport: mobile emulation widens innerWidth to fit overflowing content.
  const vw = document.documentElement.clientWidth;
  const label = el => {
    let s = el.tagName.toLowerCase();
    if (el.id) s += '#' + el.id;
    else if (typeof el.className === 'string' && el.className.trim()) s += '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.');
    const text = (el.innerText || el.getAttribute('aria-label') || el.value || '').trim().replace(/\s+/g, ' ').slice(0, 24);
    return text ? `${s} "${text}"` : s;
  };
  const shown = el => {
    const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
    return r.width > 1 && r.height > 1 && cs.visibility !== 'hidden' && +cs.opacity > 0;
  };
  const all = [...document.body.querySelectorAll('*')];
  const overflowX = Math.max(0, document.documentElement.scrollWidth - vw);
  const wide = overflowX ? all.filter(el => el.getBoundingClientRect().right > vw + 1
    && el.parentElement.getBoundingClientRect().right <= vw + 1 && shown(el)).map(label) : [];
  const tiny = all.filter(el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()) && shown(el))
    .map(el => [el, parseFloat(getComputedStyle(el).fontSize)]).filter(([, size]) => size < 12)
    .map(([el, size]) => `${label(el)} ${size}px`);
  const hits = [...document.querySelectorAll('a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button], [role=link], [role=checkbox], [role=switch], [role=tab], [tabindex]:not([tabindex="-1"])')]
    .filter(el => shown(el) && getComputedStyle(el).display !== 'inline')
    .map(el => [el, el.getBoundingClientRect()]).filter(([, r]) => r.width < 24 || r.height < 24)
    .map(([el, r]) => `${label(el)} ${Math.round(r.width)}×${Math.round(r.height)}`);
  const blank = !document.body.innerText.trim() && !document.querySelector('img, svg, canvas, video, iframe, picture');
  return {overflowX, overflowBy: wide.slice(0, 3), smallText: tiny.length, smallTextSamples: tiny.slice(0, 3),
          smallTargets: hits.length, smallTargetSamples: hits.slice(0, 3), blank};
})()"""

# Before actions: settle what is already moving, and remember it so frames show only what the actions start.
MARK = r"""(() => {
  const list = document.getAnimations();
  for (const a of list) { try { a.finish(); } catch (e) {} }
  window.__aiuiBefore = new Set(list);
})()"""

# Pause the animations at one shared moment of the longest, so staggered choreography stays intact.
SEEK = r"""(fraction => {
  const before = window.__aiuiBefore || new Set();
  const list = document.getAnimations().filter(a => !before.has(a));
  const timing = list.map(a => a.effect ? a.effect.getComputedTiming() : {});
  const ends = timing.map(t => t.endTime).filter(Number.isFinite);
  const span = ends.length ? Math.max(...ends) : Math.max(0, ...timing.map(t => (t.delay || 0) + (Number(t.duration) || 0)));
  for (const a of list) { a.pause(); a.currentTime = span * fraction; }
  return list.length;
})"""


def find_browser(explicit: str | None) -> str:
    """An explicit path, then installed browsers, then copies cached by Playwright or Puppeteer."""
    if explicit:
        if Path(explicit).is_file():
            return explicit
        raise LookupError(f"找不到指定的浏览器：{explicit}")
    home = Path.home()
    if sys.platform == "darwin":
        apps = ["Google Chrome", "Chromium", "Microsoft Edge", "Brave Browser", "Google Chrome Canary"]
        installed = [str(root / f"{app}.app/Contents/MacOS/{app}") for root in (Path("/Applications"), home / "Applications") for app in apps]
        caches, names = [home / "Library/Caches/ms-playwright", home / ".cache/puppeteer"], ["*.app/Contents/MacOS/*", "chrome-headless-shell", "headless_shell"]
    elif os.name == "nt":
        roots = [os.environ.get(key, "") for key in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA")]
        apps = ["Google/Chrome/Application/chrome.exe", "Microsoft/Edge/Application/msedge.exe",
                "Chromium/Application/chrome.exe", "BraveSoftware/Brave-Browser/Application/brave.exe"]
        installed = [str(Path(root) / app) for root in roots if root for app in apps]
        caches, names = [Path(os.environ.get("LOCALAPPDATA", home)) / "ms-playwright", home / ".cache/puppeteer"], ["chrome.exe", "chrome-headless-shell.exe", "headless_shell.exe"]
    else:
        commands = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "microsoft-edge", "microsoft-edge-stable", "brave-browser"]
        installed = [path for path in map(shutil.which, commands) if path]
        caches, names = [home / ".cache/ms-playwright", home / ".cache/puppeteer"], ["chrome", "chrome-headless-shell", "headless_shell"]
    cached = [hit for cache in caches for depth in ("chrom*/*", "chrom*/*/*") for name in names
              for hit in sorted(glob.glob(str(cache / depth / name)), reverse=True)]
    for candidate in installed + cached:
        if Path(candidate).is_file() and os.access(candidate, os.X_OK):
            return candidate
    raise LookupError("没找到 Chrome、Edge、Chromium 或 Brave；用 --browser 或环境变量 CHROME_PATH 指定可执行文件")


class Browser:
    """A headless browser process, driven over a minimal RFC 6455 WebSocket client speaking CDP."""

    def __init__(self, binary: str, timeout: float, cache: Path):
        self.timeout, self.listeners, self.next_id = timeout, [], 0
        self.buffer, self.partial, self.sock = bytearray(), bytearray(), None
        self.profile = tempfile.mkdtemp(prefix="chrome-", dir=cache)
        flags = FLAGS + [f"--user-data-dir={self.profile}"]
        if hasattr(os, "geteuid") and os.geteuid() == 0:
            flags.append("--no-sandbox")
        self.process = subprocess.Popen([binary, *flags, "about:blank"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            self._connect(self._endpoint())
        except BaseException:
            self.close()
            raise

    def _endpoint(self) -> str:
        marker, deadline = Path(self.profile) / "DevToolsActivePort", time.monotonic() + 20
        while time.monotonic() < deadline:
            if self.process.poll() is not None:
                raise RuntimeError(f"浏览器启动后立刻退出了（退出码 {self.process.returncode}）")
            try:
                lines = marker.read_text().split("\n")
            except OSError:
                lines = []
            if len(lines) > 1 and lines[0].strip().isdigit() and lines[1].strip():
                return f"ws://127.0.0.1:{lines[0].strip()}{lines[1].strip()}"
            time.sleep(0.05)
        raise RuntimeError("浏览器 20 秒内没有打开调试端口")

    def _connect(self, url: str) -> None:
        parts = urlsplit(url)
        self.sock = socket.create_connection((parts.hostname, parts.port), timeout=self.timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((f"GET {parts.path} HTTP/1.1\r\nHost: {parts.hostname}:{parts.port}\r\nUpgrade: websocket\r\n"
                           f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        while b"\r\n\r\n" not in self.buffer:
            self._fill()
        end = self.buffer.index(b"\r\n\r\n") + 4
        status = bytes(self.buffer[:end]).split(b"\r\n", 1)[0].decode("latin-1")
        del self.buffer[:end]
        if status.split()[1:2] != ["101"]:
            raise RuntimeError(f"浏览器拒绝了调试连接：{status}")

    def _fill(self) -> None:
        chunk = self.sock.recv(1 << 20)
        if not chunk:
            raise RuntimeError("浏览器断开了调试连接")
        self.buffer.extend(chunk)

    def _frame_length(self) -> int:
        """Bytes of the first frame once it has fully arrived, else 0."""
        buf = self.buffer
        if len(buf) < 2:
            return 0
        size, start = buf[1] & 0x7F, 2
        if size > 125:
            start = 4 if size == 126 else 10
            if len(buf) < start:
                return 0
            size = int.from_bytes(buf[2:start], "big")
        total = start + (4 if buf[1] & 0x80 else 0) + size
        return total if len(buf) >= total else 0

    def _read(self) -> dict | None:
        """Block for one frame and return the message it completes, if any."""
        while not (total := self._frame_length()):
            self._fill()
        frame = bytes(self.buffer[:total])
        del self.buffer[:total]
        payload = frame[{126: 4, 127: 10}.get(frame[1] & 0x7F, 2):]
        if frame[1] & 0x80:
            payload = self._mask(payload[4:], payload[:4])
        opcode = frame[0] & 0x0F
        if opcode == 0x8:
            raise RuntimeError("浏览器关闭了调试连接")
        if opcode == 0x9:
            self._write(0xA, payload)
        elif opcode in (0x0, 0x1, 0x2):
            self.partial.extend(payload)
            if frame[0] & 0x80:
                message = json.loads(bytes(self.partial))
                self.partial.clear()
                return message
        return None

    def _write(self, opcode: int, payload: bytes) -> None:
        size = len(payload)
        if size < 126:
            length = bytes([0x80 | size])
        elif size < 1 << 16:
            length = bytes([0x80 | 126]) + size.to_bytes(2, "big")
        else:
            length = bytes([0x80 | 127]) + size.to_bytes(8, "big")
        key = os.urandom(4)
        self.sock.sendall(bytes([0x80 | opcode]) + length + key + self._mask(payload, key))

    @staticmethod
    def _mask(data: bytes, key: bytes) -> bytes:
        stream = (key * (len(data) // 4 + 1))[:len(data)]
        return (int.from_bytes(data, "big") ^ int.from_bytes(stream, "big")).to_bytes(len(data), "big")

    def send(self, method: str, params: dict | None = None, session: str | None = None) -> dict:
        self.next_id += 1
        request = {"id": self.next_id, "method": method, "params": params or {}}
        if session:
            request["sessionId"] = session
        self._write(0x1, json.dumps(request).encode())
        while True:
            message = self._read()
            if message is None:
                continue
            if message.get("id") == self.next_id:
                if "error" in message:
                    raise RuntimeError(f"{method}：{message['error'].get('message')}")
                return message.get("result", {})
            self._dispatch(message)

    def pump(self, seconds: float) -> None:
        """Keep dispatching events while waiting."""
        deadline = time.monotonic() + seconds
        while (left := deadline - time.monotonic()) > 0:
            if self._frame_length() or select.select([self.sock], [], [], left)[0]:
                message = self._read()
                if message:
                    self._dispatch(message)

    def _dispatch(self, message: dict) -> None:
        for listener in self.listeners:
            listener(message)

    def evaluate(self, expression: str, session: str):
        result = self.send("Runtime.evaluate", {"expression": expression, "awaitPromise": True, "returnByValue": True}, session)
        if "exceptionDetails" in result:
            details = result["exceptionDetails"]
            raise RuntimeError(f"页面脚本出错：{(details.get('exception') or {}).get('description') or details.get('text')}")
        return result.get("result", {}).get("value")

    def close(self) -> None:
        if self.sock:
            try:
                self.send("Browser.close")
            except (OSError, RuntimeError):
                pass
            self.sock.close()
        try:
            self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()
        for _ in range(10):  # Windows keeps files locked until helper processes exit
            shutil.rmtree(self.profile, ignore_errors=True)
            if not os.path.exists(self.profile):
                break
            time.sleep(0.3)


def cache_dir(out: Path) -> Path:
    """`.cache/ai-ui-design` of the project holding the screenshots; the system temp folder when it is read-only."""
    root = next((folder for folder in (out, *out.parents) if (folder / ".git").exists() or (folder / "package.json").exists()), out)
    cache = root / ".cache" / "ai-ui-design"
    try:
        cache.mkdir(parents=True, exist_ok=True)
        (cache / ".gitignore").write_text("*\n")
        os.rmdir(tempfile.mkdtemp(dir=cache))  # entries must be creatable, not just the folder present
    except OSError:
        cache = Path(tempfile.gettempdir()) / "ai-ui-design"
        cache.mkdir(exist_ok=True)
    return cache


def in_use(profile: Path) -> bool:
    """Whether a live run still owns this profile: its browser answers, or it is under an hour old and starting up."""
    try:
        port = int((profile / "DevToolsActivePort").read_text().split("\n")[0])
    except (OSError, ValueError):
        try:
            return time.time() - profile.stat().st_mtime < 3600
        except OSError:
            return False
    try:
        socket.create_connection(("127.0.0.1", port), timeout=0.2).close()
        return True
    except OSError:
        return False


def sweep(cache: Path) -> None:
    """Delete profiles left behind by runs that were killed."""
    for profile in cache.glob("chrome-*"):
        if not in_use(profile):
            shutil.rmtree(profile, ignore_errors=True)


class Page:
    """Load state and problems of one tab, collected from its CDP events."""

    def __init__(self, session: str):
        self.session, self.frame, self.loaded, self.status = session, None, False, None
        self.inflight, self.urls, self.problems, self.last_network = set(), {}, [], time.monotonic()

    def __call__(self, message: dict) -> None:
        if message.get("sessionId") != self.session:
            return
        method, params = message.get("method", ""), message.get("params", {})
        if method.startswith("Network."):
            self.last_network = time.monotonic()
        if method == "Page.loadEventFired":
            self.loaded = True
        elif method == "Network.requestWillBeSent":
            self.inflight.add(params["requestId"])
            self.urls[params["requestId"]] = params["request"]["url"]
        elif method in ("Network.loadingFinished", "Network.loadingFailed"):
            self.inflight.discard(params["requestId"])
            if method == "Network.loadingFailed" and not params.get("canceled"):
                self.note(f"请求失败 {params.get('errorText')}：{self.urls.get(params['requestId'], '')}")
        elif method == "Network.responseReceived":
            status, url = params["response"].get("status", 0), params["response"].get("url", "")
            if params.get("type") == "Document" and params.get("frameId") == self.frame and self.status is None:
                self.status = status
            if status >= 400 and not url.endswith("/favicon.ico"):
                self.note(f"HTTP {status}：{url}")
        elif method == "Runtime.exceptionThrown":
            details = params.get("exceptionDetails", {})
            self.note("脚本异常：" + ((details.get("exception") or {}).get("description") or details.get("text", "")).split("\n")[0])
        elif method == "Runtime.consoleAPICalled" and params.get("type") == "error":
            self.note("console.error：" + " ".join(str(arg.get("value", arg.get("description", ""))) for arg in params.get("args", [])))

    def note(self, text: str) -> None:
        text = text[:240]
        if text not in self.problems:
            self.problems.append(text)


def act(browser: Browser, session: str, action: str, deadline: float, settle: bool) -> None:
    kind, _, value = action.partition(":")
    find = f"document.querySelector({json.dumps(value.split('=>')[0])})"
    if kind == "wait":
        if re.fullmatch(r"\d+(\.\d+)?", value):
            browser.pump(float(value) / 1000)
            return
        while not browser.evaluate(f"!!{find}", session):
            if time.monotonic() > deadline:
                raise RuntimeError(f"等不到元素 {value}")
            browser.pump(0.1)
        return
    if kind in ("click", "hover"):
        point = browser.evaluate(f"(el => {{ if (!el) return null; el.scrollIntoView({{block: 'center', inline: 'center'}});"
                                 f" const r = el.getBoundingClientRect(); return [r.x + r.width / 2, r.y + r.height / 2]; }})({find})", session)
        if point is None:
            raise RuntimeError(f"找不到元素 {value}")
        mouse = {"x": point[0], "y": point[1]}
        browser.send("Input.dispatchMouseEvent", {"type": "mouseMoved", **mouse}, session)
        if kind == "click":
            for phase in ("mousePressed", "mouseReleased"):
                browser.send("Input.dispatchMouseEvent", {"type": phase, "button": "left", "clickCount": 1, **mouse}, session)
    elif kind in ("focus", "type"):
        selector, _, text = value.partition("=>")
        if not browser.evaluate(f"(el => {{ el?.focus(); return !!el; }})({find})", session):
            raise RuntimeError(f"找不到元素 {selector}")
        if text:
            browser.send("Input.insertText", {"text": text}, session)
    elif kind == "press":
        key, _, times = value.partition("*")
        if key not in KEYS:
            raise ValueError(f"不支持的按键 {key}；可用 {'、'.join(KEYS)}")
        text = {"Enter": "\r", "Space": " "}.get(key)
        for _ in range(int(times or 1)):
            for phase in ("keyDown" if text else "rawKeyDown", "keyUp"):
                event = {"type": phase, "key": " " if key == "Space" else key, "code": key, "windowsVirtualKeyCode": KEYS[key]}
                if text and phase == "keyDown":
                    event["text"] = text
                browser.send("Input.dispatchKeyEvent", event, session)
    elif kind == "scroll":
        browser.evaluate(f"scrollTo(0, {value})" if re.fullmatch(r"\d+(\.\d+)?", value) else f"{find}?.scrollIntoView({{block: 'start'}})", session)
    elif kind == "eval":
        browser.evaluate(value, session)
    else:
        raise ValueError(f"不认识的动作 {action}；可用 click、hover、focus、type、press、scroll、wait、eval")
    if settle:
        browser.pump(0.2)


def shoot(browser: Browser, session: str, path: Path, viewport: tuple, full: bool, page: Page) -> str:
    width, _, scale, _ = viewport
    params: dict = {"format": "png"}
    if full:
        metrics = browser.send("Page.getLayoutMetrics", session=session)
        height, limit = (metrics.get("cssContentSize") or metrics["contentSize"])["height"], 16384 / scale
        if height > limit:
            page.note(f"页面高 {height:.0f}px，整页截图只截到前 {limit:.0f}px")
        params.update(captureBeyondViewport=True, clip={"x": 0, "y": 0, "width": width, "height": min(height, limit), "scale": 1})
    path.write_bytes(base64.b64decode(browser.send("Page.captureScreenshot", params, session)["data"]))
    return str(path)


def capture(browser: Browser, target: str, viewport: tuple, args: argparse.Namespace, out: Path) -> dict:
    width, height, scale, mobile = viewport
    tab = browser.send("Target.createTarget", {"url": "about:blank"})["targetId"]
    session = browser.send("Target.attachToTarget", {"targetId": tab, "flatten": True})["sessionId"]
    page = Page(session)
    browser.listeners.append(page)
    try:
        for domain in ("Page", "Runtime", "Network"):
            browser.send(f"{domain}.enable", session=session)
        page.frame = browser.send("Page.getFrameTree", session=session)["frameTree"]["frame"]["id"]
        browser.send("Emulation.setDeviceMetricsOverride", {"width": width, "height": height, "deviceScaleFactor": scale, "mobile": mobile}, session)
        browser.send("Emulation.setFocusEmulationEnabled", {"enabled": True}, session)
        if mobile:
            browser.send("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5}, session)
        media = [{"name": "prefers-reduced-motion", "value": "reduce"}] if args.reduced_motion else []
        if args.dark:
            media.append({"name": "prefers-color-scheme", "value": "dark"})
        if media:
            browser.send("Emulation.setEmulatedMedia", {"features": media}, session)
        if args.frames:
            # Slow the timeline so animations are still running when the frames are taken.
            browser.send("Animation.enable", session=session)
            browser.send("Animation.setPlaybackRate", {"playbackRate": 0.01}, session)
        error = browser.send("Page.navigate", {"url": target}, session).get("errorText")
        if error:
            raise RuntimeError(f"打不开 {target}：{error}")
        deadline = time.monotonic() + args.timeout
        while not page.loaded and time.monotonic() < deadline:
            browser.pump(0.1)
        if not page.loaded:
            page.note(f"{args.timeout:g} 秒内没等到 load 事件，截到的可能是加载中的画面")
        quiet_until = min(deadline, time.monotonic() + 8)
        while time.monotonic() < quiet_until and (page.inflight or time.monotonic() - page.last_network < 0.5):
            browser.pump(0.1)
        browser.evaluate("document.fonts.ready.then(() => true)", session)
        browser.pump(args.wait / 1000)
        if args.frames and args.do:
            browser.evaluate(MARK, session)
        for action in args.do:
            act(browser, session, action, deadline, settle=not args.frames)
        report = browser.evaluate(CHECKS, session) or {}
        name = shot_name(target, args.name, viewport)
        if args.frames:
            files, count = [], 0
            for index in range(args.frames):
                fraction = index / (args.frames - 1) if args.frames > 1 else 1.0
                count = browser.evaluate(f"{SEEK}({fraction})", session)
                files.append(shoot(browser, session, out / f"{name}-f{round(fraction * 100)}.png", viewport, args.full, page))
            if not count:
                page.note("没有可暂停的 CSS/WAAPI 动画；JS 逐帧驱动的动画请改用录屏")
        else:
            files = [shoot(browser, session, out / f"{name}.png", viewport, args.full, page)]
        return {"target": target, "viewport": viewport_label(viewport), "files": files, "title": browser.evaluate("document.title", session),
                "status": page.status, "problems": page.problems, **report}
    finally:
        browser.listeners.remove(page)
        try:
            browser.send("Target.closeTarget", {"targetId": tab})
        except (OSError, RuntimeError):
            pass


def viewport_label(viewport: tuple) -> str:
    width, height, scale, mobile = viewport
    return ("mobile-" if mobile else "") + f"{width}x{height}" + (f"@{scale:g}" if scale != 1 else "")


def shot_name(target: str, label: str | None, viewport: tuple) -> str:
    parts = urlsplit(target)
    base = Path(parts.path).stem if parts.scheme == "file" else " ".join(filter(None, [parts.hostname, str(parts.port or ""), parts.path, parts.query]))
    slug = lambda text: re.sub(r"[^\w]+", "-", text.lower()).strip("-_")
    return "-".join(filter(None, [slug(base) or "page", slug(label or ""), viewport_label(viewport)]))


def normalize(target: str) -> str:
    if Path(target).exists():
        return Path(target).resolve().as_uri()
    if re.match(r"(localhost|127\.0\.0\.1|\[::1\])(:\d+)?(/|$)", target):
        return "http://" + target
    if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*://|about:|data:", target):
        return target
    raise ValueError(f"{target} 既不是 URL，也不是存在的文件")


def parse_viewport(spec: str) -> tuple:
    if spec in PRESETS:
        return PRESETS[spec]
    match = re.fullmatch(r"(mobile:)?(\d+)x(\d+)(?:@(\d+(?:\.\d+)?))?", spec)
    if not match:
        raise argparse.ArgumentTypeError(f"视口写成 desktop、mobile、1280x800 或 mobile:375x667@3：{spec}")
    return int(match[2]), int(match[3]), float(match[4] or 1), bool(match[1])


def main() -> int:
    if sys.version_info < (3, 9):
        print("需要 Python 3.9 或更新版本", file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description="用本机已装的 Chrome、Edge、Chromium 或 Brave 无头截图并做基础检查；只用 Python 标准库")
    parser.add_argument("targets", nargs="+", help="URL（如 http://localhost:5173/orders）或本地 HTML 文件")
    parser.add_argument("--out", type=Path, required=True, help="截图目录，放在任务目录下")
    parser.add_argument("--viewport", action="append", type=parse_viewport,
                        help="desktop（1440x900）、mobile（390x844@2，触屏）、WxH[@DPR] 或 mobile:WxH[@DPR]；可重复，默认桌面加手机")
    parser.add_argument("--full", action="store_true", help="截整页，看长页节奏；默认只截首屏")
    parser.add_argument("--do", action="append", default=[], metavar="ACTION",
                        help="截图前依次执行：click:SEL、hover:SEL、focus:SEL、type:SEL=>文本、press:Tab*3、scroll:SEL或像素、wait:毫秒或SEL、eval:JS")
    parser.add_argument("--name", help="写进文件名的状态，如 hover、error")
    parser.add_argument("--frames", type=int, default=0, help="把动画暂停在 N 个均匀时刻各截一张；起、中、止用 3")
    parser.add_argument("--reduced-motion", action="store_true", help="模拟 prefers-reduced-motion: reduce")
    parser.add_argument("--dark", action="store_true", help="模拟 prefers-color-scheme: dark")
    parser.add_argument("--wait", type=float, default=300, help="网络空闲后再等的毫秒数（默认 300）")
    parser.add_argument("--timeout", type=float, default=30, help="单页超时秒数（默认 30）")
    parser.add_argument("--browser", default=os.environ.get("CHROME_PATH"), help="浏览器可执行文件；默认自动查找，也读 CHROME_PATH")
    args = parser.parse_args()
    out = args.out.resolve()
    if out.is_relative_to(SKILL_ROOT):
        print("未截图：截图不能写进 Skill 安装目录", file=sys.stderr)
        return 2
    try:
        targets = [normalize(target) for target in args.targets]
        binary = find_browser(args.browser)
    except (ValueError, LookupError) as exc:
        print(f"未截图：{exc}", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    for name in ("SIGTERM", "SIGHUP"):  # turn termination into SystemExit so the browser and profile get cleaned up
        if hasattr(signal, name):
            signal.signal(getattr(signal, name), lambda *_: sys.exit(1))
    shots, browser = [], None
    try:
        cache = cache_dir(out)
        sweep(cache)
        browser = Browser(binary, args.timeout, cache)
        for target in targets:
            for viewport in args.viewport or [PRESETS["desktop"], PRESETS["mobile"]]:
                try:
                    shots.append(capture(browser, target, viewport, args, out))
                except (RuntimeError, ValueError) as exc:
                    shots.append({"target": target, "viewport": viewport_label(viewport), "error": str(exc)})
    except (RuntimeError, OSError) as exc:
        shots.append({"error": f"浏览器出错：{exc}"})
    finally:
        if browser:
            browser.close()
    print(json.dumps({"browser": binary, "shots": shots}, ensure_ascii=False, indent=1))
    return 1 if any("error" in shot for shot in shots) else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Path: `skills/ai-ui-design/references/build-and-verify.md`

````markdown
# 制作与验证

动手改界面前读一次，直接照做，不逐条汇报。

## 先读项目

- 写代码前读依赖清单、样式入口与 Token 定义、要用到的共享组件的源码或类型定义。只使用读到过的组件 API、类名与 Token；拿不准就打开定义确认。
- 字体、图标、图片与链接，来源是项目已安装的依赖、本地文件，或本轮实际打开过的 URL。核实不了就用系统字体栈、字符或占位。
- 新增依赖先向用户说明用途并取得同意。
- 颜色、字阶、间距、圆角用项目现有 Token；新项目先定义成 CSS 变量，组件只引用变量。

## 成品检查

检查做出来的结果，范围限于本次新建或改动的部分：

- **对比度**用脚本算：`python3 <skill>/scripts/check_contrast.py "#1f2328 #fff" "#8a9099 #fff large"`。正文 4.5:1；大字、图标和识别控件必需的边界（输入框描边、焦点环）在色对后加 `large` 按 3:1。纯装饰的分隔线不设门槛。
- **状态**：悬停、键盘焦点、按下、禁用、加载、空、错误——页面有对应逻辑的才做。
- **真实内容**：超长名称、极端数值、中文多行标题不挤破布局。
- **视口**：手机 390×844 与桌面 1440×900，或项目既定断点。没有非预期的横向滚动；移动端适配安全区，热区不小于 24×24 CSS px（主要操作 44×44），操作栏不被虚拟键盘遮挡。
- **键盘**能走完关键操作，焦点可见；遵循 `prefers-reduced-motion`。
- **浏览器自带的表面**（新界面）：文字选区、光标、滚动条、焦点环用方向的色板定制，默认样式不属于任何设计。
- **中文字体**用系统字体栈或子集化的 woff2。
- 运行项目自己的 lint、类型检查与构建。

## 看图：一轮批量，至多两轮

1. 做完整之后，桌面与手机一起截一轮，逐张打开看，把问题一批修完。
2. 再截一轮确认，然后停。还剩的问题写进交付的遗留项。

小改动只截一张改动处的图。

截图用本 Skill 的脚本：它找本机已装的 Chrome、Edge、Chromium 或 Brave（也认 Playwright、Puppeteer 缓存的浏览器）无头运行，只用 Python 标准库，不往项目装依赖。浏览器的临时配置放在项目的 `.cache/ai-ui-design/`（自带 `.gitignore`），用完即删，被中断留下的在下次运行时清掉。

```bash
python3 <skill>/scripts/screenshot.py http://localhost:5173/orders design/a.html --out <任务目录>/shots/round-1
```

- 默认桌面 1440×900 与手机 390×844 各截首屏；`--viewport` 换尺寸。
- **状态**：`--do` 先操作再截，`--name` 把状态写进文件名。悬停 `hover:.card`，键盘焦点 `press:Tab*3`，展开 `click:#menu`，错误 `type:#email=>abc` 再 `press:Enter`。
- **报告**：输出的 JSON 列出横向溢出与撑出页面的元素、小于 12px 的文字、小于 24×24 的热区、控制台报错与失败请求、白屏。逐条修，或写明为什么保留。报告干净不等于画面好，截图仍要逐张打开看。
- 脚本找不到浏览器或起不来时，改用宿主自带的浏览器或截图工具；都没有就请用户截图，或如实写"未验证实际视觉"。
- 截图要打开看过才算数；空白页、加载中、报错页不算。
- 长页先用 `--full` 看整体节奏，再看关键局部；中文多行标题、正文、控件与窄屏换行按实际阅读尺寸看。重叠或裁切时回到内容和布局修复。
- 关键区域在 100% 与 200% 缩放下各看一次；200% 用视口减半、设备像素比 2 来近似（`--viewport 720x450@2`）。
- 动效靠静态截图验证不了：按 [动效](motion.md) 的验收取起、中、止三帧或录屏；都没看过就在交付里写动效未验证。

## 截图精准还原

- **锁定视口**：确定参考图的逻辑视口（如桌面 1440×900、手机 390×844）。物理像素不等于逻辑视口；无法确定时推断并说明假设。
- **几何拆解**：
  1. 测量主区域比例关系（侧边栏宽度、主内容栏边距、多列卡片间隙）。
  2. 提取共享对齐线：标题基线、输入框左对齐线、操作按钮垂直中轴。
  3. 测定字阶与行高：标题、正文、辅助标签的相对字号与行间距。
- **参考图是唯一基线**：主色、排版结构和风格都照参考图。
- **补齐缺失状态**：参考图没有的悬停、按下、禁用、错误与窄屏重排，按功能补齐并标注为"合理延展"。
````

## Path: `skills/ai-ui-design/references/design-direction.md`

````markdown
# 设计方向

"独特一点""随机一点"推不动模型，它只会换几处装饰。推力来自三处：先定调性，再用生成引擎起方向，最后用可检验的规则逼出差异。

题材、材质、场景、字体和配色都从当前产品的内容、受众和使用场合推出；和常见"网红风格"撞上时，说得出来自这个产品的理由才保留。

## 先分界面类型

类型由这一个界面决定，不由产品决定：工具产品的落地页仍是"说服"，时尚品牌的帮助文档仍是"阅读"。

| 类型 | 界面 | 本文件怎么用 |
| --- | --- | --- |
| 说服 | 落地页、营销、定价 | 全部适用 |
| 操作 | 工具、后台、设置、编辑器 | 调性、生成引擎、方向卡照用。跳过首屏骨架表，改比主工作区布局：导航方式、信息密度、主对象离主动作多远。品牌落在精确的细节上，记忆点放在操作反馈与边角页面 |
| 阅读 | 文档、文章、帮助 | 差异落在字族、行长、目录与章节结构上，骨架只看正文页 |
| 体验 | 作品集、展示 | 作品本身占首屏，界面退后 |

## 流程：与用户共创

分三轮，每轮等用户回应：

1. **发散与偏好**：按下文定调性，再用不同生成引擎列出 6–8 个跨度大的视觉隐喻（如博朗工业仪器、瑞士网格档案库、等距微缩工坊），每个一行，故意省略实现细节。同一条消息里请用户说出体感偏好：按钮是清脆的机械阻尼还是平滑液态；表面是哑光颗粒还是通透玻璃；哪些俗套元素绝对不要。
2. **小样**：据此写 2–3 张方向卡、过差异检验，做成可交互的轻量小样，用 [风格对比页](style-explorer.md) 并排交付；改版时把现状截图作为基线一起放进去。
   - 动手前按 [小样到生产](mockup-to-production.md) 选形态：已有工程优先做成 dev server 里的临时路由，进入生产时平移，不重写。
   - 每个小样是首屏加最能体现方向的一两个区块。
   - 介绍产品的页面展示产品真正交付的实样（一份导出的报告、一段处理后的数据），用实物代替"能做什么"的文字承诺。
3. **拼装锁定**：收集试玩反馈（如"A 的配色 + B 的布局 + C 的操作反馈"），融合成一份设计说明，用户确认后进入生产实现。

## 先定调性，再求差异

从产品的题材、受众、品牌语气和使用场合推出调性。用五个刻度描述，每个刻度都写出依据：

| 刻度 | 两端 | 在画面上看什么 |
| --- | --- | --- |
| 能量 | 安静 ↔ 喧闹 | 饱和度、对比、元素是否碰撞 |
| 完成度 | 粗粝 ↔ 精致 | 边缘处理、颗粒与噪点、对齐是否严格 |
| 密度 | 疏 ↔ 密 | 留白尺度、叠层、网格纪律 |
| 分量 | 轻 ↔ 重 | 字重、色块面积、阴影硬度 |
| 严肃度 | 活泼 ↔ 庄重 | 圆角、插画语言、动效幅度 |

例如"地下现场演出社区 → 喧闹、粗粝、密"，"冥想陪伴 → 安静、精致、疏"。两种都完全成立，失败的是没有依据的默认：
- 证据指向喧闹粗粝，交付的却是米色卡片、柔和阴影和大留白。这是最常见的失败，设计被磨回了模型默认的"安静高级"。
- 反过来，为了显得有趣，给一个本该安静的产品硬加颗粒、撕纸边和粗边框。

证据锁定调性时，所有候选留在这个调性里，在构图、色彩身份和主视觉上拉开差异，每个候选都是认真的答案而非"安静极简保底"。证据确实模糊时，候选才分布在不同调性上。

### 模糊词必须翻译

"高级、精致、克制、史诗、有文学感、简洁"不能当作设计理由。用户或你自己说出这类词时，先翻译成可观察的决定：

| 模糊词 | 翻译成什么 |
| --- | --- |
| 高级 | 先说清是哪一种高级，再决定字体的对比、分隔的方式、间距的尺度和色相的数量。只说高级什么也没决定 |
| 精致 | 公差：字距怎么调、对齐到几像素的网格、阴影最多几级、色相最多几种 |
| 克制 | 饱和度预算，例如强调色不超过画面 10%；动效幅度上限；色相数量上限 |
| 史诗 | 尺度：展示字多大、主图占多少面积、明暗对比多强 |
| 文学感 | 字族的性格、行长、行高和配色，各取什么值 |
| 粗糙 | 用哪些手段，各用到什么程度，例如错位多少像素、旋转多少度 |
| 简洁 | 密度档位，以及删掉什么、为什么删。简洁是结果，不是指令 |

翻译不出可观察决定的词，从理由里删掉。

## 用生成引擎起方向

每个方向都从一个具体的引擎出发，而不是从形容词出发。不同方向最好用不同的引擎：

- **材质 × 环境**：一种材质放在一个具体的环境里，比如"湿陶土 × 午后的工作室"。由材质推出光照、深度、边缘的处理和动效的阻尼。
- **一个具体场景**：一个有时间、地点和光线的场景，比如"凌晨两点的便利店"。由场景里的光线、声音、材料和节奏推出色彩、质感和动效速度。适合情绪型工具。
- **角色原型**：给产品一个性格，比如"一丝不苟的档案管理员"，让性格决定字体、色彩和动作。
- **一场设计运动或文化语法**：选一个和产品的题材、受众或地域有真实联系的设计运动或视觉传统（如博朗工业设计、瑞士国际主义平面网格、日本手造工坊），借用它的语法，而不是贴它的图案。
- **其他领域的整套表现形式**：把另一个领域的媒介或器物的表达方式借过来，比如把行程做成一张登机牌。只借它最有辨识度的一两个手法，页面本身仍是原来的体裁；不把那个媒介的部件一件件搬来，那会变成道具堆砌。
- **外部熵种子**：模型自己产生不了随机性，"随机"只会召回词义上的随机套路。运行 `openssl rand -hex 3`，把 6 位十六进制逐位读成 0–15 的数：第 1–2 位合成 0–255，乘 1.4 得主色相；第 3 位 mod 8 加 1，取骨架表的第几行；第 4 位 mod 5 加 1，取上面第几种引擎作为隐喻来源；第 5 位 mod 9 加 4，得网格列数；第 6 位乘 0.03 加 1.2，得字阶比例。调性仍由证据决定；这些取值照用，再为它们找出来自产品的理由，骨架和本轮其他方向撞了就重取。种子本身不出现在界面上。适合需要多套彼此迥异的方案、或结果总滑回蓝紫科技风时。
- **有意打破常规**：激进的非对称版式、不和谐的配色与字体、让人不安的大胆留白，但整体仍然好看、功能完整。

感受词从这个品牌出发，而不是从行业出发。"美味、温暖、有食欲"会把每个食品应用都推向橙色；"深夜治愈、独处、温柔"才属于某一个品牌。

## 先定首屏骨架，再写文案

模型最顽固的习惯是左右分栏：一边大标题，另一边说明、按钮或一张图。换字体、换配色、换材质都改变不了它，因为它在写文案之前就定下来了。所以骨架要在写任何文案之前决定。

每个方向先从下表选一个首屏骨架，再用 3–5 个方框画出首屏线框：每块是什么、占首屏多大面积、阅读从哪里开始。

| 骨架 | 首屏长什么样 |
| --- | --- |
| 满版图像压字 | 一张图占满首屏，标题和动作压在图的安全区里 |
| 居中单一物件 | 一个物件或一句话居中，四周是大面积空白 |
| 画面即界面 | 首屏就是产品界面或一件实物本身，标题、导航和按钮都长在它上面 |
| 满版文字 | 文字本身就是画面，字大到占满首屏、跨过边缘或被裁切 |
| 通栏上下堆叠 | 通栏大标题横跨整个宽度，下面紧接内容 |
| 网格拼贴 | 多块内容同时出现，按网格或拼贴排列，没有单一主角 |
| 纵排或斜向 | 文字竖排、斜切或旋转，打破从左到右的阅读 |
| 左右分栏 | 文字一侧，画面一侧。这是模型的默认，一轮最多一个方向使用，并写出为什么非它不可。另一侧必须是跨越结构的图像、色块或图形装置，不能是装在卡片里的产品界面 |

规则：
- 同一轮的方向，骨架互不相同。
- 左右分栏最多出现一次。所谓"大标题九栏、说明三栏"同样算左右分栏。
- 骨架定好之后再写文案。文案去适应骨架，不让骨架去适应"标题 + 说明 + 按钮"的组合。
- 每一轮至少有一个方向让你自己觉得有点冒险：放在同类产品里会显得格格不入，但仍然好看，功能完整。

最常见的模板核心不是左右分栏本身，而是"左边标题和两个按钮，右边一张装在圆角卡片里的产品界面"。那张卡片几乎总是该删的：要么让产品界面本身占满首屏，要么换成一张跨越版面结构的图、一个色块或一个图形装置。

## 方向卡

每个方向写一张方向卡，每项都填具体选择，不填形容词：

| 字段 | 要写到的程度 |
| --- | --- |
| 北极星 | 一句能指导取舍的体验意图：用起来像在什么地方、做什么事 |
| 调性 | 五个刻度的取值及依据 |
| 生成引擎 | 用了哪一种，具体是什么，来自这个产品的什么证据 |
| 首屏骨架 | 从骨架表里选的哪一种，附 3–5 个方框的首屏线框：每块是什么、占多大面积、阅读从哪里开始 |
| 页面结构 | 首屏以下怎么组织，例如单列沉浸滚动，或导航、内容、详情三栏 |
| 各区块的形式 | 首屏以下每个主要区块（实样、功能、定价、数据、结尾等）在这个方向里长成什么。形式从生成引擎推出，不是同一个模块换颜色 |
| 字体 | 具体字族、字重和尺度关系：展示、正文、数字各用什么，相差多大；每个字族注明来源（系统自带、项目已装、本地文件，或需用户同意安装）与回退字体 |
| 色彩 | 用到的十六进制色值及用途，说清这个方向的色彩身份 |
| 主视觉 | 哪张图或哪个图形承担情绪与识别，来自复用、生成还是排版本身 |
| 图标 | 用哪一套（注明已安装或需同意安装）、什么描边粗细和端点，或者不用图标、改用字符和编号 |
| 结构性突破 | 改变首屏结构的那一处偏离常规，以及它怎样放大北极星。手写批注、质感按钮这类局部细节不算 |
| 记忆点 | 集中发力的一两处：在哪个时刻或位置，用什么材质、动作或画法，见"让人记住的一刻" |
| 放弃什么 | 这个方向主动不要的常见做法 |

## 差异检验

方向卡写完、做小样之前，逐条检验：

- **比线框，不比描述**：把各方向的首屏线框并排放在一起比。线框相似就是同一骨架，重选骨架。
- **四项至多一项相同**：首屏骨架、字体、色彩、主视觉四项里，任意两个方向至多一项相同；否则就是同一方向的变体，换一个生成引擎重写其中一个。
- **不按明暗分方向**：头号失败是"一个亮、一个暗、一个暖"。每个方向要有自己的色彩身份：不同的色相家族、不同的材质感，或者黑白灰加至多一种强调色、把颜色交给内容，这常常是最高级的选择。明暗是色彩身份的结果，不是区分方向的依据。
- **结构也要不同**：不同方向可以有不同的页面组织。三个方向页面结构完全相同、只是颜色和质感不同，就还没有拉开差异。
- **至少一个走到极端**：至少一个方向在各项上都取明确的一端，不做折中。
- **至少一个打破品类套路**：在同一调性内，至少一个方向不用这个品类的默认版式。
- **盲看**：遮住名字和说明只看画面，仍能说出每个方向带给人的不同感受。

## 让人记住的一刻

模型做的页面常常处处及格，却没有一处让人记住。惊艳很少来自整页都用力，而是来自一处做到极致：通常是一个组件的一次动作，结果、材质、光影、手感和节奏都做到位。每个方向选一两处集中发力，其余保持安静。

去哪里找：
- **用户会做的动作**：点按、拖动、切换、提交，比滚动更容易成为记忆点。
- **关键时刻**：付款成功、第一次完成任务、升级、删除、上传、等结果。这些时刻情绪最强，一个小动画的回报最高。
- **边角页面**：404、空状态、加载、页脚。没人期待，风险又低，最容易出彩。
- **AI 在工作的时候**：把过程按顺序展开：步骤一个个亮起，日志一行行流进来，做完的一步收起，正在做的一步展开。白底黑字照样成立，不需要材质和发光。

怎么想：
- **让结果当场发生**：状态切换不只换一个图标，而是让被影响的东西当场变化：打开深色模式，整页像拉下遮光帘一样暗下去；拖动时间，画面的天色跟着走。
- **把数字画成看得见的量**：百分比、时长、余额，先问能不能画成一个量：点亮的格子、填满的长度、一格代表一天的网格。数字只是标签，量才是画面。
- **给抽象的状态一种材质**：先问"这个状态如果是一个实物，会是什么"，答案从产品所在的领域里找。
- **给控件物理和性格**：拖动有弹性和重量，按下有光影变化，拉过头会不情愿地弹回来。
- **一张画面垫底时，界面要退后**：做法见 [素材](media.md) 的"一张画当舞台"。
````

## Path: `skills/ai-ui-design/references/media.md`

````markdown
# 素材

好配图先承担意思，再承担气氛，最后和页面接成一体。生成图最常见的失败是画得太满：细节越丰富越像图库照片，没有重点，也和页面无关。

## 主图先定，页面围绕它排

先问："如果只保留一张图、一个标题和一个动作，哪张图值得占这个位置？"再决定是否需要更多模块。生成或挑选之前写下一句：**这张图要让人一眼看懂什么？** 答不上来就先别生成。"一张好看的使用场景"不是答案；"产品把一堆混乱变成了哪几个清楚的结果"才是。

图像的主体、视角、尺度、光线、颜色、材质和留白跟随北极星；页面的字体、背景、边缘处理与运动从这张图建立呼应，或用一处受控的反差突出主动作。统一是共享视觉逻辑，不是给所有图套同一个滤镜。

- **用对比编排信息**：整体统一成一种低调的材质或颜色（白模、单色、失焦或剪影），只让承载核心信息的少数几处具备颜色、高光或细节。例如白色仓库模型里只有出了异常的两排货架亮成橙色，灰度地图上只有正在配送的路线是彩色。所有地方都一样精细，就等于没有重点。
- **让图成为结构**：跨过版面分界、占满首屏、和文字叠在一起，页面是一个完整的世界，而不是"一张页面配一张图"。容易和页面接上的主体：
  - 能跨过两块色面分界的单个物件。
  - 能延伸出画面的线：线缆、轨道、河流、胶片、纸带。
  - 能在上面标注的空间：模型、地图、剖面、平面图。

## 图与代码分工

真实材质、玻璃折射、金属反光、3D 主体是 CSS 伪拟态的真实度上限，也是廉价 AI 味的主要来源，交给生成图。代码负责需要精确、可编辑、会响应式变化的部分：文字、界面、数据、延伸出去的细线、状态指示灯，压在图上或用引线连到图上。生图模型会画错字，画出来的字也无法修改、选中、翻译和读屏。

**引线标注**：1px 细引线加紧凑等宽文字，端点精确对准图中像素坐标。

## 生图能力与密钥

1. **宿主有生图工具**（在当前工具清单里确认存在）：主动调用，产物存入项目资源目录。
2. **没有，且设计确需**：向用户说明需要什么素材、为什么，并请求一个临时 API Key：
   > 这个设计需要生成 [素材描述]，当前环境没有生图工具。请提供临时 API Key；它只存放在本地 `.env.agents`，仅供本次素材渲染，不写入业务代码、不进版本控制。
3. **密钥隔离**：项目是 git 仓库时，先用 `git check-ignore .env.agents` 确认它被忽略（未忽略就先把它加进 `.gitignore`），再把密钥写入项目根目录 `.env.agents`；由独立的本地脚本读取密钥、生成并落地为静态文件。前端代码只引用生成好的文件。

交付说明里只写实际生成并落地的素材；没生成出来的写成素材需求与占位。

## 提示词 7 步公式

按固定顺序写，每项一两句：

1. **主体与表现形式**：什么东西，用什么体裁呈现（照片、工笔、模型、3D 黏土或等距剖面），体裁从页面的方向推出。
2. **视角与镜头**：机位的高度和角度（顶视、45度等距、平视、微距）；焦段和景深。
3. **构图**：主体在画面里的位置和占比，四周留多少边距，哪一块留空给文字。**必须明确写明"完整地放在画面内，四周留出宽松边距"**，否则常被裁掉一角，无法排版。
4. **背景**：**直接写出页面实际使用的十六进制色值**（如 `#121214`），或者明确要求纯净透明背景。
5. **材质与光**：主光方向、辅光、质感。同一页的多张图必须保持完全相同的光向。
6. **重点**：用什么对比让哪几处成为焦点，其余部分怎样退后。
7. **排除**：文字、标志、伪界面、屏幕内容；透明物件写明"地面不要阴影"。

## 让图长在页面上

- **物理取色一致**：不透明的图，从图的四角实际取色，页面背景用同一个十六进制色值。
- **边缘羽化**：四边淡出到这个颜色，图直接长在页面上（无边框、无卡片）。用 `mask-image`，或导出时直接渐隐成页面色值。
- **透明通道检查**：先放在最终背景上检查边缘白边与棋盘格残留。阴影由页面按背景用 CSS 投影添加，不烘焙在图里。

### 一张画当舞台

图不讲具体业务信息，只给宏观气氛：全页以克制的黑白灰为主，一幅有鲜明笔触的艺术画（油画、水彩、版画）或一张有情绪的摄影是唯一的色彩来源。

- 界面缩到只剩导航、一句话和真实界面的简化版，浮在画上，画从边缘露出来；文字下方的画面虚化或压暗，保证可读。
- 松和紧互相衬托：画越自由写意，界面越要精确、干净、收敛。

## 视频

### 循环悬浮主体（抠像）

适合 Hero 位的旋转晶体、解构机械、液态折射体。

1. 用视频模型生成主体在**页面最终底色上**无缝循环运动的片段。玻璃、水晶、液体会把背景折射进去，在绿幕上生成会残留抠不掉的绿边。
2. 抠像去除底色，导出两份带 Alpha 的文件：WebM（VP9，给 Chrome 与 Firefox，如 `ffmpeg -i frames/%04d.png -c:v libvpx-vp9 -b:v 0 -crf 25 -pix_fmt yuva420p hero.webm`）和 HEVC（`.mov`，给 Safari 与 iOS，它们不显示 WebM 的透明通道）。HEVC 透明视频要在 macOS 上编码；做不了时改用透明序列帧。
3. 放在两个色块或区块的分界线上，打破矩形框。HEVC 排在前面，Safari 会选它，其他浏览器跳到 WebM：

```html
<video autoplay loop muted playsinline>
  <source src="hero.mov" type='video/mp4; codecs="hvc1"'>
  <source src="hero.webm" type="video/webm">
</video>
```

### 关键帧随动（Scroll Scrubbing）

适合产品详情、硬件拆解、步骤引导。

1. 生图得到状态 0（收拢）与状态 1（展开）。
2. 把两张图作首尾帧，用视频模型插出 2–3 秒过渡。
3. 重新编码成每帧都是关键帧（如 ffmpeg 加 `-g 1`），否则拖动时卡顿跳帧。
4. 滚动或拖动进度线性映射到 `currentTime`；`loadedmetadata` 之后 `duration` 才是有效数字：

```ts
const progress = Math.min(Math.max(scrollOffset / totalDistance, 0), 1);
video.currentTime = video.duration * progress;
```

滚动叙事的节奏规则见 [动效](motion.md)。
````

## Path: `skills/ai-ui-design/references/mockup-to-production.md`

````markdown
# 小样到生产

小样的写法决定进入生产时是平移还是重写。写第一个小样前按项目选形态；方向锁定后按"平移"一节落地。

## 先看项目用什么

`package.json` 里的框架、组件库和样式方案决定 Token 与变体落在哪：

| 体系 | Token 落点 | 变体写法 |
| --- | --- | --- |
| Tailwind v4（含 shadcn/ui、shadcn-vue） | 全局 CSS 的 `@theme`；shadcn 的语义色在 `:root` 与 `.dark`，新增的名字在 `@theme inline` 里接上（`--color-brand: var(--brand)`） | 组件 `cva` 里的 variant |
| Tailwind v3、UnoCSS | 配置文件（`tailwind.config`、`uno.config`）的 theme 引用 CSS 变量。Tailwind v3 要让 `bg-brand/50` 生效，变量存成通道值并写成 `rgb(var(--brand) / <alpha-value>)`；shadcn 的 v3 模板把颜色存成不带 `hsl()` 的 HSL 通道 | 同上，或修饰类 |
| CSS 变量型组件库，如 Element Plus | 覆盖它的变量（`--el-color-primary`、`--el-border-radius-base`、`--el-font-family`）。主色的 `-light-3/5/7/8/9` 与 `-dark-2` 是编译时生成的，运行时只改主色要连这几级一起给；或用 SCSS `@forward 'element-plus/theme-chalk/src/common/var.scss' with (...)` 让它自己生成 | 先用组件已有属性（`type`、`size`、`plain`、`round`），不够再包一层组件加类 |
| 配置组件型组件库，如 Ant Design、Ant Design Vue、Naive UI | 根部配置组件：`ConfigProvider` 的 `theme.token` 与 `theme.components`；Naive UI 是 `n-config-provider` 的 `theme-overrides` | 组件级 Token 与已有属性，不够再包一层 |
| CSS Modules、Vue `<style scoped>`、原生 CSS | 全局变量文件的 `:root`，样式只引用 `var()` | 修饰类；CSS Modules 可用 `composes` |
| Web Components | 宿主页面 `:root` 上的自定义属性，能穿透 Shadow DOM；组件内部只引用 `var()` | 属性配 `:host([variant="ghost"])`，外部定制走 `::part()` |

表里没有的组件库先看主题方案属于哪类：CSS 变量型照 Element Plus 处理，配置组件型照 Ant Design 处理。

## 选小样形态

| 项目情况 | 小样形态 | 对比页候选 |
| --- | --- | --- |
| 已有工程，dev server 跑得起来 | **临时路由**：每个方向一个页面，直接用项目组件和真实的数据结构 | `kind: "url"` |
| 新项目，或 dev server 跑不起来 | **静态 HTML**：设计决定全部写进一个 Token 块，样式只引用变量 | `kind: "html"` |

### 临时路由

- **放在能整体删除的位置**：
  - Vite 项目（Vue、React 都一样）在项目根建 `design-lab/<方向>.html` 和入口脚本，照 `main.ts` 装同样的插件与全局样式；dev 下直接访问，默认构建只打包 `index.html`。
  - Nuxt 建 `pages/design-lab/[direction].vue`，开头写 `if (!import.meta.dev) throw createError({ statusCode: 404, fatal: true })`。
  - Next.js 建 `app/design-lab/<方向>/page.tsx`，开头写 `if (process.env.NODE_ENV === "production") notFound()`。
- **方向差异写成 Token 覆盖**：页面根节点加 `data-direction="a"`。CSS 变量的覆盖写在 `:root:has([data-direction="a"]) { … }`，Teleport、Portal 到 `body` 下的弹层也拿得到；写在页面容器上的覆盖管不到它们。配置组件型组件库在页面根包一层配置组件，弹层经上下文拿到 Token。
- **共享组件在方向锁定前不改**：需要新样式时，在 lab 目录里写变体草稿或复制一份改。
- 这类候选不支持对比页的点选标注，意见写进备注。

### 静态 HTML

- **Token 块用目标体系的名字**，进入生产时能原样搬到上表的落点。已有工程先把它现有的 Token 抄进小样作底，方向只改其中的值；新项目还没定技术栈时，按 Tailwind v4 的命名空间（`--color-*`、`--font-*`、`--text-*`、`--radius-*`、`--shadow-*`、`--ease-*`、`--spacing`）起名。
- **结构跟着目标组件走**：将来是卡片组件（shadcn `Card`、`el-card`）的区块就写成它的层级（标题区、内容区、底部操作），将来是按钮变体的就写成一个按钮加修饰类。
- 每个区块的落点写进设计说明的"组件映射"：现有组件、现有组件的新变体，或必须新建的组件。

## 平移

方向锁定后按顺序做，每步对照选定的小样：

1. **Token**：搬到上表的落点。临时路由的覆盖块直接升级成全局值。
2. **字体**：字体文件复制进项目，用框架的字体方案（如 Next.js 的 `next/font/local`）或 `@font-face` 指向 `public/` 里的文件，接到字体 Token。
3. **组件**：先复用，再加变体（写法见上表），最后才新建；不复制一份组件改样式。
4. **样式翻译**：小样 CSS 改写成项目的写法（工具类、CSS Modules、`<style scoped>`）时，数值先对到 Token 刻度；对不上的值如果是方向的一部分，加成新 Token，否则取最近的刻度。一次性的数值才写死。
5. **动效与素材**：缓动曲线和弹簧参数放进 Token 或项目的动效常量；素材放进 `public/` 或项目既定的资源目录，框架的图片组件补上宽高。
6. **对照验收**：用 [截图脚本](build-and-verify.md) 在同一视口各截一张选定小样和生产页面，并排看。差异要么修掉，要么在交付里写明是有意的。
7. **清理**：删掉临时路由与 lab 文件；静态小样留在任务目录作设计记录。
````

## Path: `skills/ai-ui-design/references/motion.md`

````markdown
# 动效

## 先问值不值得

加动效前先问：**如果要手写一周，还值得做吗？** 动效代码很廉价，认知负担不廉价。每个动效承担一项明确任务：反馈、连续性或品牌表达。

## 实体手感与参数映射

手感从方向的材质和调性推出，用"动作 + 物理实体"命名并选弹簧。弹簧的性格由**阻尼比 ζ** 决定：ζ ≥ 1 不过冲，越小越弹。

| 动作 | 实体参照 | ζ / 过冲 | 刚度 / 阻尼 | 适合场景 |
| --- | --- | --- | --- | --- |
| **咔嗒 (Snap)** | 磁铁吸合、卡扣、拨动开关 | 0.8 / 约 1.5% | 500 / 36 | 按钮点按、开关切换、下拉展开 |
| **滑入 (Glide)** | 气压闭门器、抽屉阻尼 | 0.9 / 几乎为 0 | 160 / 23 | 底部浮层面板、抽屉、折叠卡片 |
| **流淌 (Flow)** | 浓缩液滴、雾气弥散 | 1.1 / 无 | 80 / 20 | 页面主视觉出现、宏观背景过渡 |
| **砸落 (Drop)** | 锤击打模、重物落桌 | 0.75 / 约 3% | 700 / 40 | 确认选择、任务完成的终结反馈 |
| **弹出 (Pop)** | 弹簧扣、气泡鼓起 | 0.55 / 约 13% | 540 / 25 | 徽章、勾选标记等小物件 |

- **换算**：质量取 1，ζ = 阻尼 ÷ (2√刚度)。刚度 / 阻尼直接用于 Motion（`stiffness` / `damping`）、react-spring（`tension` / `friction`）和 Reanimated；SwiftUI 用 `response` = 2π ÷ √刚度、`dampingFraction` = ζ。
- **纯 CSS**：没有刚度和阻尼，改用 `linear()` 采样曲线。[风格对比页模板](../assets/style-explorer.html) 的 `:root` 里有采样好的 `--snap`、`--glide`、`--pop`（对应咔嗒、滑入、弹出），以及不支持 `linear()` 时的 `cubic-bezier` 回退，直接复制使用。
- **过冲控制**：整页、大面板过冲幅度不超过 1–2%，防止整个视口晃动；徽章、勾选标记等小物件可有 10–15% 弹性。
- **材质定节奏**：重材质（金属、石材、硬件控制台）用短促坚决的咔嗒与砸落；高频操作用最短的档位。
- **待机循环（漂浮）**：弹簧会停下，做不出循环。氦气球微摆、悬浮晶体这类 Hero 待机动作用周期 4–8 秒的 ease-in-out 往复，位移不超过 8px。

## 时长与幅度规范

| 交互对象 | 推荐时长 | 设计要点 |
| --- | --- | --- |
| **按钮、开关、选中态** | 150–330ms | 按下缩放至 0.96–0.98，按下瞬间立即响应（~80ms），松开弹回 |
| **下拉菜单、气泡提示** | 180–250ms | 从触发点方向展开，缩放从 0.96 开始，不从 0 突兀放大 |
| **侧边栏、抽屉、面板** | 250–400ms | 依据位移距离定；滑入用减速，滑出用加速（时长为进入的 60–70%） |
| **视图与整页切换** | 350–500ms | 500ms 是上限，再长就成了等待 |
| **卡片悬停微动** | 150–200ms | 上浮 2–4px（上限 8px），阴影微微加深 |

## 界面过渡规范

- **连续性（共享元素）**：用户点击的项目就是下一屏的主角。从列表进入详情，被点条目平滑放大为详情容器，其他元素淡出；返回时反向收拢回原位。
- **同一对象用变形**：切换视口、筛选或展开卡片时内容是同一个对象，用外框几何变形过渡，避免交叉淡化产生的鬼影。
- **选中指示底板滑行**：分段控件（Segmented Control）、标签页与菜单项，使用同一块底板滑块滑向新目标，而不是旧项瞬间熄灭、新项突然点亮。
- **随时可打断**：连击时动画从当前位置立即响应新动作，界面始终可操作。

## 滚动叙事

- **一镜到底**：将长页滚动视为摄影机运镜推拉。主角贯穿始终（推近看微观芯片、拉远看整体机箱）。
- **停下来再展示文字**：每个关键分镜留一段静止区间，文字在停顿时出现，避免边剧烈运动边让用户阅读。
- **由进度解算**：每一帧只由当前滚动进度决定，向上滚自然倒放，保留系统原生滚动。视频随动的做法见 [素材](media.md)。

## 动效验收

- **起、中、止三帧**：[截图脚本](build-and-verify.md) 用 `--do` 触发、`--frames 3` 取帧。它把 `document.getAnimations()` 里的动画暂停在开头、中点和结尾各截一张；给了 `--do` 时只取动作新触发的那些，没给就取页面加载时的入场动画。JS 逐帧驱动的动画取不到，改用录屏。
- **10% 慢放**：在开发者工具中放慢到 10%（自动化里用 CDP 的 `Animation.setPlaybackRate`），查重影、跳动、从错误坐标闪现。
- **减少动效**：遵循 `prefers-reduced-motion: reduce`：过渡与变形瞬间到位，视差与循环浮动停止。
````

## Path: `skills/ai-ui-design/references/style-explorer.md`

````markdown
# 风格对比页

用内置 [模板](../assets/style-explorer.html) 和生成器并排展示小样，不每次重做比较工具。外壳是无色相浅灰画布加系统字体，只负责比较与挑选，不带风格倾向。每个候选在独立框架中渲染，CSS 互不影响。

## 准备输入

在任务目录放 `manifest.json` 和候选文件（必须位于 manifest 所在目录或其子目录）：

- HTML 候选是带 `head` 的完整文档，CSS 写在页内；图片、字体、视频用相对路径（如 `img/hero.webp`），生成器自动内嵌。其余 `src`、`href` 只写 `#` 锚点：站内路径、外链和远程字体都会让生成器拒绝。
- 候选类型：
  - `kind: "html"`：静态视觉样本，脚本不执行。加 `"interactive": true` 运行内联 JS，可点击试玩（自动注入内存版存储垫片）。
  - `kind: "image"`：PNG / JPEG / WebP 截图。
  - `kind: "url"`：用 `"url"` 字段（不是 `source`）指向本机 dev server，在 iframe 中运行完整应用；已有工程的临时路由小样用这种。
  - `"baseline": true`：现状版本，固定排第一并标为"现状"，至多一个。

```json
{
  "schemaVersion": 1,
  "project": "<项目名称>",
  "brief": "<所有候选共同表达的内容与主要任务>",
  "round": "01",
  "candidates": [
    {
      "id": "variant-a",
      "name": "博朗工业控制台",
      "concept": "1980年代实体仪器质感，高密度紧凑数据呈现",
      "typography": "DIN 2014 展示，JetBrains Mono 数据，Inter 正文",
      "palette": ["#1c1d1f", "#e6e8eb", "#ff5500"],
      "traits": ["1px冷白分割线", "无圆角无阴影", "实体冲压按钮"],
      "kind": "html",
      "source": "candidates/variant-a.html",
      "interactive": true
    },
    {
      "id": "variant-b",
      "name": "完整原型",
      "concept": "…", "typography": "…", "palette": ["#111"], "traits": ["…"],
      "kind": "url",
      "url": "http://localhost:5173/?variant=b"
    },
    {
      "id": "baseline",
      "name": "当前线上版本",
      "concept": "存量设计基线", "typography": "系统无衬线",
      "palette": ["#ffffff", "#2563eb"], "traits": ["卡片网格", "左右分栏"],
      "kind": "image",
      "source": "candidates/baseline.png",
      "baseline": true
    }
  ]
}
```

校验规则：`id` 为小写字母数字加 `-` `_` 且不重复；`name`、`concept`、`typography` 非空；`palette` 是十六进制色值数组；`traits` 是非空字符串数组；`url` 只接受本机地址；`interactive` 只用于 html。

## 生成

需要 Python 3.9+：

```bash
python3 <skill>/scripts/build_explorer.py <任务目录>/manifest.json --output <任务目录>/style-explorer.html
```

输出是可离线双击打开的单一 HTML。已有同名输出时生成器拒绝覆盖；更新本轮对比页加 `--force`。

## 交给用户

告诉用户这些操作：

- **并排 / 单张**：默认等大并排，在桌面（1280×900）或手机（390×844）视口比较块面。点击画面进入单张查看，侧栏显示色值、字体与特征；`←` `→` 切换，`P` 选定，`Esc` 返回。
- **实际尺寸 100%**：在单张查看里检查真实字号、中文排版与按钮边界。
- **点选标注**：开启后点击 HTML 候选中的任意元素，在原位写修改意见（自动附带标签、CSS 选择器与文本片段）；可写入全局备注并复制，或只复制这一条。本机地址和截图候选不支持点选，意见写进备注。
- **选择即复制**：点"选择"会把方案名、轮次和备注复制到剪贴板，粘贴回对话即为用户的决策。
````

## Path: `skills/ai-ui-design/references/visual-language.md`

````markdown
# 视觉语言

## 从整体到局部

先看信息焦点、构图和内容密度，再调空间、排版、色彩与细节。前一层已解决问题，就停在那一层。

每次修改说得出：哪个可见元素、哪种关系有问题、调整什么、期待改善什么。源码检查能证明样式不一致，不能单独证明画面更好。

## 焦点、空间与去容器化

- **主次鲜明**：每个任务区域有一个可辨认的主信息或主动作，辅助信息通过尺度、字重、对比或位置退后。
- **留白建构**：同类关系同类间距，组内紧、组间松。先用对齐与留白建立结构，再判断是否需要容器或分隔线。
- **去容器化**：内容直接放在画布上，用对齐、字号和留白组织。容器只在确有分组、选择、背景对比或操作边界时出现，嵌套至多 1 层（页面底为 0 层，卡片为 1 层）。
- **一条线只做一件事**：留白已经分开的地方不补线；同一处分隔用单线或单框之一。线本身是风格的一部分时保留，只删重复的。

## 字体与排版

按标题、正文、辅助信息、标签和数据建立稳定的文字角色，层级拉开足够差距；换行和空间由实际内容长度决定。字族先确认来源：项目已安装、本地有字体文件，或系统自带；每个字族写出回退到系统字体栈的完整 `font-family`。价格、计时、表格里会变化或需要上下对齐的数字用等宽数字（`font-variant-numeric: tabular-nums`）。

### 可读性是交付门槛

在真实视口、实际字体、100% 尺寸下判断：

- **正文**：阅读型页面中文正文 16–18px 起步，产品界面 14–16px，高密度专业工具可到 13–14px；行高 1.6–1.75；操作文字 14–16px。9–11px 的微型字不是"精致"。
- **标题行高**：多行中文标题先用 1.2–1.35，按真实字形检查；标题高度随内容自适应，后续内容保持正常流。展示字更紧时，看过每个视口的实际换行、确认字形不碰撞。
- **中文断行**：`text-wrap: pretty`/`balance` 只能减少孤字。数字与单位（38 秒、47 分钟）和固定词组用不换行包裹；首屏说明、页边批注按语义手动断句。行末只剩一两个字、词被拆到两行，都算缺陷。

### 示例数据要像真的

- 用不整齐的真实数字：1,238 位用户、+1.83%；时间有"刚刚""昨天 16:12""3 月 14 日"；名字有长有短，顺便验证长名字的排版。
- 按钮说出具体动作："保存草稿""周二发送"，替代"了解更多""立即开始"。
- 一页有多个演示时，共用一个具体的虚构场景：同一个产品、同一批人、同一组文件和数字，彼此呼应。

## 色彩与表面

- **语义明确**：颜色按文字、背景、动作、选中与状态使用；重要状态除颜色外还有形状或文字区别。
- **强调色有预算**：强调色的数量和面积按方向卡执行，方向卡没写时全局 1 种；功能色（成功/告警）只在对应状态出现。
- **去掉发光也成立**：去掉所有发光和模糊、再转成灰度看一遍，层级仍然分明；每个前景/背景组合用 `scripts/check_contrast.py` 计算，达到 [制作与验证](build-and-verify.md) 的门槛。
- **色温分层**：表面层级可以用色温、色相的轻微偏移区分，不只靠阴影和描边。
- **质感按调性取用**：精致端用表面高光、柔和分层阴影、细微冷暖交叉、细线分隔；粗粝端用手工和印刷痕迹，从方向的生成引擎里找。

## 控件与图标

- 复杂交互优先用平台原生控件（Web 上是 `<dialog>`、`<details>`、`<select>` 与原生表单控件）或项目组件库，它们自带键盘、读屏支持与用户直觉。
- 陌生图标配可见文字；纯图标按钮有可访问名称。`↗` 只表示打开新页面或外部链接。
- **一个产品一套图标**，统一画布尺寸与描边。描边跟字重走：细字配 1–1.5px，粗黑体配 2px 以上或实心；尺寸约为字号的 1–1.25 倍。
- **能用字符就用字符**：编辑类或极简界面优先 `→` `↗` `※` `§`、编号、缩写；图标只放在能显著加快扫描的地方。
- 自包含小样只内联用到的 SVG；字体用系统字体栈或任务目录里的字体文件，[风格对比页](style-explorer.md) 的生成器会把它们内嵌。

模型默认 Lucide / Heroicons（24px、2px、圆头）。图标是设计身份的一部分，按方向选。下表是候选起点：选定后确认该库已安装或已获同意安装，图标名从库的实际导出或文件里查到再用；查不到的图标改用字符或自绘 SVG。

| 气质 | 图标库 |
| --- | --- |
| 精致、编辑、杂志 | Phosphor Thin/Light、Iconoir |
| 工业仪器、企业数据工具 | Carbon、Material Symbols Sharp、Radix（15px 紧凑界面） |
| 消费级、友好圆润 | Phosphor Fill/Duotone、MingCute |
| 中文密集业务 | IconPark（可调描边与端点）、Remix Icon |
| 像素、游戏、极客 | Pixelarticons |
| 品牌标识 | Simple Icons |

## AI 味自查

交付前逐项排查，出现即按右列修：

| 症状 | 修法 |
| --- | --- |
| 蓝紫弥散渐变、泛滥发光、渐变文字标题 | 换成方向卡的色彩身份；发光和渐变至多留 1 处点缀 |
| 没经过选择的默认值：Inter 配 Tailwind 蓝紫（`#3b82f6`、`#6366f1`），处处大圆角加柔和阴影 | 字体、色值、圆角与阴影从方向卡或项目 Token 取 |
| 卡片套卡片 | 只留真正起分组或操作边界作用的那一层，其余层去掉边框与背景，用留白和字阶分组 |
| 三列等宽特性卡（图标 + 标题 + 两行说明） | 按内容轻重排成不等宽的版式，或用实样、截图、真实数字代替说明 |
| 每行配一个小图标、emoji 充当图标 | 只留高辨识度的通用符号，或改用字符与编号 |
| 标题上方的胶囊小标签（"✨ 全新上线"）、统计三连（"10K+ 用户 · 99.9% 可用 · 24/7 支持"） | 删掉；确有真实数字时放进正文或实样 |
| 全屏文本居中 | 长文与列表左对齐，只让短 KPI 或单句居中 |
| 过度解释、空洞文案 | 删形容词，留"动词 + 数字/名词" |
| 无任务的动效：处处淡入上浮、漂浮光斑、CSS 3D 倾斜 | 按 [动效](motion.md) 逐个问值不值得，留下承担反馈、连续性或记忆点的；真实立体感交给生成的静态或视频素材 |
| 均质化排布，处处及格无一处出彩 | 选一两处记忆点集中发力，其余退后（存量精修沿用现有记忆点，不强求新增） |
````

## Path: `skills/ai-ui-design/references/visual-review.md`

````markdown
# 视觉评审协议

写代码的 Agent 有自利偏误：会同情实现难度、为自己的选择辩护。评审交给一个**无状态 Critic**：只看渲染结果、对标真实案例、不知道及格线。

## 模式与门禁

评审前向用户确认模式，等用户回应后再派发；仅当用户明确要求直接交付时，按单轮诊断推进并列为假设：

- **严格**：Critic 打分，主 Agent 按修改清单修正后重新提审，直到 ≥9/10 或满 3 轮。
- **单轮诊断**：Critic 审 1 轮，给差距诊断与 3–5 条修改，主 Agent 修正后直接交付。

门槛与轮数只存在于主 Agent 心里；Critic 的提示词每轮逐字相同、不含任何及格线，评分才可比、不通胀。

宿主没有子 Agent 时只能单轮诊断：主 Agent 只对着截图按同一模板自评，评审记录注明"非独立评审"，不打分。

## 派发 Critic

用宿主提供的隔离子 Agent 能力（可选模型时选视觉理解最强的），每轮全新上下文，提示词用下方模板。

| 交给 Critic | 留在主 Agent |
| --- | --- |
| 用户任务、受众、交付范围、目标设备 | 制作者的论证、实现难度、投入时间 |
| 已定方向、品牌与不可改约束 | 源码、DOM 结构、技术解释 |
| 当前版本截图，注明页面、状态与逻辑视口 | 旧截图、旧评分、旧评审记录 |
| 同领域真实案例图（Moodboard），有几张给几张 | 预设问题清单、希望被赞同的答案 |
| 记忆点是动效时：3–5 秒录屏或起/中/止三帧 | 及格分数与轮数 |

Moodboard 是评审稳定的关键：只问"好不好看"评分会剧烈波动；"设想顶级工作室怎么做"有框架但无锚点；把真实案例与待审截图并排对比，主观品味才变成可比较的差距。

**Moodboard 只收真实图像**：用户提供的参考图，或本轮实际打开并截图的真实页面（[截图脚本](build-and-verify.md) 对外部 URL 同样适用；评审记录里记下 URL 与截图路径）。凭记忆描述的"某某产品的风格"不算案例。拿不到真实图像时不附 Moodboard，模板第 1 条改为只指出差距，评审记录注明"无参考锚点，评分仅供本任务内各轮比较"。

### 新设计评审模板

```text
你是国际顶级设计工作室（如 Apple / Pentagram）的设计总监。
待审截图：[路径]
同流派参考案例（Moodboard）：[路径1, 路径2, ...]
用户任务与约束：[简述]

1. 对照参考案例，设想顶级团队会如何执行这个风格，指出当前设计最大的 1–3 处差距。
2. 宏观看结构、构图张力与负空间节奏；微观看字体紧致度、对齐与边距。后台或高密度工具，看一屏能看到几个对象、主动作离当前对象多远。
3. AI 模板痕迹重扣：泛滥发光渐变、多层圆角卡片嵌套、三列等宽特性卡、通用占位图标、标题上方的胶囊小标签与统计三连、空洞居中文案、重复线框、画面上的制作说明（"示例""未接入"）。
4. 观点鲜明。若处处及格却没有一处让人记住，指出最值得集中做到极致的一两处。
5. 给 3–5 条具体、可执行的修改指令，不写散文。每条注明所指的截图与画面位置（如"首屏左上导航""第二屏定价表第三列"），只评论截图里看得见的内容。
6. 给出 1–10 分，度量与参考案例的真实差距。
```

## 复核 Critic 意见

Critic 只看到截图，也会看错或臆测。收到意见后逐条对照同一张截图：画面上确实如此的才修；找不到所指元素或与截图不符的，跳过并在交付里提一句。

## 已有界面评审

适用：在已有项目里润色了一整页或多页、做完局部重构，或用户要求评审现有界面而非重新设计。标准是这个产品自己的规范，不是评审者心中的理想风格。1 轮，不打分。

1. **定规范**：有成文规范（设计系统文档、Token 文件、组件库文档）以它为准；没有时读现有样式配置与共享组件，整理一份简短现状规范（字阶、颜色用途、圆角间距、关键组件样式）。
2. **交接**：当前截图 + 规范摘录 + 不能动的清单（品牌色、字体、全局导航）+ 用户任务。

```text
根据提供的设计规范、不能改动的清单、用户任务和当前画面，评审这个已有界面。
第一部分：逐条列出偏离规范之处（规范外的颜色/字号/间距/圆角，同类组件样式不统一，未复用共享组件）。
第二部分：在规范范围内指出最影响完成度的 3 处问题，依据视觉层级、对齐、留白、文字、状态和减法；每条建议都能用现有设计变量和组件做到。
另列可直接删掉的冗余文字与细节瑕疵。
每条注明所指的截图位置与对应的规范条目。
只给诊断与调整方向，不改代码，不打分。
```
````

