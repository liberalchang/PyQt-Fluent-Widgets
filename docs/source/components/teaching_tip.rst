TeachingTip 教学提示模块
========================

TeachingTip 模块提供教学提示控件，用于引导用户了解界面功能。支持多种位置和动画效果。

主要功能
--------

- **教学引导** - 提供功能介绍和使用指导
- **多种位置** - 支持多种提示位置配置
- **动画效果** - 提供流畅的显示/隐藏动画
- **自定义内容** - 支持文本和图像内容
- **位置管理** - 智能的位置计算和调整

核心组件
--------

TeachingTip
~~~~~~~~~~~

教学提示控件，提供基础的教学提示功能。

TeachingTipManager
~~~~~~~~~~~~~~~~~

教学提示管理器，处理位置和显示逻辑。

使用示例
--------

基础教学提示使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.teaching_tip import TeachingTip
   
   # 创建教学提示
   tip = TeachingTip("标题", "这是功能说明", target_widget, parent=self)
   tip.show()

注意事项
--------

1. **内容简洁** - 保持教学提示简洁明了
2. **位置选择** - 选择合适的提示位置
3. **显示时机** - 在合适的时机显示提示

相关组件
--------

- :doc:`tool_tip` - 工具提示控件
- :doc:`flyout` - 弹出控件
