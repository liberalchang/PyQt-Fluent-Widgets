# CommandBar 方向控制和可移动停靠功能使用示例

## 概述

CommandBar 组件现在支持以下新功能:
- **方向控制**: 支持水平和竖直两种布局方向
- **竖直命令栏**: 提供独立的 VerticalCommandBar 类
- **响应式命令栏**: ResponsiveCommandBar 支持自适应布局
- **可移动停靠**: MovableCommandBar 支持拖动和停靠功能

## 1. 基础用法 - 水平方向 (默认)

```python
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from qfluentwidgets import CommandBar, FluentIcon

# 创建水平命令栏 (默认)
bar = CommandBar(parent)
bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

# 添加操作
bar.addAction(QAction(FluentIcon.ADD.icon(), "New", parent))
bar.addAction(QAction(FluentIcon.FOLDER.icon(), "Open", parent))
bar.addSeparator()
bar.addAction(QAction(FluentIcon.SAVE.icon(), "Save", parent))

# 调整到合适宽度
bar.resizeToSuitableWidth()
```

## 2. 竖直方向命令栏

### 方法 1: 使用 VerticalCommandBar 类

```python
from qfluentwidgets import VerticalCommandBar, FluentIcon

# 创建竖直命令栏
bar = VerticalCommandBar(parent)
bar.setToolButtonStyle(Qt.ToolButtonIconOnly)

# 添加操作
bar.addAction(QAction(FluentIcon.HOME.icon(), "Home", parent))
bar.addAction(QAction(FluentIcon.SEARCH.icon(), "Search", parent))
bar.addSeparator()
bar.addAction(QAction(FluentIcon.SETTING.icon(), "Settings", parent))

# 调整到合适高度
bar.resizeToSuitableHeight()
```

### 方法 2: 动态设置方向

```python
from qfluentwidgets import CommandBar

# 创建命令栏
bar = CommandBar(parent)

# 设置为竖直方向
bar.setOrientation(Qt.Vertical)
bar.resizeToSuitableHeight()

# 或切换回水平方向
bar.setOrientation(Qt.Horizontal)
bar.resizeToSuitableWidth()
```

## 3. 响应式命令栏

响应式命令栏会在空间不足时自动隐藏按钮,并将其放入"更多"菜单中:

```python
from qfluentwidgets import ResponsiveCommandBar

# 创建响应式命令栏
bar = ResponsiveCommandBar(parent)

# 添加多个操作
for i in range(10):
    bar.addAction(QAction(FluentIcon.ADD.icon(), f"Action {i}", parent))

# 添加隐藏操作(始终在"更多"菜单中)
bar.addHiddenAction(QAction(FluentIcon.SETTING.icon(), "Hidden Action", parent))

# 控制响应式模式
bar.setResponsive(True)   # 启用响应式(默认)
bar.setResponsive(False)  # 禁用响应式,显示所有按钮

# 检查响应式状态
if bar.isResponsive():
    print("Responsive mode enabled")
```

## 4. 可移动和停靠命令栏

MovableCommandBar 支持拖动并自动停靠到窗口边缘:

```python
from qfluentwidgets import MovableCommandBar, DockPosition

# 创建可移动命令栏
bar = MovableCommandBar(parent)

# 添加操作
bar.addAction(QAction(FluentIcon.EDIT.icon(), "Edit", parent))
bar.addAction(QAction(FluentIcon.DELETE.icon(), "Delete", parent))

# 设置停靠位置
bar.setDockPosition(DockPosition.TOP)     # 顶部
bar.setDockPosition(DockPosition.BOTTOM)  # 底部
bar.setDockPosition(DockPosition.LEFT)    # 左侧
bar.setDockPosition(DockPosition.RIGHT)   # 右侧

# 获取当前停靠位置
position = bar.dockPosition()

# 注意: 停靠位置会自动影响方向
# TOP/BOTTOM -> 水平方向
# LEFT/RIGHT -> 竖直方向
```

### 拖动行为

- 点击并拖动命令栏顶部的拖动手柄区域
- 拖动到窗口边缘附近(50像素内)时会自动吸附
- 释放鼠标后命令栏会固定到相应位置
- 方向会根据停靠位置自动调整

## 5. 方向和分隔符

