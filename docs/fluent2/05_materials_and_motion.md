# Windows 11 Fluent Design: 材质与动效 (Materials & Motion)

**最后更新**: 2025-12-29
**参考**: 
- [Materials](https://learn.microsoft.com/zh-cn/windows/apps/design/signature-experiences/materials)
- [Motion](https://learn.microsoft.com/zh-cn/windows/apps/design/signature-experiences/motion)

## 1. 材质系统 (Materials)

材质不仅仅是装饰，它们提供了层次感和上下文。

### 1.1 Mica (云母)
*   **定义**: 一种不透明的动态材质，采样用户桌面壁纸的颜色并进行混合。
*   **用途**: 专用于 **应用窗口背景 (App Background)**。
*   **特性**: 
    *   仅在窗口激活 (Focused) 时显示效果，失焦时回退到纯色。
    *   性能开销极低。
    *   **Mica Alt**: 变体，背景色稍深，用于区分主次。

### 1.2 Acrylic (亚克力)
*   **定义**: 一种半透明材质，采样应用背后的所有像素（包括其他窗口）。
*   **用途**: **瞬态 UI 表面 (Transient UI)**。
    *   右键菜单 (Context Menu)
    *   弹出窗口 (Flyout)
    *   侧边导航栏 (Navigation Pane - 以前版本常用，Win11 倾向于 Mica)
*   **特性**: 提供模糊效果，建立强烈的层级感。

### 1.3 Smoke (烟雾)
*   **定义**: 黑色半透明遮罩。
*   **用途**: 模态对话框 (ContentDialog) 下方，用于变暗背景，聚焦用户注意力。

## 2. 动效设计 (Motion)

### 2.1 核心原则
*   **自然 (Natural)**: 模拟物理世界的惯性和摩擦。
*   **即时 (Immediate)**: 对用户操作迅速响应。
*   **引导 (Directional)**: 指示空间关系（如从右侧滑入表示进入下一级）。

### 2.2 常见过渡 (Transitions)
*   **页面过渡 (Page Transitions)**:
    *   **Drill-in**: 点击列表项进入详情页。内容“向内”移动。
    *   **Slide from Right/Bottom**: 新内容滑入。
*   **内容过渡 (Content Transitions)**:
    *   **Add/Delete**: 列表项添加/删除时的位移和淡入淡出。
    *   **Reposition**: 布局变化时元素的平滑移动。

### 2.3 连贯动画 (Connected Animation)
*   当元素在不同视图间共享时（如列表中的图片变为详情页的大图），使用连贯动画平滑过渡，维持上下文。
