Navigation Widget 导航控件模块
==================================

Navigation Widget 模块提供导航控件的基础组件，支持树形结构和多种显示模式。
该模块为导航面板和导航栏提供基础控件，支持展开/折叠动画和自定义样式。

主要功能
--------

- **导航控件** - 提供基础的导航控件功能
- **树形结构** - 支持层级树形结构
- **动画效果** - 支持展开/折叠和指示器动画
- **用户卡片** - 提供用户信息展示控件
- **分隔符** - 提供导航项分隔功能

核心组件
--------

NavigationWidget
~~~~~~~~~~~~~~

导航控件基类，提供基础的导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationWidget
   
   # 创建导航控件
   nav_widget = NavigationWidget(isSelectable=True)
   
   # 设置选中状态
   nav_widget.setSelected(True)
   
   # 设置紧凑状态
   nav_widget.setCompacted(False)

**主要信号：**
- ``clicked`` - 点击信号
- ``selectedChanged`` - 选中状态变化信号

**主要方法：**
- ``setSelected()`` - 设置选中状态
- ``setCompacted()`` - 设置紧凑状态
- ``setIndicatorColor()`` - 设置指示器颜色

NavigationPushButton
~~~~~~~~~~~~~~~~~~~~

导航按钮，提供按钮式导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationPushButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建导航按钮
   nav_button = NavigationPushButton(
       icon=FIF.HOME,
       text="首页",
       isSelectable=True
   )

NavigationTreeWidget
~~~~~~~~~~~~~~~~~~

导航树控件，提供树形结构导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationTreeWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建导航树控件
   tree_widget = NavigationTreeWidget(
       icon=FIF.FOLDER,
       text="文件夹",
       isSelectable=True
   )
   
   # 添加子项
   tree_widget.addChild(child_widget)

NavigationUserCard
~~~~~~~~~~~~~~~~~~

导航用户卡片，提供用户信息展示功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationUserCard
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建用户卡片
   user_card = NavigationUserCard()
   user_card.setTitle("用户名")
   user_card.setSubtitle("user@example.com")
   user_card.setAvatar(FIF.PERSON)

实际应用
--------

