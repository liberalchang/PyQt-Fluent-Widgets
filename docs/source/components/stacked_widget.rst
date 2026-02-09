StackedWidget 堆叠控件模块
==========================

StackedWidget 模块提供堆叠控件，用于管理多个页面的切换显示。支持多种切换动画效果。

主要功能
--------

- **页面管理** - 管理多个页面的显示和切换
- **切换动画** - 提供多种页面切换动画
- **透明度动画** - 支持透明度渐变效果
- **弹出动画** - 支持弹出式切换效果
- **过渡效果** - 提供流畅的页面过渡

核心组件
--------

TransitionStackedWidget
~~~~~~~~~~~~~~~~~~~~~

过渡堆叠控件，提供基础的页面切换功能。

**主要子类：**
- ``OpacityAniStackedWidget`` - 透明度动画堆叠控件
- ``PopUpAniStackedWidget`` - 弹出动画堆叠控件
- ``EntranceTransitionStackedWidget`` - 入场过渡堆叠控件
- ``DrillInTransitionStackedWidget`` - 钻入过渡堆叠控件

使用示例
--------

基础堆叠控件使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.stacked_widget import TransitionStackedWidget
   
   # 创建堆叠控件
   stacked_widget = TransitionStackedWidget()
   
   # 添加页面
   page1 = QWidget()
   page2 = QWidget()
   stacked_widget.addWidget(page1)
   stacked_widget.addWidget(page2)
   
   # 切换页面
   stacked_widget.setCurrentIndex(1)

注意事项
--------

1. **页面管理** - 正确管理页面索引
2. **动画选择** - 选择合适的切换动画
3. **性能考虑** - 大量页面时注意性能优化

相关组件
--------

- :doc:`tab_view` - 标签视图控件
- :doc:`button` - 按钮控件
