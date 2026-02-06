Segmented Widget 分段控件模块
==================================

Segmented Widget 模块提供分段控件功能，支持工具栏和切换按钮样式。
该模块提供现代化的分段控件界面，支持水平分段导航和切换动画。

主要功能
--------

- **分段控件** - 提供水平分段导航功能
- **工具栏样式** - 支持工具栏式的分段控件
- **切换按钮** - 支持切换按钮式的分段控件
- **动画效果** - 支持指示器的滑动动画
- **自定义样式** - 支持自定义指示器颜色和字体

核心组件
--------

SegmentedWidget
~~~~~~~~~~~~~~

分段控件，提供完整的分段导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.segmented_widget import SegmentedWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建分段控件
   segmented = SegmentedWidget()
   
   # 添加分段项
   segmented.addItem("home", "首页")
   segmented.addItem("settings", "设置")
   segmented.addItem("help", "帮助")
   
   # 设置当前项
   segmented.setCurrentItem("home")

**主要方法：**
- ``addItem()`` - 添加分段项
- ``setCurrentItem()`` - 设置当前选中项
- ``removeWidget()`` - 移除分段项
- ``clear()`` - 清空所有分段项

SegmentedItem
~~~~~~~~~~~~~

分段项，表示单个分段标签。

.. code-block:: python

   from qfluentwidgets.components.navigation.segmented_widget import SegmentedItem
   
   # 创建分段项
   segmented_item = SegmentedItem(text="首页", parent=segmented)

SegmentedToolWidget
~~~~~~~~~~~~~~~~~~~

分段工具控件，提供工具栏式的分段功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.segmented_widget import SegmentedToolWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建分段工具控件
   segmented_tool = SegmentedToolWidget()
   
   # 添加工具项
   segmented_tool.addItem("cut", FIF.CUT)
   segmented_tool.addItem("copy", FIF.COPY)
   segmented_tool.addItem("paste", FIF.PASTE)

SegmentedToggleToolWidget
~~~~~~~~~~~~~~~~~~~~~~

分段切换工具控件，提供切换按钮式的分段功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.segmented_widget import SegmentedToggleToolWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建分段切换工具控件
   segmented_toggle = SegmentedToggleToolWidget()
   
   # 添加切换项
   segmented_toggle.addItem("view", FIF.VIEW)
   segmented_toggle.addItem("edit", FIF.EDIT)

实际应用
--------

基本分段控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.segmented_widget import SegmentedWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicSegmentedWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("分段控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建分段控件
           self.segmented = SegmentedWidget()
           
           # 添加分段项
           self.add_segmented_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.segmented)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_segmented_items(self):
           """添加分段项"""
           items = [
               ("home", "首页"),
               ("explore", "探索"),
               ("favorites", "收藏"),
               ("settings", "设置")
           ]
           
           for route_key, text in items:
               self.segmented.addItem(route_key, text)
       
       def setup_connections(self):
           """设置连接"""
           self.segmented.currentItemChanged.connect(self.on_current_changed)
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           item_names = {
               "home": "首页",
               "explore": "探索",
               "favorites": "收藏",
               "settings": "设置"
           }
           
           item_name = item_names.get(route_key, "未知")
           self.current_label.setText(f"当前选择: {item_name}")

工具栏分段控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.segmented_widget import SegmentedToolWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class ToolSegmentedWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("工具栏分段控件")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建工具栏分段控件
           self.segmented_tool = SegmentedToolWidget()
           
           # 添加工具项
           self.add_tool_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 剪切")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.segmented_tool)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_tool_items(self):
           """添加工具项"""
           tools = [
               ("cut", FIF.CUT),
               ("copy", FIF.COPY),
               ("paste", FIF.PASTE),
               ("delete", FIF.DELETE),
               ("undo", FIF.UNDO),
               ("redo", FIF.REDO)
           ]
           
           for route_key, icon in tools:
               self.segmented_tool.addItem(route_key, icon)
       
       def setup_connections(self):
           """设置连接"""
           self.segmented_tool.currentItemChanged.connect(self.on_current_changed)
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           tool_names = {
               "cut": "剪切",
               "copy": "复制",
               "paste": "粘贴",
               "delete": "删除",
               "undo": "撤销",
               "redo": "重做"
           }
           
           tool_name = tool_names.get(route_key, "未知")
           self.current_label.setText(f"当前选择: {tool_name}")

高级用法
--------

