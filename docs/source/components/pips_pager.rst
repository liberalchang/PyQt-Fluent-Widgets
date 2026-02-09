PipsPager 分页指示器模块
========================

PipsPager 模块提供分页指示器控件，用于显示页面位置和导航。支持水平和垂直方向的分页指示。

主要功能
--------

- **分页指示** - 显示当前页面位置
- **导航功能** - 支持页面导航
- **多种样式** - 支持不同的指示器样式
- **方向支持** - 支持水平和垂直方向
- **动画效果** - 提供平滑的切换动画

核心组件
--------

PipsPager
~~~~~~~~~

分页指示器控件，提供基础的分页功能。

**主要子类：**
- ``HorizontalPipsPager`` - 水平分页指示器
- ``VerticalPipsPager`` - 垂直分页指示器

ScrollButton
~~~~~~~~~~~~

滚动按钮控件，用于页面导航。

PipsDelegate
~~~~~~~~~~~~

分页委托，用于自定义指示器显示。

使用示例
--------

基础分页指示器使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.pips_pager import PipsPager
   
   # 创建分页指示器
   pager = PipsPager()
   pager.setPageCount(5)
   pager.setCurrentPage(0)

注意事项
--------

1. **页面数量** - 正确设置页面总数
2. **当前页面** - 及时更新当前页面索引
3. **方向选择** - 根据布局选择合适的方向

相关组件
--------

- :doc:`button` - 按钮控件
- :doc:`scroll_bar` - 滚动条控件
