对话框组件 (Dialog Box)
======================

本节介绍 PySide6-Fluent-Widgets 中的对话框组件。

MessageBox
----------

消息对话框，用于显示信息、警告、错误等。

.. code-block:: python

   from qfluentwidgets import MessageBox

   # 信息对话框
   info_dialog = MessageBox(
       title='提示',
       content='操作成功完成！',
       parent=self
   )
   
   # 显示对话框
   if info_dialog.exec():
       print('用户点击了确定')
   else:
       print('用户点击了取消')

   # 警告对话框
   warning_dialog = MessageBox(
       title='警告',
       content='此操作可能存在风险，是否继续？',
       parent=self
   )

   # 错误对话框
   error_dialog = MessageBox(
       title='错误',
       content='操作失败，请重试',
       parent=self
   )

FileDialog
----------

文件对话框，用于选择文件或文件夹。

.. code-block:: python

   from qfluentwidgets import FileDialog

   # 选择单个文件
   file_path, _ = FileDialog.getOpenFileName(
       parent=self,
       caption='选择文件',
       directory='C:/',
       filter='所有文件 (*.*)'
   )
   
   if file_path:
       print(f'选择的文件: {file_path}')

   # 选择多个文件
   file_paths, _ = FileDialog.getOpenFileNames(
       parent=self,
       caption='选择文件',
       directory='C:/',
       filter='所有文件 (*.*)'
   )
   
   # 保存文件
   save_path, _ = FileDialog.getSaveFileName(
       parent=self,
       caption='保存文件',
       directory='C:/',
       filter='文本文件 (*.txt)'
   )

   # 选择文件夹
   folder_path = FileDialog.getExistingDirectory(
       parent=self,
       caption='选择文件夹',
       directory='C:/'
   )

ColorDialog
-----------

颜色选择对话框。

.. code-block:: python

   from qfluentwidgets import ColorDialog

   # 创建颜色对话框
   color_dialog = ColorDialog(
       title='选择颜色',
       parent=self
   )
   
   # 设置初始颜色
   color_dialog.setColor('#0078d4')
   
   # 显示对话框
   if color_dialog.exec():
       color = color_dialog.selectedColor()
       print(f'选择的颜色: {color.name()}')

FolderListDialog
----------------

文件夹列表对话框，用于浏览和选择文件夹。

.. code-block:: python

   from qfluentwidgets import FolderListDialog

   # 创建文件夹列表对话框
   folder_dialog = FolderListDialog(
       title='选择文件夹',
       parent=self
   )
   
   # 设置初始路径
   folder_dialog.setFolder('C:/')
   
   # 显示对话框
   if folder_dialog.exec():
       selected_folder = folder_dialog.getFolder()
       print(f'选择的文件夹: {selected_folder}')

InputDialog
----------

输入对话框，用于获取用户输入。

.. code-block:: python

   from qfluentwidgets import LineEditDialog, TextEditDialog

   # 单行输入对话框
   input_dialog = LineEditDialog(
       title='输入文本',
       content='请输入您的姓名：',
       parent=self
   )
   
   if input_dialog.exec():
       text = input_dialog.getText()
       print(f'输入的文本: {text}')

   # 多行输入对话框
   text_dialog = TextEditDialog(
       title='输入描述',
       content='请输入详细描述：',
       parent=self
   )
   
   if text_dialog.exec():
       text = text_dialog.getText()
       print(f'输入的文本: {text}')

ProgressDialog
--------------

进度对话框，用于显示长时间操作的进度。

.. code-block:: python

   from qfluentwidgets import ProgressDialog
   from PySide6.QtCore import QTimer

   # 创建进度对话框
   progress_dialog = ProgressDialog(
       title='处理中',
       content='正在处理数据，请稍候...',
       parent=self
   )
   
   # 设置范围
   progress_dialog.setRange(0, 100)
   progress_dialog.setValue(0)
   
   # 显示对话框
   progress_dialog.show()
   
   # 模拟进度更新
   def update_progress():
       current_value = progress_dialog.value()
       if current_value < 100:
           progress_dialog.setValue(current_value + 10)
       else:
           progress_dialog.close()
   
   # 使用定时器更新进度
   timer = QTimer()
   timer.timeout.connect(update_progress)
   timer.start(500)

QuestionDialog
---------------

问题对话框，用于询问用户选择。

.. code-block:: python

   from qfluentwidgets import QuestionDialog

   # 创建问题对话框
   question_dialog = QuestionDialog(
       title='确认',
       content='是否删除选中的项目？',
       parent=self
   )
   
   # 显示对话框
   if question_dialog.exec():
       print('用户确认删除')
   else:
       print('用户取消删除')

