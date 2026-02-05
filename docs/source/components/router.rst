Router 路由管理模块
====================

Router 模块提供页面路由管理功能，支持多级页面导航、历史记录管理和状态保持。
该模块主要用于管理QStackedWidget的页面切换，提供类似Web应用的路由体验。

主要功能
--------

- **页面路由** - 管理页面之间的导航
- **历史记录** - 维护页面访问历史
- **状态保持** - 保持页面状态不丢失
- **多级导航** - 支持多个堆栈控件的路由
- **信号通知** - 路由状态变化信号

核心组件
--------

Router
~~~~~~

路由管理器，负责管理页面导航和历史记录。

.. code-block:: python

   from qfluentwidgets.common.router import Router, qrouter
   from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QPushButton
   from PySide6.QtCore import QObject
   
   # 创建路由器
   router = Router()
   
   # 使用全局路由器
   router = qrouter
   
   # 设置默认路由
   stacked_widget = QStackedWidget()
   router.setDefaultRouteKey(stacked_widget, "home")

**主要方法：**
- ``setDefaultRouteKey()`` - 设置默认路由键
- ``push()`` - 推入新的路由
- ``pop()`` - 弹出当前路由
- ``remove()`` - 移除指定路由

RouteItem
~~~~~~~~~~

路由项，表示一个路由记录。

.. code-block:: python

   from qfluentwidgets.common.router import RouteItem
   
   # 创建路由项
   route_item = RouteItem(stacked_widget, "page_key")
   
   # 比较路由项
   is_equal = route_item == other_route_item

StackedHistory
~~~~~~~~~~~~~~

堆栈历史记录，管理单个QStackedWidget的路由历史。

.. code-block:: python

   from qfluentwidgets.common.router import StackedHistory
   
   # 创建历史记录
   history = StackedHistory(stacked_widget)
   
   # 设置默认路由
   history.setDefaultRouteKey("home")
   
   # 推入路由
   history.push("settings")
   
   # 弹出路由
   history.pop()
   
   # 移除路由
   history.remove("settings")
   
   # 获取顶部路由
   top_route = history.top()

实际应用
--------

