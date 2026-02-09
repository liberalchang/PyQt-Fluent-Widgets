Slider 滑块模块
================

Slider 模块提供滑块控件，用于数值选择和调节。支持多种样式和交互模式。

主要功能
--------

- **数值调节** - 提供直观的数值调节界面
- **多种样式** - 支持不同的滑块样式
- **工具提示** - 支持数值显示工具提示
- **点击交互** - 支持点击跳转到指定位置
- **动画效果** - 提供平滑的滑动动画

核心组件
--------

Slider
~~~~~~~

滑块控件，提供基础的数值调节功能。

**主要子类：**
- ``ClickableSlider`` - 可点击滑块
- ``ToolTipSlider`` - 带工具提示滑块

SliderHandle
~~~~~~~~~~~~

滑块手柄控件，用于拖拽操作。

使用示例
--------

基础滑块使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.slider import Slider
   
   # 创建滑块
   slider = Slider(Qt.Horizontal)
   slider.setRange(0, 100)
   slider.setValue(50)

注意事项
--------

1. **范围设置** - 正确设置滑块范围
2. **值更新** - 及时响应滑块值变化
3. **样式定制** - 合理自定义滑块样式

相关组件
--------

- :doc:`progress_bar` - 进度条控件
- :doc:`spin_box` - 数值输入框控件
