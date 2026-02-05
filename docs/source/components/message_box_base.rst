Message Box Base 消息框基类模块
===================================

Message Box Base 模块提供消息框的基础功能，继承自遮罩对话框基类。
该模块为各种消息框提供统一的布局和按钮管理，支持表单验证和按钮显示控制。

主要功能
--------

- **基础布局** - 提供标准消息框布局结构
- **按钮管理** - 统一管理确定和取消按钮
- **表单验证** - 支持关闭前的数据验证
- **按钮控制** - 支持按钮的显示和隐藏
- **样式统一** - 提供统一的样式和阴影效果

核心组件
--------

MessageBoxBase
~~~~~~~~~~~~~

消息框基类，提供消息框的基础功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_box_base import MessageBoxBase
   from PySide6.QtWidgets import QLabel, QVBoxLayout
   
   class CustomMessageBox(MessageBoxBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           # 在self.viewLayout中添加内容
           layout = QVBoxLayout()
           
           title_label = QLabel("标题")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
           
           content_label = QLabel("这是消息框的内容")
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           
           # 添加到视图布局
           self.viewLayout.addLayout(layout)
       
       def validate(self) -> bool:
           """验证表单数据"""
           # 在这里添加验证逻辑
           return True

**主要方法：**
- ``validate()`` - 验证表单数据
- ``hideYesButton()`` - 隐藏确定按钮
- ``hideCancelButton()`` - 隐藏取消按钮

实际应用
--------

基本消息框
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_box_base import MessageBoxBase
   from qfluentwidgets import PushButton, CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicMessageBox(MessageBoxBase):
       """基本消息框"""
       
       def __init__(self, title: str, content: str, parent=None):
           super().__init__(parent)
           self.setup_ui(title, content)
       
       def setup_ui(self, title, content):
           # 添加标题
           title_label = QLabel(title)
           title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
           
           # 添加内容
           content_label = QLabel(content)
           content_label.setStyleSheet("color: #666; padding: 10px 0;")
           content_label.setWordWrap(True)
           
           # 添加到视图布局
           self.viewLayout.addWidget(title_label)
           self.viewLayout.addWidget(content_label)
           
           # 设置最小宽度
           self.widget.setMinimumWidth(300)
   
   class BasicMessageBoxWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.show_info_btn = PushButton("显示信息")
           self.show_warning_btn = PushButton("显示警告")
           self.show_error_btn = PushButton("显示错误")
           
           layout.addWidget(self.show_info_btn)
           layout.addWidget(self.show_warning_btn)
           layout.addWidget(self.show_error_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_info_btn.clicked.connect(self.show_info_message)
           self.show_warning_btn.clicked.connect(self.show_warning_message)
           self.show_error_btn.clicked.connect(self.show_error_message)
       
       def show_info_message(self):
           """显示信息消息"""
           message_box = BasicMessageBox("信息", "这是一条信息消息。", self)
           message_box.exec()
       
       def show_warning_message(self):
           """显示警告消息"""
           message_box = BasicMessageBox("警告", "请注意，这可能存在风险！", self)
           message_box.exec()
       
       def show_error_message(self):
           """显示错误消息"""
           message_box = BasicMessageBox("错误", "操作失败，请重试。", self)
           message_box.exec()

表单验证消息框
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_box_base import MessageBoxBase
   from qfluentwidgets import PushButton, CardWidget, Label, LineEdit
   from PySide6.QtWidgets import QVBoxLayout
   
   class FormMessageBox(MessageBoxBase):
       """表单验证消息框"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           # 添加标题
           title_label = QLabel("用户信息")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
           
           # 添加输入字段
           name_label = QLabel("姓名:")
           self.name_input = LineEdit()
           self.name_input.setPlaceholderText("请输入姓名")
           
           email_label = QLabel("邮箱:")
           self.email_input = LineEdit()
           self.email_input.setPlaceholderText("请输入邮箱")
           
           # 添加到视图布局
           self.viewLayout.addWidget(title_label)
           self.viewLayout.addWidget(name_label)
           self.viewLayout.addWidget(self.name_input)
           self.viewLayout.addWidget(email_label)
           self.viewLayout.addWidget(self.email_input)
           
           # 设置最小宽度
           self.widget.setMinimumWidth(350)
       
       def validate(self) -> bool:
           """验证表单数据"""
           name = self.name_input.text().strip()
           email = self.email_input.text().strip()
           
           if not name:
               self.name_input.setStyleSheet("border: 1px solid red;")
               return False
           
           if not email or "@" not in email:
               self.email_input.setStyleSheet("border: 1px solid red;")
               return False
           
           return True
       
       def get_name(self):
           """获取姓名"""
           return self.name_input.text().strip()
       
       def get_email(self):
           """获取邮箱"""
           return self.email_input.text().strip()
   
   class FormMessageBoxWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.show_form_btn = PushButton("显示表单")
           
           # 显示结果
           self.result_label = Label("未提交")
           
           layout.addWidget(self.show_form_btn)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_form_btn.clicked.connect(self.show_form_message)
       
       def show_form_message(self):
           """显示表单消息框"""
           form_dialog = FormMessageBox(self)
           
           if form_dialog.exec():
               name = form_dialog.get_name()
               email = form_dialog.get_email()
               
               self.result_label.setText(f"提交成功:\n姓名: {name}\n邮箱: {email}")
           else:
               self.result_label.setText("用户取消了提交")

高级用法
--------

自定义按钮消息框
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_box_base import MessageBoxBase
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   
   class CustomButtonMessageBox(MessageBoxBase):
       """自定义按钮消息框"""
       
       def __init__(self, title: str, content: str, button_type: str, parent=None):
           super().__init__(parent)
           self.button_type = button_type
           self.setup_ui(title, content)
           self.setup_buttons()
       
       def setup_ui(self, title, content):
           # 添加标题
           title_label = QLabel(title)
           title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
           
           # 添加内容
           content_label = QLabel(content)
           content_label.setStyleSheet("color: #666; padding: 10px 0;")
           content_label.setWordWrap(True)
           
           # 添加到视图布局
           self.viewLayout.addWidget(title_label)
           self.viewLayout.addWidget(content_label)
           
           # 设置最小宽度
           self.widget.setMinimumWidth(300)
       
       def setup_buttons(self):
           """设置按钮"""
           if self.button_type == "ok_only":
               self.hideCancelButton()
               self.yesButton.setText("确定")
           elif self.button_type == "yes_no":
               self.yesButton.setText("是")
               self.cancelButton.setText("否")
           elif self.button_type == "retry_cancel":
               self.yesButton.setText("重试")
               self.cancelButton.setText("取消")
           elif self.button_type == "continue":
               self.hideCancelButton()
               self.yesButton.setText("继续")
   
   class CustomButtonMessageBoxWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义按钮消息框")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建不同类型的按钮
           self.ok_only_btn = PushButton("仅确定按钮")
           self.yes_no_btn = PushButton("是否按钮")
           self.retry_cancel_btn = PushButton("重试取消按钮")
           self.continue_btn = PushButton("继续按钮")
           
           layout.addWidget(title_label)
           layout.addWidget(self.ok_only_btn)
           layout.addWidget(self.yes_no_btn)
           layout.addWidget(self.retry_cancel_btn)
           layout.addWidget(self.continue_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.ok_only_btn.clicked.connect(self.show_ok_only)
           self.yes_no_btn.clicked.connect(self.show_yes_no)
           self.retry_cancel_btn.clicked.connect(self.show_retry_cancel)
           self.continue_btn.clicked.connect(self.show_continue)
       
       def show_ok_only(self):
           """显示仅确定按钮"""
           message_box = CustomButtonMessageBox(
               "提示", "操作已完成！", "ok_only", self
           )
           message_box.exec()
       
       def show_yes_no(self):
           """显示是否按钮"""
           message_box = CustomButtonMessageBox(
               "确认", "确定要删除这个项目吗？", "yes_no", self
           )
           message_box.exec()
       
       def show_retry_cancel(self):
           """显示重试取消按钮"""
           message_box = CustomButtonMessageBox(
               "错误", "连接失败，是否重试？", "retry_cancel", self
           )
           message_box.exec()
       
       def show_continue(self):
           """显示继续按钮"""
           message_box = CustomButtonMessageBox(
               "进度", "第一步已完成，点击继续。", "continue", self
           )
           message_box.exec()

进度确认消息框
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_box_base import MessageBoxBase
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QProgressBar
   from PySide6.QtCore import QTimer
   
   class ProgressMessageBox(MessageBoxBase):
       """进度确认消息框"""
       
       def __init__(self, title: str, steps: list, parent=None):
           super().__init__(parent)
           self.steps = steps
           self.current_step = 0
           self.setup_ui(title)
           self.setup_progress()
       
       def setup_ui(self, title):
           # 添加标题
           title_label = QLabel(title)
           title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
           
           # 添加步骤说明
           self.step_label = QLabel(f"步骤 {self.current_step + 1}/{len(self.steps)}: {self.steps[self.current_step]}")
           self.step_label.setStyleSheet("color: #666; padding: 10px 0;")
           
           # 添加进度条
           self.progress_bar = QProgressBar()
           self.progress_bar.setRange(0, len(self.steps))
           self.progress_bar.setValue(self.current_step)
           
           # 添加到视图布局
           self.viewLayout.addWidget(title_label)
           self.viewLayout.addWidget(self.step_label)
           self.viewLayout.addWidget(self.progress_bar)
           
           # 设置最小宽度
           self.widget.setMinimumWidth(400)
       
       def setup_progress(self):
           """设置进度"""
           # 修改确定按钮文本
           self.yesButton.setText("下一步")
           
           # 如果是最后一步，改为完成
           if self.current_step == len(self.steps) - 1:
               self.yesButton.setText("完成")
       
       def validate(self) -> bool:
           """验证当前步骤"""
           # 这里可以添加当前步骤的验证逻辑
           return True
       
       def next_step(self):
           """下一步"""
           if self.current_step < len(self.steps) - 1:
               self.current_step += 1
               self.update_ui()
               return False  # 不关闭对话框
           else:
               return True  # 关闭对话框
       
       def update_ui(self):
           """更新界面"""
           self.step_label.setText(f"步骤 {self.current_step + 1}/{len(self.steps)}: {self.steps[self.current_step]}")
           self.progress_bar.setValue(self.current_step + 1)
           self.setup_progress()
       
       def get_current_step(self):
           """获取当前步骤"""
           return self.current_step
       
       def __onYesButtonClicked(self):
           """重写确定按钮点击事件"""
           if self.validate():
               if self.next_step():
                   self.accept()
   
   class ProgressMessageBoxWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("进度确认消息框")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建触发按钮
           self.show_progress_btn = PushButton("显示进度向导")
           
           # 显示结果
           self.result_label = Label("未开始")
           
           layout.addWidget(title_label)
           layout.addWidget(self.show_progress_btn)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_progress_btn.clicked.connect(self.show_progress_wizard)
       
       def show_progress_wizard(self):
           """显示进度向导"""
           steps = [
               "选择安装路径",
               "选择组件",
               "确认安装设置",
               "开始安装"
           ]
           
           progress_dialog = ProgressMessageBox("安装向导", steps, self)
           
           if progress_dialog.exec():
               self.result_label.setText("安装向导已完成！")
           else:
               current_step = progress_dialog.get_current_step()
               self.result_label.setText(f"用户在第 {current_step + 1} 步取消了")

最佳实践
--------

1. **继承使用** - 通过继承MessageBoxBase创建自定义消息框
2. **表单验证** - 在validate方法中实现数据验证逻辑
3. **按钮控制** - 根据需要隐藏或修改按钮
4. **用户体验** - 提供清晰的反馈和引导
5. **样式统一** - 保持与整体应用的一致性

注意事项
--------

- 消息框需要正确设置父窗口
- 表单验证失败时需要提供明确的错误提示
- 按钮文本需要根据场景合理设置
- 复杂的验证逻辑可能需要额外的UI反馈
- 消息框的大小需要考虑内容长度

相关模块
--------

- :doc:`components.dialog_box.mask_dialog_base` - 遮罩对话框基类
- :doc:`components.dialog_box.dialog` - 标准对话框
- :doc:`components.widgets.button` - 按钮组件
