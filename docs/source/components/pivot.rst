Pivot 透视导航模块
========================

Pivot 模块提供透视导航功能，支持标签页式导航和滑动动画。
该模块提供现代化的透视导航界面，支持水平标签导航和指示器动画。

主要功能
--------

- **透视导航** - 提供标签页式导航功能
- **滑动动画** - 支持指示器的平滑滑动动画
- **动态管理** - 支持动态添加、删除和插入导航项
- **自定义样式** - 支持自定义指示器颜色和字体大小
- **路由支持** - 集成路由系统进行页面导航

核心组件
--------

Pivot
~~~~~~

透视导航控件，提供完整的导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.pivot import Pivot
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建透视导航
   pivot = Pivot()
   
   # 添加导航项
   pivot.addItem("home", "首页")
   pivot.addItem("settings", "设置")
   pivot.addItem("help", "帮助")
   
   # 设置当前项
   pivot.setCurrentItem("home")

**主要信号：**
- ``currentItemChanged`` - 当前项变化信号

**主要方法：**
- ``addItem()`` - 添加导航项
- ``setCurrentItem()`` - 设置当前选中项
- ``removeWidget()`` - 移除导航项
- ``clear()`` - 清空所有导航项

PivotItem
~~~~~~~~~~~~

透视导航项，表示单个导航标签。

.. code-block:: python

   from qfluentwidgets.components.navigation.pivot import PivotItem
   
   # 创建透视导航项
   pivot_item = PivotItem(text="首页", parent=pivot)

实际应用
--------

基本透视导航
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.pivot import Pivot
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicPivotWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("透视导航示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建透视导航
           self.pivot = Pivot()
           
           # 添加导航项
           self.add_pivot_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.pivot)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_pivot_items(self):
           """添加透视导航项"""
           items = [
               ("home", "首页"),
               ("explore", "探索"),
               ("favorites", "收藏"),
               ("settings", "设置")
           ]
           
           for route_key, text in items:
               self.pivot.addItem(route_key, text)
       
       def setup_connections(self):
           """设置连接"""
           self.pivot.currentItemChanged.connect(self.on_current_changed)
       
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

带图标的透视导航
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.pivot import Pivot
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class IconPivotWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("带图标的透视导航")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建透视导航
           self.pivot = Pivot()
           
           # 添加带图标的导航项
           self.add_icon_pivot_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.pivot)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_icon_pivot_items(self):
           """添加带图标的透视导航项"""
           items = [
               ("home", "🏠 首页", FIF.HOME),
               ("explore", "🔍 探索", FIF.SEARCH),
               ("favorites", "❤️ 收藏", FIF.HEART),
               ("settings", "⚙️ 设置", FIF.SETTING)
           ]
           
           for route_key, text, icon in items:
               self.pivot.addItem(route_key, text, icon=icon.name())
       
       def setup_connections(self):
           """设置连接"""
           self.pivot.currentItemChanged.connect(self.on_current_changed)
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           item_names = {
               "home": "🏠 首页",
               "explore": "🔍 探索",
               "favorites": "❤️ 收藏",
               "settings": "⚙️ 设置"
           }
           
           item_name = item_names.get(route_key, "未知")
           self.current_label.setText(f"当前选择: {item_name}")

高级用法
--------

动态透视导航
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.pivot import Pivot
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class DynamicPivotWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态透视导航")
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
           
           # 创建透视导航
           self.pivot = Pivot()
           
           # 添加初始项
           self.add_initial_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.pivot)
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
               self.pivot.addItem(route_key, text)
       
       def setup_connections(self):
           """设置连接"""
           self.add_btn.clicked.connect(self.add_item)
           self.insert_btn.clicked.connect(self.insert_item)
           self.remove_btn.clicked.connect(self.remove_item)
           self.clear_btn.clicked.connect(self.clear_items)
           
           self.pivot.currentItemChanged.connect(self.on_current_changed)
       
       def add_item(self):
           """添加项"""
           import random
           
           additional_items = [
               ("documents", "文档"),
               ("pictures", "图片"),
               ("music", "音乐"),
               ("videos", "视频"),
               ("downloads", "下载")
           ]
           
           route_key, text = random.choice(additional_items)
           self.pivot.addItem(route_key, text)
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
           self.pivot.insertItem(1, route_key, text)
           self.current_label.setText(f"已插入: {text}")
       
       def remove_item(self):
           """移除当前项"""
           current_key = self.pivot.currentRouteKey()
           if current_key:
               self.pivot.removeWidget(current_key)
               self.current_label.setText(f"已移除: {current_key}")
           else:
               self.current_label.setText("没有可移除的项")
       
       def clear_items(self):
           """清空所有项"""
           self.pivot.clear()
           self.current_label.setText("已清空所有项")
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           if route_key:
               self.current_label.setText(f"当前选择: {route_key}")
           else:
               self.current_label.setText("当前选择: 无")

自定义样式透视导航
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.pivot import Pivot
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class CustomStylePivotWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义样式透视导航")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建透视导航
           self.pivot = Pivot()
           
           # 设置自定义样式
           self.setup_custom_style()
           
           # 添加导航项
           self.add_custom_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.pivot)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_custom_style(self):
           """设置自定义样式"""
           # 设置自定义指示器颜色
           self.pivot.setIndicatorColor(QColor(255, 100, 100), QColor(100, 255, 100))
           
           # 设置自定义字体大小
           self.pivot.setItemFontSize(16)
           
           # 设置自定义指示器长度
           self.pivot.setIndicatorLength(20)
       
       def add_custom_items(self):
           """添加自定义项"""
           items = [
               ("dashboard", "📊 仪表板"),
               ("analytics", "📈 数据分析"),
               ("reports", "📄 报告"),
               ("team", "👥 团队")
           ]
           
           for route_key, text in items:
               self.pivot.addItem(route_key, text)
       
       def setup_connections(self):
           """设置连接"""
           self.pivot.currentItemChanged.connect(self.on_current_changed)
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           if route_key:
               self.current_label.setText(f"当前选择: {route_key}")
           else:
               self.current_label.setText("当前选择: 无")

最佳实践
--------

1. **项管理** - 合理管理导航项的添加、删除和插入
2. **样式统一** - 保持透视导航的视觉风格一致性
3. **动画效果** - 合理使用滑动动画提升用户体验
4. **路由集成** - 正确集成路由系统实现页面导航
5. **响应式设计** - 考虑不同屏幕尺寸下的显示效果

注意事项
--------

- 透视导航会自动处理指示器的位置和动画
- 导航项数量过多时可能影响显示效果
- 自定义样式需要考虑主题适配
- 路由键需要唯一标识每个导航项
- 动画效果可能影响性能，需要合理使用

相关模块
--------

- :doc:`components.navigation.navigation_panel` - 导航面板
- :doc:`components.navigation.navigation_interface` - 导航接口
- :doc:`components.navigation.navigation_bar` - 导航栏
