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
