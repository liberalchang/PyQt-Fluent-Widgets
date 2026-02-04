# 交互式绘图应用设计文档

## 概述
一个完整的交互式绘图应用程序，集成 `InteractiveDrawingWidget`、`VerticalToolPanel` 和顶部属性配置栏。

## 架构
- **主窗口**: `DrawingApp`
    - **顶部**: `ConfigPanel` (属性控件堆栈)
    - **中央**: `InteractiveDrawingWidget` (绘图画布)
    - **左侧**: `VerticalToolPanel` (工具栏)

## 组件

### 1. 工具栏 (`VerticalToolPanel`)
映射到 `InteractionMode` (交互模式):
- **光标** (`DEFAULT`): 平移/缩放。
- **移动** (`MOVE`): 选择/移动图元。
- **点** (`DRAW_POINT`): 绘制点。
- **线条组** (支持二级菜单):
    - 多段线 (`DRAW_LINE`) - 默认
    - 贝塞尔曲线 (`DRAW_BEZIER`)
- **形状组** (支持二级菜单):
    - 矩形 (`DRAW_RECTANGLE`) - 默认
    - 椭圆 (`DRAW_ELLIPSE`)
    - 圆形 (`DRAW_CIRCLE`)
    - 多边形 (`DRAW_POLYGON`)

### 2. 配置面板 (`ConfigPanel`)
位于顶部。根据当前选择的工具切换显示内容。

#### 通用控件
- **标签**: `CaptionLabel` (来自 `qfluentwidgets`)。
- **数值**: `DoubleSpinBox` (来自 `qfluentwidgets`)。
- **颜色**: 自定义按钮，点击弹出 `ColorDialog`。
- **选项**: `CheckBox` (来自 `qfluentwidgets`)。

#### 页面
1.  **光标/移动页**:
    - 仅显示模式图标和名称。
2.  **点页**:
    - 图标: 点。
    - **描边**: 颜色 (按钮), 宽度 (SpinBox)。
    - **大小**: 数值 (SpinBox)。
    - **填充**: 颜色 (按钮)。
3.  **线条/贝塞尔页**:
    - 图标: 线条。
    - **线条**: 颜色 (按钮), 宽度 (SpinBox)。
    - **选项**: 是否添加端点 (CheckBox)。
4.  **形状页** (矩形/圆/多边形):
    - 图标: 形状。
    - **描边**: 颜色 (按钮), 宽度 (SpinBox)。
    - **填充**: 颜色 (按钮)。
    - **选项**: 是否添加端点 (CheckBox)。

### 3. 逻辑
- **工具选择**:
    - 用户点击 `ToolPanel` 或选择二级菜单。
    - `drawingWidget` 切换到对应的交互模式。
    - `ConfigPanel` 切换到对应的配置页面。
    - 恢复上次的配置状态 (如 CheckBox 状态)。
- **属性变更**:
    - 用户在 `ConfigPanel` 修改数值或颜色。
    - `DrawingApp` 调用 `drawingWidget.setDefaultStyle(new_style)` 更新默认样式。
    - 用户勾选/取消"添加端点"。
    - `DrawingApp` 调用 `drawingWidget.setCreateHandles(bool)`。

## 数据流
`StyleData` <-> `ConfigPanel`

- **初始化**: 加载默认样式。
- **更新**: 修改配置面板时，实时更新默认样式。
