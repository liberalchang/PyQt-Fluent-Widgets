# Windows 11 Fluent Design: 几何与分层 (Geometry & Layering)

**最后更新**: 2025-12-29
**参考**: 
- [Layering](https://learn.microsoft.com/zh-cn/windows/apps/design/signature-experiences/layering)
- [Geometry](https://learn.microsoft.com/zh-cn/windows/apps/design/signature-experiences/geometry)
- [Rounded Corner](https://learn.microsoft.com/zh-cn/windows/apps/design/style/rounded-corner)

## 1. 几何形状 (Geometry)

### 1.1 圆角 (Rounded Corners)
Windows 11 全面引入圆角设计，使界面更加柔和、友好。
*   **Overlay Corner Radius (8px)**: 适用于独立悬浮的 UI 表面。
    *   应用主窗口 (Window)
    *   弹出窗口 (Flyout)
    *   对话框 (Dialog)
    *   菜单 (Menu)
*   **Control Corner Radius (4px)**: 适用于布局内部的控件元素。
    *   按钮 (Button)
    *   输入框 (TextBox)
    *   列表项 (ListViewItem) selection indicator
    *   复选框 (CheckBox)

### 1.2 嵌套规则
*   当一个 4px 圆角的控件位于 8px 圆角的容器内时，视觉上更加和谐。
*   避免直角 (0px)，除非是全屏视图或特定边缘对齐场景。

## 2. 分层与提升 (Layering & Elevation)

### 2.1 基础概念
分层通过 Z 轴深度 (Depth) 和 阴影 (Shadow) 来组织 UI。
*   **Base (基础层)**: 应用的最底层，通常是 Mica 材质背景。
*   **Content (内容层)**: 承载具体内容的区域，通常位于 Base 之上。
*   **Controls (控件层)**: 按钮、输入框等交互元素。
*   **Popups (弹出层)**: 菜单、对话框、Tooltip，位于最顶层。

### 2.2 阴影 (Shadows)
阴影用于表现“提升 (Elevation)”。
*   **Elevation 2**: 适用于轻微悬浮的元素（如卡片 hover）。
*   **Elevation 8**: 适用于菜单、Tooltip。
*   **Elevation 16**: 适用于模态对话框 (ContentDialog)。
*   **Elevation 32**: 适用于大型弹出窗口或主窗口。

### 2.3 视觉区分
*   在深色模式下，仅靠阴影难以区分层级。需配合 **边框 (Stroke)** 和 **表面颜色 (Surface Color)** 变化。
*   **高层级表面** 通常比 **低层级表面** 颜色更亮（在深色模式下）。

## 3. 应用轮廓 (App Silhouette)
*   应用窗口应具有清晰定义的边界。
*   在非最大化状态下，窗口四周应有系统阴影和圆角。
