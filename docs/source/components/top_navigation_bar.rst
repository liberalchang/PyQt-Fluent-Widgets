Top Navigation Bar 顶部导航栏模块
====================================

Top Navigation Bar 模块提供顶部导航栏功能，支持水平布局和响应式设计。
该模块提供现代化的顶部导航栏界面，支持滚动区域和指示器动画。

主要功能
--------

- **顶部导航** - 提供水平方向的导航功能
- **响应式设计** - 支持根据窗口宽度自动调整显示模式
- **滚动区域** - 支持大量导航项的滚动显示
- **指示器动画** - 支持选中项的滑动指示器动画
- **返回按钮** - 支持可选的返回按钮功能

核心组件
--------

TopNavigationBar
~~~~~~~~~~~~~~

顶部导航栏，提供完整的导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.top_navigation_bar import TopNavigationBar
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建顶部导航栏
   top_nav = TopNavigationBar(showReturnButton=True)
   
   # 添加导航项
   top_nav.addItem("home", FIF.HOME, "首页")
   top_nav.addItem("explore", FIF.SEARCH, "探索")
   top_nav.addItem("settings", FIF.SETTING, "设置")
   
   # 设置当前项
   top_nav.setCurrentItem("home")

**主要方法：**
- ``addItem()`` - 添加导航项
- ``setCurrentItem()`` - 设置当前选中项
- ``removeWidget()`` - 移除导航项
- ``setTextVisible()`` - 设置文本可见性
- ``setResponsiveWidth()`` - 设置响应式宽度阈值

TopNavigationBarPushButton
~~~~~~~~~~~~~~~~~~~~~~~~

顶部导航栏按钮，提供按钮式导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.top_navigation_bar import TopNavigationBarPushButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建顶部导航栏按钮
   nav_button = TopNavigationBarPushButton(
       icon=FIF.HOME,
       text="首页",
       isSelectable=True
   )

实际应用
--------

基本顶部导航栏
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.top_navigation_bar import TopNavigationBar
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicTopNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("顶部导航栏示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建顶部导航栏
           self.top_nav = TopNavigationBar(showReturnButton=True)
           
           # 添加导航项
           self.add_navigation_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.top_nav)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_navigation_items(self):
           """添加导航项"""
           items = [
               ("home", "首页"),
               ("explore", "探索"),
               ("favorites", "收藏"),
               ("settings", "设置")
           ]
           
           icons = [FIF.HOME, FIF.SEARCH, FIF.HEART, FIF.SETTING]
           
           for (route_key, text), icon in zip(items, icons):
               self.top_nav.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           self.top_nav.currentItemChanged.connect(self.on_current_changed)
       
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

响应式顶部导航栏
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.top_navigation_bar import TopNavigationBar
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class ResponsiveTopNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("响应式顶部导航栏")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.show_text_btn = PushButton("显示文本")
           self.hide_text_btn = PushButton("隐藏文本")
           self.set_responsive_btn = PushButton("设置响应式")
           
           button_layout.addWidget(self.show_text_btn)
           button_layout.addWidget(self.hide_text_btn)
           button_layout.addWidget(self.set_responsive_btn)
           
           # 创建顶部导航栏
           self.top_nav = TopNavigationBar(showReturnButton=True)
           
           # 设置响应式宽度
           self.top_nav.setResponsiveWidth(600, 1000)
           
           # 添加导航项
           self.add_navigation_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.top_nav)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_navigation_items(self):
           """添加导航项"""
           items = [
               ("dashboard", "仪表板"),
               ("analytics", "数据分析"),
               ("reports", "报告"),
               ("team", "团队"),
               ("projects", "项目"),
               ("calendar", "日历")
           ]
           
           icons = [FIF.DASHBOARD, FIF.CHART, FIF.DOCUMENT, FIF.PEOPLE, FIF.FOLDER, FIF.CALENDAR]
           
           for (route_key, text), icon in zip(items, icons):
               self.top_nav.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           self.show_text_btn.clicked.connect(self.show_text)
           self.hide_text_btn.clicked.connect(self.hide_text)
           self.set_responsive_btn.clicked.connect(self.set_responsive)
           
           self.top_nav.currentItemChanged.connect(self.on_current_changed)
       
       def show_text(self):
           """显示文本"""
           self.top_nav.setTextVisible(True)
           self.current_label.setText("文本显示已启用")
       
       def hide_text(self):
           """隐藏文本"""
           self.top_nav.setTextVisible(False)
           self.current_label.setText("文本显示已禁用")
       
       def set_responsive(self):
           """设置响应式"""
           self.top_nav.setResponsiveWidth(800, 1200)
           self.current_label.setText("响应式阈值已更新: 800px - 1200px")
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           item_names = {
               "dashboard": "仪表板",
               "analytics": "数据分析",
               "reports": "报告",
               "team": "团队",
               "projects": "项目",
               "calendar": "日历"
           }
           
           item_name = item_names.get(route_key, "未知")
           self.current_label.setText(f"当前选择: {item_name}")

高级用法
--------

自定义样式顶部导航栏
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.top_navigation_bar import TopNavigationBar
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class CustomStyleTopNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义样式顶部导航栏")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建顶部导航栏
           self.top_nav = TopNavigationBar(showReturnButton=True)
           
           # 设置自定义样式
           self.setup_custom_style()
           
           # 添加导航项
           self.add_navigation_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.top_nav)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_custom_style(self):
           """设置自定义样式"""
           # 设置自定义选中颜色
           self.top_nav.setSelectedColor(QColor(255, 100, 100), QColor(100, 255, 100))
           
           # 设置响应式宽度
           self.top_nav.setResponsiveWidth(700, 1100)
       
       def add_navigation_items(self):
           """添加导航项"""
           items = [
               ("creative", "创意"),
               ("design", "设计"),
               ("develop", "开发"),
               ("test", "测试"),
               ("deploy", "部署")
           ]
           
           icons = [FIF.PALETTE, FIF.BRUSH, FIF.CODE, FIF.BUG, FIF.CLOUD_UPLOAD]
           
           for (route_key, text), icon in zip(items, icons):
               self.top_nav.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           self.top_nav.currentItemChanged.connect(self.on_current_changed)
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           item_names = {
               "creative": "创意",
               "design": "设计",
               "develop": "开发",
               "test": "测试",
               "deploy": "部署"
           }
           
           item_name = item_names.get(route_key, "未知")
           self.current_label.setText(f"当前选择: {item_name}")

动态顶部导航栏
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.top_navigation_bar import TopNavigationBar
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class DynamicTopNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态顶部导航栏")
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
           
           # 创建顶部导航栏
           self.top_nav = TopNavigationBar(showReturnButton=True)
           
           # 添加初始项
           self.add_initial_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.top_nav)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_initial_items(self):
           """添加初始项"""
           items = [
               ("home", "首页"),
               ("explore", "探索"),
               ("favorites", "收藏")
           ]
           
           icons = [FIF.HOME, FIF.SEARCH, FIF.HEART]
           
           for (route_key, text), icon in zip(items, icons):
               self.top_nav.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           self.add_btn.clicked.connect(self.add_item)
           self.insert_btn.clicked.connect(self.insert_item)
           self.remove_btn.clicked.connect(self.remove_item)
           self.clear_btn.clicked.connect(self.clear_items)
           
           self.top_nav.currentItemChanged.connect(self.on_current_changed)
       
       def add_item(self):
           """添加项"""
           import random
           
           additional_items = [
               ("documents", "文档"),
               ("pictures", "图片"),
               ("music", "音乐"),
               ("videos", "视频")
           ]
           
           icons = [FIF.DOCUMENT, FIF.PHOTO, FIF.MUSIC, FIF.VIDEO]
           
           (route_key, text), icon = random.choice(list(zip(additional_items, icons)))
           self.top_nav.addItem(route_key, icon, text)
           self.current_label.setText(f"已添加: {text}")
       
       def insert_item(self):
           """插入项"""
           import random
           
           additional_items = [
               ("settings", "设置"),
               ("help", "帮助"),
               ("about", "关于")
           ]
           
           icons = [FIF.SETTING, FIF.HELP, FIF.INFO]
           
           (route_key, text), icon = random.choice(list(zip(additional_items, icons)))
           # 插入到第二个位置
           self.top_nav.insertItem(1, route_key, icon, text)
           self.current_label.setText(f"已插入: {text}")
       
       def remove_item(self):
           """移除当前项"""
           current_key = self.top_nav.currentRouteKey()
           if current_key:
               self.top_nav.removeWidget(current_key)
               self.current_label.setText(f"已移除: {current_key}")
           else:
               self.current_label.setText("没有可移除的项")
       
       def clear_items(self):
           """清空所有项"""
           self.top_nav.clear()
           self.current_label.setText("已清空所有项")
       
       def on_current_changed(self, route_key):
           """当前项变化处理"""
           if route_key:
               self.current_label.setText(f"当前选择: {route_key}")
           else:
               self.current_label.setText("当前选择: 无")

最佳实践
--------

1. **响应式设计** - 合理设置响应式宽度阈值
2. **项管理** - 合理管理导航项的添加、删除和插入
3. **样式统一** - 保持顶部导航栏的视觉风格一致性
4. **动画效果** - 合理使用指示器动画提升用户体验
5. **布局管理** - 正确使用左、中、右三个区域

注意事项
--------

- 顶部导航栏会根据窗口宽度自动调整文本显示
- 导航项过多时会自动显示滚动条
- 返回按钮需要手动启用
- 指示器动画需要正确设置颜色
- 响应式设计需要考虑不同屏幕尺寸
- 路由键需要唯一标识每个导航项

相关模块
--------

- :doc:`components.navigation.navigation_panel` - 导航面板
- :doc:`components.navigation.navigation_interface` - 导航接口
- :doc:`components.navigation.navigation_bar` - 导航栏
