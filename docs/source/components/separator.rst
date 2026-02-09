Separator 分隔符模块
====================

Separator 模块提供分隔符控件，用于在界面中创建视觉分隔。支持水平和垂直方向的分隔符。

主要功能
--------

- **视觉分隔** - 提供清晰的视觉分隔效果
- **多种方向** - 支持水平和垂直分隔符
- **样式定制** - 提供Fluent Design样式
- **主题适配** - 自动适应系统主题
- **尺寸自适应** - 根据布局自动调整尺寸

核心组件
--------

HorizontalSeparator
~~~~~~~~~~~~~~~~~~

水平分隔符控件，用于创建水平分隔线。

VerticalSeparator
~~~~~~~~~~~~~~~~

垂直分隔符控件，用于创建垂直分隔线。

使用示例
--------

基础分隔符使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.separator import HorizontalSeparator, VerticalSeparator
   
   # 创建水平分隔符
   h_separator = HorizontalSeparator()
   h_separator.setFixedHeight(1)
   
   # 创建垂直分隔符
   v_separator = VerticalSeparator()
   v_separator.setFixedWidth(1)

注意事项
--------

1. **方向选择** - 根据布局选择合适的分隔符方向
2. **尺寸设置** - 合理设置分隔符尺寸
3. **布局使用** - 在布局中正确使用分隔符

相关组件
--------

- :doc:`button` - 按钮控件
- :doc:`label` - 标签控件
