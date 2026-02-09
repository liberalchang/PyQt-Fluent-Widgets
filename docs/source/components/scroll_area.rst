ScrollArea 滚动区域模块
========================

ScrollArea 模块提供滚动区域控件，用于显示超出显示区域的内容。支持平滑滚动和多种滚动模式。

主要功能
--------

- **平滑滚动** - 提供平滑的滚动效果
- **多种模式** - 支持单方向和全方向滚动
- **自定义滚动** - 支持自定义滚动行为
- **性能优化** - 针对大数据量优化
- **样式定制** - 提供Fluent Design样式

核心组件
--------

ScrollArea
~~~~~~~~~~

滚动区域控件，提供基础的滚动功能。

**主要子类：**
- ``SingleDirectionScrollArea`` - 单方向滚动区域
- ``SmoothScrollArea`` - 平滑滚动区域

使用示例
--------

基础滚动区域使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.scroll_area import ScrollArea
   
   # 创建滚动区域
   scroll_area = ScrollArea()
   
   # 设置内容控件
   content_widget = QWidget()
   scroll_area.setWidget(content_widget)

注意事项
--------

1. **内容设置** - 正确设置内容控件
2. **滚动策略** - 根据需求选择合适的滚动策略
3. **性能考虑** - 大量内容时注意性能优化

相关组件
--------

- :doc:`scroll_bar` - 滚动条控件
- :doc:`button` - 按钮控件
