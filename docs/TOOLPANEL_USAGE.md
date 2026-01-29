# ToolPanel 使用文档

## 概述

`ToolPanel` 是一个类似 Adobe Photoshop 工具栏的工具面板组件，提供灵活的工具选择和管理功能。

## 核心特性

- ✅ **双向布局**: 支持水平和垂直两种布局方向
- ✅ **显示模式**: 支持仅图标、图标+文本（文本在上/下/旁）
- ✅ **互斥选择**: 同一工具面板内的工具选择互斥，带选中状态背景
- ✅ **二级选项**: 支持右键菜单或长按（1秒）显示子工具选项
- ✅ **响应式布局**: 空间不足时自动隐藏溢出工具到"更多"菜单
- ✅ **数据模型驱动**: 支持通过字典批量创建和管理工具
- ✅ **工具提示**: 集成 ToolTipFilter，支持显示快捷键
- ✅ **快捷键**: 支持全局快捷键配置
- ✅ **主题适配**: 完整支持浅色/深色主题，符合 Fluent2 设计规范
- ✅ **视图封装**: 提供高级视图封装类，支持自动布局和滚动
- ✅ **文本显示**: 完全支持工具按钮的文本显示和布局
- ✅ **滚动支持**: 可滚动和响应式视图，支持大量工具显示

## 快速开始

### 基础用法

```python
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from qfluentwidgets import ToolPanel, FluentIcon, FluentStyleSheet

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        
        # 创建工具面板
        self.toolPanel = ToolPanel(self)
        
        # 应用样式
        FluentStyleSheet.TOOL_PANEL.apply(self.toolPanel)
        
        # 添加到布局
        self.layout().addWidget(self.toolPanel)
        
        # 调整面板尺寸
        self.toolPanel.resizeToSuitableWidth()

if __name__ == '__main__':
    app = QApplication([])
    demo = Demo()
    demo.show()
    app.exec()
```

### 添加工具

#### 方法1: 使用数据模型批量添加

```python
# 定义工具数据
tools = [
    {
        'icon': FluentIcon.BRUSH,
        'name': 'Brush Tool',
        'tooltip': 'Brush Tool (B)',
        'checked': True,
        'shortcut': 'B',
        'subOptions': [
            {'icon': FluentIcon.BRUSH, 'name': 'Brush Tool', 'checked': True},
            {'icon': FluentIcon.PENCIL_INK, 'name': 'Pencil Tool', 'checked': False},
        ]
    },
    {
        'icon': FluentIcon.EDIT,
        'name': 'Eraser Tool',
        'tooltip': 'Eraser Tool (E)',
        'shortcut': 'E',
    },
]

# 批量添加工具
self.toolPanel.addTools(tools)
```

#### 方法2: 单独添加工具

```python
# 添加单个工具
button = self.toolPanel.addTool(
    icon=FluentIcon.BRUSH,
    name='Brush Tool',
    tooltip='Brush Tool (B)',
    shortcut='B',
    checked=True
)

# 添加分隔符
self.toolPanel.addSeparator()

# 添加另一个工具
button2 = self.toolPanel.addTool(
    icon=FluentIcon.EDIT,
    name='Eraser Tool',
    tooltip='Eraser Tool (E)',
    shortcut='E'
)
```

## 数据模型

### 工具数据结构

```python
{
    'icon': FluentIcon.BRUSH,           # 必需: 工具图标
    'name': 'Brush Tool',                # 必需: 工具名称
    'tooltip': 'Brush Tool (B)',         # 可选: 工具提示文本
    'checked': True,                     # 可选: 是否选中 (默认 False)
    'enabled': True,                     # 可选: 是否启用 (默认 True)
    'shortcut': 'B',                     # 可选: 快捷键
    'index': 0,                          # 可选: 位置索引
    'subOptions': [                      # 可选: 二级选项列表
        {
            'icon': FluentIcon.BRUSH,
            'name': 'Brush Tool',
            'checked': True
        },
        {
            'icon': FluentIcon.PENCIL_INK,
            'name': 'Pencil Tool',
            'checked': False
        }
    ],
    'userData': None                     # 可选: 用户自定义数据
}
```

## 布局方向

### 水平布局（默认）

