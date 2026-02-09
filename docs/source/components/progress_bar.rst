ProgressBar 进度条模块
====================

ProgressBar 模块提供进度条控件，用于显示操作进度。支持确定和不确定进度模式。

主要功能
--------

- **进度显示** - 显示操作进度
- **多种模式** - 支持确定和不确定进度
- **样式定制** - 提供Fluent Design样式
- **动画效果** - 支持平滑的进度动画
- **状态指示** - 支持不同状态的进度显示

核心组件
--------

ProgressBar
~~~~~~~~~~~

进度条控件，提供基础的进度显示功能。

IndeterminateProgressBar
~~~~~~~~~~~~~~~~~~~~~~~

不确定进度条，用于显示未知时长的操作进度。

使用示例
--------

基础进度条使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.progress_bar import ProgressBar
   
   # 创建进度条
   progress_bar = ProgressBar()
   progress_bar.setRange(0, 100)
   progress_bar.setValue(30)

注意事项
--------

1. **进度范围** - 正确设置进度范围
2. **进度更新** - 及时更新进度值
3. **模式选择** - 根据操作类型选择合适的进度模式

相关组件
--------

- :doc:`progress_ring` - 环形进度条
- :doc:`button` - 按钮控件
