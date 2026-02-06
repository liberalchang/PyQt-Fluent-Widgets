Navigation Interface 导航接口模块
===================================

Navigation Interface 模块提供导航界面的统一接口，支持多种导航组件的集成。
该模块为导航面板和导航栏提供统一的接口，支持灵活的导航配置。

主要功能
--------

- **统一接口** - 提供导航组件的统一接口
- **多种组件** - 支持导航项、用户卡片、分隔符等
- **位置控制** - 支持顶部、底部、滚动区域的位置控制
- **显示模式** - 支持菜单和紧凑显示模式
- **亚克力效果** - 支持亚克力背景效果

核心组件
--------

NavigationInterface
~~~~~~~~~~~~~~~~~

导航接口，提供完整的导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_interface import NavigationInterface
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建导航接口
   nav_interface = NavigationInterface(
       parent=parent,
       showMenuButton=True,
       showReturnButton=False,
       collapsible=True
   )
   
   # 添加导航项
   nav_interface.addItem("home", FIF.HOME, "首页")
   nav_interface.addItem("settings", FIF.SETTING, "设置")
   
   # 设置当前项
   nav_interface.setCurrentItem("home")

**主要方法：**
- ``addItem()`` - 添加导航项
- ``addWidget()`` - 添加自定义控件
- ``addUserCard()`` - 添加用户卡片
- ``setCurrentItem()`` - 设置当前选中项
- ``expand()`` - 展开导航面板
- ``toggle()`` - 切换导航面板状态

实际应用
--------

基本导航接口
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_interface import NavigationInterface
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicNavigationInterfaceWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("导航接口示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航接口
           self.nav_interface = NavigationInterface(
               parent=self,
               showMenuButton=True,
               showReturnButton=False,
               collapsible=True
           )
           
           # 添加导航项
           self.add_navigation_items()
           
           # 显示当前选择
           self.current_label = Label("当前选择: 首页")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_interface, 1)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def add_navigation_items(self):
           """添加导航项"""
           # 主要功能
           main_items = [
               ("dashboard", FIF.DASHBOARD, "仪表板"),
               ("documents", FIF.DOCUMENT, "文档"),
               ("pictures", FIF.PHOTO, "图片"),
               ("music", FIF.MUSIC, "音乐")
           ]
           
           for route_key, icon, text in main_items:
               self.nav_interface.addItem(route_key, icon, text)
           
           # 设置功能
           setting_items = [
               ("settings", FIF.SETTING, "设置"),
               ("help", FIF.HELP, "帮助"),
               ("about", FIF.INFO, "关于")
           ]
           
           for route_key, icon, text in setting_items:
               self.nav_interface.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           # 监听导航变化
           pass

