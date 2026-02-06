CommandBarViews 命令栏视图控件模块
===============================

CommandBarViews 模块提供命令栏的视图封装控件，专门用于弹出式显示和Flyout集成。这些视图类继承自FlyoutViewBase，为不同类型的命令栏提供统一的视图接口。

主要功能
--------

- **视图封装** - 为命令栏提供Flyout视图封装
- **委托模式** - 将所有操作委托给内部命令栏
- **默认样式** - 提供适合视图显示的默认样式
- **尺寸管理** - 自动管理视图的合适尺寸
- **弹出支持** - 完全支持Flyout弹出显示

核心组件
--------

VerticalCommandBarView
~~~~~~~~~~~~~~~~~~~~~~

垂直命令栏视图封装，提供垂直布局的命令栏视图。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar_views import VerticalCommandBarView
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建垂直命令栏视图
   vertical_view = VerticalCommandBarView(parent=parent)
   
   # 添加命令动作
   vertical_view.addAction(QAction(FIF.HOME, "首页"))
   vertical_view.addAction(QAction(FIF.SETTING, "设置"))
   vertical_view.addSeparator()
   vertical_view.addAction(QAction(FIF.HELP, "帮助"))
   
   # 调整到合适高度
   vertical_view.resizeToSuitableHeight()

**构造函数：**
- ``VerticalCommandBarView(parent: QWidget = None)``

**主要方法：**
- ``addAction(action)`` - 添加动作
- ``addActions(actions)`` - 批量添加动作
- ``addSeparator()`` - 添加分隔符
- ``insertSeparator(index: int)`` - 在指定位置插入分隔符
- ``removeAction(action)`` - 移除动作
- ``setToolButtonStyle(style)`` - 设置按钮样式
- ``setButtonTight(isTight: bool)`` - 设置紧凑模式
- ``setIconSize(size: QSize)`` - 设置图标尺寸
- ``setFont(font)`` - 设置字体
- ``setSpacing(spacing: int)`` - 设置间距
- ``suitableHeight()`` - 获取合适高度
- ``resizeToSuitableHeight()`` - 调整到合适高度
- ``actions()`` - 获取所有动作

**特点：**
- 继承自FlyoutViewBase
- 内部使用VerticalCommandBar
- 默认紧凑模式和小图标
- 垂直布局管理
- 自动高度调整

ResponsiveCommandBarView
~~~~~~~~~~~~~~~~~~~~~~~~

响应式命令栏视图封装，提供响应式布局的命令栏视图。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar_views import ResponsiveCommandBarView
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建响应式命令栏视图
   responsive_view = ResponsiveCommandBarView(parent=parent)
   
   # 添加多个命令动作
   actions = [
       QAction(FIF.NEW_DOCUMENT, "新建"),
       QAction(FIF.OPEN, "打开"),
       QAction(FIF.SAVE, "保存"),
       QAction(FIF.EDIT, "编辑"),
       QAction(FIF.COPY, "复制"),
       QAction(FIF.PASTE, "粘贴")
   ]
   
   responsive_view.addActions(actions)
   
   # 启用响应式模式
   responsive_view.setResponsive(True)
   
   # 调整到合适宽度
   responsive_view.resizeToSuitableWidth()

**构造函数：**
- ``ResponsiveCommandBarView(parent: QWidget = None)``

**主要方法：**
- ``setResponsive(enabled: bool)`` - 设置响应式模式
- ``isResponsive()`` - 获取响应式状态
- ``suitableWidth()`` - 获取合适宽度
- ``resizeToSuitableWidth()`` - 调整到合适宽度
- 以及所有基础命令栏方法

**特点：**
- 继承自FlyoutViewBase
- 内部使用ResponsiveCommandBar
- 支持响应式布局
- 水平布局管理
- 自动宽度调整

MovableCommandBarView
~~~~~~~~~~~~~~~~~~~~~

可移动命令栏视图封装，提供可拖拽停靠的命令栏视图。

.. code-block:: python

   from qfluentwidgets.components.widgets.command_bar_views import MovableCommandBarView
   from qfluentwidgets.components.widgets.command_bar import DockPosition
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建可移动命令栏视图
   movable_view = MovableCommandBarView(parent=parent)
   
   # 添加命令动作
   movable_view.addAction(QAction(FIF.FILE, "文件"))
   movable_view.addAction(QAction(FIF.EDIT, "编辑"))
   movable_view.addAction(QAction(FIF.VIEW, "视图"))
   
   # 设置停靠位置
   movable_view.setDockPosition(DockPosition.TOP)
   
   # 启用响应式模式
   movable_view.setResponsive(True)
   
   # 调整尺寸
   movable_view.resizeToSuitableWidth()
   movable_view.resizeToSuitableHeight()

**构造函数：**
- ``MovableCommandBarView(parent: QWidget = None)``