```python
panel = ToolPanel(Qt.Horizontal, self)
# 或
panel = ToolPanel(self)  # 默认水平
```

### 垂直布局

```python
panel = ToolPanel(Qt.Vertical, self)
# 或使用便捷类
panel = VerticalToolPanel(self)
```

### 动态切换布局方向

```python
# 切换到垂直布局
panel.setOrientation(Qt.Vertical)
panel.resizeToSuitableHeight()

# 切换到水平布局
panel.setOrientation(Qt.Horizontal)
panel.resizeToSuitableWidth()
```

## 显示模式

```python
from PySide6.QtCore import Qt

# 仅显示图标 (默认)
panel.setToolButtonStyle(Qt.ToolButtonIconOnly)

# 文本在图标旁边
panel.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

# 文本在图标下方
panel.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
```

## 二级选项

### 设置二级选项

```python
button = panel.addTool(
    icon=FluentIcon.BRUSH,
    name='Brush Tool',
    subOptions=[
        {'icon': FluentIcon.BRUSH, 'name': 'Brush Tool', 'checked': True},
        {'icon': FluentIcon.PENCIL_INK, 'name': 'Pencil Tool', 'checked': False},
        {'icon': FluentIcon.PENCIL_INK, 'name': 'Color Pencil', 'checked': False},
    ]
)
```

### 触发方式

- **右键点击**: 工具按钮上右键点击弹出二级选项菜单
- **长按**: 按住鼠标左键超过1秒弹出二级选项菜单

### 获取和设置当前二级选项

```python
# 获取当前选中的二级选项
current_option = button.currentSubOption()
print(current_option['name'])  # 输出: 'Brush Tool'

# 设置当前二级选项（通过索引）
button.setCurrentSubOption(1)  # 选择第二个子选项

# 监听二级选项变化
button.subOptionChanged.connect(lambda index, option: 
    print(f"切换到: {option['name']}")
)
```

## 状态管理

### 获取当前选中的工具

```python
# 获取当前选中的工具按钮
current_tool = panel.currentTool()
if current_tool:
    data = current_tool.toolData()
    print(f"当前工具: {data['name']}")
```

### 监听工具切换

```python
# 监听工具选中事件
panel.toolClicked.connect(lambda button: 
    print(f"点击工具: {button.toolData()['name']}")
)

panel.toolChanged.connect(lambda button: 
    print(f"切换到工具: {button.toolData()['name']}")
)
```

### 导出工具数据

```python
# 获取所有工具的数据
all_tools = panel.getToolsData()

# 导出为JSON
import json
json_data = json.dumps(all_tools, indent=2)
print(json_data)
```

## 响应式布局

工具面板会根据容器尺寸自动调整显示的工具数量。当空间不足时，超出的工具会自动隐藏到"更多"菜单中。

```python
# 手动触发布局更新
panel.updateGeometry()

# 调整到合适的尺寸
panel.resizeToSuitableWidth()   # 水平布局
panel.resizeToSuitableHeight()  # 垂直布局
```

## 样式定制

### 应用内置主题

```python
from qfluentwidgets import FluentStyleSheet

# 应用 Fluent 样式
FluentStyleSheet.TOOL_PANEL.apply(panel)
```

### 自定义样式

工具面板的样式文件位于：
- 深色主题: `qfluentwidgets/_rc/qss/dark/tool_panel.qss`
- 浅色主题: `qfluentwidgets/_rc/qss/light/tool_panel.qss`

可以修改这些文件来自定义样式，或者直接使用 `setStyleSheet()`:

```python
panel.setStyleSheet("""
    ToolPanel {
        background-color: transparent;
        border: none;
    }
    
    ToolPanelButton {
        border-radius: 8px;
        padding: 8px;
    }
    
    ToolPanelButton:checked {
        background-color: rgba(0, 120, 212, 0.1);
    }
""")
```

## 工具提示

工具提示使用 `ToolTipFilter` 实现，支持显示快捷键和自定义位置。

```python
from qfluentwidgets.components.widgets.tool_tip import ToolTipPosition

# 添加工具时指定工具提示
button = panel.addTool(
    icon=FluentIcon.BRUSH,
    name='Brush Tool',
    tooltip='Brush Tool (B)\nClick to select',  # 支持多行
    shortcut='B'
)

# 工具提示会自动显示在工具按钮上方
# 延迟300ms显示，持续时间1000ms
```

