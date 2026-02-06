CommandBar 命令栏控件模块
==========================

CommandBar 模块提供Fluent Design风格的命令栏控件，支持多种布局模式和交互方式。该模块实现了现代化的命令栏样式，提供丰富的按钮组织和管理功能。

主要功能
--------

- **多种布局** - 支持水平、垂直、响应式等多种布局模式
- **命令按钮** - 专门设计的命令按钮控件
- **分隔符** - 支持命令分组和视觉分隔
- **菜单支持** - 集成下拉菜单功能
- **拖拽停靠** - 支持可拖拽和停靠功能
- **响应式设计** - 自动适应窗口大小变化
- **工具提示** - 智能的工具提示显示

核心组件
--------

CommandBar
~~~~~~~~~~

基础命令栏控件，提供命令按钮的组织和管理功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import CommandBar
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建命令栏
   command_bar = CommandBar(parent=parent)
   
   # 添加命令按钮
   save_action = QAction(FIF.SAVE, "保存")
   save_action.triggered.connect(self.save_file)
   command_bar.addAction(save_action)
   
   # 添加分隔符
   command_bar.addSeparator()
   
   # 添加更多操作
   more_action = QAction(FIF.MORE, "更多")
   command_bar.addAction(more_action)

**构造函数：**
- ``CommandBar(parent: QWidget = None)``

**主要方法：**
- ``addAction(action: QAction)`` - 添加动作
- ``addSeparator()`` - 添加分隔符
- ``addWidget(widget: QWidget)`` - 添加自定义控件
- ``clear()`` - 清空所有内容
- ``setOrientation(orientation: Qt.Orientation)`` - 设置方向
- ``setToolButtonStyle(style: Qt.ToolButtonStyle)`` - 设置按钮样式
- ``setIconSize(size: QSize)`` - 设置图标大小

**布局管理：**
- 支持水平布局（默认）
- 支持垂直布局
- 自动调整按钮排列

CommandButton
~~~~~~~~~~~~~

命令按钮控件，专门为命令栏设计。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import CommandButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建命令按钮
   button = CommandButton(FIF.EDIT, "编辑", parent=parent)
   
   # 设置按钮样式
   button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
   
   # 设置紧凑模式
   button.setTight(True)
   
   # 连接动作
   action = QAction(FIF.EDIT, "编辑")
   button.setAction(action)

**构造函数：**
- ``CommandButton(parent: QWidget = None)``
- ``CommandButton(icon: QIcon | str | FluentIconBase, parent: QWidget = None)``

**主要方法：**
- ``setTight(isTight: bool)`` - 设置紧凑模式
- ``isTight()`` - 获取紧凑模式状态
- ``setAction(action: QAction)`` - 关联动作
- ``action()`` - 获取关联的动作
- ``setText(text: str)`` - 设置文本
- ``text()`` - 获取文本

**特点：**
- 专门为命令栏优化的尺寸
- 支持图标、文本、组合显示
- 智能工具提示
- 紧凑模式支持

MoreActionsButton
~~~~~~~~~~~~~~~~~

更多操作按钮，用于显示溢出的命令。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import MoreActionsButton
   
   # 创建更多操作按钮
   more_button = MoreActionsButton(parent=parent)
   
   # 通常由CommandBar自动管理
   # 当空间不足时自动显示

**特点：**
- 固定尺寸（40x34）
- 默认使用"更多"图标
- 自动管理状态清除

CommandSeparator
~~~~~~~~~~~~~~~~

命令分隔符控件，用于视觉上分隔命令组。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import CommandSeparator
   from PySide6.QtCore import Qt
   
   # 创建分隔符
   separator = CommandSeparator(parent=parent)
   
   # 设置方向
   separator.setOrientation(Qt.Horizontal)  # 水平
   separator.setOrientation(Qt.Vertical)    # 垂直

**构造函数：**
- ``CommandSeparator(parent: QWidget = None)``

**主要方法：**
- ``setOrientation(orientation: Qt.Orientation)`` - 设置方向
- ``orientation()`` - 获取方向

**特点：**
- 自动适应主题颜色
- 支持水平和垂直方向
- 固定尺寸（水平：9x34，垂直：34x9）

CommandMenu
~~~~~~~~~~~

命令菜单控件，继承自RoundMenu。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import CommandMenu
   
   # 创建命令菜单
   menu = CommandMenu(parent=parent)
   
   # 添加动作
   menu.addAction("选项1")
   menu.addAction("选项2")

**特点：**
- 专门为命令栏设计的菜单
- 支持动画效果
- 自动调整位置

VerticalCommandBar
~~~~~~~~~~~~~~~~~~

垂直命令栏控件，支持垂直布局。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import VerticalCommandBar
   
   # 创建垂直命令栏
   vertical_bar = VerticalCommandBar(parent=parent)
   
   # 添加命令（垂直排列）
   vertical_bar.addAction(action1)
   vertical_bar.addAction(action2)