基本页面导航
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.router import qrouter
   from qfluentwidgets import NavigationInterface, NavigationItemPosition
   from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QLabel, QPushButton
   
   class MainWindow(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_router()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建堆栈控件
           self.stacked_widget = QStackedWidget()
           
           # 创建页面
           self.home_page = self.create_page("首页", "这是首页内容")
           self.settings_page = self.create_page("设置", "这是设置页面")
           self.about_page = self.create_page("关于", "这是关于页面")
           
           # 添加到堆栈控件
           self.stacked_widget.addWidget(self.home_page)
           self.stacked_widget.addWidget(self.settings_page)
           self.stacked_widget.addWidget(self.about_page)
           
           layout.addWidget(self.stacked_widget)
           self.setLayout(layout)
       
       def setup_router(self):
           """设置路由"""
           # 设置默认路由
           qrouter.setDefaultRouteKey(self.stacked_widget, "home")
           
           # 设置页面对象名称
           self.home_page.setObjectName("home")
           self.settings_page.setObjectName("settings")
           self.about_page.setObjectName("about")
       
       def create_page(self, title, content):
           """创建页面"""
           page = QWidget()
           layout = QVBoxLayout()
           
           label = QLabel(content)
           button = QPushButton(f"跳转到{title}")
           
           layout.addWidget(label)
           layout.addWidget(button)
           page.setLayout(layout)
           
           return page
   
   # 使用路由导航
   window = MainWindow()
   
   # 推入新路由
   qrouter.push(window.stacked_widget, "settings")
   qrouter.push(window.stacked_widget, "about")
   
   # 弹出路由
   qrouter.pop()

导航界面集成
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets import NavigationInterface, NavigationItemPosition, FluentIcon
   from qfluentwidgets.common.router import qrouter
   
   class NavigationWindow(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_navigation()
           self.setup_router()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建导航界面
           self.navigation = NavigationInterface(self, showMenuButton=True)
           
           # 创建堆栈控件
           self.stacked_widget = QStackedWidget()
           
           layout.addWidget(self.navigation)
           self.setLayout(layout)
       
       def setup_navigation(self):
           """设置导航"""
           # 添加导航项
           self.navigation.addItem(
               routeKey="home",
               icon=FluentIcon.HOME,
               text="首页",
               onClick=lambda: qrouter.push(self.stacked_widget, "home")
           )
           
           self.navigation.addItem(
               routeKey="settings",
               icon=FluentIcon.SETTING,
               text="设置",
               onClick=lambda: qrouter.push(self.stacked_widget, "settings")
           )
           
           self.navigation.addItem(
               routeKey="about",
               icon=FluentIcon.INFO,
               text="关于",
               onClick=lambda: qrouter.push(self.stacked_widget, "about")
           )
       
       def setup_router(self):
           """设置路由"""
           qrouter.setDefaultRouteKey(self.stacked_widget, "home")
           
           # 创建页面
           self.home_page = QWidget()
           self.home_page.setObjectName("home")
           
           self.settings_page = QWidget()
           self.settings_page.setObjectName("settings")
           
           self.about_page = QWidget()
           self.about_page.setObjectName("about")
           
           # 添加到堆栈控件
           self.stacked_widget.addWidget(self.home_page)
           self.stacked_widget.addWidget(self.settings_page)
           self.stacked_widget.addWidget(self.about_page)
           
           # 设置导航界面的堆栈控件
           self.navigation.stackedWidget = self.stacked_widget

多级页面管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.router import qrouter
   from PySide6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel
   
   class MultiLevelNavigation(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_router()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 主堆栈控件
           self.main_stacked = QStackedWidget()
           
           # 设置页面堆栈控件
           self.settings_stacked = QStackedWidget()
           
           # 创建主页面
           self.home_page = self.create_main_page("首页")
           self.settings_page = self.create_main_page("设置")
           
           # 创建设置子页面
           self.general_settings = self.create_settings_page("常规设置")
           self.advanced_settings = self.create_settings_page("高级设置")
           
           # 添加到主堆栈
           self.main_stacked.addWidget(self.home_page)
           self.main_stacked.addWidget(self.settings_page)
           
           # 添加到设置堆栈
           self.settings_stacked.addWidget(self.general_settings)
           self.settings_stacked.addWidget(self.advanced_settings)
           
           layout.addWidget(self.main_stacked)
           self.setLayout(layout)
       
       def setup_router(self):
           """设置路由"""
           # 设置默认路由
           qrouter.setDefaultRouteKey(self.main_stacked, "home")
           qrouter.setDefaultRouteKey(self.settings_stacked, "general")
           
           # 设置对象名称
           self.home_page.setObjectName("home")
           self.settings_page.setObjectName("settings")
           self.general_settings.setObjectName("general")
           self.advanced_settings.setObjectName("advanced")
       
       def create_main_page(self, title):
           """创建主页面"""
           page = QWidget()
           layout = QVBoxLayout()
           
           label = QLabel(f"{title}页面")
           button = QPushButton("进入设置")
           button.clicked.connect(lambda: qrouter.push(self.main_stacked, "settings"))
           
           layout.addWidget(label)
           layout.addWidget(button)
           page.setLayout(layout)
           
           return page
       
       def create_settings_page(self, title):
           """创建设置页面"""
           page = QWidget()
           layout = QVBoxLayout()
           
           label = QLabel(f"{title}")
           back_button = QPushButton("返回")
           back_button.clicked.connect(qrouter.pop)
           
           layout.addWidget(label)
           layout.addWidget(back_button)
           page.setLayout(layout)
           
           return page

路由状态管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.router import qrouter
   from PySide6.QtCore import QObject, Signal
   
   class RouteManager(QObject):
       """路由管理器"""
       
       routeChanged = Signal(str)  # 路由变化信号
       
       def __init__(self):
           super().__init__()
           self.setup_connections()
       
       def setup_connections(self):
           """设置连接"""
           qrouter.emptyChanged.connect(self.on_empty_changed)
       
       def on_empty_changed(self, is_empty):
           """路由空状态变化"""
           if is_empty:
               print("路由历史为空")
           else:
               print("路由历史不为空")
       
       def navigate_to(self, stacked_widget, route_key):
           """导航到指定路由"""
           qrouter.push(stacked_widget, route_key)
           self.routeChanged.emit(route_key)
       
       def go_back(self):
           """返回上一页"""
           qrouter.pop()
       
       def clear_history(self, route_key):
           """清除指定路由的历史"""
           qrouter.remove(route_key)
   
   # 使用路由管理器
   route_manager = RouteManager()
   
   # 导航
   route_manager.navigate_to(stacked_widget, "settings")

高级用法
--------

自定义路由行为
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.router import Router, StackedHistory
   from PySide6.QtWidgets import QStackedWidget
   
   class CustomRouter(Router):
       """自定义路由器"""
       
       def __init__(self):
           super().__init__()
           self.max_history = 10  # 最大历史记录数
       
       def push(self, stacked: QStackedWidget, routeKey: str):
           """重写push方法，限制历史记录数量"""
           # 检查历史记录数量
           if len(self.history) >= self.max_history:
               # 移除最旧的历史记录
               oldest_item = self.history[0]
               self.history.pop(0)
               if oldest_item.stacked in self.stackHistories:
                   self.stackHistories[oldest_item.stacked].remove(oldest_item.routeKey)
           
           # 调用父类方法
           super().push(stacked, routeKey)
   
   class CustomStackedHistory(StackedHistory):
       """自定义堆栈历史"""
       
       def __init__(self, stacked: QStackedWidget):
           super().__init__(stacked)
           self.max_size = 5  # 最大堆栈大小
       
       def push(self, routeKey: str):
           """重写push方法，限制堆栈大小"""
           if len(self.history) >= self.max_size:
               # 移除除了默认路由外的最旧记录
               if len(self.history) > 1:
                   self.history.pop(1)
           
           return super().push(routeKey)
   
   # 使用自定义路由器
   custom_router = CustomRouter()

路由守卫
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.router import qrouter
   from PySide6.QtWidgets import QMessageBox
   
   class RouteGuard:
       """路由守卫"""
       
       def __init__(self):
           self.protected_routes = {"admin", "settings"}
           self.user_permissions = ["user"]
       
       def can_navigate(self, route_key):
           """检查是否可以导航到指定路由"""
           if route_key in self.protected_routes:
               return "admin" in self.user_permissions
           return True
       
       def navigate_with_guard(self, stacked_widget, route_key):
           """带守卫的导航"""
           if self.can_navigate(route_key):
               qrouter.push(stacked_widget, route_key)
           else:
               QMessageBox.warning(None, "权限不足", "您没有访问该页面的权限")
   
   # 使用路由守卫
   guard = RouteGuard()
   
   # 尝试导航
   guard.navigate_with_guard(stacked_widget, "admin")  # 可能被阻止
   guard.navigate_with_guard(stacked_widget, "home")   # 允许

路由动画
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.router import qrouter
   from PySide6.QtWidgets import QStackedWidget, QPropertyAnimation
   from PySide6.QtCore import QEasingCurve, QRect
   
   class AnimatedStackedWidget(QStackedWidget):
       """带动画的堆栈控件"""
       
       def __init__(self):
           super().__init__()
           self.animation = QPropertyAnimation(self, b"geometry")
           self.animation.setEasingCurve(QEasingCurve.InOutQuad)
           self.animation.setDuration(300)
       
       def setCurrentWidget(self, widget, animated=True):
           """设置当前控件，支持动画"""
           if animated and self.currentWidget():
               # 执行动画切换
               self.animate_transition(widget)
           else:
               super().setCurrentWidget(widget)
       
       def animate_transition(self, new_widget):
           """执行切换动画"""
           current = self.currentWidget()
           if not current:
               super().setCurrentWidget(new_widget)
               return
           
           # 设置动画
           old_geometry = current.geometry()
           new_geometry = new_widget.geometry()
           
           # 移入动画
           new_widget.setGeometry(new_geometry.translated(self.width(), 0))
           super().setCurrentWidget(new_widget)
           
           self.animation.setTargetObject(new_widget)
           self.animation.setStartValue(new_geometry.translated(self.width(), 0))
           self.animation.setEndValue(new_geometry)
           self.animation.start()
   
   # 使用动画堆栈控件
   animated_stacked = AnimatedStackedWidget()
   qrouter.push(animated_stacked, "settings")

最佳实践
--------

1. **路由命名** - 使用有意义的路由键名
2. **状态管理** - 合理管理页面状态和历史
3. **权限控制** - 实现路由守卫保护敏感页面
4. **性能优化** - 避免过多的历史记录
5. **用户体验** - 提供清晰的导航反馈

注意事项
--------

- 路由键必须与页面的objectName一致
- 历史记录会占用内存，需要定期清理
- 多个QStackedWidget可以共享同一个路由器
- 路由变化会触发信号，可以用于UI更新

相关模块
--------

- :doc:`components.navigation` - 导航组件
- :doc:`components.widgets` - UI组件
- :doc:`common.signal_bus` - 信号总线