带用户卡片的导航接口
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_interface import NavigationInterface
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class UserCardNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("用户卡片导航接口")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_card_btn = PushButton("添加用户卡片")
           self.expand_btn = PushButton("展开")
           self.collapse_btn = PushButton("折叠")
           
           button_layout.addWidget(self.add_card_btn)
           button_layout.addWidget(self.expand_btn)
           button_layout.addWidget(self.collapse_btn)
           
           # 创建导航接口
           self.nav_interface = NavigationInterface(
               parent=self,
               showMenuButton=True,
               showReturnButton=True,
               collapsible=True
           )
           
           # 添加用户卡片
           self.add_user_cards()
           
           # 添加导航项
           self.add_navigation_items()
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.nav_interface, 1)
           self.setLayout(layout)
       
       def add_user_cards(self):
           """添加用户卡片"""
           users = [
               ("user1", FIF.PERSON, "张三", "zhangsan@example.com", "高级开发工程师"),
               ("user2", FIF.PEOPLE, "李四", "lisi@example.com", "产品经理"),
               ("user3", FIF.EMOTICON_SMILE, "王五", "wangwu@example.com", "UI设计师")
           ]
           
           for route_key, avatar, name, email, role in users:
               self.nav_interface.addUserCard(
                   routeKey=route_key,
                   avatar=avatar,
                   title=name,
                   subtitle=f"{role}\n{email}",
                   onClick=lambda r=route_key: self.on_user_clicked(r)
               )
       
       def add_navigation_items(self):
           """添加导航项"""
           nav_items = [
               ("home", FIF.HOME, "首页"),
               ("messages", FIF.MAIL, "消息"),
               ("calendar", FIF.CALENDAR, "日历"),
               ("tasks", FIF.CHECKBOX, "任务")
           ]
           
           for route_key, icon, text in nav_items:
               self.nav_interface.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           self.add_card_btn.clicked.connect(self.add_random_user_card)
           self.expand_btn.clicked.connect(self.nav_interface.expand)
           self.collapse_btn.clicked.connect(self.nav_interface.toggle)
       
       def on_user_clicked(self, route_key):
           """用户卡片点击处理"""
           print(f"用户 {route_key} 被点击")
       
       def add_random_user_card(self):
           """添加随机用户卡片"""
           import random
           
           names = ["赵六", "钱七", "孙八", "周九"]
           roles = ["后端开发", "前端开发", "测试工程师", "运维工程师"]
           emails = ["zhaoliu@example.com", "qianqi@example.com", "sunba@example.com", "zhoujiu@example.com"]
           
           name = random.choice(names)
           role = random.choice(roles)
           email = random.choice(emails)
           
           self.nav_interface.addUserCard(
               routeKey=f"user_{random.randint(100, 999)}",
               avatar=FIF.PERSON,
               title=name,
               subtitle=f"{role}\n{email}",
               onClick=lambda: print(f"新用户 {name} 被点击")
           )

高级用法
--------

分组导航接口
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_interface import NavigationInterface
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
           title_label = Label("分组导航接口")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航接口
           self.nav_interface = NavigationInterface(
               parent=self,
               showMenuButton=True,
               showReturnButton=False,
               collapsible=True
           )
           
           # 添加分组导航
           self.add_grouped_navigation()
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_interface, 1)
           self.setLayout(layout)
       
       def add_grouped_navigation(self):
           """添加分组导航"""
           # 工作相关
           self.nav_interface.addItemHeader("工作", position=NavigationItemPosition.TOP)
           
           work_items = [
               ("projects", FIF.FOLDER, "项目"),
               ("tasks", FIF.CHECKBOX, "任务"),
               ("calendar", FIF.CALENDAR, "日历"),
               ("meetings", FIF.VIDEO, "会议")
           ]
           
           for route_key, icon, text in work_items:
               self.nav_interface.addItem(route_key, icon, text)
           
           # 添加分隔符
           self.nav_interface.addSeparator()
           
           # 协作相关
           self.nav_interface.addItemHeader("协作", position=NavigationItemPosition.TOP)
           
           collab_items = [
               ("team", FIF.PEOPLE, "团队"),
               ("chat", FIF.COMMENT, "聊天"),
               ("files", FIF.DOCUMENT, "文件"),
               ("wiki", FIF.BOOK, "知识库")
           ]
           
           for route_key, icon, text in collab_items:
               self.nav_interface.addItem(route_key, icon, text)
           
           # 添加分隔符
           self.nav_interface.addSeparator()
           
           # 设置相关
           self.nav_interface.addItemHeader("设置", position=NavigationItemPosition.TOP)
           
           setting_items = [
               ("preferences", FIF.SETTING, "偏好设置"),
               ("account", FIF.PERSON, "账户管理"),
               ("privacy", FIF.LOCK, "隐私设置"),
               ("help", FIF.HELP, "帮助中心")
           ]
           
           for route_key, icon, text in setting_items:
               self.nav_interface.addItem(route_key, icon, text)
       
       def setup_connections(self):
           """设置连接"""
           pass

