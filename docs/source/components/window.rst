窗口组件 (Window)
==================

本节介绍 PySide6-Fluent-Widgets 中的窗口相关组件。

FluentWindow
-----------

Fluent 风格的主窗口组件，提供现代化的窗口界面。

.. code-block:: python

   from qfluentwidgets import FluentWindow, NavigationItemPosition, FluentIcon

   class MainWindow(FluentWindow):
       def __init__(self):
           super().__init__()
           
           # 设置窗口属性
           self.setWindowTitle('Fluent Window 示例')
           self.resize(800, 600)
           
           # 添加导航项
           self.add_navigation_items()

       def add_navigation_items(self):
           """添加导航项"""
           # 首页
           self.navigationInterface.addItem(
               routeKey='home',
               icon=FluentIcon.HOME,
               text='首页',
               widget=self.create_home_widget(),
               position=NavigationItemPosition.TOP
           )
           
           # 设置
           self.navigationInterface.addItem(
               routeKey='settings',
               icon=FluentIcon.SETTING,
               text='设置',
               widget=self.create_settings_widget(),
               position=NavigationItemPosition.TOP
           )

       def create_home_widget(self):
           """创建首页组件"""
           from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
           
           widget = QWidget()
           layout = QVBoxLayout(widget)
           layout.addWidget(QLabel('欢迎使用 Fluent Window'))
           return widget

       def create_settings_widget(self):
           """创建设置组件"""
           from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
           
           widget = QWidget()
           layout = QVBoxLayout(widget)
           layout.addWidget(QLabel('设置页面'))
           return widget

DrawerWindow
------------

抽屉窗口组件，支持从四个方向滑出的抽屉面板。

.. code-block:: python

   from qfluentwidgets import DrawerWindow
   from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 创建抽屉窗口
           self.drawer_window = DrawerWindow(self)
           
           # 创建主界面
           self.setup_ui()

       def setup_ui(self):
           """设置主界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 添加按钮来触发抽屉
           left_btn = QPushButton('显示左侧抽屉')
           right_btn = QPushButton('显示右侧抽屉')
           top_btn = QPushButton('显示顶部抽屉')
           bottom_btn = QPushButton('显示底部抽屉')
           
           layout.addWidget(left_btn)
           layout.addWidget(right_btn)
           layout.addWidget(top_btn)
           layout.addWidget(bottom_btn)
           
           # 连接信号
           left_btn.clicked.connect(lambda: self.show_drawer('left'))
           right_btn.clicked.connect(lambda: self.show_drawer('right'))
           top_btn.clicked.connect(lambda: self.show_drawer('top'))
           bottom_btn.clicked.connect(lambda: self.show_drawer('bottom'))

       def show_drawer(self, direction):
           """显示抽屉"""
           # 创建抽屉内容
           content = QWidget()
           content_layout = QVBoxLayout(content)
           content_layout.addWidget(QLabel(f'{direction} 抽屉内容'))
           
           # 添加关闭按钮
           close_btn = QPushButton('关闭')
           close_btn.clicked.connect(self.drawer_window.hide_drawer)
           content_layout.addWidget(close_btn)
           
           # 显示抽屉
           self.drawer_window.show_drawer(
               direction=direction,
               content=content,
               size=300
           )

Drawer
------

抽屉组件，可以从四个方向滑出。

.. code-block:: python

   from qfluentwidgets import Drawer
   from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 创建抽屉
           self.left_drawer = Drawer(self, "left")
           self.right_drawer = Drawer(self, "right")
           
           # 设置抽屉内容
           self.setup_drawers()
           
           # 创建主界面
           self.setup_ui()

       def setup_drawers(self):
           """设置抽屉内容"""
           # 左侧抽屉内容
           left_content = QWidget()
           left_layout = QVBoxLayout(left_content)
           left_layout.addWidget(QLabel('左侧抽屉'))
           
           close_left_btn = QPushButton('关闭左侧抽屉')
           close_left_btn.clicked.connect(self.left_drawer.hide_drawer)
           left_layout.addWidget(close_left_btn)
           
           self.left_drawer.content_layout.addWidget(left_content)
           
           # 右侧抽屉内容
           right_content = QWidget()
           right_layout = QVBoxLayout(right_content)
           right_layout.addWidget(QLabel('右侧抽屉'))
           
           close_right_btn = QPushButton('关闭右侧抽屉')
           close_right_btn.clicked.connect(self.right_drawer.hide_drawer)
           right_layout.addWidget(close_right_btn)
           
           self.right_drawer.content_layout.addWidget(right_content)

       def setup_ui(self):
           """设置主界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 添加按钮来触发抽屉
           left_btn = QPushButton('显示左侧抽屉')
           right_btn = QPushButton('显示右侧抽屉')
           
           layout.addWidget(left_btn)
           layout.addWidget(right_btn)
           
           # 连接信号
           left_btn.clicked.connect(lambda: self.left_drawer.show_drawer(300))
           right_btn.clicked.connect(lambda: self.right_drawer.show_drawer(300))

SplashScreen
-------------

启动画面组件，用于应用程序启动时显示。

.. code-block:: python

   from qfluentwidgets import SplashScreen
   from PySide6.QtCore import QTimer

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 创建启动画面
           self.splash = SplashScreen(self)
           self.splash.setIcon(FluentIcon.ROBOT)
           self.splash.setTitle('应用程序名称')
           self.splash.setContent('正在启动...')
           
           # 显示启动画面
           self.splash.show()
           
           # 模拟加载过程
           QTimer.singleShot(2000, self.on_loading_finished)

       def on_loading_finished(self):
           """加载完成"""
           self.splash.close()
           
           # 显示主窗口
           self.setWindowTitle('主窗口')
           self.resize(800, 600)
           self.show()

