# 颜色组件文档

本文档提供了 `qfluentwidgets` 中颜色相关组件的架构、API 参考和使用指南。

## 目录
1. [CircleColorPicker (圆形颜色选择器)](#circlecolorpicker)
2. [ColorPalette (颜色面板)](#colorpalette)
3. [ColorPickerButton (颜色选择按钮)](#colorpickerbutton)
4. [ColorDialog (颜色对话框)](#colordialog)
5. [ScreenColorPicker (屏幕取色器)](#screencolorpicker)

---

## CircleColorPicker
**文件:** `qfluentwidgets/components/dialog_box/circle_color_picker.py`

### 架构
`CircleColorPicker` 管理一组圆形颜色按钮 (`CircleColorItem`)。它使用 `QButtonGroup` 确保单一选择（单选按钮行为），并提供一个“添加”按钮来追加新颜色。每个颜色项都支持通过右键菜单进行删除。

### API 参考

#### 类 `CircleColorPicker`
继承自 `QWidget`。

**信号 (Signals)**
- `colorChanged(QColor)`: 当用户选择一种颜色时发出。
- `colorAdded(QColor)`: 当添加新颜色到列表时发出。
- `colorRemoved(QColor)`: 当通过上下文菜单移除颜色时发出。
- `colorsChanged(list)`: 当内部颜色列表发生变化（添加或移除）时发出。
- `addColorClicked()`: 当点击“添加”按钮时发出。

**方法 (Methods)**
- `__init__(colors: List[Union[QColor, str]] = None, parent=None)`
  - 初始化选择器，可选择传入初始颜色列表。
- `setColors(colors: List[Union[QColor, str]])`
  - 用新列表替换当前的颜色列表。
- `addColor(color: QColor, updateLayout=True)`
  - 向选择器添加新颜色。使用 `updateLayout=False` 进行批量添加以提高性能。
- `removeColor(color: QColor)`
  - 从选择器中移除指定颜色。
- `setColor(color: QColor)`
  - 如果列表中存在该颜色，则通过编程方式选中它。
- `color() -> QColor`
  - 返回当前选中的颜色。如果没有选中，则返回无效的 `QColor`。

### 使用示例
```python
from PySide6.QtCore import Qt
from qfluentwidgets import CircleColorPicker

picker = CircleColorPicker(parent=self)
picker.setColors(["#FF0000", "#00FF00", "#0000FF"])

# 处理选择
picker.colorChanged.connect(lambda c: print(f"已选择: {c.name()}"))

# 添加自定义颜色
picker.addColor(Qt.cyan)
```

---

## ColorPalette
**文件:** `qfluentwidgets/components/dialog_box/color_palette.py`

### 架构
该模块提供了下拉颜色选择面板的实现。
- **`ColorPalette`**: 一个综合性的弹出窗口小部件，包含：
  - 屏幕取色器 (Screen Color Picker)
  - 主题颜色 (网格布局)
  - 标准颜色 (列表布局)
  - 最近/自定义颜色 (集成了 `CircleColorPicker`)
  - “更多颜色”按钮 (打开 `ColorDialog`)

### API 参考

#### 类 `ColorPalette`
继承自 `FlyoutViewBase`。

**信号 (Signals)**
- `colorSelected(QColor)`: 当选取颜色时发出。
- `customColorsChanged(list)`: 当自定义颜色列表发生变化时发出。

**方法 (Methods)**
- `__init__(customColors=None, parent=None)`
  - 初始化面板。`customColors` 是填充“最近使用的颜色”部分的颜色列表。

---

## ColorPickerButton
**文件:** `qfluentwidgets/components/dialog_box/color_picker_button.py`

### 架构
该模块提供了一组下拉按钮，用于以不同形式展示颜色选择功能。所有按钮都继承自 `ColorButton`。
- **`ColorButton`**: 通用按钮，默认集成 `ColorPalette`（下拉面板）。
- **`ColorDialogButton`**: 点击下拉箭头直接弹出 `ColorDialog` 嵌入式界面。
- **`CircleColorButton`**: 点击下拉箭头直接弹出 `CircleColorPicker` 嵌入式界面。
- **`ScreenColorButton`**: 点击下拉箭头直接激活屏幕取色覆盖层 (`ScreenColorPickerOverlay`)。

### API 参考

#### 类 `ColorButton`
继承自 `QPushButton`。

**信号 (Signals)**
- `colorChanged(QColor)`: 当通过面板或对话框更改颜色时发出。

**方法 (Methods)**
- `__init__(color, title: str, parent=None, icon=None, showPreview=True)`
  - `color`: 初始颜色。
  - `title`: 按钮文本。
  - `icon`: 可选图标（字符串路径、QIcon 或 FluentIcon）。
  - `showPreview`: 如果为 True，在文本旁边显示方形颜色预览。
- `color() -> QColor`
  - 返回当前颜色。
- `setColor(color)`
  - 设置当前颜色并更新 UI。
- `setIcon(icon)`
  - 更新按钮图标。

#### 类 `ColorDialogButton`
继承自 `ColorButton`。
点击下拉箭头时，会在 Flyout 中显示 `ColorDialog` 的精简版（无标题栏）。

#### 类 `CircleColorButton`
继承自 `ColorButton`。
点击下拉箭头时，会在 Flyout 中显示 `CircleColorPicker`。

#### 类 `ScreenColorButton`
继承自 `ColorButton`。
点击下拉箭头时，直接激活全屏取色覆盖层。

### 使用示例
```python
from qfluentwidgets import ColorButton, ColorDialogButton, CircleColorButton, ScreenColorButton, FluentIcon as FIF

# 1. 标准下拉颜色面板
btn1 = ColorButton(Qt.red, "标准颜色面板", icon=FIF.PALETTE)

# 2. 下拉颜色对话框
btn2 = ColorDialogButton(Qt.blue, "颜色对话框", icon=FIF.Edit)

# 3. 下拉圆形颜色选择器
btn3 = CircleColorButton(Qt.green, "圆形选择器", icon=FIF.BRUSH)

# 4. 下拉屏幕取色器
btn4 = ScreenColorButton(Qt.white, "屏幕取色", icon=FIF.EYE_SHOW)

# 连接信号
for btn in [btn1, btn2, btn3, btn4]:
    btn.colorChanged.connect(lambda c: print(f"选中的颜色: {c.name()}"))
    layout.addWidget(btn)
```

---

## ColorDialog
**文件:** `qfluentwidgets/components/dialog_box/color_dialog.py`

### 架构
`ColorDialog` 是继承自 `MaskDialogBase` 的模态对话框。它提供了用于精确颜色选择的完整界面：
- **`HuePanel`**: 基于色相背景的饱和度和明度 2D 选择面板。
- **`BrightnessSlider`**: 调整亮度 (Value) 的滑块。
- **`ColorLineEdit`**: 红、绿、蓝、Alpha (不透明度) 和十六进制代码的数值输入框。
- **`ColorCard`**: 原始颜色与新颜色的视觉对比。

### API 参考

#### 类 `ColorDialog`
继承自 `MaskDialogBase`。

**信号 (Signals)**
- `colorChanged(QColor)`: 当用户点击“确定”且颜色发生变化时发出。

**方法 (Methods)**
- `__init__(color, title: str, parent=None, enableAlpha=False)`
  - `color`: 初始颜色。
  - `title`: 对话框标题。
  - `enableAlpha`: 如果为 True，显示不透明度控件并允许 Alpha 通道选择。
- `setColor(color, movePicker=True)`
  - 更新显示的颜色。如果 `movePicker` 为 True，则更新 HuePanel 上的选择器位置。

### 使用示例
```python
from qfluentwidgets import ColorDialog

dialog = ColorDialog(Qt.blue, "选择颜色", parent=self, enableAlpha=True)
if dialog.exec():
    new_color = dialog.color
    print(f"用户选择了: {new_color.name()}")
```

---

## ScreenColorPicker
**文件:** `qfluentwidgets/components/dialog_box/screen_color_picker.py`

### 架构
`ScreenColorPicker` 允许从屏幕上的任何像素选取颜色。
- **`ScreenColorPickerOverlay`**: 一个透明、全屏、置顶的小部件。它捕获屏幕内容，在光标周围渲染放大镜（缩放网格），并处理鼠标点击以选择像素。
- **`ScreenColorPicker`**: 包含预览标签、十六进制值输入框和工具按钮的小部件。点击按钮可激活覆盖层。

### API 参考

#### 类 `ScreenColorPicker`
继承自 `QWidget`。

**信号 (Signals)**
- `colorChanged(QColor)`: 当选取屏幕颜色时发出。

**方法 (Methods)**
- `__init__(color=Qt.white, parent=None)`
  - 初始化选择器，默认颜色为白色。
- `startPicking()`
  - 创建并显示 `ScreenColorPickerOverlay` 以开始取色过程。
- `setColor(color)`
  - 手动设置当前颜色并更新预览。

#### 类 `ScreenColorPickerOverlay`
继承自 `QWidget`。

**主要特性**:
- **实时捕获**: 使用定时器实时抓取光标下的屏幕内容。
- **放大镜**: 在光标周围显示放大的像素网格。
- **滚动缩放**: 鼠标滚轮调整网格大小（缩放级别）。
- **多屏幕支持**: 使用 `mapFromGlobal` 正确处理跨多个显示器的坐标。

### 使用示例
```python
from qfluentwidgets import ScreenColorPicker

picker = ScreenColorPicker(parent=self)
picker.colorChanged.connect(lambda c: print(f"屏幕颜色: {c.name()}"))

# 编程方式开始取色
# picker.startPicking()
```
