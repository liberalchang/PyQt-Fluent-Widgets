TabView 标签视图模块
====================

TabView 模块提供标签视图控件，用于管理多个标签页面的显示和切换。支持标签关闭和自定义样式。

主要功能
--------

- **标签管理** - 管理多个标签页面的显示
- **标签关闭** - 支持标签页的关闭功能
- **切换动画** - 提供平滑的标签切换效果
- **样式定制** - 支持Fluent Design样式
- **布局灵活** - 支持多种标签布局模式

核心组件
--------

TabWidget
~~~~~~~~~~

标签控件，提供基础的标签页面管理功能。

TabBar
~~~~~~~

标签栏控件，用于显示和管理标签。

TabItem
~~~~~~~~

标签项控件，表示单个标签页。

使用示例
--------

基础标签视图使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.tab_view import TabWidget
   
   # 创建标签控件
   tab_widget = TabWidget()
   
   # 添加标签页
   tab1 = QWidget()
   tab2 = QWidget()
   tab_widget.addTab(tab1, "标签1")
   tab_widget.addTab(tab2, "标签2")

注意事项
--------

1. **标签管理** - 正确管理标签页索引
2. **关闭策略** - 合理设置标签关闭策略
3. **样式定制** - 适当自定义标签样式

相关组件
--------

- :doc:`stacked_widget` - 堆叠控件
- :doc:`button` - 按钮控件
