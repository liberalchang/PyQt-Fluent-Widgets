ScrollBar 滚动条模块
====================

ScrollBar 模块提供滚动条控件，用于控制滚动区域的内容显示。支持平滑滚动和自定义样式。

主要功能
--------

- **平滑滚动** - 提供平滑的滚动动画
- **多种样式** - 支持不同的滚动条样式
- **自定义行为** - 支持自定义滚动行为
- **动画效果** - 提供流畅的滚动动画
- **主题适配** - 自动适应系统主题

核心组件
--------

ScrollBar
~~~~~~~~~

滚动条控件，提供基础的滚动功能。

**主要子类：**
- ``SmoothScrollBar`` - 平滑滚动条

SmoothScrollDelegate
~~~~~~~~~~~~~~~~~~

平滑滚动委托，用于实现平滑滚动效果。

使用示例
--------

基础滚动条使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.scroll_bar import ScrollBar
   
   # 创建滚动条
   scroll_bar = ScrollBar(Qt.Horizontal)
   scroll_bar.setRange(0, 100)
   scroll_bar.setValue(50)

注意事项
--------

1. **范围设置** - 正确设置滚动范围
2. **值更新** - 及时更新滚动位置
3. **样式定制** - 合理自定义滚动条样式

相关组件
--------

- :doc:`scroll_area` - 滚动区域控件
- :doc:`slider` - 滑块控件
