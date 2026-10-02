# 风格对比页

用内置 [模板](../assets/style-explorer.html) 和生成器并排展示小样，不每次重做比较工具。外壳是无色相浅灰画布加系统字体，只负责比较与挑选，不带风格倾向。每个候选在独立框架中渲染，CSS 互不影响。

## 准备输入

在任务目录放 `manifest.json` 和候选文件（必须位于 manifest 所在目录或其子目录）：

- HTML 候选是带 `head` 的完整文档，CSS 写在页内；图片、字体、视频用相对路径（如 `img/hero.webp`），生成器自动内嵌。
- 候选类型：
  - `kind: "html"`：静态视觉样本，脚本不执行。加 `"interactive": true` 运行内联 JS，可点击试玩（自动注入内存版存储垫片）。
  - `kind: "image"`：PNG / JPEG / WebP 截图。
  - `kind: "url"`：用 `"url"` 字段（不是 `source`）指向本机 dev server，在 iframe 中运行完整应用。
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

需要 Python 3.10+：

```bash
python3 <skill>/scripts/build_explorer.py <任务目录>/manifest.json --output <任务目录>/style-explorer.html
```

输出是可离线双击打开的单一 HTML。已有同名输出时生成器拒绝覆盖；更新本轮对比页加 `--force`。

## 交给用户

告诉用户这些操作：

- **并排 / 单张**：默认等大并排，在桌面（1280×900）或手机（390×844）视口比较块面。点击画面进入单张查看，侧栏显示色值、字体与特征；`←` `→` 切换，`P` 选定，`Esc` 返回。
- **实际尺寸 100%**：在单张查看里检查真实字号、中文排版与按钮边界。
- **点选标注**：开启后点击候选中任意元素，在原位写修改意见（自动附带标签、CSS 选择器与文本片段）；可写入全局备注并复制，或只复制这一条。
- **选择即复制**：点"选择"会把方案名、轮次和备注复制到剪贴板，粘贴回对话即为用户的决策。