自定义对话框
----------

可以继承基类创建自定义对话框：

.. code-block:: python

   from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit, PushButton

   class CustomDialog(MessageBoxBase):
       """自定义对话框"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           
           # 创建标题
           self.titleLabel = SubtitleLabel('自定义对话框', self)
           
           # 创建输入框
           self.nameEdit = LineEdit(self)
           self.nameEdit.setPlaceholderText('请输入名称')
           
           # 创建按钮
           self.okButton = PushButton('确定', self)
           self.cancelButton = PushButton('取消', self)
           
           # 布局
           self.viewLayout.addWidget(self.titleLabel)
           self.viewLayout.addWidget(self.nameEdit)
           
           # 添加按钮到按钮组
           self.buttonGroup.addWidget(self.okButton)
           self.buttonGroup.addWidget(self.cancelButton)
           
           # 连接信号
           self.okButton.clicked.connect(self.accept)
           self.cancelButton.clicked.connect(self.reject)
           
           # 设置最小宽度
           self.widget.setMinimumWidth(300)

       def getName(self):
           """获取输入的名称"""
           return self.nameEdit.text()

   # 使用自定义对话框
   dialog = CustomDialog(self)
   if dialog.exec():
       name = dialog.getName()
       print(f'输入的名称: {name}')

完整示例
--------

下面是一个完整的对话框使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, PushButton
   from qfluentwidgets import *

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('对话框示例')
           self.resize(400, 300)
           
           # 创建中央窗口
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           # 创建布局
           layout = QVBoxLayout(central_widget)
           
           # 创建按钮
           info_btn = PushButton('信息对话框')
           file_btn = PushButton('文件对话框')
           color_btn = PushButton('颜色对话框')
           input_btn = PushButton('输入对话框')
           
           # 添加到布局
           layout.addWidget(info_btn)
           layout.addWidget(file_btn)
           layout.addWidget(color_btn)
           layout.addWidget(input_btn)
           
           # 连接信号
           info_btn.clicked.connect(self.show_info_dialog)
           file_btn.clicked.connect(self.show_file_dialog)
           color_btn.clicked.connect(self.show_color_dialog)
           input_btn.clicked.connect(self.show_input_dialog)

       def show_info_dialog(self):
           """显示信息对话框"""
           dialog = MessageBox(
               title='信息',
               content='这是一个信息对话框示例',
               parent=self
           )
           dialog.exec()

       def show_file_dialog(self):
           """显示文件对话框"""
           file_path, _ = FileDialog.getOpenFileName(
               parent=self,
               caption='选择文件',
               filter='所有文件 (*.*)'
           )
           
           if file_path:
               InfoBar.success(
                   title='成功',
                   content=f'选择了文件: {file_path}',
                   parent=self
               )

       def show_color_dialog(self):
           """显示颜色对话框"""
           dialog = ColorDialog(title='选择颜色', parent=self)
           
           if dialog.exec():
               color = dialog.selectedColor()
               InfoBar.success(
                   title='成功',
                   content=f'选择了颜色: {color.name()}',
                   parent=self
               )

       def show_input_dialog(self):
           """显示输入对话框"""
           dialog = LineEditDialog(
               title='输入',
               content='请输入文本：',
               parent=self
           )
           
           if dialog.exec():
               text = dialog.getText()
               InfoBar.success(
                   title='成功',
                   content=f'输入的文本: {text}',
                   parent=self
               )

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = MainWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **选择合适的对话框类型**: 根据需要选择消息框、文件对话框等
2. **提供清晰的提示信息**: 对话框标题和内容要简洁明了
3. **合理设置父窗口**: 确保对话框在正确的父窗口上显示
4. **处理用户响应**: 根据用户的选择执行相应的操作
5. **避免过度使用**: 不要滥用对话框影响用户体验

样式自定义
--------

可以通过 QSS 自定义对话框样式：

.. code-block:: python

   # 自定义对话框样式
   dialog.setStyleSheet("""
       MessageBoxBase {
           background-color: white;
           border: 1px solid #e1e1e1;
           border-radius: 8px;
       }
       
       SubtitleLabel {
           color: #0078d4;
           font-size: 16px;
           font-weight: bold;
       }
       
       PushButton {
           background-color: #0078d4;
           color: white;
           border: none;
           border-radius: 4px;
           padding: 8px 16px;
       }
       
       PushButton:hover {
           background-color: #106ebe;
       }
   """)