## 快捷键

### 全局快捷键配置

快捷键通过 `qconfig` 全局配置管理：

```python
from qfluentwidgets import qconfig, ConfigItem

# 定义快捷键配置项
BRUSH_TOOL_SHORTCUT = ConfigItem("Shortcuts", "BrushTool", "B")
ERASER_TOOL_SHORTCUT = ConfigItem("Shortcuts", "EraserTool", "E")

# 注册配置
qconfig.set(BRUSH_TOOL_SHORTCUT, "B")
qconfig.set(ERASER_TOOL_SHORTCUT, "E")

# 在工具面板中使用
tools = [
    {
        'icon': FluentIcon.BRUSH,
        'name': 'Brush Tool',
        'tooltip': f'Brush Tool ({qconfig.get(BRUSH_TOOL_SHORTCUT)})',
        'shortcut': qconfig.get(BRUSH_TOOL_SHORTCUT),
    },
]
```

## 完整示例

```python
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from qfluentwidgets import (
    ToolPanel, VerticalToolPanel, FluentIcon, FluentStyleSheet
)

class PhotoshopStyleDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ToolPanel Demo')
        self.resize(800, 600)
        
        # 主布局
        mainLayout = QHBoxLayout(self)
        
        # 左侧垂直工具面板
        self.leftPanel = VerticalToolPanel(self)
        self.setupLeftPanel()
        mainLayout.addWidget(self.leftPanel)
        
        # 中间内容区域
        centerWidget = QWidget()
        centerLayout = QVBoxLayout(centerWidget)
        
        # 顶部水平工具面板
        self.topPanel = ToolPanel(Qt.Horizontal, centerWidget)
        self.setupTopPanel()
        centerLayout.addWidget(self.topPanel)
        
        # 添加到主布局
        mainLayout.addWidget(centerWidget, 1)
        
        # 应用样式
        FluentStyleSheet.TOOL_PANEL.apply(self.leftPanel)
        FluentStyleSheet.TOOL_PANEL.apply(self.topPanel)
        
        # 调整尺寸
        self.leftPanel.resizeToSuitableWidth()
        self.topPanel.resizeToSuitableHeight()
        
        # 连接信号
        self.connectSignals()
    
    def setupLeftPanel(self):
        """设置左侧工具面板"""
        tools = [
            {
                'icon': FluentIcon.MOVE,
                'name': 'Move Tool',
                'tooltip': 'Move Tool (V)',
                'checked': True,
                'shortcut': 'V',
            },
            {
                'icon': FluentIcon.BRUSH,
                'name': 'Brush Tool',
                'tooltip': 'Brush Tool (B)',
                'shortcut': 'B',
                'subOptions': [
                    {'icon': FluentIcon.BRUSH, 'name': 'Brush Tool', 'checked': True},
                    {'icon': FluentIcon.PENCIL_INK, 'name': 'Pencil Tool', 'checked': False},
                ]
            },
            {
                'icon': FluentIcon.EDIT,
                'name': 'Eraser Tool',
                'tooltip': 'Eraser Tool (E)',
                'shortcut': 'E',
            },
            {
                'icon': FluentIcon.PALETTE,
                'name': 'Paint Bucket',
                'tooltip': 'Paint Bucket Tool (G)',
                'shortcut': 'G',
            },
        ]
        self.leftPanel.addTools(tools)
    
    def setupTopPanel(self):
        """设置顶部工具面板"""
        tools = [
            {
                'icon': FluentIcon.SAVE,
                'name': 'Save',
                'tooltip': 'Save (Ctrl+S)',
                'shortcut': 'Ctrl+S',
            },
            {
                'icon': FluentIcon.CANCEL,
                'name': 'Undo',
                'tooltip': 'Undo (Ctrl+Z)',
                'shortcut': 'Ctrl+Z',
            },
            {
                'icon': FluentIcon.UPDATE,
                'name': 'Redo',
                'tooltip': 'Redo (Ctrl+Y)',
                'shortcut': 'Ctrl+Y',
            },
        ]
        self.topPanel.addTools(tools)
    
    def connectSignals(self):
        """连接信号"""
        self.leftPanel.toolClicked.connect(
            lambda btn: print(f"左侧面板点击: {btn.toolData()['name']}")
        )
        
        self.leftPanel.toolChanged.connect(
            lambda btn: print(f"左侧面板切换到: {btn.toolData()['name']}")
        )
        
        self.topPanel.toolClicked.connect(
            lambda btn: print(f"顶部面板点击: {btn.toolData()['name']}")
        )

if __name__ == '__main__':
    app = QApplication([])
    demo = PhotoshopStyleDemo()
    demo.show()
    app.exec()
```

