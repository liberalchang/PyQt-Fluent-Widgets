导航组件 (Navigation)
====================

本节介绍 PySide6-Fluent-Widgets 中的导航相关组件。

NavigationInterface
-------------------

完整的导航界面组件。

.. code-block:: python

   from qfluentwidgets import NavigationInterface, NavigationItemPosition, FluentIcon

   navigation = NavigationInterface()
   
   # 添加导航项
   navigation.addItem(
       routeKey='home',
       icon=FluentIcon.HOME,
       text='首页',
       widget=home_widget,
       position=NavigationItemPosition.TOP
   )

NavigationPanel
----------------

导航面板组件。

.. code-block:: python

   from qfluentwidgets import NavigationPanel, NavigationItemPosition

   panel = NavigationPanel()
   panel.addWidget(widget, '标题', FluentIcon.HOME)

NavigationBar
------------

导航栏组件。

.. code-block:: python

   from qfluentwidgets import NavigationBar

   nav_bar = NavigationBar()
   nav_bar.addItem('项目1')
   nav_bar.addItem('项目2')

TopNavigationBar
---------------

顶部导航栏。

.. code-block:: python

   from qfluentwidgets import TopNavigationBar

   top_nav = TopNavigationBar()
   top_nav.addItem('顶部项目1')
   top_nav.addItem('顶部项目2')

Pivot
-----

透视导航控件。

.. code-block:: python

   from qfluentwidgets import Pivot

   pivot = Pivot()
   pivot.addItem('首页')
   pivot.addItem('设置')
   pivot.addItem('关于')

SegmentedWidget
---------------

分段控件。

.. code-block:: python

   from qfluentwidgets import SegmentedWidget

   segmented = SegmentedWidget()
   segmented.addItem('选项1')
   segmented.addItem('选项2')
   segmented.addItem('选项3')

BreadcrumbBar
-------------

面包屑导航。

.. code-block:: python

   from qfluentwidgets import BreadcrumbBar, BreadcrumbItem

   breadcrumb = BreadcrumbBar()
   breadcrumb.addItem(BreadcrumbItem('首页', 'home'))
   breadcrumb.addItem(BreadcrumbItem('设置', 'settings'))

NavigationWidget
----------------

导航项控件。

.. code-block:: python

   from qfluentwidgets import NavigationWidget

   nav_widget = NavigationWidget(
       icon=FluentIcon.DOCUMENT,
       text='文档',
       routeKey='docs'
   )

NavigationPushButton
-------------------

导航按钮控件。

.. code-block:: python

   from qfluentwidgets import NavigationPushButton

   nav_btn = NavigationPushButton(
       icon=FluentIcon.SETTING,
       text='设置'
   )

NavigationSeparator
------------------

导航分隔符。

.. code-block:: python

   from qfluentwidgets import NavigationSeparator

   separator = NavigationSeparator()

NavigationTreeWidget
--------------------

导航树形控件。

.. code-block:: python

   from qfluentwidgets import NavigationTreeWidget

   tree_widget = NavigationTreeWidget()
   tree_widget.addItem('根节点')
   tree_widget.addChild('子节点')

NavigationAvatarWidget
----------------------

导航头像控件。

.. code-block:: python

   from qfluentwidgets import NavigationAvatarWidget

   avatar = NavigationAvatarWidget()
   avatar.setAvatar('path/to/avatar.png')

NavigationItemHeader
--------------------

导航项头部。

.. code-block:: python

   from qfluentwidgets import NavigationItemHeader

   header = NavigationItemHeader('分组标题')

NavigationUserCard
------------------

导航用户卡片。

.. code-block:: python

   from qfluentwidgets import NavigationUserCard

   user_card = NavigationUserCard()
   user_card.setName('用户名')
   user_card.setAvatar('path/to/avatar.png')

完整示例
--------

下面是一个完整的导航组件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QStackedWidget
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class NavigationDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('导航组件示例')
           self.resize(1000, 700)
           
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           # 创建导航界面
           self.navigation = NavigationInterface(self, showMenuButton=True)
           
           # 创建内容区域
           self.stacked_widget = QStackedWidget()
           
           # 创建页面
           self.create_pages()
           
           # 添加导航项
           self.add_navigation_items()
           
           # 设置中央窗口
           self.navigation.addWidget(self.stacked_widget)
           self.setCentralWidget(self.navigation)

       def create_pages(self):
           """创建各个页面"""
           # 首页
           home_page = QWidget()
           home_layout = QVBoxLayout(home_page)
           home_layout.addWidget(QLabel('这是首页'))
           self.stacked_widget.addWidget(home_page)
           
           # 设置页
           settings_page = QWidget()
           settings_layout = QVBoxLayout(settings_page)
           settings_layout.addWidget(QLabel('这是设置页'))
           self.stacked_widget.addWidget(settings_page)
           
           # 关于页
           about_page = QWidget()
           about_layout = QVBoxLayout(about_page)
           about_layout.addWidget(QLabel('这是关于页'))
           self.stacked_widget.addWidget(about_page)
           
           # 用户页
           user_page = QWidget()
           user_layout = QVBoxLayout(user_page)
           user_layout.addWidget(QLabel('这是用户页'))
           self.stacked_widget.addWidget(user_page)

       def add_navigation_items(self):
           """添加导航项"""
           # 首页
           self.navigation.addItem(
               routeKey='home',
               icon=FluentIcon.HOME,
               text='首页',
               widget=self.stacked_widget.widget(0),
               position=NavigationItemPosition.TOP
           )
           
           # 设置
           self.navigation.addItem(
               routeKey='settings',
               icon=FluentIcon.SETTING,
               text='设置',
               widget=self.stacked_widget.widget(1),
               position=NavigationItemPosition.TOP
           )
           
           # 关于
           self.navigation.addItem(
               routeKey='about',
               icon=FluentIcon.INFO,
               text='关于',
               widget=self.stacked_widget.widget(2),
               position=NavigationItemPosition.TOP
           )
           
           # 用户卡片（底部）
           user_card = NavigationUserCard()
           user_card.setName('用户名')
           user_card.setAvatar('path/to/avatar.png')
           
           self.navigation.addWidget(
               routeKey='user',
               icon=FluentIcon.PERSON,
               text='用户',
               widget=self.stacked_widget.widget(3),
               position=NavigationItemPosition.BOTTOM
           )
           
           # 连接信号
           self.navigation.currentItemChanged.connect(self.on_navigation_changed)

       def on_navigation_changed(self, routeKey):
           """导航切换处理"""
           if routeKey == 'home':
               self.stacked_widget.setCurrentIndex(0)
           elif routeKey == 'settings':
               self.stacked_widget.setCurrentIndex(1)
           elif routeKey == 'about':
               self.stacked_widget.setCurrentIndex(2)
           elif routeKey == 'user':
               self.stacked_widget.setCurrentIndex(3)

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = NavigationDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **导航结构**: 合理组织导航项的层次结构
2. **图标选择**: 为每个导航项选择直观的图标
3. **位置安排**: 重要功能放在顶部，用户相关放在底部
4. **响应式设计**: 确保导航在不同窗口大小下正常工作
5. **状态管理**: 正确处理导航状态和页面切换