动态导航接口
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_interface import NavigationInterface
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
           title_label = Label("动态导航接口")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_item_btn = PushButton("添加项")
           self.add_card_btn = PushButton("添加卡片")
           self.clear_btn = PushButton("清空")
           
           button_layout.addWidget(self.add_item_btn)
           button_layout.addWidget(self.add_card_btn)
           button_layout.addWidget(self.clear_btn)
           
           # 创建导航接口
           self.nav_interface = NavigationInterface(
               parent=self,
               showMenuButton=True,
               showReturnButton=True,
               collapsible=True
           )
           
           # 添加初始内容
           self.add_initial_content()
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.nav_interface, 1)
           self.setLayout(layout)
       
       def add_initial_content(self):
           """添加初始内容"""
           # 添加一些导航项
           items = [
               ("home", FIF.HOME, "首页"),
               ("explore", FIF.GLOBE, "探索"),
               ("favorites", FIF.HEART, "收藏")
           ]
           
           for route_key, icon, text in items:
               self.nav_interface.addItem(route_key, icon, text)
           
           # 添加用户卡片
           self.nav_interface.addUserCard(
               routeKey="current_user",
               avatar=FIF.PERSON,
               title="当前用户",
               subtitle="user@example.com",
               onClick=lambda: print("当前用户卡片被点击")
           )
       
       def setup_connections(self):
           """设置连接"""
           self.add_item_btn.clicked.connect(self.add_random_item)
           self.add_card_btn.clicked.connect(self.add_random_card)
           self.clear_btn.clicked.connect(self.clear_navigation)
       
       def add_random_item(self):
           """添加随机导航项"""
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
           self.nav_interface.addItem(route_key, icon, text)
       
       def add_random_card(self):
           """添加随机用户卡片"""
           import random
           
           names = ["新用户1", "新用户2", "新用户3"]
           roles = ["开发者", "设计师", "测试员"]
           
           name = random.choice(names)
           role = random.choice(roles)
           
           self.nav_interface.addUserCard(
               routeKey=f"new_user_{random.randint(100, 999)}",
               avatar=FIF.EMOTICON_SMILE,
               title=name,
               subtitle=f"角色: {role}",
               onClick=lambda: print(f"新用户 {name} 被点击")
           )
       
       def clear_navigation(self):
           """清空导航"""
           # NavigationInterface没有直接的clear方法
           # 需要重新创建接口或逐个移除
           pass

自定义样式导航接口
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_interface import NavigationInterface
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class CustomStyleNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义样式导航接口")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航接口
           self.nav_interface = NavigationInterface(
               parent=self,
               showMenuButton=True,
               showReturnButton=False,
               collapsible=True
           )
           
           # 设置自定义样式
           self.setup_custom_styles()
           
           # 添加导航项
           self.add_custom_items()
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_interface, 1)
           self.setLayout(layout)
       
       def setup_custom_styles(self):
           """设置自定义样式"""
           # 设置亚克力效果
           self.nav_interface.setAcrylicEnabled(True)
           
           # 设置指示器动画
           self.nav_interface.setIndicatorAnimationEnabled(True)
           
           # 设置自动调整大小范围
           self.nav_interface.setAutoResizeRange(300, 800)
           self.nav_interface.setAutoResizeEnabled(True)
       
       def add_custom_items(self):
           """添加自定义导航项"""
           custom_items = [
               ("dashboard", FIF.DASHBOARD, "控制台"),
               ("analytics", FIF.CHART, "数据分析"),
               ("reports", FIF.FILE_MULTIPLE, "报告"),
               ("notifications", FIF.RINGER, "通知")
           ]
           
           for route_key, icon, text in custom_items:
               self.nav_interface.addItem(
                   routeKey=route_key,
                   icon=icon,
                   text=text,
                   tooltip=f"点击进入{text}页面"
               )
       
       def setup_connections(self):
           """设置连接"""
           pass

最佳实践
--------

1. **层次结构** - 合理组织导航项的层次关系
2. **用户卡片** - 为用户提供清晰的个人信息展示
3. **分组管理** - 使用分隔符和标题进行分组
4. **动态更新** - 支持运行时动态添加和移除导航项
5. **样式统一** - 保持导航界面的视觉一致性

注意事项
--------

- 导航接口会自动处理展开/折叠状态
- 用户卡片适合显示个人信息和快速操作
- 分组功能有助于组织大量导航项
- 亚克力效果需要正确的背景支持
- 自动调整大小功能需要合理设置范围

相关模块
--------

- :doc:`components.navigation.navigation_panel` - 导航面板
- :doc:`components.navigation.navigation_bar` - 导航栏
- :doc:`components.navigation.breadcrumb` - 面包屑导航
