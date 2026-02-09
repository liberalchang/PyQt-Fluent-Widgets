TableView 表格视图模块
======================

TableView 模块提供表格视图控件，用于显示和管理表格数据。支持自定义委托和多种显示模式。

主要功能
--------

- **表格显示** - 提供标准的表格数据显示
- **自定义委托** - 支持自定义单元格显示
- **选择管理** - 提供灵活的行/列选择
- **排序过滤** - 支持数据排序和过滤
- **性能优化** - 针对大数据量优化

核心组件
--------

TableView
~~~~~~~~~~

表格视图控件，提供基础的表格显示功能。

使用示例
--------

基础表格视图使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.table_view import TableView
   from PySide6.QtCore import QStandardItemModel
   
   # 创建表格视图
   table_view = TableView()
   
   # 设置数据模型
   model = QStandardItemModel()
   table_view.setModel(model)

注意事项
--------

1. **模型选择** - 根据数据类型选择合适的模型
2. **委托定制** - 合理自定义单元格委托
3. **性能考虑** - 大量数据时注意性能优化

相关组件
--------

- :doc:`list_view` - 列表视图控件
- :doc:`scroll_bar` - 滚动条控件