## 视图封装类

### VerticalToolPanelView

竖直工具面板视图封装，提供自动布局和样式管理。

```python
from qfluentwidgets.components.widgets.tool_panel_views import VerticalToolPanelView

# 创建竖直工具面板视图
panelView = VerticalToolPanelView(parent)

# 添加工具
tools = [
    {'icon': FluentIcon.BRUSH, 'name': 'Brush Tool', 'tooltip': 'Brush Tool (B)'},
    {'icon': FluentIcon.EDIT, 'name': 'Eraser Tool', 'tooltip': 'Eraser Tool (E)'},
]
panelView.addTools(tools)

# 设置样式
panelView.setButtonTight(True)  # 紧凑模式
panelView.setIconSize(QSize(16, 16))

# 自动调整尺寸
panelView.resizeToSuitableHeight()

# 监听事件
panelView.toolClicked.connect(lambda btn: print(f"点击: {btn.toolData()['name']}"))
```

### HorizontalToolPanelView

水平工具面板视图封装，支持混合样式。

```python
from qfluentwidgets.components.widgets.tool_panel_views import HorizontalToolPanelView
from PySide6.QtCore import Qt

# 创建水平工具面板视图
panelView = HorizontalToolPanelView(parent)

# 添加图标模式工具
icon_tools = [
    {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save (Ctrl+S)'},
    {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open (Ctrl+O)'},
]
panelView.addTools(icon_tools)
panelView.addSeparator()

# 添加文本模式工具
panelView.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
text_tools = [
    {'icon': FluentIcon.CANCEL, 'name': 'Undo', 'tooltip': 'Undo (Ctrl+Z)'},
    {'icon': FluentIcon.RETURN, 'name': 'Redo', 'tooltip': 'Redo (Ctrl+Y)'},
]
panelView.addTools(text_tools)

# 自动调整尺寸
panelView.resizeToSuitableWidth()
```

### ScrollableToolPanelView

可滚动工具面板视图，支持大量工具显示。

```python
from qfluentwidgets.components.widgets.tool_panel_views import ScrollableToolPanelView
from PySide6.QtCore import Qt

# 创建可滚动竖直面板
panelView = ScrollableToolPanelView(Qt.Vertical, parent)

# 添加大量工具
tools = [{'icon': FluentIcon.SAVE, 'name': f'Tool {i+1}', 'tooltip': f'Tool {i+1}'} 
         for i in range(30)]
panelView.addTools(tools)

# 设置滚动区域尺寸
panelView.scrollArea.setFixedHeight(200)  # 限制高度，强制滚动
panelView.scrollArea.setMinimumWidth(60)    # 设置最小宽度

# 强制更新滚动尺寸
panelView.resizeToSuitableSize()
panelView.panel.resizeToSuitableHeight()
panelView.scrollArea.widget().resize(panelView.panel.sizeHint())
```

### ResponsiveToolPanelView

响应式工具面板视图，智能适应空间。

```python
from qfluentwidgets.components.widgets.tool_panel_views import ResponsiveToolPanelView
from PySide6.QtCore import Qt

# 创建响应式水平面板
panelView = ResponsiveToolPanelView(Qt.Horizontal, parent)

# 添加工具
tools = [
    {'icon': FluentIcon.SAVE, 'name': 'Save', 'tooltip': 'Save (Ctrl+S)'},
    {'icon': FluentIcon.FOLDER, 'name': 'Open', 'tooltip': 'Open (Ctrl+O)'},
    # ... 更多工具
]
panelView.addTools(tools)

# 窗口缩小时会自动启用滚动
# 也可以手动设置样式
panelView.setButtonTight(False)
panelView.setIconSize(QSize(20, 20))
```

