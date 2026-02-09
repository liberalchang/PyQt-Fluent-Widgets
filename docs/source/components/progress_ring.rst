ProgressRing 环形进度条模块
==========================

ProgressRing 模块提供环形进度条控件，用于显示操作进度。支持确定和不确定进度模式。

主要功能
--------

- **环形显示** - 环形进度显示
- **多种模式** - 支持确定和不确定进度
- **样式定制** - 提供Fluent Design样式
- **动画效果** - 支持平滑的旋转动画
- **状态指示** - 支持不同状态的进度显示

核心组件
--------

ProgressRing
~~~~~~~~~~~

环形进度条控件，提供基础的环形进度显示功能。

使用示例
--------

基础环形进度条使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.progress_ring import ProgressRing
   
   # 创建环形进度条
   progress_ring = ProgressRing()
   progress_ring.setRange(0, 100)
   progress_ring.setValue(50)

注意事项
--------

1. **进度范围** - 正确设置进度范围
2. **进度更新** - 及时更新进度值
3. **尺寸设置** - 合理设置环形进度条尺寸

相关组件
--------

- :doc:`progress_bar` - 进度条
- :doc:`button` - 按钮控件