**构造函数：**
- ``VerticalCommandBar(parent: QWidget = None)``

**特点：**
- 默认垂直布局
- 适合侧边栏使用
- 自动调整按钮尺寸

ResponsiveCommandBar
~~~~~~~~~~~~~~~~~~~~

响应式命令栏控件，自动适应窗口大小变化。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import ResponsiveCommandBar
   
   # 创建响应式命令栏
   responsive_bar = ResponsiveCommandBar(parent=parent)
   
   # 添加多个命令
   for i in range(10):
       action = QAction(f"命令{i+1}")
       responsive_bar.addAction(action)

**构造函数：**
- ``ResponsiveCommandBar(parent: QWidget = None)``

**特点：**
- 自动隐藏溢出的按钮
- 智能空间管理
- 保持重要按钮可见

MovableCommandBar
~~~~~~~~~~~~~~~~~

可移动命令栏控件，支持拖拽和停靠功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import MovableCommandBar
   from qfluentwidgets.components.widgets.command_bar import DockPosition
   
   # 创建可移动命令栏
   movable_bar = MovableCommandBar(parent=parent)
   
   # 设置停靠位置
   movable_bar.setDockPosition(DockPosition.TOP)

**构造函数：**
- ``MovableCommandBar(parent: QWidget = None)``

**主要方法：**
- ``setDockPosition(position: DockPosition)`` - 设置停靠位置
- ``dockPosition()`` - 获取停靠位置

**停靠位置：**
- ``DockPosition.TOP`` - 顶部
- ``DockPosition.BOTTOM`` - 底部
- ``DockPosition.LEFT`` - 左侧
- ``DockPosition.RIGHT`` - 右侧

CommandViewBar
~~~~~~~~~~~~~~

命令视图栏，专门为视图设计的命令栏。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import CommandViewBar
   
   # 创建命令视图栏
   view_bar = CommandViewBar(parent=parent)
   
   # 添加视图相关命令
   view_bar.addAction(zoom_in_action)
   view_bar.addAction(zoom_out_action)

**构造函数：**
- ``CommandViewBar(parent: QWidget = None)``

**特点：**
- 专门为视图操作优化
- 支持视图相关功能
- 集成菜单系统

CommandBarView
~~~~~~~~~~~~~~

命令栏视图控件，提供弹出式命令栏功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import CommandBarView
   
   # 创建命令栏视图
   bar_view = CommandBarView(parent=parent)
   
   # 添加命令
   bar_view.addAction(action1)
   bar_view.addAction(action2)

**构造函数：**
- ``CommandBarView(parent: QWidget = None)``

**特点：**
- 继承自FlyoutViewBase
- 支持弹出显示
- 适合临时命令显示

DockPosition
~~~~~~~~~~~~

停靠位置枚举，定义命令栏的停靠位置。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import DockPosition
   
   # 停靠位置常量
   DockPosition.TOP    # 顶部停靠
   DockPosition.BOTTOM # 底部停靠
   DockPosition.LEFT   # 左侧停靠
   DockPosition.RIGHT  # 右侧停靠

使用示例
--------

