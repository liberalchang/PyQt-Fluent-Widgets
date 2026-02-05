Message Dialog 消息对话框模块
=================================

Message Dialog 模块提供Win10风格的消息对话框，继承自遮罩对话框基类。
该模块提供简洁的消息显示界面，支持自动文本换行和固定宽度限制。

主要功能
--------

- **Win10风格** - 提供Windows 10风格的消息对话框界面
- **自动换行** - 支持长文本的自动换行处理
- **固定宽度** - 限制最大宽度以保持良好的显示效果
- **信号通知** - 提供确定和取消操作的信号通知
- **遮罩背景** - 继承遮罩对话框的遮罩效果

核心组件
--------

MessageDialog
~~~~~~~~~~~~~

Win10风格消息对话框，提供简洁的消息显示功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_dialog import MessageDialog
   from PySide6.QtWidgets import QApplication
   
   # 创建消息对话框
   message_dialog = MessageDialog(
       title="提示",
       content="这是一条消息内容",
       parent=parent
   )
   
   # 连接信号
   message_dialog.yesSignal.connect(on_yes_clicked)
   message_dialog.cancelSignal.connect(on_cancel_clicked)
   
   # 显示对话框
   message_dialog.exec()

**主要信号：**
- ``yesSignal`` - 确定按钮点击信号
- ``cancelSignal`` - 取消按钮点击信号

实际应用
--------

基本消息对话框
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_dialog import MessageDialog
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicMessageDialogWidget(CardWidget):
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
           message_dialog = MessageDialog(
               title="信息",
               content="这是一条信息消息，用于向用户展示一般性的信息。",
               parent=self
           )
           
           # 连接信号
           message_dialog.yesSignal.connect(self.on_message_yes)
           message_dialog.cancelSignal.connect(self.on_message_cancel)
           
           # 显示对话框
           message_dialog.exec()
       
       def show_warning_message(self):
           """显示警告消息"""
           message_dialog = MessageDialog(
               title="警告",
               content="请注意，此操作可能存在风险，建议在操作前仔细阅读相关说明。",
               parent=self
           )
           
           message_dialog.exec()
       
       def show_error_message(self):
           """显示错误消息"""
           message_dialog = MessageDialog(
               title="错误",
               content="操作失败，请检查网络连接或稍后重试。如果问题持续存在，请联系技术支持。",
               parent=self
           )
           
           message_dialog.exec()
       
       def on_message_yes(self):
           """消息确定处理"""
           print("用户点击了确定")
       
       def on_message_cancel(self):
           """消息取消处理"""
           print("用户点击了取消")

