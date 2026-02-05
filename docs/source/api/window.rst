Window 模块 API
================

Window 模块提供应用窗口和框架组件，用于构建现代化的桌面应用界面。
这些窗口组件集成了 Fluent Design 的设计语言，提供一致的用户体验。

主要功能：
- Fluent 风格主窗口
- 带侧边抽屉的窗口
- 应用启动画面
- 窗口堆叠管理
- 标题栏集成

使用方法：
.. code-block:: python

   from qfluentwidgets import FluentWindow, NavigationInterface, NavigationItemPosition
   
   # 创建主窗口
   window = FluentWindow()
   
   # 添加导航界面
   navigation = NavigationInterface(window, True)
   
   # 添加导航项
   navigation.addItem(
       routeKey='home',
       icon=FluentIcon.HOME,
       text='主页',
       onClick=lambda: print('主页点击')
   )

.. automodule:: qfluentwidgets.window
   :members:
   :undoc-members:
   :show-inheritance:

FluentWindow
------------

Fluent 风格主窗口，提供现代化的应用窗口框架。

主要功能：
- 集成标题栏、菜单栏、工具栏
- 支持窗口状态管理
- 自适应主题变化
- 内置窗口动画效果

适用于构建桌面应用的主窗口。

.. automodule:: qfluentwidgets.window.fluent_window
   :members:
   :undoc-members:
   :show-inheritance:

DrawerWindow
------------

带侧边抽屉的窗口，提供侧边栏导航功能。

主要功能：
- 可折叠的侧边抽屉
- 平滑的抽屉动画
- 自定义抽屉内容
- 响应式布局

适用于需要侧边导航的应用。

.. automodule:: qfluentwidgets.window.drawer_window
   :members:
   :undoc-members:
   :show-inheritance:

SplashScreen
-------------

应用启动画面，提供专业的启动体验。

主要功能：
- 自定义启动画面内容
- 进度显示支持
- 自动关闭功能
- 动画效果

提升应用启动时的用户体验。

.. automodule:: qfluentwidgets.window.splash_screen
   :members:
   :undoc-members:
   :show-inheritance:

StackedWidget
--------------

窗口堆叠管理器，提供多页面管理功能。

主要功能：
- 页面堆叠和切换
- 平滑的页面切换动画
- 页面历史管理
- 自定义切换效果

适用于管理多个页面或视图。

.. automodule:: qfluentwidgets.window.stacked_widget
   :members:
   :undoc-members:
   :show-inheritance:
