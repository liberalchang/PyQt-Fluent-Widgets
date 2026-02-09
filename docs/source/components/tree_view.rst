TreeView 树形视图模块
======================

TreeView 模块提供树形视图控件，用于显示和管理层次结构数据。支持展开/折叠和自定义委托。

主要功能
--------

- **层次显示** - 显示层次结构数据
- **展开折叠** - 支持节点的展开和折叠
- **自定义委托** - 支持自定义节点显示
- **选择管理** - 提供灵活的节点选择
- **性能优化** - 针对大数据量优化

核心组件
--------

TreeView
~~~~~~~~~

树形视图控件，提供基础的树形显示功能。

TreeWidget
~~~~~~~~~~~

树形控件，提供基础的树形管理功能。

TreeItemDelegate
~~~~~~~~~~~~~~~~

树形项委托，用于自定义树形项显示。

使用示例
--------

基础树形视图使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.tree_view import TreeWidget
   from PySide6.QtWidgets import QTreeWidgetItem
   
   # 创建树形控件
   tree_widget = TreeWidget()
   
   # 添加节点
   root_item = QTreeWidgetItem(["根节点"])
   child_item = QTreeWidgetItem(["子节点"])
   root_item.addChild(child_item)
   tree_widget.addTopLevelItem(root_item)

注意事项
--------

1. **层次结构** - 正确组织数据的层次结构
2. **展开状态** - 合理设置节点的展开状态
3. **性能考虑** - 大量节点时注意性能优化

相关组件
--------

- :doc:`list_view` - 列表视图控件
- :doc:`table_view` - 表格视图控件