CommandSeparator 会自动适应 CommandBar 的方向:

```python
# 水平方向: 分隔符垂直显示(高度 34px, 宽度 9px)
bar.setOrientation(Qt.Horizontal)
bar.addSeparator()

# 竖直方向: 分隔符水平显示(宽度 34px, 高度 9px)
bar.setOrientation(Qt.Vertical)
bar.addSeparator()
```

## 6. 完整示例

```python
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from qfluentwidgets import (
    CommandBar, VerticalCommandBar, ResponsiveCommandBar, MovableCommandBar,
    DockPosition, FluentIcon
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CommandBar Demo")
        
        # 中心部件
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        
        # 1. 水平命令栏
        hBar = CommandBar(self)
        hBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        hBar.addAction(QAction(FluentIcon.ADD.icon(), "New", self))
        hBar.addAction(QAction(FluentIcon.SAVE.icon(), "Save", self))
        hBar.resizeToSuitableWidth()
        layout.addWidget(hBar)
        
        # 2. 竖直命令栏
        vBar = VerticalCommandBar(self)
        vBar.addAction(QAction(FluentIcon.HOME.icon(), "Home", self))
        vBar.addAction(QAction(FluentIcon.SEARCH.icon(), "Search", self))
        vBar.resizeToSuitableHeight()
        layout.addWidget(vBar)
        
        # 3. 响应式命令栏
        rBar = ResponsiveCommandBar(self)
        for i in range(8):
            rBar.addAction(QAction(FluentIcon.ADD.icon(), f"Action {i}", self))
        layout.addWidget(rBar)
        
        # 4. 可移动命令栏
        mBar = MovableCommandBar(self)
        mBar.addAction(QAction(FluentIcon.EDIT.icon(), "Edit", self))
        mBar.setDockPosition(DockPosition.TOP)
        layout.addWidget(mBar)
```

## 7. API 参考

### CommandBar

| 方法 | 说明 |
|------|------|
| `setOrientation(orientation: Qt.Orientation)` | 设置命令栏方向 |
| `orientation() -> Qt.Orientation` | 获取命令栏方向 |
| `suitableWidth() -> int` | 计算合适的宽度 |
| `suitableHeight() -> int` | 计算合适的高度 |
| `resizeToSuitableWidth()` | 调整到合适的宽度 |
| `resizeToSuitableHeight()` | 调整到合适的高度 |

### VerticalCommandBar

继承自 CommandBar,构造时自动设置为竖直方向。

### ResponsiveCommandBar

| 方法 | 说明 |
|------|------|
| `setResponsive(enabled: bool)` | 设置响应式模式 |
| `isResponsive() -> bool` | 获取响应式模式状态 |

### MovableCommandBar

| 方法 | 说明 |
|------|------|
| `setDockPosition(position: DockPosition)` | 设置停靠位置 |
| `dockPosition() -> DockPosition` | 获取停靠位置 |
| `setResponsive(enabled: bool)` | 设置响应式模式 |
| `isResponsive() -> bool` | 获取响应式模式状态 |

### DockPosition 枚举

| 值 | 说明 |
|----|------|
| `DockPosition.TOP` | 顶部停靠 (水平方向) |
| `DockPosition.BOTTOM` | 底部停靠 (水平方向) |
| `DockPosition.LEFT` | 左侧停靠 (竖直方向) |
| `DockPosition.RIGHT` | 右侧停靠 (竖直方向) |

## 8. 注意事项

1. **方向切换**: 切换方向时会自动更新所有分隔符的方向
2. **尺寸管理**: 
   - 水平方向使用 `resizeToSuitableWidth()`
   - 竖直方向使用 `resizeToSuitableHeight()`
3. **响应式行为**: 只在响应式模式启用时生效,禁用后显示所有按钮
4. **停靠行为**: MovableCommandBar 的停靠位置会自动影响方向,无需手动设置
5. **向后兼容**: 现有 CommandBar 代码无需修改,默认保持水平方向

## 9. 测试文件

项目提供了两个测试文件来演示所有功能:

- `tests/test_command_bar_orientation.py` - 基础功能测试
- `tests/test_command_bar_advanced.py` - 高级功能演示

运行测试:
```bash
python tests/test_command_bar_orientation.py
python tests/test_command_bar_advanced.py
```
