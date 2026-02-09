WindowStackedWidget 窗口堆叠控件模块
======================================

WindowStackedWidget 模块提供窗口级别的堆叠控件，用于窗口中多个页面的管理。支持页面切换和动画效果。

主要功能
--------

- **页面管理** - 管理窗口中的多个页面
- **切换动画** - 提供页面切换动画效果
- **窗口集成** - 专门为窗口环境设计
- **状态管理** - 提供页面状态管理功能
- **性能优化** - 针对窗口环境优化

核心组件
--------

StackedWidget
~~~~~~~~~~~~~

堆叠控件，提供基础的页面堆叠功能。

使用示例
--------

基础窗口堆叠控件使用：

.. code-block:: python

   from qfluentwidgets.window.stacked_widget import StackedWidget
   
   # 创建堆叠控件
   stacked_widget = StackedWidget()
   
   # 添加页面
   page1 = QWidget()
   page2 = QWidget()
   stacked_widget.addWidget(page1)
   stacked_widget.addWidget(page2)
   
   # 切换页面
   stacked_widget.setCurrentIndex(1)

注意事项
--------

1. **页面管理** - 正确管理页面索引
2. **切换逻辑** - 合理实现页面切换逻辑
3. **内存管理** - 注意页面资源的内存管理

相关组件
--------

- :doc:`fluent_window` - Fluent窗口控件
- :doc:`stacked_widget` - 堆叠控件
