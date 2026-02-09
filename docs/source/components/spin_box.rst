SpinBox 数值输入框模块
========================

SpinBox 模块提供数值输入框控件，用于数值的精确输入。支持多种数值类型和格式。

主要功能
--------

- **数值输入** - 提供精确的数值输入功能
- **多种类型** - 支持整数、浮点数、日期时间等
- **步进调节** - 支持按钮步进调节
- **格式化显示** - 支持多种数值格式
- **验证功能** - 内置数值验证机制

核心组件
--------

SpinBox
~~~~~~~

数值输入框控件，提供基础的数值输入功能。

**主要子类：**
- ``CompactSpinBox`` - 紧凑型数值输入框
- ``DoubleSpinBox`` - 浮点数输入框
- ``CompactDoubleSpinBox`` - 紧凑型浮点数输入框
- ``TimeEdit`` - 时间输入框
- ``DateEdit`` - 日期输入框
- ``DateTimeEdit`` - 日期时间输入框

使用示例
--------

基础数值输入框使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.spin_box import SpinBox, DoubleSpinBox
   
   # 创建整数输入框
   spin_box = SpinBox()
   spin_box.setRange(0, 100)
   spin_box.setValue(50)
   
   # 创建浮点数输入框
   double_spin = DoubleSpinBox()
   double_spin.setRange(0.0, 100.0)
   double_spin.setValue(50.0)

注意事项
--------

1. **范围设置** - 正确设置输入范围
2. **步进值** - 合理设置步进值
3. **数值类型** - 根据需求选择合适的数值类型

相关组件
--------

- :doc:`slider` - 滑块控件
- :doc:`line_edit` - 行编辑控件
