Animation 动画模块
==================

Animation 模块提供了一套完整的动画系统，用于实现流畅的界面过渡效果和交互动画。
这些动画基于 Qt 的属性动画系统，提供了 Fluent Design 风格的动画效果。

主要功能
--------

- **基础动画框架** - 提供动画基类和事件处理
- **平移动画** - Y轴方向的按压反馈动画
- **背景动画** - 颜色过渡和背景变化动画
- **缓动函数** - 多种缓动曲线支持
- **动画链** - 支持串行和并行动画组合

核心组件
--------

AnimationBase
~~~~~~~~~~~~

动画基类，提供统一的事件处理接口。

.. code-block:: python

   from qfluentwidgets.common.animation import AnimationBase
   
   class CustomAnimation(AnimationBase):
       def __init__(self, parent):
           super().__init__(parent)
           
       def _onHover(self, e):
           # 鼠标悬停时的动画
           pass
           
       def _onPress(self, e):
           # 鼠标按下时的动画
           pass
           
       def _onRelease(self, e):
           # 鼠标释放时的动画
           pass

**特点：**
- 自动安装事件过滤器
- 统一的鼠标事件处理
- 可重写的动画方法

TranslateYAnimation
~~~~~~~~~~~~~~~~~~~

Y轴平移动画，常用于按钮的按压反馈效果。

.. code-block:: python

   from qfluentwidgets.common.animation import TranslateYAnimation
   from qfluentwidgets import PushButton
   
   button = PushButton('点击我')
   animation = TranslateYAnimation(button, offset=2)
   
   # 连接值变化信号
   animation.valueChanged.connect(lambda y: print(f"Y偏移: {y}"))

**参数：**
- ``parent`` - 父控件
- ``offset`` - 最大偏移量，默认为2

**动画效果：**
- 按压时向下移动
- 释放时弹性回弹

BackgroundAnimationWidget
~~~~~~~~~~~~~~~~~~~~~~~~~

背景动画混入类，为控件添加背景色过渡效果。

.. code-block:: python

   from qfluentwidgets.common.animation import BackgroundAnimationWidget
   from qfluentwidgets import PushButton
   
   class AnimatedButton(PushButton, BackgroundAnimationWidget):
       def __init__(self, text):
           super().__init__(text)
           
       def _normalBackgroundColor(self):
           return QColor(255, 255, 255)
           
       def _disabledBackgroundColor(self):
           return QColor(200, 200, 200)

**使用方法：**
1. 继承 BackgroundAnimationWidget
2. 实现颜色方法
3. 自动获得背景动画效果

动画类型
--------

FluentAnimationSpeed
~~~~~~~~~~~~~~~~~~~

动画速度枚举，定义标准的动画时长。

.. code-block:: python

   from qfluentwidgets.common.animation import FluentAnimationSpeed
   
   # 快速动画 (150ms)
   speed = FluentAnimationSpeed.FAST
   
   # 标准动画 (300ms)
   speed = FluentAnimationSpeed.NORMAL
   
   # 慢速动画 (500ms)
   speed = FluentAnimationSpeed.SLOW

FluentAnimationType
~~~~~~~~~~~~~~~~~~~

动画类型枚举，定义不同的动画效果。

.. code-block:: python

   from qfluentwidgets.common.animation import FluentAnimationType
   
   # 线性动画
   anim_type = FluentAnimationType.LINEAR
   
   # 弹性动画
   anim_type = FluentAnimationType.ELASTIC
   
   # 缓入缓出动画
   anim_type = FluentAnimationType.EASE_IN_OUT

高级用法
--------

自定义动画
~~~~~~~~~~

创建自定义动画效果：

.. code-block:: python

   from qfluentwidgets.common.animation import AnimationBase
   from PySide6.QtCore import QPropertyAnimation, QEasingCurve
   
   class ScaleAnimation(AnimationBase):
       def __init__(self, parent):
           super().__init__(parent)
           self.scale = 1.0
           self.animation = QPropertyAnimation(self, b"scale", self)
           
       def _onHover(self, e):
           self.animation.setEndValue(1.1)
           self.animation.setEasingCurve(QEasingCurve.OutQuad)
           self.animation.setDuration(200)
           self.animation.start()
           
       def _onLeave(self, e):
           self.animation.setEndValue(1.0)
           self.animation.setEasingCurve(QEasingCurve.OutQuad)
           self.animation.setDuration(200)
           self.animation.start()

动画链组合
~~~~~~~~~~

使用动画组创建复杂的动画序列：

.. code-block:: python

   from PySide6.QtCore import QParallelAnimationGroup, QSequentialAnimationGroup
   
   # 并行动画
   parallel_group = QParallelAnimationGroup()
   parallel_group.addAnimation(translate_animation)
   parallel_group.addAnimation(scale_animation)
   parallel_group.start()
   
   # 串行动画
   sequential_group = QSequentialAnimationGroup()
   sequential_group.addAnimation(fade_in_animation)
   sequential_group.addAnimation(translate_animation)
   sequential_group.start()

最佳实践
--------

1. **动画时长** - 使用标准的动画时长，保持一致性
2. **缓动函数** - 选择合适的缓动曲线，提升用户体验
3. **性能优化** - 避免过复杂的动画，影响性能
4. **可访问性** - 尊重用户的动画偏好设置

注意事项
--------

- 动画会自动处理事件过滤，无需手动安装
- 确保父控件支持动画效果
- 在控件销毁时，动画会自动清理
- 可以通过信号监听动画状态变化

相关模块
--------

- :doc:`common.style_sheet` - 样式表管理
- :doc:`common.config` - 配置管理
- :doc:`components.widgets` - UI组件
