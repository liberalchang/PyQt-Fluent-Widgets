FluentWindow Fluent窗口模块
==========================

FluentWindow 模块提供Fluent Design风格的窗口控件。支持多种窗口样式和标题栏配置。

主要功能
--------

- **Fluent样式** - 提供完整的Fluent Design样式
- **多种窗口** - 支持标准和分割窗口样式
- **标题栏定制** - 支持自定义标题栏
- **主题支持** - 自动适应系统主题
- **窗口管理** - 提供完整的窗口管理功能

核心组件
--------

FluentWindow
~~~~~~~~~~~~

Fluent窗口控件，提供基础的Fluent窗口功能。

**主要子类：**
- ``MSFluentWindow`` - Microsoft风格Fluent窗口
- ``SplitFluentWindow`` - 分割式Fluent窗口
- ``TopNavigationFluentWindow`` - 顶部导航Fluent窗口

FluentTitleBar
~~~~~~~~~~~~~~~~

Fluent标题栏控件，提供Fluent风格的标题栏。

使用示例
--------

基础Fluent窗口使用：

.. code-block:: python

   from qfluentwidgets.window.fluent_window import FluentWindow
   
   # 创建Fluent窗口
   window = FluentWindow()
   
   # 设置中心控件
   central_widget = QWidget()
   window.setCentralWidget(central_widget)
   
   window.show()

注意事项
--------

1. **窗口样式** - 根据应用选择合适的窗口样式
2. **标题栏配置** - 合理配置标题栏功能
3. **主题适配** - 确保窗口正确适应系统主题

相关组件
--------

- :doc:`drawer_window` - 抽屉窗口控件
- :doc:`frameless_window` - 无边框窗口控件