StackedWidget
-------------

堆叠窗口组件，用于管理多个页面的切换。

.. code-block:: python

   from qfluentwidgets import StackedWidget
   from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel, QPushButton

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 创建堆叠窗口
           self.stacked_widget = StackedWidget()
           
           # 添加页面
           self.setup_pages()
           
           # 设置主界面
           self.setup_ui()

       def setup_pages(self):
           """设置页面"""
           # 页面1
           page1 = QWidget()
           layout1 = QVBoxLayout(page1)
           layout1.addWidget(QLabel('页面 1'))
           self.stacked_widget.addWidget(page1)
           
           # 页面2
           page2 = QWidget()
           layout2 = QVBoxLayout(page2)
           layout2.addWidget(QLabel('页面 2'))
           self.stacked_widget.addWidget(page2)
           
           # 页面3
           page3 = QWidget()
           layout3 = QVBoxLayout(page3)
           layout3.addWidget(QLabel('页面 3'))
           self.stacked_widget.addWidget(page3)

       def setup_ui(self):
           """设置主界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 添加切换按钮
           btn1 = QPushButton('页面 1')
           btn2 = QPushButton('页面 2')
           btn3 = QPushButton('页面 3')
           
           layout.addWidget(btn1)
           layout.addWidget(btn2)
           layout.addWidget(btn3)
           layout.addWidget(self.stacked_widget)
           
           # 连接信号
           btn1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
           btn2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
           btn3.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

完整示例
--------

下面是一个完整的窗口组件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
   from qfluentwidgets import *

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 设置窗口属性
           self.setWindowTitle('窗口组件示例')
           self.resize(800, 600)
           
           # 创建抽屉窗口
           self.drawer_window = DrawerWindow(self)
           
           # 创建主界面
           self.setup_ui()

       def setup_ui(self):
           """设置主界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 添加标题
           title = SubtitleLabel('窗口组件示例')
           layout.addWidget(title)
           
           # 抽屉窗口示例
           drawer_btn = PrimaryPushButton('显示抽屉窗口')
           drawer_btn.clicked.connect(self.show_drawer_window)
           layout.addWidget(drawer_btn)
           
           # Fluent Window 示例按钮
           fluent_btn = PrimaryPushButton('打开 Fluent Window')
           fluent_btn.clicked.connect(self.open_fluent_window)
           layout.addWidget(fluent_btn)

       def show_drawer_window(self):
           """显示抽屉窗口"""
           # 创建抽屉内容
           content = QWidget()
           content_layout = QVBoxLayout(content)
           content_layout.addWidget(QLabel('这是抽屉窗口的内容'))
           
           # 添加一些控件
           btn = QPushButton('测试按钮')
           content_layout.addWidget(btn)
           
           # 显示抽屉
           self.drawer_window.show_drawer(
               direction='right',
               content=content,
               size=350
           )

       def open_fluent_window(self):
           """打开 Fluent Window"""
           fluent_window = MyFluentWindow()
           fluent_window.show()

   class MyFluentWindow(FluentWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('Fluent Window 示例')
           self.resize(600, 400)
           
           # 添加导航项
           self.add_navigation_items()

       def add_navigation_items(self):
           """添加导航项"""
           # 首页
           home_widget = QWidget()
           home_layout = QVBoxLayout(home_widget)
           home_layout.addWidget(QLabel('这是首页'))
           self.navigationInterface.addItem(
               routeKey='home',
               icon=FluentIcon.HOME,
               text='首页',
               widget=home_widget,
               position=NavigationItemPosition.TOP
           )
           
           # 设置
           settings_widget = QWidget()
           settings_layout = QVBoxLayout(settings_widget)
           settings_layout.addWidget(QLabel('这是设置页面'))
           self.navigationInterface.addItem(
               routeKey='settings',
               icon=FluentIcon.SETTING,
               text='设置',
               widget=settings_widget,
               position=NavigationItemPosition.TOP
           )

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = MainWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **选择合适的窗口类型**: 
   - 使用 FluentWindow 作为主窗口
   - 使用 DrawerWindow 作为辅助面板
   - 使用 SplashScreen 作为启动画面

2. **合理设置抽屉方向**: 
   - 左侧抽屉适合导航菜单
   - 右侧抽屉适合设置面板
   - 顶部抽屉适合工具栏
   - 底部抽屉适合状态信息

3. **优化用户体验**: 
   - 提供清晰的关闭按钮
   - 设置合适的动画时长
   - 避免同时显示多个抽屉

4. **响应式设计**: 
   - 根据窗口大小调整抽屉尺寸
   - 在小屏幕上使用全屏抽屉

样式自定义
--------

可以通过 QSS 自定义窗口组件样式：

.. code-block:: python

   # 自定义抽屉样式
   drawer.setStyleSheet("""
       Drawer {
           background-color: white;
           border: 1px solid #e1e1e1;
           border-radius: 8px;
       }
       
       Drawer QLabel#title_label {
           color: #0078d4;
           font-size: 16px;
           font-weight: bold;
       }
   """)
   
   # 自定义 Fluent Window 样式
   fluent_window.setStyleSheet("""
       FluentWindow {
           background-color: #f3f3f3;
       }
       
       NavigationWidget {
           background-color: white;
           border: none;
       }
   """)
