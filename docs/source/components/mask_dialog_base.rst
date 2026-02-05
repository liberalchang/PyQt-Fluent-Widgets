Mask Dialog Base 遮罩对话框基类模块
=====================================

Mask Dialog Base 模块提供带遮罩的对话框基类，支持淡入淡出动画和阴影效果。
该模块是所有模态对话框的基础，提供统一的遮罩层、动画效果和交互行为。

主要功能
--------

- **遮罩层** - 提供半透明的遮罩背景
- **动画效果** - 支持淡入淡出的动画效果
- **阴影效果** - 提供专业的阴影效果
- **拖拽支持** - 支持对话框的拖拽移动
- **点击关闭** - 支持点击遮罩层关闭对话框

核心组件
--------

MaskDialogBase
~~~~~~~~~~~~~~

遮罩对话框基类，提供基础的遮罩对话框功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.mask_dialog_base import MaskDialogBase
   from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
   from PySide6.QtGui import QColor
   
   class CustomDialog(MaskDialogBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           # 在self.widget中添加内容
           layout = QVBoxLayout(self.widget)
           label = QLabel("这是一个自定义对话框")
           layout.addWidget(label)
           
           # 设置遮罩颜色
           self.setMaskColor(QColor(0, 0, 0, 100))
           
           # 设置阴影效果
           self.setShadowEffect(60, (0, 10), QColor(0, 0, 0, 50))
           
           # 设置可拖拽
           self.setDraggable(True)
           
           # 设置点击遮罩关闭
           self.setClosableOnMaskClicked(True)

**主要方法：**
- ``setShadowEffect()`` - 设置阴影效果
- ``setMaskColor()`` - 设置遮罩颜色
- ``setDraggable()`` - 设置是否可拖拽
- ``setClosableOnMaskClicked()`` - 设置点击遮罩是否关闭

实际应用
--------

基本遮罩对话框
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.mask_dialog_base import MaskDialogBase
   from qfluentwidgets import PushButton, CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class BasicMaskDialog(MaskDialogBase):
       """基本遮罩对话框"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout(self.widget)
           
           # 添加标题
           title_label = Label("提示")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
           
           # 添加内容
           content_label = Label("这是一个基本的遮罩对话框示例")
           
           # 添加按钮
           button_layout = QHBoxLayout()
           
           from qfluentwidgets import PrimaryPushButton
           ok_btn = PrimaryPushButton("确定")
           cancel_btn = PushButton("取消")
           
           ok_btn.clicked.connect(self.accept)
           cancel_btn.clicked.connect(self.reject)
           
           button_layout.addStretch()
           button_layout.addWidget(ok_btn)
           button_layout.addWidget(cancel_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           layout.addLayout(button_layout)
           
           # 设置样式
           self.widget.setFixedSize(300, 150)
           self.widget.setStyleSheet("""
               QFrame#centerWidget {
                   background-color: white;
                   border-radius: 8px;
               }
           """)
   
   class BasicMaskDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.show_dialog_btn = PushButton("显示遮罩对话框")
           
           layout.addWidget(self.show_dialog_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_dialog_btn.clicked.connect(self.show_mask_dialog)
       
       def show_mask_dialog(self):
           """显示遮罩对话框"""
           dialog = BasicMaskDialog(self)
           
           # 设置遮罩颜色
           dialog.setMaskColor(QColor(0, 0, 0, 120))
           
           # 设置阴影效果
           dialog.setShadowEffect(80, (0, 15), QColor(0, 0, 0, 60))
           
           # 设置点击遮罩关闭
           dialog.setClosableOnMaskClicked(True)
           
           # 显示对话框
           dialog.exec()

可拖拽对话框
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.mask_dialog_base import MaskDialogBase
   from qfluentwidgets import PushButton, CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   class DraggableMaskDialog(MaskDialogBase):
       """可拖拽遮罩对话框"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout(self.widget)
           
           # 添加标题栏
           title_label = Label("可拖拽对话框")
           title_label.setStyleSheet("""
               font-size: 16px; 
               font-weight: bold; 
               padding: 10px;
               background-color: #f0f0f0;
               border-top-left-radius: 8px;
               border-top-right-radius: 8px;
           """)
           
           # 添加内容
           content_label = Label("你可以拖拽这个对话框的标题栏来移动它")
           content_label.setAlignment(Qt.AlignCenter)
           content_label.setStyleSheet("padding: 20px;")
           
           # 添加关闭按钮
           from qfluentwidgets import TransparentToolButton
           from qfluentwidgets.common.icon import FluentIcon as FIF
           
           close_btn = TransparentToolButton(FIF.CLOSE, self.widget)
           close_btn.setFixedSize(30, 30)
           close_btn.move(self.widget.width() - 30, 0)
           close_btn.clicked.connect(self.reject)
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           
           # 设置样式
           self.widget.setFixedSize(350, 200)
           self.widget.setStyleSheet("""
               QFrame#centerWidget {
                   background-color: white;
                   border-radius: 8px;
               }
           """)
           
           # 设置可拖拽
           self.setDraggable(True)
           self.setClosableOnMaskClicked(True)
   
   class DraggableDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.show_draggable_btn = PushButton("显示可拖拽对话框")
           
           layout.addWidget(self.show_draggable_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_draggable_btn.clicked.connect(self.show_draggable_dialog)
       
       def show_draggable_dialog(self):
           """显示可拖拽对话框"""
           dialog = DraggableMaskDialog(self)
           
           # 设置遮罩颜色
           dialog.setMaskColor(QColor(0, 0, 0, 100))
           
           # 显示对话框
           dialog.exec()

高级用法
--------

自定义动画对话框
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.mask_dialog_base import MaskDialogBase
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect
   from PySide6.QtGui import QColor
   
   class AnimatedMaskDialog(MaskDialogBase):
       """自定义动画遮罩对话框"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout(self.widget)
           
           # 添加标题
           title_label = Label("动画对话框")
           title_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 15px;")
           
           # 添加内容
           content_label = Label("这个对话框有自定义的动画效果")
           content_label.setAlignment(Qt.AlignCenter)
           content_label.setStyleSheet("padding: 30px;")
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           
           # 设置样式
           self.widget.setFixedSize(400, 250)
           self.widget.setStyleSheet("""
               QFrame#centerWidget {
                   background-color: white;
                   border-radius: 12px;
               }
           """)
       
       def showEvent(self, e):
           """自定义显示动画"""
           # 先调用父类方法
           super().showEvent(e)
           
           # 添加缩放动画
           self.widget.setGeometry(0, 0, 400, 250)
           self.widget.move(
               (self.width() - 400) // 2,
               (self.height() - 250) // 2
           )
           
           # 缩放动画
           scale_animation = QPropertyAnimation(self.widget, b"geometry", self)
           scale_animation.setDuration(300)
           scale_animation.setEasingCurve(QEasingCurve.OutBack)
           
           # 从中心点开始缩放
           center_x = (self.width() - 400) // 2
           center_y = (self.height() - 250) // 2
           
           scale_animation.setStartValue(
               QRect(center_x + 200, center_y + 125, 0, 0)
           )
           scale_animation.setEndValue(
               QRect(center_x, center_y, 400, 250)
           )
           scale_animation.start()
       
       def done(self, code):
           """自定义关闭动画"""
           # 添加缩放动画
           scale_animation = QPropertyAnimation(self.widget, b"geometry", self)
           scale_animation.setDuration(200)
           scale_animation.setEasingCurve(QEasingCurve.InBack)
           
           center_x = (self.width() - 400) // 2
           center_y = (self.height() - 250) // 2
           
           scale_animation.setStartValue(
               QRect(center_x, center_y, 400, 250)
           )
           scale_animation.setEndValue(
               QRect(center_x + 200, center_y + 125, 0, 0)
           )
           scale_animation.finished.connect(lambda: super().done(code))
           scale_animation.start()
   
   class AnimatedDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义动画对话框")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建触发按钮
           self.show_animated_btn = PushButton("显示动画对话框")
           
           layout.addWidget(title_label)
           layout.addWidget(self.show_animated_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_animated_btn.clicked.connect(self.show_animated_dialog)
       
       def show_animated_dialog(self):
           """显示动画对话框"""
           dialog = AnimatedMaskDialog(self)
           
           # 设置渐变遮罩
           dialog.setMaskColor(QColor(0, 0, 0, 80))
           
           # 设置特殊阴影
           dialog.setShadowEffect(100, (0, 20), QColor(0, 0, 0, 80))
           
           # 显示对话框
           dialog.exec()

多功能对话框
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.mask_dialog_base import MaskDialogBase
   from qfluentwidgets import CardWidget, Label, PushButton, CheckBox, LineEdit
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class MultiFunctionMaskDialog(MaskDialogBase):
       """多功能遮罩对话框"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout(self.widget)
           
           # 标题区域
           title_layout = QHBoxLayout()
           title_label = Label("多功能对话框")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
           
           from qfluentwidgets import TransparentToolButton
           from qfluentwidgets.common.icon import FluentIcon as FIF
           
           close_btn = TransparentToolButton(FIF.CLOSE, self.widget)
           close_btn.clicked.connect(self.reject)
           
           title_layout.addWidget(title_label)
           title_layout.addStretch()
           title_layout.addWidget(close_btn)
           
           # 内容区域
           content_layout = QVBoxLayout()
           
           # 输入框
           input_label = Label("请输入内容:")
           self.input_field = LineEdit()
           self.input_field.setPlaceholderText("输入一些文字...")
           
           # 复选框
           self.remember_checkbox = CheckBox("记住我的选择")
           
           content_layout.addWidget(input_label)
           content_layout.addWidget(self.input_field)
           content_layout.addWidget(self.remember_checkbox)
           
           # 按钮区域
           button_layout = QHBoxLayout()
           
           from qfluentwidgets import PrimaryPushButton
           self.ok_btn = PrimaryPushButton("确定")
           self.cancel_btn = PushButton("取消")
           
           self.ok_btn.clicked.connect(self.accept)
           self.cancel_btn.clicked.connect(self.reject)
           
           button_layout.addStretch()
           button_layout.addWidget(self.ok_btn)
           button_layout.addWidget(self.cancel_btn)
           
           # 添加到主布局
           layout.addLayout(title_layout)
           layout.addLayout(content_layout)
           layout.addLayout(button_layout)
           
           # 设置样式
           self.widget.setFixedSize(400, 300)
           self.widget.setStyleSheet("""
               QFrame#centerWidget {
                   background-color: white;
                   border-radius: 10px;
               }
           """)
           
           # 设置功能
           self.setDraggable(True)
           self.setClosableOnMaskClicked(True)
       
       def get_input_text(self):
           """获取输入文本"""
           return self.input_field.text()
       
       def is_remember_checked(self):
           """是否记住选择"""
           return self.remember_checkbox.isChecked()
   
   class MultiFunctionDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("多功能对话框示例")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建触发按钮
           self.show_multi_btn = PushButton("显示多功能对话框")
           
           # 显示结果
           self.result_label = Label("未操作")
           self.result_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addWidget(self.show_multi_btn)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_multi_btn.clicked.connect(self.show_multi_dialog)
       
       def show_multi_dialog(self):
           """显示多功能对话框"""
           dialog = MultiFunctionMaskDialog(self)
           
           # 设置遮罩
           dialog.setMaskColor(QColor(0, 0, 0, 90))
           
           # 显示对话框
           if dialog.exec():
               input_text = dialog.get_input_text()
               remember = dialog.is_remember_checked()
               
               result_text = f"用户输入: {input_text}\n记住选择: {'是' if remember else '否'}"
               self.result_label.setText(result_text)
           else:
               self.result_label.setText("用户取消了操作")

最佳实践
--------

1. **继承使用** - 通过继承MaskDialogBase创建自定义对话框
2. **动画效果** - 合理使用动画效果提升用户体验
3. **拖拽功能** - 为大型对话框提供拖拽功能
4. **遮罩颜色** - 根据主题调整遮罩颜色
5. **阴影效果** - 使用合适的阴影效果增强层次感

注意事项
--------

- 遮罩对话框需要正确设置父窗口
- 自定义动画需要在适当的时候调用父类方法
- 拖拽功能需要在非交互区域启用
- 遮罩颜色的透明度需要合理设置
- 对话框大小需要考虑屏幕尺寸限制

相关模块
--------

- :doc:`components.dialog_box.dialog` - 标准对话框
- :doc:`components.dialog_box.message_box` - 消息框
- :doc:`components.widgets.button` - 按钮组件