## 视图封装的优势

### 1. 自动布局管理
- 自动设置合适的边距和布局约束
- 无需手动调整尺寸
- 支持紧凑和宽松两种模式

### 2. 统一的API接口
- 所有视图类提供相同的方法签名
- 便于在不同布局间切换
- 简化代码维护

### 3. 便捷的样式设置
```python
# 一键设置紧凑模式
panelView.setButtonTight(True)  # 间距=0, 图标=16x16

# 一键设置宽松模式
panelView.setButtonTight(False)  # 间距=4, 图标=20x20

# 自定义图标尺寸
panelView.setIconSize(QSize(24, 24))
```

### 4. 智能滚动支持
- 自动检测空间不足
- 透明背景，无黑色显示
- 支持鼠标滚轮和拖拽滚动

## API 参考

### ToolPanel

#### 构造函数
```python
ToolPanel(orientation: Qt.Orientation = Qt.Horizontal, parent: QWidget = None)
```

#### 主要方法
- `addTool(icon, name, tooltip='', checked=False, enabled=True, shortcut='', subOptions=None) -> ToolPanelButton`
- `addTools(tools: List[Dict]) -> List[ToolPanelButton]`
- `addSeparator() -> ToolPanelSeparator`
- `currentTool() -> ToolPanelButton`
- `getToolsData() -> List[Dict]`
- `setOrientation(orientation: Qt.Orientation)`
- `setToolButtonStyle(style: Qt.ToolButtonStyle)`
- `resizeToSuitableWidth()`
- `resizeToSuitableHeight()`
- `updateGeometry()`

#### 信号
- `toolClicked(button: ToolPanelButton)` - 工具被点击
- `toolChanged(button: ToolPanelButton)` - 选中工具改变

### ToolPanelButton

#### 主要方法
- `setSubOptions(options: List[Dict])`
- `currentSubOption() -> Dict`
- `setCurrentSubOption(index: int)`
- `toolData() -> Dict`
- `setToolData(data: Dict)`

#### 信号
- `subOptionChanged(index: int, option: Dict)` - 二级选项改变

### 视图封装类

#### VerticalToolPanelView
```python
VerticalToolPanelView(parent: QWidget = None)
```

**主要方法:**
- `addTool(data: Dict) -> ToolPanelButton`
- `addTools(tools: List[Dict]) -> List[ToolPanelButton]`
- `setTools(tools: List[Dict])`
- `addSeparator() -> ToolPanelSeparator`
- `setButtonTight(tight: bool)`
- `setIconSize(size: QSize)`
- `resizeToSuitableHeight()`

**属性:**
- `panel: VerticalToolPanel` - 内部的工具面板
- `toolClicked: Signal` - 工具点击信号
- `toolChanged: Signal` - 工具切换信号

#### HorizontalToolPanelView
```python
HorizontalToolPanelView(parent: QWidget = None)
```

**主要方法:**
- `addTool(data: Dict) -> ToolPanelButton`
- `addTools(tools: List[Dict]) -> List[ToolPanelButton]`
- `setTools(tools: List[Dict])`
- `addSeparator() -> ToolPanelSeparator`
- `setButtonTight(tight: bool)`
- `setIconSize(size: QSize)`
- `resizeToSuitableWidth()`

**属性:**
- `panel: ToolPanel` - 内部的工具面板
- `toolClicked: Signal` - 工具点击信号
- `toolChanged: Signal` - 工具切换信号

#### ScrollableToolPanelView
```python
ScrollableToolPanelView(orientation: Qt.Orientation = Qt.Vertical, parent: QWidget = None)
```

**主要方法:**
- `addTool(data: Dict) -> ToolPanelButton`
- `addTools(tools: List[Dict]) -> List[ToolPanelButton]`
- `setTools(tools: List[Dict])`
- `addSeparator() -> ToolPanelSeparator`
- `setButtonTight(tight: bool)`
- `setIconSize(size: QSize)`
- `resizeToSuitableSize()`
- `setOrientation(orientation: Qt.Orientation)`

**属性:**
- `panel: ToolPanel | VerticalToolPanel` - 内部的工具面板
- `scrollArea: QScrollArea` - 滚动区域
- `toolClicked: Signal` - 工具点击信号
- `toolChanged: Signal` - 工具切换信号

