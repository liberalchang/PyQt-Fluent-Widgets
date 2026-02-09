ModelComboBox 模型组合框模块
=============================

ModelComboBox 模块提供基于数据模型的组合框控件，支持复杂数据绑定和自定义显示。

主要功能
--------

- **数据绑定** - 支持数据模型绑定
- **自定义显示** - 支持自定义项显示
- **编辑功能** - 支持可编辑模式
- **搜索过滤** - 支持搜索和过滤功能
- **性能优化** - 针对大数据量优化

核心组件
--------

ModelComboBox
~~~~~~~~~~~~

模型组合框控件，提供基础的模型绑定功能。

ModelComboBoxBase
~~~~~~~~~~~~~~~~

模型组合框基类，提供基础的模型功能。

EditableModelComboBox
~~~~~~~~~~~~~~~~~~~~

可编辑模型组合框，支持用户输入和编辑。

使用示例
--------

基础模型组合框使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.model_combo_box import ModelComboBox
   from PySide6.QtCore import QStringListModel
   
   # 创建模型组合框
   combo = ModelComboBox()
   
   # 设置数据模型
   model = QStringListModel(["选项1", "选项2", "选项3"])
   combo.setModel(model)

注意事项
--------

1. **模型选择** - 根据数据类型选择合适的模型
2. **显示定制** - 合理自定义项的显示方式
3. **性能考虑** - 大量数据时注意性能优化

相关组件
--------

- :doc:`combo_box` - 组合框控件
- :doc:`line_edit` - 行编辑控件
