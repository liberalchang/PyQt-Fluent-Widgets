# Windows 11 Fluent Design: 导航与命令 (Navigation & Commanding)

**最后更新**: 2025-12-29
**参考**: 
- [Navigation basics](https://learn.microsoft.com/zh-cn/windows/apps/design/basics/navigation-basics)
- [Commanding basics](https://learn.microsoft.com/zh-cn/windows/apps/design/basics/commanding-basics)

## 1. 导航模式 (Navigation Patterns)

### 1.1 侧边导航 (NavigationView - Left)
*   **适用**: 顶级导航，页面数量较多 (5+)。
*   **结构**: 
    *   顶部: 菜单按钮 (Hamburger)、搜索、后退。
    *   中部: 导航项列表。
    *   底部: 设置、账户。
*   **显示模式**: 
    *   Minimal (仅汉堡按钮)
    *   Compact (仅图标)
    *   Expanded (图标+文字)

### 1.2 顶部导航 (NavigationView - Top)
*   **适用**: 页面数量较少，且需要最大化水平空间。
*   **行为**: 类似于标签页或菜单栏。

### 1.3 标签页 (Pivot / Tabs)
*   **适用**: 同一层级内容的快速切换。
*   **TabView**: 用于动态文档管理（如浏览器标签）。

### 1.4 面包屑 (BreadcrumbBar)
*   **适用**: 显示当前页面在层级结构中的位置，支持快速返回上级。

## 2. 命令控件 (Commanding)

### 2.1 命令栏 (CommandBar)
*   **位置**: 通常位于页面顶部或内容区域顶部。
*   **结构**:
    *   **主要命令**: 图标按钮，直接展示。
    *   **次要命令**: 放入“更多 (...)” 溢出菜单。
*   **动态性**: 根据可用宽度自动将主要命令折叠入溢出菜单。

### 2.2 上下文菜单 (Context Menu)
*   **触发**: 右键点击或长按。
*   **样式**: 8px 圆角，Acrylic 材质，阴影 Elevation 8。
*   **内容**: 仅包含与当前对象相关的操作。

### 2.3 快捷键 (Keyboard Accelerators)
*   **Tooltip**: 在 Tooltip 中显示快捷键提示（如 "Save (Ctrl+S)"）。
*   **Access Keys**: 按住 Alt 键显示按键提示。

## 3. 交互反馈
*   **Hover**: 鼠标悬停时显示浅灰色背景 (Subtle Fill)。
*   **Pressed**: 按下时显示深灰色背景并略微缩小 (Scale 0.98)。
