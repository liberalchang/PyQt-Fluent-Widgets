# 抽屉窗口组件 (DrawerWindow) 使用文档

## 简介

`DrawerWindow` 是一个通用的带抽屉功能的窗口组件，位于 `qfluentwidgets.window` 模块下。它支持从窗口的四个方向（左、右、顶、底）滑出抽屉，并带有平滑的动画效果和背景遮罩。该组件设计用于方便地集成到现有的 `FluentWindow` 或作为独立的窗口容器使用。

### 主要特性

*   **多方向支持**：支持左、右、顶、底四个方向的抽屉。
*   **平滑动画**：抽屉显示和隐藏时带有缓动动画（OutQuart/InQuart）。
*   **自动遮罩**：抽屉打开时自动显示半透明遮罩，点击遮罩可关闭抽屉。
*   **主题适配**：自动适配深色和浅色主题。
*   **灵活扩展**：通过 `content_layout` 轻松向抽屉添加自定义内容。

---

## 架构设计

`DrawerWindow` 继承自 `QWidget`，其内部结构包含：

1.  **中心区域 (Central Widget)**：用于放置主界面内容。
2.  **四个抽屉实例 (Drawer)**：预先初始化了 `left_drawer`, `right_drawer`, `top_drawer`, `bottom_drawer`，默认隐藏。
3.  **遮罩层 (Mask)**：全屏覆盖的半透明层，用于阻挡对主界面的操作并提供点击关闭功能。

抽屉 (`Drawer`) 继承自 `QFrame`，内部包含标题栏（可选）和内容区域。

---

## 接口说明 (API Reference)

### DrawerWindow 类

`qfluentwidgets.window.DrawerWindow`

#### 方法

*   **`__init__(parent=None)`**
    *   初始化抽屉窗口。

*   **`set_central_widget(widget: QWidget)`**
    *   设置窗口的中心内容组件。
    *   **参数**:
        *   `widget`: 要显示的中心组件。

*   **`show_drawer(direction: str, size: int = 300, title: str = None)`**
    *   显示指定方向的抽屉。
    *   **参数**:
        *   `direction`: 抽屉方向，可选值 `'left'`, `'right'`, `'top'`, `'bottom'`。
        *   `size`: 抽屉尺寸（像素）。对于左右抽屉为宽度，对于顶底抽屉为高度。
        *   `title`: (可选) 抽屉标题栏显示的文字。

*   **`hide_all_drawers()`**
    *   关闭当前所有打开的抽屉。

#### 属性

*   **`left_drawer`**: 左侧抽屉实例 (`Drawer`)。
*   **`right_drawer`**: 右侧抽屉实例 (`Drawer`)。
*   **`top_drawer`**: 顶部抽屉实例 (`Drawer`)。
*   **`bottom_drawer`**: 底部抽屉实例 (`Drawer`)。

### Drawer 类

`qfluentwidgets.window.drawer_window.Drawer`

通常不需要直接实例化该类，而是通过 `DrawerWindow` 的属性访问。

#### 属性与方法

*   **`content_layout`**: `QVBoxLayout` 类型。用于向抽屉添加内容的布局管理器。
*   **`set_title(title: str)`**: 设置抽屉标题。
*   **`hide_drawer()`**: 隐藏该抽屉。

---

## 使用示例

### 1. 基础用法

作为一个独立的窗口使用，或者作为 `FluentWindow` 的子界面。

```python
from PySide6.QtWidgets import QLabel, QPushButton
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets.window import DrawerWindow

class MyInterface(DrawerWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 1. 设置主界面内容
        self.main_content = QLabel("这是主界面内容", self)
        self.main_content.setAlignment(Qt.AlignCenter)
        self.set_central_widget(self.main_content)
        
        # 2. 向右侧抽屉添加内容
        self.right_drawer.set_title("功能面板")
        self.right_drawer.content_layout.addWidget(QLabel("这里是抽屉内容"))
        self.right_drawer.content_layout.addWidget(PrimaryPushButton("执行操作"))
        self.right_drawer.content_layout.addStretch(1) # 底部填充
        
        # 3. 添加按钮触发抽屉
        self.btn = QPushButton("打开右侧抽屉", self.main_content)
        self.btn.clicked.connect(lambda: self.show_drawer('right', 300, "功能面板"))

# 在 FluentWindow 中使用
# window.addSubInterface(MyInterface(window), 'my_interface', '我的界面')
```

### 2. 继承扩展

可以继承 `DrawerWindow` 来封装复杂的业务逻辑。

```python
class SearchFilteringInterface(DrawerWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_main_ui()
        self._init_drawer_ui()
        
    def _init_main_ui(self):
        # 初始化主列表等
        pass
        
    def _init_drawer_ui(self):
        # 初始化筛选器抽屉
        self.filter_drawer = self.right_drawer
        self.filter_drawer.content_layout.addWidget(QLabel("筛选条件"))
        # ... 添加更多控件
        
    def open_filters(self):
        self.show_drawer('right', 350, "高级筛选")
```

---

## 注意事项

1.  **布局管理**：向抽屉添加内容时，请直接使用 `drawer.content_layout.addWidget()`。避免直接设置 drawer 的 layout，否则可能会破坏内部结构。
2.  **层级关系**：`DrawerWindow` 会自动处理层级关系，确保抽屉和遮罩始终位于中心内容之上。
3.  **事件处理**：组件内部使用了 `eventFilter` 来处理遮罩的点击事件。如果你重写了 `eventFilter`，请确保调用 `super().eventFilter(obj, event)`。
