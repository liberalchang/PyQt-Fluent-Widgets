Flyout 弹出控件模块
====================

Flyout 模块提供Fluent Design风格的弹出控件，支持多种动画效果和位置管理。该模块实现了现代化的弹出界面，提供流畅的动画效果和灵活的显示方式。

主要功能
--------

- **多种动画** - 支持上拉、下拉、左右滑动、淡入等多种动画效果
- **位置管理** - 智能的弹出位置计算和调整
- **动画管理** - 可扩展的动画管理系统
- **视图封装** - 提供基础的弹出视图类
- **图标支持** - 内置图标显示控件
- **信号机制** - 完整的显示/隐藏信号支持
- **自动关闭** - 支持点击外部自动关闭

核心组件
--------

Flyout
~~~~~~

主要的弹出控件类，提供静态方法创建弹出界面。

.. code-block:: python

   from qfluentwidgets.components.widgets.flyout import Flyout
   from PySide6.QtWidgets import QLabel, QPushButton
   from PySide6.QtCore import QPoint
   
   # 创建要显示的内容
   content = QLabel("这是一个弹出消息")
   
   # 显示弹出控件
   pos = QPoint(100, 100)
   flyout = Flyout.make(content, pos, parent, isDeleteOnClose=True)
   
   # 或者使用更简单的方式
   Flyout.show("简单消息", parent, pos)

**主要静态方法：**
- ``make(content, pos, parent, aniType=FlyoutAnimationType.DROP_DOWN, isDeleteOnClose=False)`` - 创建弹出控件
- ``show(text, parent, pos, duration=3000)`` - 显示简单文本消息
- ``create(title, content, parent, target, isDeleteOnClose=True)`` - 创建带标题的弹出控件

**参数说明：**
- ``content`` - 要显示的内容控件
- ``pos`` - 弹出位置（全局坐标）
- ``parent`` - 父控件
- ``aniType`` - 动画类型
- ``isDeleteOnClose`` - 关闭时是否自动删除

**信号：**
- ``closed`` - 弹出控件关闭时发出

FlyoutView
~~~~~~~~~~

弹出视图控件，提供基础的弹出界面功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.flyout import FlyoutView
   from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton
   
   # 创建弹出视图
   view = FlyoutView(parent=parent)
   
   # 添加内容
   layout = QVBoxLayout(view)
   layout.addWidget(QLabel("标题"))
   layout.addWidget(QLabel("内容描述"))
   layout.addWidget(QPushButton("确定"))
   
   # 显示视图
   view.exec(pos)

**主要方法：**
- ``exec(pos, ani=True, aniType=FlyoutAnimationType.DROP_DOWN)`` - 执行弹出显示
- ``close()`` - 关闭弹出视图

**信号：**
- ``closed`` - 视图关闭时发出

**特点：**
- 圆角背景样式
- 支持动画效果
- 自动尺寸调整

FlyoutViewBase
~~~~~~~~~~~~~~

