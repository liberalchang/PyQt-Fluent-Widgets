导航组件 (Navigation)
====================

本节介绍 PySide6-Fluent-Widgets 中的导航相关组件。

Pivot
-----

透视导航控件，用于在不同视图间切换。

.. code-block:: python

   from qfluentwidgets import Pivot, PivotItem

   # 创建透视导航
   pivot = Pivot()
   
   # 添加页面
   pivot.addItem('首页')
   pivot.addItem('设置')
   pivot.addItem('关于')
   
   # 连接信号
   pivot.currentItemChanged.connect(lambda index: print(f'切换到: {index}'))

Segmented
---------

分段控件，用于在少量选项间切换。

.. code-block:: python

   from qfluentwidgets import SegmentedWidget

   segmented = SegmentedWidget()
   segmented.addItem('选项1')
   segmented.addItem('选项2')
   segmented.addItem('选项3')
   
   # 连接信号
   segmented.currentItemChanged.connect(lambda index: print(f'选择: {index}'))

Breadcrumb
----------

面包屑导航，显示当前页面的路径。

.. code-block:: python

   from qfluentwidgets import BreadcrumbBar, BreadcrumbItem

   breadcrumb = BreadcrumbBar()
   
   # 添加路径项
   breadcrumb.addItem(BreadcrumbItem('首页', 'home'))
   breadcrumb.addItem(BreadcrumbItem('设置', 'settings'))
   breadcrumb.addItem(BreadcrumbItem('显示', 'display'))
   
   # 连接信号
   breadcrumb.itemClicked.connect(lambda item: print(f'点击: {item.text}'))

TabBar
------

标签栏控件。

.. code-block:: python

   from qfluentwidgets import TabBar, TabItem

   tab_bar = TabBar()
   
   # 添加标签
   tab_bar.addTab('标签1')
   tab_bar.addTab('标签2')
   tab_bar.addTab('标签3')
   
   # 设置图标
   tab_bar.setTabIcon(0, FluentIcon.HOME)
   tab_bar.setTabIcon(1, FluentIcon.SETTING)
   
   # 连接信号
   tab_bar.currentChanged.connect(lambda index: print(f'切换到标签: {index}'))

NavigationInterface
-------------------

完整的导航界面组件，包含侧边栏和内容区域。

.. code-block:: python

   from qfluentwidgets import NavigationInterface, NavigationItemPosition
   from PySide6.QtWidgets import QStackedWidget

   # 创建导航界面
   navigation = NavigationInterface()
   
   # 创建内容区域
   stacked_widget = QStackedWidget()
   
   # 添加导航项
   navigation.addItem(
       routeKey='home',
       icon=FluentIcon.HOME,
       text='首页',
       widget=home_widget,
       position=NavigationItemPosition.TOP
   )
   
   navigation.addItem(
       routeKey='settings',
       icon=FluentIcon.SETTING,
       text='设置',
       widget=settings_widget,
       position=NavigationItemPosition.TOP
   )
   
   navigation.addItem(
       routeKey='about',
       icon=FluentIcon.INFO,
       text='关于',
       widget=about_widget,
       position=NavigationItemPosition.BOTTOM
   )
   
   # 连接信号
   navigation.currentItemChanged.connect(lambda key: print(f'导航到: {key}'))

NavigationWidget
----------------

导航项控件。

.. code-block:: python

   from qfluentwidgets import NavigationWidget, NavigationItemPosition

   nav_widget = NavigationWidget(
       icon=FluentIcon.DOCUMENT,
       text='文档',
       routeKey='docs'
   )
   
   # 设置位置
   nav_widget.setPosition(NavigationItemPosition.TOP)
   
   # 设置为可展开
   nav_widget.setExpand(True)

NavigationMenu
--------------

导航菜单。

.. code-block:: python

   from qfluentwidgets import NavigationMenu, NavigationMenuPushButton

   # 创建菜单
   menu = NavigationMenu('工具', FluentIcon.TOOLS)
   
   # 添加菜单项
   menu.addAction(NavigationMenuPushButton('计算器', FluentIcon.CALCULATOR))
   menu.addAction(NavigationMenuPushButton('记事本', FluentIcon.DOCUMENT))
   
   # 添加到导航界面
   navigation.addWidget(menu)

完整示例
--------

下面是一个完整的导航界面示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
   from qfluentwidgets import *

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 设置窗口属性
           self.setWindowTitle('导航示例')
           self.resize(800, 600)
           
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

       def add_navigation_items(self):
           """添加导航项"""
           # 首页
           self.navigation.addItem(
               routeKey='home',
               icon=FluentIcon.HOME,
               text='首页',
               widget=self.stacked_widget.widget(0)
           )
           
           # 设置
           self.navigation.addItem(
               routeKey='settings',
               icon=FluentIcon.SETTING,
               text='设置',
               widget=self.stacked_widget.widget(1)
           )
           
           # 关于
           self.navigation.addItem(
               routeKey='about',
               icon=FluentIcon.INFO,
               text='关于',
               widget=self.stacked_widget.widget(2),
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

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = MainWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **合理组织导航结构**: 将相关功能分组，使用菜单或子导航
2. **使用合适的图标**: 为每个导航项选择直观的图标
3. **保持导航简洁**: 避免过多的导航项导致界面混乱
4. **提供面包屑**: 在深层页面提供面包屑导航
5. **响应式设计**: 确保导航在不同窗口大小下都能正常工作

样式自定义
--------

可以通过 QSS 自定义导航组件样式：

.. code-block:: python

   # 自定义导航栏样式
   navigation.setStyleSheet("""
       NavigationInterface {
           background-color: #f3f3f3;
       }
       
       NavigationWidget {
           background-color: transparent;
           border: none;
           padding: 8px 12px;
           margin: 2px 4px;
           border-radius: 4px;
       }
       
       NavigationWidget:hover {
           background-color: #e1e1e1;
       }
       
       NavigationWidget:selected {
           background-color: #0078d4;
           color: white;
       }
   """)
