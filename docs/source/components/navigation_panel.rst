Navigation Panel 导航面板模块
==================================

Navigation Panel 模块提供现代化的导航面板功能，支持树形结构和多种显示模式。
该模块提供灵活的导航面板界面，支持展开/折叠、亚克力效果和自定义样式。

主要功能
--------

- **树形导航** - 支持层级树形结构导航
- **多种模式** - 支持最小、紧凑、扩展、菜单四种显示模式
- **亚克力效果** - 支持亚克力背景效果
- **动画效果** - 支持展开/折叠动画和指示器动画
- **自动调整** - 支持根据窗口大小自动调整面板宽度

核心组件
--------

NavigationPanel
~~~~~~~~~~~~~

导航面板，提供完整的导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_panel import NavigationPanel
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建导航面板
   nav_panel = NavigationPanel(
       parent=parent,
       isMinimalEnabled=False,
       showReturnButton=True
   collapsible=True
   )
   
   # 添加导航项
   nav_panel.addItem("home", FIF.HOME, "首页")
   nav_panel.addItem("settings", FIF.SETTING, "设置")
   
   # 设置当前项
   nav_panel.setCurrentItem("home")

**主要信号：**
- ``displayModeChanged`` - 显示模式变化信号

**主要方法：**
- ``addItem()`` - 添加导航项
- ``setCurrentItem()`` - 设置当前选中项
- ``expand()`` - 展开导航面板
- ``collapse()`` - 折叠导航面板
- ``setAcrylicEnabled()`` - 设置亚克力效果

NavigationItem
~~~~~~~~~~~~

导航项，表示单个导航节点。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_panel import NavigationItem
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建导航项
   nav_item = NavigationItem(
       routeKey="home",
       parentRouteKey="root",
       widget=widget
   )

NavigationTreeWidget
~~~~~~~~~~~~~~~~~~~

导航树控件，提供树形结构导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_panel import NavigationTreeWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建导航树控件
   tree_widget = NavigationTreeWidget(
       icon=FIF.FOLDER,
       text="文件夹",
       selectable=True
   )

实际应用
--------

