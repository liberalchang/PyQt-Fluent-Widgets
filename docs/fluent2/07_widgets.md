# Windows 11 Fluent Design: 小组件 (Widgets)

**最后更新**: 2025-12-29
**参考**: [Widgets design fundamentals](https://learn.microsoft.com/zh-cn/windows/apps/design/widgets/widgets-design-fundamentals)

## 1. 概述
Windows 11 小组件是显示在小组件板 (Widgets Board) 上的动态卡片。它们提供一目了然的信息（Glanceable）和轻量级交互。

## 2. 设计原则
*   **一目了然 (Glanceable)**: 用户无需点击即可获取核心信息。
*   **相关性 (Relevant)**: 个性化内容，与用户当前关注点相关。
*   **一致性 (Consistent)**: 遵循 Fluent Design 视觉规范。

## 3. 尺寸 (Sizes)
小组件必须支持标准尺寸，基于 4 列网格：
*   **Small (小)**: 1列 x 1行 (约 300x150px)。适合简单状态、单个数据点。
*   **Medium (中)**: 2列 x 1行 (约 600x150px)。适合列表、图文组合。
*   **Large (大)**: 2列 x 2行 (约 600x300px)。适合详细数据视图、新闻流。

## 4. 结构 (Anatomy)
每个小组件包含三个区域：
1.  **Header (头部)**: 
    *   图标 + 标题 (左侧)。
    *   “更多选项 (...)” (右侧)。
    *   必须保持系统一致性，不可完全自定义。
2.  **Content (内容)**: 
    *   主要信息区域。
    *   使用 8px 圆角容器。
    *   留白适中 (12px 或 16px Padding)。
3.  **Footer (底部 - 可选)**: 
    *   更新时间、来源链接或次要操作。

## 5. 交互 (Interaction)
*   **点击行为**: 
    *   点击小组件背景或标题应打开主应用，并**深度链接 (Deep Link)** 到对应内容详情页。
    *   小组件内部可包含简单交互（如刷新、点赞、切换条目），但不应承载复杂任务。
*   **状态**:
    *   加载中 (Loading): 使用骨架屏 (Skeleton loader)。
    *   空状态 (Empty): 引导用户配置。
    *   错误状态 (Error): 友好的错误提示。