弹出视图基类，提供基础的绘制功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.flyout import FlyoutViewBase
   
   # 创建自定义弹出视图
   class CustomFlyoutView(FlyoutViewBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           # 自定义内容

**特点：**
- 提供基础的圆角绘制
- 可继承扩展
- 样式适配

FlyoutAnimationType
~~~~~~~~~~~~~~~~~~

弹出动画类型枚举，定义不同的动画效果。

.. code-block:: python

   from qfluentwidgets.components.widgets.flyout import FlyoutAnimationType
   
   # 动画类型
   FlyoutAnimationType.PULL_UP      # 上拉动画
   FlyoutAnimationType.DROP_DOWN    # 下拉动画
   FlyoutAnimationType.SLIDE_LEFT   # 左滑动画
   FlyoutAnimationType.SLIDE_RIGHT  # 右滑动画
   FlyoutAnimationType.FADE_IN      # 淡入动画
   FlyoutAnimationType.NONE         # 无动画

**动画类型说明：**
- ``PULL_UP`` - 从下方滑入
- ``DROP_DOWN`` - 从上方滑入
- ``SLIDE_LEFT`` - 从右侧滑入
- ``SLIDE_RIGHT`` - 从左侧滑入
- ``FADE_IN`` - 原地淡入
- ``NONE`` - 直接显示

IconWidget
~~~~~~~~~~

图标控件，用于在弹出界面中显示图标。

.. code-block:: python

   from qfluentwidgets.components.widgets.flyout import IconWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建图标控件
   icon_widget = IconWidget(FIF.INFORMATION, parent=parent)
   icon_widget.setFixedSize(32, 32)

**构造函数：**
- ``IconWidget(icon, parent=None)``

**特点：**
- 支持FluentIcon
- 自动尺寸适配
- 主题颜色适配

FlyoutAnimationManager
~~~~~~~~~~~~~~~~~~~~~~

弹出动画管理器基类，提供动画管理功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.flyout import FlyoutAnimationManager
   
   # 动画管理器通常由系统自动管理
   # 可以通过注册方式扩展自定义动画

**主要方法：**
- ``register(animation_type)`` - 注册动画管理器
- ``create(animation_type)`` - 创建动画管理器实例
- ``exec(pos: QPoint)`` - 执行动画

**动画管理器子类：**
- ``PullUpFlyoutAnimationManager`` - 上拉动画管理器
- ``DropDownFlyoutAnimationManager`` - 下拉动画管理器
- ``SlideLeftFlyoutAnimationManager`` - 左滑动画管理器
- ``SlideRightFlyoutAnimationManager`` - 右滑动画管理器
- ``FadeInFlyoutAnimationManager`` - 淡入动画管理器
- ``DummyFlyoutAnimationManager`` - 无动画管理器

使用示例
--------

基础弹出消息示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
   from PySide6.QtCore import QPoint
   from qfluentwidgets.components.widgets.flyout import Flyout, FlyoutAnimationType
   from qfluentwidgets import FluentIcon as FIF
   
   class FlyoutDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建触发按钮
           self.info_btn = QPushButton("显示信息", self)
           self.warning_btn = QPushButton("显示警告", self)
           self.error_btn = QPushButton("显示错误", self)
           self.custom_btn = QPushButton("自定义弹出", self)
           
           # 连接信号
           self.info_btn.clicked.connect(self.show_info)
           self.warning_btn.clicked.connect(self.show_warning)
           self.error_btn.clicked.connect(self.show_error)
           self.custom_btn.clicked.connect(self.show_custom)
           
           layout.addWidget(self.info_btn)
           layout.addWidget(self.warning_btn)
           layout.addWidget(self.error_btn)
           layout.addWidget(self.custom_btn)
           
       def show_info(self):
           pos = self.info_btn.mapToGlobal(self.info_btn.rect().bottomLeft())
           Flyout.show("这是一个信息提示", self, pos)
           
       def show_warning(self):
           pos = self.warning_btn.mapToGlobal(self.warning_btn.rect().bottomLeft())
           Flyout.show("这是一个警告消息", self, pos, duration=5000)
           
       def show_error(self):
           pos = self.error_btn.mapToGlobal(self.error_btn.rect().bottomLeft())
           Flyout.show("这是一个错误提示", self, pos, duration=-1)  # 不自动关闭
           
       def show_custom(self):
           from PySide6.QtWidgets import QLabel, QHBoxLayout
           
           # 创建自定义内容
           content = QWidget()
           layout = QHBoxLayout(content)
           
           icon = IconWidget(FIF.HELP, content)
           icon.setFixedSize(24, 24)
           
           label = QLabel("这是一个自定义弹出内容")
           
           layout.addWidget(icon)
           layout.addWidget(label)
           
           pos = self.custom_btn.mapToGlobal(self.custom_btn.rect().bottomLeft())
           Flyout.make(content, pos, self, FlyoutAnimationType.FADE_IN, True)
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       demo = FlyoutDemo()
       demo.show()
       sys.exit(app.exec())

复杂弹出内容示例：

.. code-block:: python

   from PySide6.QtWidgets import QFormLayout, QLineEdit, QPushButton
   from qfluentwidgets.components.widgets.line_edit import LineEdit
   from qfluentwidgets.components.widgets.button import PrimaryPushButton
   
   class ComplexFlyoutDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           self.form_btn = PrimaryPushButton("显示表单", self)
           self.form_btn.clicked.connect(self.show_form_flyout)
           
           layout.addWidget(self.form_btn)
           
       def show_form_flyout(self):
           # 创建表单内容
           from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton
           
           form_widget = QWidget()
           form_layout = QFormLayout(form_widget)
           
           name_edit = LineEdit()
           email_edit = LineEdit()
           password_edit = LineEdit()
           password_edit.setEchoMode(LineEdit.Password)
           
           submit_btn = QPushButton("提交")
           cancel_btn = QPushButton("取消")
           
           form_layout.addRow("姓名:", name_edit)
           form_layout.addRow("邮箱:", email_edit)
           form_layout.addRow("密码:", password_edit)
           
           button_layout = QHBoxLayout()
           button_layout.addWidget(submit_btn)
           button_layout.addWidget(cancel_btn)
           
           form_layout.addRow(button_layout)
           
           # 连接信号
           submit_btn.clicked.connect(lambda: self.submit_form(name_edit.text(), email_edit.text()))
           cancel_btn.clicked.connect(lambda: self.close_flyout(form_widget))
           
           # 显示弹出
           pos = self.form_btn.mapToGlobal(self.form_btn.rect().bottomLeft())
           flyout = Flyout.make(form_widget, pos, self, FlyoutAnimationType.DROP_DOWN, True)
           
           # 保存flyout引用以便关闭
           form_widget.flyout = flyout
           
       def submit_form(self, name, email):
           print(f"提交表单: 姓名={name}, 邮箱={email}")
           Flyout.show("表单提交成功！", self, self.mapToGlobal(self.rect().center()))
           
       def close_flyout(self, widget):
           if hasattr(widget, 'flyout'):
               widget.flyout.close()

不同动画类型示例：

.. code-block:: python

   class AnimationDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建不同动画类型的按钮
           animations = [
               ("上拉动画", FlyoutAnimationType.PULL_UP),
               ("下拉动画", FlyoutAnimationType.DROP_DOWN),
               ("左滑动画", FlyoutAnimationType.SLIDE_LEFT),
               ("右滑动画", FlyoutAnimationType.SLIDE_RIGHT),
               ("淡入动画", FlyoutAnimationType.FADE_IN),
               ("无动画", FlyoutAnimationType.NONE)
           ]
           
           for text, ani_type in animations:
               btn = QPushButton(text, self)
               btn.clicked.connect(lambda checked, t=text, a=ani_type: self.show_animation(t, a))
               layout.addWidget(btn)
               
       def show_animation(self, text, ani_type):
           content = QLabel(f"这是{text}效果")
           content.setStyleSheet("padding: 20px; background-color: rgba(255, 255, 255, 0.9); border-radius: 8px;")
           
           pos = self.mapToGlobal(self.rect().center())
           Flyout.make(content, pos, self, ani_type, True)

上下文菜单示例：

.. code-block:: python

   from PySide6.QtCore import Qt
   
   class ContextMenuDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           self.setFixedSize(300, 200)
           self.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2);")
           
       def contextMenuEvent(self, event):
           # 创建上下文菜单内容
           from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
           
           menu_widget = QWidget()
           menu_layout = QVBoxLayout(menu_widget)
           
           actions = ["复制", "粘贴", "剪切", "删除", "属性"]
           
           for action_text in actions:
               btn = QPushButton(action_text)
               btn.clicked.connect(lambda checked, text=action_text: self.handle_action(text))
               menu_layout.addWidget(btn)
           
           # 显示上下文菜单
           pos = self.mapToGlobal(event.pos())
           flyout = Flyout.make(menu_widget, pos, self, FlyoutAnimationType.DROP_DOWN, True)
           
       def handle_action(self, action):
           Flyout.show(f"执行操作: {action}", self, self.mapToGlobal(self.rect().center()))

