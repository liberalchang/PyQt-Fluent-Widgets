SplashScreen 启动画面模块
==========================

SplashScreen 模块提供启动画面控件，用于应用程序启动时的加载界面。支持动画效果和进度显示。

主要功能
--------

- **启动显示** - 提供应用程序启动时的加载界面
- **动画效果** - 支持加载动画和过渡效果
- **进度显示** - 支持加载进度的显示
- **自定义内容** - 支持自定义启动画面内容
- **自动关闭** - 支持主窗口显示时自动关闭

核心组件
--------

SplashScreen
~~~~~~~~~~~~

启动画面控件，提供基础的启动画面功能。

使用示例
--------

基础启动画面使用：

.. code-block:: python

   from qfluentwidgets.window.splash_screen import SplashScreen
   
   # 创建启动画面
   splash = SplashScreen()
   splash.show()
   
   # 模拟加载过程
   for i in range(101):
       splash.setProgress(i)
       QApplication.processEvents()
       time.sleep(0.01)
   
   # 显示主窗口
   main_window = MainWindow()
   main_window.show()
   splash.finish()

注意事项
--------

1. **加载时间** - 控制启动画面的显示时间
2. **进度更新** - 及时更新加载进度
3. **资源管理** - 注意启动画面资源的内存管理

相关组件
--------

- :doc:`fluent_window` - Fluent窗口控件
- :doc:`progress_bar` - 进度条控件
