Navigation Bar 导航栏模块
=============================

Navigation Bar 模块提供现代化的导航栏功能，支持图标滑动动画和指示器。
该模块提供垂直导航栏界面，支持选中状态动画和自定义样式。

主要功能
--------

- **导航栏** - 提供垂直导航栏功能
- **图标动画** - 支持选中项的图标滑动动画
- **指示器** - 提供选中状态的视觉指示器
- **滚动支持** - 支持滚动区域的导航项
- **自定义样式** - 支持自定义选中颜色和文本显示

核心组件
--------

NavigationBar
~~~~~~~~~~~~~

导航栏，提供完整的导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_bar import NavigationBar
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建导航栏
   nav_bar = NavigationBar()
   
   # 添加导航项
   nav_bar.addItem("home", FIF.HOME, "首页")
   nav_bar.addItem("settings", FIF.SETTING, "设置")
   nav_bar.addItem("profile", FIF.PERSON, "个人资料")
   
   # 设置当前项
   nav_bar.setCurrentItem("home")

**主要方法：**
- ``addItem()`` - 添加导航项
- ``setCurrentItem()`` - 设置当前选中项
- ``removeWidget()`` - 移除导航项
- ``setSelectedColor()`` - 设置选中颜色

NavigationBarPushButton
~~~~~~~~~~~~~~~~~~~~~~

导航栏按钮，提供单个导航项功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_bar import NavigationBarPushButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建导航按钮
   nav_button = NavigationBarPushButton(
       icon=FIF.HOME,
       text="首页",
       isSelectable=True
   )

实际应用
--------