工具提示示例：

.. code-block:: python

   class TooltipDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建需要工具提示的控件
           from PySide6.QtWidgets import QSlider, QSpinBox
           
           self.slider = QSlider(Qt.Horizontal, self)
           self.slider.valueChanged.connect(self.show_slider_tooltip)
           
           self.spinbox = QSpinBox(self)
           self.spinbox.valueChanged.connect(self.show_spinbox_tooltip)
           
           layout.addWidget(QLabel("滑块（移动时显示提示）:"))
           layout.addWidget(self.slider)
           layout.addWidget(QLabel("数字框（改变时显示提示）:"))
           layout.addWidget(self.spinbox)
           
       def show_slider_tooltip(self, value):
           content = QLabel(f"当前值: {value}")
           content.setStyleSheet("padding: 8px; background-color: rgba(0, 0, 0, 0.8); color: white; border-radius: 4px;")
           
           # 计算滑块位置
           slider_pos = self.slider.mapToGlobal(self.slider.rect().topLeft())
           tip_pos = QPoint(slider_pos.x() + self.slider.value() * self.slider.width() // 100, slider_pos.y() - 30)
           
           Flyout.make(content, tip_pos, self, FlyoutAnimationType.FADE_IN, True)
           
       def show_spinbox_tooltip(self, value):
           if value % 10 == 0:  # 每10个单位显示一次提示
               content = QLabel(f"达到里程碑: {value}")
               content.setStyleSheet("padding: 8px; background-color: rgba(0, 120, 212, 0.9); color: white; border-radius: 4px;")
               
               pos = self.spinbox.mapToGlobal(self.spinbox.rect().bottomLeft())
               Flyout.make(content, pos, self, FlyoutAnimationType.SLIDE_RIGHT, True)

样式自定义
----------

可以通过样式表自定义弹出控件的外观：

.. code-block:: python

   # 自定义FlyoutView样式
   view = FlyoutView()
   view.setStyleSheet("""
       FlyoutView {
           background-color: rgba(30, 30, 30, 0.95);
           border: 1px solid rgba(0, 120, 212, 0.5);
           border-radius: 12px;
           padding: 16px;
       }
   """)

自定义内容样式：

.. code-block:: python

   # 创建自定义样式的内容
   content = QLabel("自定义样式消息")
   content.setStyleSheet("""
       QLabel {
           background-color: rgba(255, 255, 255, 0.95);
           color: #333333;
           border: 2px solid #0078d4;
           border-radius: 8px;
           padding: 12px 16px;
           font-size: 14px;
           font-weight: 500;
       }
   """)

自定义动画管理器：

.. code-block:: python

   from qfluentwidgets.components.widgets.flyout import FlyoutAnimationManager, FlyoutAnimationType
   
   # 创建自定义动画类型
   class CustomAnimationType:
       BOUNCE = 10
   
   @FlyoutAnimationManager.register(CustomAnimationType.BOUNCE)
   class BounceFlyoutAnimationManager(FlyoutAnimationManager):
       def exec(self, pos: QPoint):
           # 实现弹跳动画
           target = self.target
           target.show()
           
           # 弹跳动画逻辑
           from PySide6.QtCore import QPropertyAnimation, QEasingCurve
           
           animation = QPropertyAnimation(target, b"geometry", target)
           animation.setDuration(800)
           animation.setEasingCurve(QEasingCurve.OutBounce)
           
           start_geo = target.geometry()
           end_geo = start_geo.translated(0, -50)
           
           animation.setStartValue(start_geo)
           animation.setEndValue(end_geo)
           animation.start()

注意事项
--------

1. **内存管理** - 设置isDeleteOnClose=True时，弹出控件会在关闭时自动销毁
2. **位置计算** - 使用mapToGlobal()获取正确的全局坐标位置
3. **动画性能** - 复杂内容时建议使用简单的动画效果
4. **事件处理** - 弹出控件会自动处理点击外部关闭事件
5. **父子关系** - 确保设置正确的父控件以保证正确的显示层级
6. **线程安全** - 不要在非主线程中创建和显示弹出控件
7. **尺寸适配** - 内容控件会自动调整大小，但建议设置合适的尺寸
8. **动画冲突** - 避免同时显示多个弹出控件造成动画冲突

相关组件
--------

- :doc:`menu` - 菜单控件，类似的弹出功能
- :doc:`tooltip` - 工具提示控件
- :doc:`button` - 按钮控件，常用于触发弹出
- :doc:`label` - 标签控件，常用于弹出内容