基础命令栏示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QAction
   from qfluentwidgets.components.widgets.command_bar import CommandBar, CommandSeparator
   from qfluentwidgets import FluentIcon as FIF
   
   class TextEditor(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建命令栏
           self.command_bar = CommandBar(self)
           
           # 创建文件操作动作
           new_action = QAction(FIF.NEW_DOCUMENT, "新建", self)
           new_action.triggered.connect(self.new_file)
           
           open_action = QAction(FIF.FOLDER, "打开", self)
           open_action.triggered.connect(self.open_file)
           
           save_action = QAction(FIF.SAVE, "保存", self)
           save_action.triggered.connect(self.save_file)
           
           # 添加到命令栏
           self.command_bar.addAction(new_action)
           self.command_bar.addAction(open_action)
           self.command_bar.addAction(save_action)
           
           # 添加分隔符
           self.command_bar.addWidget(CommandSeparator(self))
           
           # 创建编辑操作动作
           cut_action = QAction(FIF.CUT, "剪切", self)
           copy_action = QAction(FIF.COPY, "复制", self)
           paste_action = QAction(FIF.PASTE, "粘贴", self)
           
           self.command_bar.addAction(cut_action)
           self.command_bar.addAction(copy_action)
           self.command_bar.addAction(paste_action)
           
           # 创建文本编辑器
           self.text_edit = QTextEdit(self)
           
           # 添加到布局
           layout.addWidget(self.command_bar)
           layout.addWidget(self.text_edit)
           
       def new_file(self):
           self.text_edit.clear()
           
       def open_file(self):
           # 实现打开文件功能
           pass
           
       def save_file(self):
           # 实现保存文件功能
           pass
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       editor = TextEditor()
       editor.show()
       sys.exit(app.exec())

垂直命令栏示例：

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import VerticalCommandBar
   
   class SideBarWidget(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QHBoxLayout(self)
           
           # 创建垂直命令栏
           self.sidebar = VerticalCommandBar(self)
           self.sidebar.setFixedWidth(60)
           
           # 添加导航动作
           home_action = QAction(FIF.HOME, "首页")
           home_action.triggered.connect(self.go_home)
           
           settings_action = QAction(FIF.SETTING, "设置")
           settings_action.triggered.connect(self.go_settings)
           
           help_action = QAction(FIF.HELP, "帮助")
           help_action.triggered.connect(self.show_help)
           
           self.sidebar.addAction(home_action)
           self.sidebar.addWidget(CommandSeparator(self.sidebar))
           self.sidebar.addAction(settings_action)
           self.sidebar.addAction(help_action)
           
           # 主内容区域
           self.content_area = QWidget(self)
           
           layout.addWidget(self.sidebar)
           layout.addWidget(self.content_area)
           
       def go_home(self):
           # 导航到首页
           pass
           
       def go_settings(self):
           # 导航到设置
           pass
           
       def show_help(self):
           # 显示帮助
           pass

可移动命令栏示例：

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar import MovableCommandBar, DockPosition
   
   class MovableBarDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建可移动命令栏
           self.movable_bar = MovableCommandBar(self)
           
           # 添加一些动作
           actions = [
               ("文件", FIF.FOLDER),
               ("编辑", FIF.EDIT),
               ("视图", FIF.EYE),
               ("工具", FIF.SETTING)
           ]
           
           for text, icon in actions:
               action = QAction(icon, text)
               self.movable_bar.addAction(action)
           
           # 设置停靠位置
           self.movable_bar.setDockPosition(DockPosition.TOP)
           
           # 添加停靠位置切换按钮
           from qfluentwidgets.components.widgets.button import PushButton
           
           dock_buttons = QVBoxLayout()
           
           top_btn = PushButton("顶部停靠", self)
           top_btn.clicked.connect(lambda: self.set_dock_position(DockPosition.TOP))
           
           bottom_btn = PushButton("底部停靠", self)
           bottom_btn.clicked.connect(lambda: self.set_dock_position(DockPosition.BOTTOM))
           
           left_btn = PushButton("左侧停靠", self)
           left_btn.clicked.connect(lambda: self.set_dock_position(DockPosition.LEFT))
           
           right_btn = PushButton("右侧停靠", self)
           right_btn.clicked.connect(lambda: self.set_dock_position(DockPosition.RIGHT))
           
           dock_buttons.addWidget(top_btn)
           dock_buttons.addWidget(bottom_btn)
           dock_buttons.addWidget(left_btn)
           dock_buttons.addWidget(right_buttons)
           
           layout.addWidget(self.movable_bar)
           layout.addLayout(dock_buttons)
           
       def set_dock_position(self, position):
           self.movable_bar.setDockPosition(position)

样式自定义
----------

可以通过样式表自定义命令栏的外观：

.. code-block:: python

   # 自定义命令栏样式
   command_bar = CommandBar()
   command_bar.setStyleSheet("""
       CommandBar {
           background-color: rgba(255, 255, 255, 0.1);
           border: 1px solid rgba(255, 255, 255, 0.2);
           border-radius: 6px;
           padding: 4px;
       }
       CommandButton {
           background: transparent;
           border: none;
           border-radius: 4px;
           padding: 6px;
           margin: 2px;
       }
       CommandButton:hover {
           background-color: rgba(255, 255, 255, 0.1);
       }
       CommandButton:pressed {
           background-color: rgba(255, 255, 255, 0.2);
       }
       CommandSeparator {
           background-color: rgba(255, 255, 255, 0.3);
       }
   """)

自定义按钮样式：

.. code-block:: python

   # 设置按钮样式
   command_bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
   command_bar.setIconSize(QSize(16, 16))

注意事项
--------

1. **布局管理** - 不同类型的命令栏有不同的布局特性
2. **性能考虑** - 大量按钮时考虑使用响应式命令栏
3. **停靠功能** - MovableCommandBar需要合适的父容器支持停靠
4. **动作管理** - 确保QAction的生命周期管理正确
5. **图标尺寸** - 命令栏图标建议使用16x16或20x20尺寸
6. **分隔符使用** - 合理使用分隔符提高命令组织性
7. **工具提示** - CommandButton会自动为图标模式显示工具提示

相关组件
--------

- :doc:`button` - 按钮控件，CommandButton的基类
- :doc:`menu` - 菜单控件，CommandMenu的基类
- :doc:`separator` - 分隔符控件
- :doc:`flyout` - 弹出控件，CommandBarView的基类