切换按钮分段控件
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.segmented_widget import SegmentedToggleToolWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class ToggleSegmentedWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("切换按钮分段控件")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建切换按钮分段控件
           self.segmented_toggle = SegmentedToggleToolWidget()
           
           # 添加切换项
           self.add_toggle_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 查看")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.segmented_toggle)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_toggle_items(self):
           """添加切换项"""
           toggles = [
               ("view", FIF.VIEW),
               ("edit", FIF.EDIT),
               ("preview", FIF.PREVIEW)
           ("code", FIF.CODE)
           ("design", FIF.PALETTE)
           ]
           
           for route_key, icon in toggles:
               self.segmented_toggle.addItem(route_key, icon)
       
       def setup_connections(self):
           """设置连接"""
           self.segmented_toggle.currentItemChanged.connect(self.on_current_changed)
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           toggle_names = {
               "view": "查看",
               "edit": "编辑",
               "preview": "预览",
               "code": "代码",
               "design": "设计"
           }
           
           toggle_name = toggle_names.get(route_key, "未知")
           self.current_label.setText(f"当前选择: {toggle_name}")

动态分段控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.segmented_widget import SegmentedWidget
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class DynamicSegmentedWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态分段控件")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_btn = PushButton("添加项")
           self.insert_btn = PushButton("插入项")
           self.remove_btn = PushButton("移除项")
           self.clear_btn = PushButton("清空")
           
           button_layout.addWidget(self.add_btn)
           button_layout.addWidget(self.insert_btn)
           button_layout.addWidget(self.remove_btn)
           button_layout.addWidget(self.clear_btn)
           
           # 创建分段控件
           self.segmented = SegmentedWidget()
           
           # 添加初始项
           self.add_initial_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.segmented)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_initial_items(self):
           """添加初始项"""
           items = [
               ("home", "首页"),
               ("explore", "探索"),
               ("favorites", "收藏")
           ]
           
           for route_key, text in items:
               self.segmented.addItem(route_key, text)
       
       def setup_connections(self):
           """设置连接"""
           self.add_btn.clicked.connect(self.add_item)
           self.insert_btn.clicked.connect(self.insert_item)
           self.remove_btn.clicked.connect(self.remove_item)
           self.clear_btn.clicked.connect(self.clear_items)
           
           self.segmented.currentItemChanged.connect(self.on_current_changed)
       
       def add_item(self):
           """添加项"""
           import random
           
           additional_items = [
               ("documents", "文档"),
               ("pictures", "图片"),
               ("music", "音乐"),
               ("videos", "视频")
           ]
           
           route_key, text = random.choice(additional_items)
           self.segmented.addItem(route_key, text)
           self.current_label.setText(f"已添加: {text}")
       
       def insert_item(self):
           """插入项"""
           import random
           
           additional_items = [
               ("settings", "设置"),
               ("help", "帮助"),
               ("about", "关于")
           ]
           
           route_key, text = random.choice(additional_items)
           # 插入到第二个位置
           self.segmented.insertItem(1, route_key, text)
           self.current_label.setText(f"已插入: {text}")
       
       def remove_item(self):
           """移除当前项"""
           current_key = self.segmented.currentRouteKey()
           if current_key:
               self.segmented.removeWidget(current_key)
               self.current_label.setText(f"已移除: {current_key}")
           else:
               self.current_label.setText("没有可移除的项")
       
       def clear_items(self):
           """清空所有项"""
           self.segmented.clear()
           self.current_label.setText("已清空所有项")
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           if route_key:
               self.current_label.setText(f"当前选择: {route_key}")
           else:
               self.current_label.setText("当前选择: 无")

最佳实践
--------

1. **项管理** - 合理管理分段项的添加、删除和插入
2. **样式选择** - 根据使用场景选择合适的分段控件样式
3. **图标使用** - 为工具栏分段控件使用合适的图标
4. **动画效果** - 合理使用滑动动画提升用户体验
5. **响应式设计** - 考虑不同屏幕尺寸下的显示效果

注意事项
--------

- 分段控件会自动处理指示器的位置和动画
- 分段项数量过多时可能影响显示效果
- 工具栏分段控件适合工具操作场景
- 切换按钮分段控件适合二选一场景
- 自定义样式需要考虑主题适配
- 路由键需要唯一标识每个分段项

相关模块
--------

- :doc:`components.navigation.navigation_panel` - 导航面板
- :doc:`components.navigation.navigation_interface` - 导航接口
- :doc:`components.navigation.pivot` - 透视导航