基本导航控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationWidget
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
           title_label = Label("导航控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航控件
           self.nav_widget = NavigationWidget(isSelectable=True)
           
           # 显示当前状态
           self.status_label = Label("状态: 未选中")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.nav_widget.clicked.connect(self.on_clicked)
           self.nav_widget.selectedChanged.connect(self.on_selected_changed)
       
       def on_clicked(self, triggered_by_user):
           """点击处理"""
           if triggered_by_user:
               self.status_label.setText("状态: 用户点击")
           else:
               self.status_label.setText("状态: 程序触发")
       
       def on_selected_changed(self, is_selected):
           """选中状态变化处理"""
           if is_selected:
               self.status_label.setText("状态: 已选中")
           else:
               self.status_label.setText("状态: 未选中")

导航按钮
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationPushButton
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class NavigationButtonWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("导航按钮示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建导航按钮
           self.home_btn = NavigationPushButton(FIF.HOME, "首页", True)
           self.settings_btn = NavigationPushButton(FIF.SETTING, "设置", True)
           self.help_btn = NavigationPushButton(FIF.HELP, "帮助", True)
           
           # 显示当前选择
           self.current_label = Label("当前选择: 无")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.home_btn)
           layout.addWidget(self.settings_btn)
           layout.addWidget(self.help_btn)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.home_btn.clicked.connect(lambda: self.on_button_clicked("首页"))
           self.settings_btn.clicked.connect(lambda: self.on_button_clicked("设置"))
           self.help_btn.clicked.connect(lambda: self.on_button_clicked("帮助"))
       
       def on_button_clicked(self, button_name):
           """按钮点击处理"""
           self.current_label.setText(f"当前选择: {button_name}")

高级用法
--------

树形导航控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationTreeWidget
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class TreeNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("树形导航控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_child_btn = PushButton("添加子项")
           self.expand_btn = PushButton("展开")
           self.collapse_btn = PushButton("折叠")
           
           button_layout.addWidget(self.add_child_btn)
           button_layout.addWidget(self.expand_btn)
           button_layout.addWidget(self.collapse_btn)
           
           # 创建树形导航控件
           self.tree_widget = NavigationTreeWidget(
               icon=FIF.FOLDER,
               text="根节点",
               isSelectable=True
           )
           
           # 添加一些子项
           self.add_initial_children()
           
           # 显示当前状态
           self.status_label = Label("状态: 未展开")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.tree_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def add_initial_children(self):
           """添加初始子项"""
           children = [
               ("文档", FIF.DOCUMENT),
               ("图片", FIF.PHOTO),
               ("音乐", FIF.MUSIC)
           ]
           
           for name, icon in children:
               child = NavigationTreeWidget(icon, name, True)
               self.tree_widget.addChild(child)
       
       def setup_connections(self):
           """设置连接"""
           self.add_child_btn.clicked.connect(self.add_child)
           self.expand_btn.clicked.connect(lambda: self.tree_widget.setExpanded(True))
           self.collapse_btn.clicked.connect(lambda: self.tree_widget.setExpanded(False))
           
           self.tree_widget.expanded.connect(self.on_expanded_changed)
       
       def add_child(self):
           """添加子项"""
           import random
           
           names = ["新文件", "新图片", "新音乐", "新视频"]
           icons = [FIF.DOCUMENT, FIF.PHOTO, FIF.MUSIC, FIF.VIDEO]
           
           name = random.choice(names)
           icon = random.choice(icons)
           
           child = NavigationTreeWidget(icon, name, True)
           self.tree_widget.addChild(child)
           self.status_label.setText(f"状态: 已添加 {name}")
       
       def on_expanded_changed(self, is_expanded):
           """展开状态变化处理"""
           if is_expanded:
               self.status_label.setText("状态: 已展开")
           else:
               self.status_label.setText("状态: 已折叠")

用户卡片控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationUserCard
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class UserCardWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("用户卡片控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.set_info_btn = PushButton("设置信息")
           self.set_avatar_btn = PushButton("设置头像")
           self.animate_btn = PushButton("动画效果")
           
           button_layout.addWidget(self.set_info_btn)
           button_layout.addWidget(self.set_avatar_btn)
           button_layout.addWidget(self.animate_btn)
           
           # 创建用户卡片
           self.user_card = NavigationUserCard()
           self.user_card.setTitle("张三")
           self.user_card.setSubtitle("zhangsan@example.com\n高级开发工程师")
           self.user_card.setAvatar(FIF.PERSON)
           
           # 显示当前状态
           self.status_label = Label("状态: 就绪")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.user_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.set_info_btn.clicked.connect(self.set_user_info)
           self.set_avatar_btn.clicked.connect(self.set_user_avatar)
           self.animate_btn.clicked.connect(self.toggle_animation)
           
           self.user_card.clicked.connect(self.on_card_clicked)
       
       def set_user_info(self):
           """设置用户信息"""
           self.user_card.setTitle("李四")
           self.user_card.setSubtitle("lisi@example.com\n产品经理")
           self.status_label.setText("状态: 已更新用户信息")
       
       def set_user_avatar(self):
           """设置用户头像"""
           self.user_card.setAvatar(FIF.EMOTICON_SMILE)
           self.status_label.setText("状态: 已更新头像")
       
       def toggle_animation(self):
           """切换动画效果"""
           # 这里可以触发一些动画效果
           self.status_label.setText("状态: 动画效果已触发")
       
       def on_card_clicked(self, triggered_by_user):
           """卡片点击处理"""
           if triggered_by_user:
               self.status_label.setText("状态: 用户点击卡片")
           else:
               self.status_label.setText("状态: 程序触发卡片")

自定义导航控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.navigation_widget import NavigationWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor, QFont
   
   class CustomNavigationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义导航控件")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建自定义导航控件
           self.nav_widget = CustomWidget(isSelectable=True)
           
           # 显示当前状态
           self.status_label = Label("状态: 未选中")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.nav_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.nav_widget.clicked.connect(self.on_clicked)
           self.nav_widget.selectedChanged.connect(self.on_selected_changed)
       
       def on_clicked(self, triggered_by_user):
           """点击处理"""
           if triggered_by_user:
               self.status_label.setText("状态: 用户点击自定义控件")
           else:
               self.status_label.setText("状态: 程序触发自定义控件")
       
       def on_selected_changed(self, is_selected):
           """选中状态变化处理"""
           if is_selected:
               self.status_label.setText("状态: 自定义控件已选中")
           else:
               self.status_label.setText("状态: 自定义控件未选中")
   
   class CustomWidget(NavigationWidget):
       """自定义导航控件"""
       
       def __init__(self, isSelectable=True, parent=None):
           super().__init__(isSelectable, parent)
           self.setup_custom_style()
       
       def setup_custom_style(self):
           """设置自定义样式"""
           # 自定义文本颜色
           self.setLightTextColor(QColor(100, 100, 255))  # 蓝色
           self.setDarkTextColor(QColor(255, 200, 100))  # 橙色
           
           # 自定义指示器颜色
           self.setIndicatorColor(QColor(255, 100, 100), QColor(100, 255, 100))
           
           # 自定义字体
           custom_font = QFont()
           custom_font.setFamily("Microsoft YaHei")
           custom_font.setPointSize(12)
           custom_font.setBold(True)
           self.setFont(custom_font)
       
       def paintEvent(self, event):
           """自定义绘制"""
           super().paintEvent(event)
           
           # 可以在这里添加额外的绘制逻辑
           # 例如：绘制自定义背景、边框等

最佳实践
--------

1. **状态管理** - 正确管理选中、展开、紧凑等状态
2. **动画效果** - 合理使用动画提升用户体验
3. **自定义样式** - 根据需要自定义颜色、字体等样式
4. **层级结构** - 正确设置父子关系和层级深度
5. **事件处理** - 合理处理点击、悬停等用户交互

注意事项
--------

- 导航控件会根据显示模式自动调整布局
- 树形结构需要正确设置父子关系
- 动画效果可能影响性能，需要合理使用
- 自定义绘制需要正确处理主题适配
- 用户卡片支持动画效果和自定义样式
- 分隔符用于视觉分组，不参与导航逻辑

相关模块
--------

- :doc:`components.navigation.navigation_panel` - 导航面板
- :doc:`components.navigation.navigation_interface` - 导航接口
- :doc:`components.navigation.navigation_bar` - 导航栏