基本导航面板
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_panel import NavigationPanel
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicNavigationPanelWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("导航面板示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航面板
           self.nav_panel = NavigationPanel(
               parent=self,
               isMinimalEnabled=False,
               showReturnButton=True,
               collapsible=True
           )
           
           # 添加导航项
           self.add_navigation_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_panel, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_navigation_items(self):
           """添加导航项"""
           # 主要功能
           main_items = [
               ("dashboard", FIF.DASHBOARD, "仪表板"),
               ("documents", FIF.DOCUMENT, "文档"),
               ("pictures", FIF.PHOTO, "图片")
               ("music", FIF.MUSIC, "音乐")
           ]
           
           for route_key, icon, text in main_items:
               self.nav_panel.addItem(route_key, icon, text)
           
           # 设置功能
           setting_items = [
               ("settings", FIF.SETTING, "设置"),
               ("help", FIF.HELP, "帮助"),
               ("about", FIF.INFO, "关于")
           ]
           
           for route_key, icon, text in setting_items:
               self.nav_panel.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           # 监听导航变化
           pass

树形导航面板
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_panel import NavigationPanel
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class TreeNavigationPanelWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("树形导航面板示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航面板
           self.nav_panel = NavigationPanel(
               parent=self,
               isMinimalEnabled=False,
               showReturnButton=True,
               collapsible=True
           )
           
           # 添加树形导航
           self.add_tree_navigation()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 项目管理")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_panel, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_tree_navigation(self):
           """添加树形导航"""
           # 项目管理
           self.nav_panel.addItemHeader("项目管理")
           
           project_items = [
               ("active", FIF.CHECKBOX, "进行中"),
               ("completed", FIF.CIRCLE_CHECK, "已完成"),
               ("archived", FIF.ARCHIVE, "已归档")
           ]
           
           for route_key, icon, text in project_items:
               self.nav_panel.addItem(route_key, icon, text)
           
           # 添加分隔符
           self.nav_panel.addSeparator()
           
           # 团队管理
           self.nav_panel.addItemHeader("团队管理")
           
           team_items = [
               ("developers", FIF.PEOPLE, "开发团队"),
               ("designers", FIF.PALETTE, "设计团队"),
               ("testers", FIF.EMOTICON_SMILE, "测试团队")
           ]
           
           for route_key, icon, text in team_items:
               self.nav_panel.addItem(route_key, icon, text)
           
           # 添加分隔符
           self.nav_panel.addSeparator()
           
           # 资源管理
           self.nav_panel.addItemHeader("资源管理")
           
           resource_items = [
               ("assets", FIF.FOLDER, "资源文件"),
               ("templates", FIF.FILE_MULTIPLE, "模板文件"),
               ("documentation", FIF.BOOK, "文档资料")
           ]
           
           for route_key, icon, text in resource_items:
               self.nav_panel.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           # 监听导航变化
           pass

高级用法
--------

亚克力导航面板
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_panel import NavigationPanel
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AcrylicNavigationPanelWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("亚克力导航面板")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航面板
           self.nav_panel = NavigationPanel(
               parent=self,
               isMinimalEnabled=False,
               showReturnButton=True,
               collapsible=True
           )
           
           # 启用亚克力效果
           self.nav_panel.setAcrylicEnabled(True)
           
           # 添加导航项
           self.add_navigation_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_panel, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_navigation_items(self):
           """添加导航项"""
           items = [
               ("home", FIF.HOME, "首页"),
               ("explore", FIF.GLOBE, "探索"),
               ("favorites", FIF.HEART, "收藏"),
               ("settings", FIF.SETTING, "设置")
           ]
           
           for route_key, icon, text in items:
               self.nav_panel.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           # 监听导航变化
           pass

自动调整导航面板
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_panel import NavigationPanel
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AutoResizeNavigationPanelWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自动调整导航面板")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.enable_btn = PushButton("启用自动调整")
           self.disable_btn = PushButton("禁用自动调整")
           self.set_range_btn = PushButton("设置范围")
           
           button_layout.addWidget(self.enable_btn)
           button_layout.addWidget(self.disable_btn)
           button_layout.addWidget(self.set_range_btn)
           
           # 创建导航面板
           self.nav_panel = NavigationPanel(
               parent=self,
               isMinimalEnabled=False,
               showReturnButton=True,
               collapsible=True
           )
           
           # 设置自动调整范围
           self.nav_panel.setAutoResizeRange(300, 800)
           
           # 添加导航项
           self.add_navigation_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.nav_panel, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_navigation_items(self):
           """添加导航项"""
           items = [
               ("home", FIF.HOME, "首页"),
               ("workspace", FIF.FOLDER, "工作区"),
               ("projects", FIF.CODE, "项目"),
               ("tools", FIF.WRENCH, "工具")
           ]
           
           for route_key, icon, text in items:
               self.nav_panel.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           self.enable_btn.clicked.connect(self.enable_auto_resize)
           self.disable_btn.clicked.connect(self.disable_auto_resize)
           self.set_range_btn.clicked.connect(self.set_resize_range)
           
           # 监听导航变化
           pass
       
       def enable_auto_resize(self):
           """启用自动调整"""
           self.nav_panel.setAutoResizeEnabled(True)
           self.current_label.setText("自动调整已启用")
       
       def disable_auto_resize(self):
           """禁用自动调整"""
           self.nav_panel.setAutoResizeEnabled(False)
           self.current_label.setText("自动调整已禁用")
       
       def set_resize_range(self):
           """设置调整范围"""
           self.nav_panel.setAutoResizeRange(400, 1200)
           self.current_label.setText(f"调整范围: 400px - 1200px")

最小化导航面板
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_panel import NavigationPanel
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class MinimalNavigationPanelWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("最小化导航面板")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建最小化导航面板
           self.nav_panel = NavigationPanel(
               parent=self,
               isMinimalEnabled=True,
               showReturnButton=False,
               collapsible=False
           )
           
           # 添加导航项
           self.add_minimal_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_panel, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_minimal_items(self):
           """添加最小化导航项"""
           items = [
               ("home", FIF.HOME, "首页"),
               ("search", FIF.SEARCH, "搜索"),
               ("menu", FIF.MENU, "菜单")
           ("back", FIF.RETURN, "返回")
           ]
           
           for route_key, icon, text in items:
               self.nav_panel.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           # 监听导航变化
           pass

最佳实践
--------

1. **模式选择** - 根据使用场景选择合适的显示模式
2. **层级结构** - 合理组织导航项的层级关系
3. **亚克力效果** - 在需要时启用亚克力背景效果
4. **自动调整** - 合理设置自动调整范围以提升用户体验
5. **动画效果** - 合理使用动画效果提升交互体验

注意事项
--------

- 导航面板会根据显示模式自动调整布局
- 树形结构需要正确设置父子关系
- 亚克力效果需要正确的背景支持
- 自动调整功能需要合理设置范围阈值
- 大量导航项可能影响性能
- 折叠/展开状态会自动保存和恢复

相关模块
--------

- :doc:`components.navigation.navigation_interface` - 导航接口
- :doc:`components.navigation.navigation_bar` - 导航栏
- :doc:`components.navigation.breadcrumb` - 面包屑导航