**主要方法：**
- ``setDockPosition(position)`` - 设置停靠位置
- ``dockPosition()`` - 获取停靠位置
- ``setResponsive(enabled: bool)`` - 设置响应式模式
- ``isResponsive()`` - 获取响应式状态
- ``suitableWidth()`` - 获取合适宽度
- ``suitableHeight()`` - 获取合适高度
- ``resizeToSuitableWidth()`` - 调整到合适宽度
- ``resizeToSuitableHeight()`` - 调整到合适高度
- 以及所有基础命令栏方法

**特点：**
- 继承自FlyoutViewBase
- 内部使用MovableCommandBar
- 支持拖拽停靠
- 支持响应式布局
- 双向尺寸调整

使用示例
--------

Flyout弹出命令栏示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QAction
   from qfluentwidgets.components.widgets.command_bar_views import (
       VerticalCommandBarView, ResponsiveCommandBarView, MovableCommandBarView
   )
   from qfluentwidgets.components.widgets.flyout import Flyout
   from qfluentwidgets import FluentIcon as FIF
   
   class CommandBarViewDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建按钮来触发不同的命令栏视图
           vertical_btn = QPushButton("显示垂直命令栏", self)
           vertical_btn.clicked.connect(self.show_vertical_bar)
           
           responsive_btn = QPushButton("显示响应式命令栏", self)
           responsive_btn.clicked.connect(self.show_responsive_bar)
           
           movable_btn = QPushButton("显示可移动命令栏", self)
           movable_btn.clicked.connect(self.show_movable_bar)
           
           layout.addWidget(vertical_btn)
           layout.addWidget(responsive_btn)
           layout.addWidget(movable_btn)
           
       def create_vertical_bar(self):
           """创建垂直命令栏视图"""
           view = VerticalCommandBarView()
           
           # 添加导航动作
           actions = [
               (FIF.HOME, "首页"),
               (FIF.FOLDER, "文件"),
               (FIF.SETTING, "设置"),
               (FIF.HELP, "帮助")
           ]
           
           for icon, text in actions:
               action = QAction(icon, text)
               action.triggered.connect(lambda checked, t=text: self.on_action_clicked(t))
               view.addAction(action)
           
           view.addSeparator()
           
           # 添加退出动作
           exit_action = QAction(FIF.POWER, "退出")
           exit_action.triggered.connect(self.close)
           view.addAction(exit_action)
           
           view.resizeToSuitableHeight()
           return view
           
       def create_responsive_bar(self):
           """创建响应式命令栏视图"""
           view = ResponsiveCommandBarView()
           
           # 添加文件操作动作
           file_actions = [
               (FIF.NEW_DOCUMENT, "新建"),
               (FIF.OPEN, "打开"),
               (FIF.SAVE, "保存"),
               (FIF.SAVE_AS, "另存为")
           ]
           
           for icon, text in file_actions:
               action = QAction(icon, text)
               action.triggered.connect(lambda checked, t=text: self.on_action_clicked(t))
               view.addAction(action)
           
           view.addSeparator()
           
           # 添加编辑动作
           edit_actions = [
               (FIF.CUT, "剪切"),
               (FIF.COPY, "复制"),
               (FIF.PASTE, "粘贴")
           ]
           
           for icon, text in edit_actions:
               action = QAction(icon, text)
               action.triggered.connect(lambda checked, t=text: self.on_action_clicked(t))
               view.addAction(action)
           
           view.setResponsive(True)
           view.resizeToSuitableWidth()
           return view
           
       def create_movable_bar(self):
           """创建可移动命令栏视图"""
           view = MovableCommandBarView()
           
           # 添加工具栏动作
           actions = [
               (FIF.UNDO, "撤销"),
               (FIF.REDO, "重做"),
               (FIF.SEARCH, "搜索"),
               (FIF.DOWNLOAD, "下载"),
               (FIF.UPLOAD, "上传")
           ]
           
           for icon, text in actions:
               action = QAction(icon, text)
               action.triggered.connect(lambda checked, t=text: self.on_action_clicked(t))
               view.addAction(action)
           
           view.setResponsive(True)
           view.resizeToSuitableWidth()
           view.resizeToSuitableHeight()
           return view
           
       def show_vertical_bar(self):
           """显示垂直命令栏"""
           view = self.create_vertical_bar()
           pos = self.mapToGlobal(self.rect().center())
           Flyout.make(view, pos, self, isDeleteOnClose=True)
           
       def show_responsive_bar(self):
           """显示响应式命令栏"""
           view = self.create_responsive_bar()
           pos = self.mapToGlobal(self.rect().center())
           Flyout.make(view, pos, self, isDeleteOnClose=True)
           
       def show_movable_bar(self):
           """显示可移动命令栏"""
           view = self.create_movable_bar()
           pos = self.mapToGlobal(self.rect().center())
           Flyout.make(view, pos, self, isDeleteOnClose=True)
           
       def on_action_clicked(self, action_name):
           print(f"执行动作: {action_name}")
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       demo = CommandBarViewDemo()
       demo.show()
       sys.exit(app.exec())