长文本消息对话框
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_dialog import MessageDialog
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   class LongTextMessageDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.show_long_text_btn = PushButton("显示长文本消息")
           self.show_terms_btn = PushButton("显示服务条款")
           self.show_privacy_btn = PushButton("显示隐私政策")
           
           layout.addWidget(self.show_long_text_btn)
           layout.addWidget(self.show_terms_btn)
           layout.addWidget(self.show_privacy_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_long_text_btn.clicked.connect(self.show_long_text_message)
           self.show_terms_btn.clicked.connect(self.show_terms_message)
           self.show_privacy_btn.clicked.connect(self.show_privacy_message)
       
       def show_long_text_message(self):
           """显示长文本消息"""
           long_content = (
               "这是一个长文本消息的示例。MessageDialog组件支持自动文本换行功能，"
               "能够很好地处理较长的文本内容。当文本内容超过对话框的宽度限制时，"
               "系统会自动进行换行处理，确保文本内容能够完整显示。"
               "这种设计使得消息对话框能够适应不同长度的文本内容，"
               "为用户提供更好的阅读体验。"
           )
           
           message_dialog = MessageDialog(
               title="长文本示例",
               content=long_content,
               parent=self
           )
           
           message_dialog.exec()
       
       def show_terms_message(self):
           """显示服务条款"""
           terms_content = (
               "服务条款\n\n"
               "1. 使用本服务即表示您同意这些条款。\n"
               "2. 您必须遵守所有适用的法律法规。\n"
               "3. 您不得使用本服务进行任何非法活动。\n"
               "4. 我们保留随时修改这些条款的权利。\n"
               "5. 继续使用本服务即表示您接受修改后的条款。\n\n"
               "如有疑问，请联系我们的客服团队。"
           )
           
           message_dialog = MessageDialog(
               title="服务条款",
               content=terms_content,
               parent=self
           )
           
           message_dialog.exec()
       
       def show_privacy_message(self):
           """显示隐私政策"""
           privacy_content = (
               "隐私政策\n\n"
               "我们重视您的隐私保护。本政策说明我们如何收集、使用和保护您的个人信息。\n\n"
               "信息收集：我们仅在必要范围内收集您的个人信息。\n"
               "信息使用：收集的信息仅用于提供和改进我们的服务。\n"
               "信息保护：我们采取合理措施保护您的个人信息安全。\n"
               "信息共享：未经您的同意，我们不会与第三方共享您的个人信息。\n\n"
               "如有任何隐私相关问题，请随时联系我们。"
           )
           
           message_dialog = MessageDialog(
               title="隐私政策",
               content=privacy_content,
               parent=self
           )
           
           message_dialog.exec()

高级用法
--------

自定义消息对话框
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_dialog import MessageDialog
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   class CustomMessageDialog(MessageDialog):
       """自定义消息对话框"""
       
       def __init__(self, title: str, content: str, message_type: str, parent=None):
           super().__init__(title, content, parent)
           self.message_type = message_type
           self.setup_custom_style()
       
       def setup_custom_style(self):
           """设置自定义样式"""
           # 根据消息类型设置不同的样式
           if self.message_type == "success":
               self.setMaskColor(QColor(0, 255, 0, 60))
               self.yesButton.setText("完成")
           elif self.message_type == "warning":
               self.setMaskColor(QColor(255, 165, 0, 60))
               self.yesButton.setText("知道了")
           elif self.message_type == "error":
               self.setMaskColor(QColor(255, 0, 0, 60))
               self.yesButton.setText("重试")
           elif self.message_type == "info":
               self.setMaskColor(QColor(0, 0, 255, 60))
               self.yesButton.setText("了解")
   
   class CustomMessageDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义消息对话框")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建不同类型的按钮
           self.success_btn = PushButton("成功消息")
           self.warning_btn = PushButton("警告消息")
           self.error_btn = PushButton("错误消息")
           self.info_btn = PushButton("信息消息")
           
           layout.addWidget(title_label)
           layout.addWidget(self.success_btn)
           layout.addWidget(self.warning_btn)
           layout.addWidget(self.error_btn)
           layout.addWidget(self.info_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.success_btn.clicked.connect(self.show_success_message)
           self.warning_btn.clicked.connect(self.show_warning_message)
           self.error_btn.clicked.connect(self.show_error_message)
           self.info_btn.clicked.connect(self.show_info_message)
       
       def show_success_message(self):
           """显示成功消息"""
           custom_dialog = CustomMessageDialog(
               title="操作成功",
               content="您的操作已成功完成！系统已保存所有更改。",
               message_type="success",
               parent=self
           )
           
           custom_dialog.exec()
       
       def show_warning_message(self):
           """显示警告消息"""
           custom_dialog = CustomMessageDialog(
               title="注意事项",
               content="检测到系统资源使用率较高，建议关闭不必要的应用程序以提高性能。",
               message_type="warning",
               parent=self
           )
           
           custom_dialog.exec()
       
       def show_error_message(self):
           """显示错误消息"""
           custom_dialog = CustomMessageDialog(
               title="连接错误",
               content="无法连接到服务器，请检查网络连接或稍后重试。",
               message_type="error",
               parent=self
           )
           
           custom_dialog.exec()
       
       def show_info_message(self):
           """显示信息消息"""
           custom_dialog = CustomMessageDialog(
               title="系统信息",
               content="系统版本：v2.1.0\n最后更新：2024年1月15日\n下次维护：2024年2月1日",
               message_type="info",
               parent=self
           )
           
           custom_dialog.exec()

确认对话框管理器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.message_dialog import MessageDialog
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   class ConfirmDialogManager:
       """确认对话框管理器"""
       
       def __init__(self, parent):
           self.parent = parent
       
       def show_delete_confirm(self, item_name: str) -> bool:
           """显示删除确认对话框"""
           content = f"确定要删除 '{item_name}' 吗？\n\n此操作不可撤销，请谨慎操作。"
           
           dialog = MessageDialog(
               title="确认删除",
               content=content,
               parent=self.parent
           )
           
           # 设置红色遮罩表示危险操作
           dialog.setMaskColor(QColor(255, 0, 0, 40))
           
           return dialog.exec() == QDialog.Accepted
       
       def show_save_confirm(self, file_name: str) -> bool:
           """显示保存确认对话框"""
           content = f"文件 '{file_name}' 已修改，是否保存更改？"
           
           dialog = MessageDialog(
               title="保存确认",
               content=content,
               parent=self.parent
           )
           
           # 设置蓝色遮罩表示信息操作
           dialog.setMaskColor(QColor(0, 0, 255, 40))
           
           return dialog.exec() == QDialog.Accepted
       
       def show_exit_confirm(self) -> bool:
           """显示退出确认对话框"""
           content = "确定要退出应用程序吗？\n\n未保存的更改将会丢失。"
           
           dialog = MessageDialog(
               title="确认退出",
               content=content,
               parent=self.parent
           )
           
           # 设置橙色遮罩表示警告
           dialog.setMaskColor(QColor(255, 165, 0, 40))
           
           return dialog.exec() == QDialog.Accepted
   
   class ConfirmDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.dialog_manager = ConfirmDialogManager(self)
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("确认对话框管理器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建触发按钮
           self.delete_btn = PushButton("删除项目")
           self.save_btn = PushButton("保存文件")
           self.exit_btn = PushButton("退出应用")
           
           # 显示操作结果
           self.result_label = Label("等待操作...")
           self.result_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addWidget(self.delete_btn)
           layout.addWidget(self.save_btn)
           layout.addWidget(self.exit_btn)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.delete_btn.clicked.connect(self.confirm_delete)
           self.save_btn.clicked.connect(self.confirm_save)
           self.exit_btn.clicked.connect(self.confirm_exit)
       
       def confirm_delete(self):
           """确认删除"""
           if self.dialog_manager.show_delete_confirm("重要文档"):
               self.result_label.setText("项目已删除")
           else:
               self.result_label.setText("取消删除")
       
       def confirm_save(self):
           """确认保存"""
           if self.dialog_manager.show_save_confirm("报告.docx"):
               self.result_label.setText("文件已保存")
           else:
               self.result_label.setText("取消保存")
       
       def confirm_exit(self):
           """确认退出"""
           if self.dialog_manager.show_exit_confirm():
               self.result_label.setText("应用程序已退出")
               QApplication.quit()
           else:
               self.result_label.setText("取消退出")

最佳实践
--------

1. **简洁明了** - 消息内容要简洁明了，突出重点
2. **合理分类** - 根据消息类型选择合适的显示方式
3. **用户体验** - 提供清晰的操作反馈
4. **颜色区分** - 使用不同颜色区分消息的重要性
5. **文本处理** - 合理处理长文本的显示效果

注意事项
--------

- 消息对话框的最大宽度为540像素
- 长文本会自动换行，但需要考虑阅读体验
- 遮罩颜色可以根据消息类型进行调整
- 确定按钮在点击后会禁用，防止重复操作
- 消息对话框适合用于简单的确认和信息提示

相关模块
--------

- :doc:`components.dialog_box.mask_dialog_base` - 遮罩对话框基类
- :doc:`components.dialog_box.message_box_base` - 消息框基类
- :doc:`components.dialog_box.dialog` - 标准对话框