基本导航栏
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_bar import NavigationBar
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("导航栏示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航栏
           self.nav_bar = NavigationBar()
           
           # 添加导航项
           self.nav_bar.addItem("dashboard", FIF.DASHBOARD, "仪表板")
           self.nav_bar.addItem("documents", FIF.DOCUMENT, "文档")
           self.nav_bar.addItem("pictures", FIF.PHOTO, "图片")
           self.nav_bar.addItem("music", FIF.MUSIC, "音乐")
           self.nav_bar.addItem("videos", FIF.VIDEO, "视频")
           self.nav_bar.addItem("settings", FIF.SETTING, "设置")
           
           # 显示当前选择
           self.current_label = Label("当前选择: 仪表板")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_bar, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           # 导航栏选择变化会通过路由系统处理
           pass

带滚动区域的导航栏
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_bar import NavigationBar
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class ScrollableNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("滚动导航栏示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航栏
           self.nav_bar = NavigationBar()
           
           # 添加大量导航项到滚动区域
           categories = [
               ("home", FIF.HOME, "首页"),
               ("explore", FIF.GLOBE, "探索"),
               ("trending", FIF.TRENDING_UP, "热门"),
               ("subscriptions", FIF.HEART, "订阅"),
               ("library", FIF.LIBRARY, "库"),
               ("history", FIF.HISTORY, "历史"),
               ("watch_later", FIF.CLOCK, "稍后观看"),
               ("liked", FIF.LIKE, "喜欢"),
               ("downloads", FIF.DOWNLOAD, "下载"),
               ("settings", FIF.SETTING, "设置"),
               ("help", FIF.HELP, "帮助"),
               ("about", FIF.INFO, "关于")
           ]
           
           for route_key, icon, text in categories:
               self.nav_bar.addItem(route_key, icon, text)
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_bar, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           # 监听导航变化
           pass

高级用法
--------

自定义样式导航栏
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_bar import NavigationBar, NavigationBarPushButton
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor, QFont
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class CustomNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义样式导航栏")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航栏
           self.nav_bar = NavigationBar()
           
           # 设置自定义选中颜色
           self.nav_bar.setSelectedColor("#FF6B6B", "#4ECDC4")
           
           # 设置自定义字体
           custom_font = QFont()
           custom_font.setFamily("Microsoft YaHei")
           custom_font.setPointSize(12)
           custom_font.setBold(True)
           self.nav_bar.setFont(custom_font)
           
           # 添加导航项
           nav_items = [
               ("home", FIF.HOME, "🏠 首页"),
               ("workspace", FIF.FOLDER, "📁 工作区"),
               ("projects", FIF.CODE, "💻 项目"),
               ("team", FIF.PEOPLE, "👥 团队"),
               ("calendar", FIF.CALENDAR, "📅 日历"),
               ("messages", FIF.MAIL, "📧 消息"),
               ("analytics", FIF.CHART, "📊 分析")
           ]
           
           for route_key, icon, text in nav_items:
               self.nav_bar.addItem(route_key, icon, text)
           
           # 显示当前选择
           self.current_label = Label("当前选择: 🏠 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_bar, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           pass

动态导航栏
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_bar import NavigationBar
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class DynamicNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态导航栏")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_btn = PushButton("添加项")
           self.remove_btn = PushButton("移除项")
           self.clear_btn = PushButton("清空")
           
           button_layout.addWidget(self.add_btn)
           button_layout.addWidget(self.remove_btn)
           button_layout.addWidget(self.clear_btn)
           
           # 创建导航栏
           self.nav_bar = NavigationBar()
           
           # 添加初始项
           self.add_initial_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.nav_bar, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_initial_items(self):
           """添加初始导航项"""
           initial_items = [
               ("home", FIF.HOME, "首页"),
               ("explore", FIF.GLOBE, "探索"),
               ("favorites", FIF.HEART, "收藏")
           ]
           
           for route_key, icon, text in initial_items:
               self.nav_bar.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           self.add_btn.clicked.connect(self.add_item)
           self.remove_btn.clicked.connect(self.remove_item)
           self.clear_btn.clicked.connect(self.clear_items)
       
       def add_item(self):
           """添加导航项"""
           import random
           
           additional_items = [
               ("documents", FIF.DOCUMENT, "文档"),
               ("pictures", FIF.PHOTO, "图片"),
               ("music", FIF.MUSIC, "音乐"),
               ("videos", FIF.VIDEO, "视频"),
               ("downloads", FIF.DOWNLOAD, "下载"),
               ("settings", FIF.SETTING, "设置")
           ]
           
           route_key, icon, text = random.choice(additional_items)
           self.nav_bar.addItem(route_key, icon, text)
       
       def remove_item(self):
           """移除当前项"""
           current_item = self.nav_bar.currentItem()
           if current_item:
               # 获取当前项的route key
               # 这里需要通过其他方式获取，因为currentItem()返回的是widget
               pass
       
       def clear_items(self):
           """清空所有项"""
           # NavigationBar没有直接的clear方法，需要重新创建
           pass

分组导航栏
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_bar import NavigationBar
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class GroupedNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("分组导航栏")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航栏
           self.nav_bar = NavigationBar()
           
           # 添加分组导航项
           
           # 主要功能
           main_items = [
               ("home", FIF.HOME, "首页"),
               ("dashboard", FIF.DASHBOARD, "仪表板"),
               ("analytics", FIF.CHART, "数据分析")
           ]
           
           for route_key, icon, text in main_items:
               self.nav_bar.addItem(route_key, icon, text)
           
           # 工具功能
           tool_items = [
               ("editor", FIF.EDIT, "编辑器"),
               ("terminal", FIF.COMMAND_PROMPT, "终端"),
               ("file_manager", FIF.FOLDER, "文件管理")
           ]
           
           for route_key, icon, text in tool_items:
               self.nav_bar.addItem(route_key, icon, text)
           
           # 设置功能
           setting_items = [
               ("preferences", FIF.SETTING, "偏好设置"),
               ("account", FIF.PERSON, "账户管理"),
               ("help", FIF.HELP, "帮助中心")
           ]
           
           for route_key, icon, text in setting_items:
               self.nav_bar.addItem(route_key, icon, text)
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_bar, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           pass

最佳实践
--------

1. **图标选择** - 使用合适的图标增强视觉效果
2. **文本简洁** - 导航项文本要简洁明了
3. **分组合理** - 合理组织导航项的层次结构
4. **状态管理** - 正确处理选中状态和切换
5. **动画效果** - 合理使用动画提升用户体验

注意事项
--------

- 导航栏会自动处理滚动区域的显示
- 选中项会有图标滑动动画效果
- 大量导航项会自动启用滚动
- 自定义颜色需要同时设置亮色和暗色模式
- 路由键需要唯一标识每个导航项

相关模块
--------

- :doc:`components.navigation.navigation_panel` - 导航面板
- :doc:`components.navigation.breadcrumb` - 面包屑导航
- :doc:`components.navigation.navigation_interface` - 导航接口