上下文菜单示例：

.. code-block:: python

   from PySide6.QtWidgets import QLabel
   from PySide6.QtCore import QPoint
   
   class ContextMenuWidget(QLabel):
       def __init__(self):
           super().__init__("右键点击显示上下文菜单")
           self.setMinimumSize(300, 200)
           self.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2);")
           
       def contextMenuEvent(self, event):
           """右键菜单事件"""
           # 创建垂直命令栏视图作为上下文菜单
           view = VerticalCommandBarView()
           
           # 添加上下文动作
           actions = [
               (FIF.COPY, "复制"),
               (FIF.CUT, "剪切"),
               (FIF.PASTE, "粘贴"),
               (FIF.DELETE, "删除")
           ]
           
           for icon, text in actions:
               action = QAction(icon, text)
               view.addAction(action)
           
           view.addSeparator()
           
           # 添加更多动作
           more_actions = [
               (FIF.PROPERTIES, "属性"),
               (FIF.REFRESH, "刷新")
           ]
           
           for icon, text in more_actions:
               action = QAction(icon, text)
               view.addAction(action)
           
           view.resizeToSuitableHeight()
           
           # 显示Flyout菜单
           pos = self.mapToGlobal(event.pos())
           Flyout.make(view, pos, self, isDeleteOnClose=True)

工具栏配置示例：

.. code-block:: python

   class ConfigurableToolbar(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建可配置的响应式命令栏视图
           self.toolbar_view = ResponsiveCommandBarView()
           
           # 初始化默认动作
           self.setup_default_actions()
           
           # 添加配置按钮
           config_btn = QPushButton("配置工具栏", self)
           config_btn.clicked.connect(self.show_config_dialog)
           
           layout.addWidget(self.toolbar_view)
           layout.addWidget(config_btn)
           
       def setup_default_actions(self):
           """设置默认动作"""
           default_actions = [
               (FIF.NEW_DOCUMENT, "新建"),
               (FIF.OPEN, "打开"),
               (FIF.SAVE, "保存")
           ]
           
           for icon, text in default_actions:
               action = QAction(icon, text)
               self.toolbar_view.addAction(action)
           
           self.toolbar_view.resizeToSuitableWidth()
           
       def show_config_dialog(self):
           """显示配置对话框"""
           # 创建临时命令栏视图用于配置
           config_view = ResponsiveCommandBarView()
           
           # 添加可选动作
           optional_actions = [
               (FIF.EDIT, "编辑"),
               (FIF.VIEW, "视图"),
               (FIF.TOOLS, "工具"),
               (FIF.HELP, "帮助")
           ]
           
           for icon, text in optional_actions:
               action = QAction(icon, text)
               # 模拟配置动作
               action.triggered.connect(lambda checked, t=text: self.toggle_action(t))
               config_view.addAction(action)
           
           config_view.resizeToSuitableWidth()
           
           # 显示配置Flyout
           pos = self.mapToGlobal(self.rect().center())
           Flyout.make(config_view, pos, self, isDeleteOnClose=True)
           
       def toggle_action(self, action_name):
           """切换动作显示状态"""
           print(f"切换动作: {action_name}")
           # 这里可以实现实际的添加/移除逻辑

样式自定义
----------

可以通过样式表自定义命令栏视图的外观：

.. code-block:: python

   # 自定义视图样式
   view = VerticalCommandBarView()
   view.setStyleSheet("""
       VerticalCommandBarView {
           background-color: rgba(255, 255, 255, 0.95);
           border: 1px solid rgba(0, 0, 0, 0.1);
           border-radius: 8px;
       }
       VerticalCommandBar {
           background: transparent;
       }
   """)

自定义按钮样式：

.. code-block:: python

   # 设置按钮样式和图标尺寸
   view.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
   view.setIconSize(QSize(16, 16))
   view.setButtonTight(False)  # 关闭紧凑模式

注意事项
--------

1. **视图生命周期** - Flyout视图会在关闭时自动销毁
2. **尺寸管理** - 使用resizeToSuitableWidth/Height方法确保合适尺寸
3. **委托模式** - 所有操作都委托给内部命令栏，保持API一致性
4. **响应式特性** - ResponsiveCommandBarView和MovableCommandBarView支持响应式布局
5. **默认样式** - 视图默认使用紧凑模式和小图标，适合弹出显示
6. **Flyout集成** - 专门为Flyout设计，提供最佳的弹出体验
7. **动作管理** - 确保QAction的生命周期管理正确

相关组件
--------

- :doc:`command_bar` - 命令栏控件，视图封装的基础
- :doc:`flyout` - 弹出控件，视图显示的基础
- :doc:`button` - 按钮控件
- :doc:`menu` - 菜单控件
