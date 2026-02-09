StateToolTip 状态工具提示模块
=============================

StateToolTip 模块提供状态工具提示控件，用于显示状态信息和操作提示。支持自动关闭和自定义样式。

主要功能
--------

- **状态显示** - 显示操作状态和结果
- **自动关闭** - 支持自动定时关闭
- **关闭按钮** - 提供手动关闭功能
- **样式定制** - 支持Fluent Design样式
- **位置管理** - 智能的位置计算和显示

核心组件
--------

StateToolTip
~~~~~~~~~~~~

状态工具提示控件，提供基础的状态提示功能。

StateCloseButton
~~~~~~~~~~~~~~~~

状态关闭按钮控件，用于关闭状态提示。

使用示例
--------

基础状态工具提示使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.state_tool_tip import StateToolTip
   
   # 创建状态提示
   tip = StateToolTip("成功", "操作已完成", parent=self)
   tip.show()

注意事项
--------

1. **内容简洁** - 保持提示内容简洁明了
2. **显示时长** - 合理设置自动关闭时间
3. **位置选择** - 选择合适的显示位置

相关组件
--------

- :doc:`tool_tip` - 工具提示控件
- :doc:`flyout` - 弹出控件
