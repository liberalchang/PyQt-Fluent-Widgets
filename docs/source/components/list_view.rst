ListView 列表视图模块
====================

ListView 模块提供列表视图控件，用于显示和管理列表数据。支持自定义委托和多种显示模式。

主要功能
--------

- **自定义委托** - 支持自定义列表项委托
- **多种模式** - 支持列表和视图模式
- **选择管理** - 提供灵活的选择机制
- **样式定制** - 支持Fluent Design样式
- **性能优化** - 针对大数据量优化

核心组件
--------

ListWidget
~~~~~~~~~~

列表控件，提供基础的列表显示功能。

ListView
~~~~~~~~~

列表视图控件，提供更高级的列表功能。

ListItemDelegate
~~~~~~~~~~~~~~~~

列表项委托，用于自定义列表项的显示。

ListBase
~~~~~~~~~

列表基类，提供基础的列表功能。

使用示例
--------

基础列表使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.list_view import ListWidget
   
   # 创建列表控件
   list_widget = ListWidget()
   
   # 添加项目
   items = ["项目1", "项目2", "项目3"]
   list_widget.addItems(items)

注意事项
--------

1. **委托选择** - 根据需求选择合适的委托
2. **性能考虑** - 大量数据时注意性能优化
3. **样式定制** - 合理自定义列表项样式

相关组件
--------

- :doc:`scroll_bar` - 滚动条控件
- :doc:`button` - 按钮控件