#### ResponsiveToolPanelView
```python
ResponsiveToolPanelView(orientation: Qt.Orientation = Qt.Vertical, parent: QWidget = None)
```

**主要方法:**
- `addTool(data: Dict) -> ToolPanelButton`
- `addTools(tools: List[Dict]) -> List[ToolPanelButton]`
- `setTools(tools: List[Dict])`
- `addSeparator() -> ToolPanelSeparator`
- `setButtonTight(tight: bool)`
- `setIconSize(size: QSize)`
- `resizeToSuitableSize()`

**属性:**
- `panel: ToolPanel | VerticalToolPanel` - 内部的工具面板
- `toolClicked: Signal` - 工具点击信号
- `toolChanged: Signal` - 工具切换信号

### VerticalToolPanel

垂直工具面板的便捷类，继承自 `ToolPanel`。

```python
VerticalToolPanel(parent: QWidget = None)
```

## 注意事项

1. **样式应用**: 记得调用 `FluentStyleSheet.TOOL_PANEL.apply(panel)` 应用样式
2. **尺寸调整**: 添加工具后调用 `resizeToSuitableWidth()` 或 `resizeToSuitableHeight()`
3. **互斥选择**: 默认情况下，同一面板内的工具选择是互斥的
4. **二级选项**: 右键或长按触发二级选项菜单，二级选项间也是互斥的
5. **响应式**: 容器尺寸变化时会自动重新布局
6. **资源文件**: QSS 样式使用 resource.py 资源系统，修改后需手动运行 rcc 转换

## 常见问题

**Q: 如何禁用工具的互斥选择？**
A: 目前工具面板设计为互斥选择，如需多选功能请使用 CommandBar 组件。

**Q: 如何自定义长按触发时间？**
A: 可以通过 `button._longPressThreshold = 2000` 设置为2秒（默认1000ms）。

**Q: 响应式布局不生效？**
A: 确保容器有固定尺寸，并且调用了 `updateGeometry()` 方法。

**Q: 工具提示不显示？**
A: 检查是否设置了 tooltip 参数，ToolTipFilter 会自动安装到按钮上。

**Q: 如何获取所有工具的状态？**
A: 使用 `panel.getToolsData()` 可以导出所有工具的完整数据。

**Q: 工具按钮文本不显示怎么办？**
A: 确保设置了正确的工具按钮样式：
```python
panel.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 文本在图标旁
panel.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 文本在图标下
panel.setToolButtonStyle(Qt.ToolButtonTextOnly)        # 仅显示文本
```

**Q: 滚动面板无法滚动怎么办？**
A: 检查以下几点：
```python
# 1. 强制更新滚动尺寸
panelView.resizeToSuitableSize()
panelView.panel.resizeToSuitableHeight()
panelView.scrollArea.widget().resize(panelView.panel.sizeHint())

# 2. 设置滚动区域尺寸
panelView.scrollArea.setFixedHeight(200)  # 限制高度强制滚动

# 3. 确保有足够的内容
if len(tools) > 10:  # 工具数量足够多时才需要滚动
    panelView.scrollArea.setFixedHeight(200)
```

**Q: 视图封装类和原始ToolPanel有什么区别？**
A: 视图封装类提供以下优势：
- 自动布局管理（边距、尺寸约束）
- 便捷的样式设置（`setButtonTight`、`setIconSize`）
- 统一的API接口
- 智能滚动支持（ScrollableToolPanelView、ResponsiveToolPanelView）
- 基于 FlyoutViewBase 的额外功能

**Q: 如何在视图封装中设置滚动条策略？**
A: 可以直接访问内部的滚动区域：
```python
# 设置滚动条策略
panelView.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
panelView.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

# 设置背景透明
panelView.scrollArea.setStyleSheet("QScrollArea { background: transparent; }")
panelView.scrollArea.viewport().setStyleSheet("background: transparent;")
```

**Q: 响应式面板什么时候启用滚动？**
A: 当可用空间小于面板所需尺寸时自动启用：
```python
# 手动检查是否启用了滚动
if hasattr(panelView, '_scrollArea'):
    print("已启用滚动模式")
else:
    print("普通模式")
```
