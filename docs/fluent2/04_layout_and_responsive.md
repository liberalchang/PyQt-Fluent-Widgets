# Windows 11 Fluent Design: 布局与响应式 (Layout & Responsive)

**最后更新**: 2025-12-29
**参考**: 
- [Layout](https://learn.microsoft.com/zh-cn/windows/apps/design/layout/)
- [Screen sizes](https://learn.microsoft.com/zh-cn/windows/apps/design/layout/screen-sizes-and-breakpoints-for-responsive-design)

## 1. 布局基础

### 1.1 间距 (Spacing)
Fluent Design 使用 **4px** 倍数的网格系统。
*   **常用间距**: 4px, 8px, 12px, 16px, 24px, 32px, 48px。
*   **Gutter (槽)**: 元素之间的间隙通常为 8px 或 12px。

### 1.2 边距 (Margins)
*   **页面边距**: 内容距离窗口边缘的距离。
    *   小窗口: 12px 或 16px
    *   大窗口: 24px 或更多
*   **一致性**: 保持左、右边距一致。

## 2. 响应式设计 (Responsive Design)

### 2.1 断点 (Breakpoints)
根据窗口宽度调整布局：
*   **Compact (小)**: 0px - 640px
    *   行为: 侧边导航折叠为汉堡菜单，单列布局。
*   **Medium (中)**: 641px - 1007px
    *   行为: 侧边导航显示图标栏 (Slim)，双列布局。
*   **Expanded (大)**: 1008px +
    *   行为: 侧边导航完全展开，多列布局，利用更多空白。

### 2.2 布局技术
*   **Reposition (重定位)**: 改变元素位置（如从横向排列变为纵向）。
*   **Resize (调整大小)**: 调整图片或容器尺寸。
*   **Reflow (重排)**: 内容自动换行。
*   **Reveal/Hide (显示/隐藏)**: 在小屏幕隐藏次要信息。

## 3. 标题栏设计 (Title Bar)
*   **自定义标题栏**: 将应用内容延伸到标题栏区域 (Extending content into the title bar)。
*   **拖拽区域 (Drag Region)**: 必须保留足够的空白区域供用户拖动窗口。通常标题栏高度为 32px 或 48px。
*   **系统按钮**: 必须保留最小化、最大化、关闭按钮的功能和位置（右上角）。

## 4. 对齐 (Alignment)
*   **视觉对齐**: 元素应基于视觉重心对齐，而非仅仅是边界框。
*   **文本对齐**: 保持文本左对齐，增强阅读流。
