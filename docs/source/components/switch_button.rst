SwitchButton 开关按钮模块
========================

SwitchButton 模块提供开关按钮控件，用于二值状态的切换。支持多种样式和位置配置。

主要功能
--------

- **状态切换** - 提供直观的开关状态切换
- **多种样式** - 支持不同的开关样式
- **位置配置** - 支持指示器位置配置
- **动画效果** - 提供平滑的切换动画
- **主题适配** - 自动适应系统主题

核心组件
--------

SwitchButton
~~~~~~~~~~~~

开关按钮控件，提供基础的开关功能。

Indicator
~~~~~~~~~~~

指示器控件，用于显示开关状态。

IndicatorPosition
~~~~~~~~~~~~~~~~~

指示器位置枚举，定义指示器的显示位置。

使用示例
--------

基础开关按钮使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.switch_button import SwitchButton
   
   # 创建开关按钮
   switch = SwitchButton()
   switch.setChecked(True)
   
   # 连接信号
   switch.checkedChanged.connect(self.on_switch_changed)

注意事项
--------

1. **状态管理** - 正确管理开关状态
2. **信号连接** - 及时响应状态变化
3. **样式定制** - 合理自定义开关样式

相关组件
--------

- :doc:`button` - 按钮控件
- :doc:`check_box` - 复选框控件
