Folder List Dialog 文件夹列表对话框模块
=========================================

Folder List Dialog 模块提供文件夹列表管理功能，支持添加、删除和选择文件夹。
该模块提供专业的文件夹管理界面，包含文件夹卡片显示和文件对话框集成。

主要功能
--------

- **文件夹管理** - 支持文件夹的添加和删除
- **列表显示** - 以卡片形式显示文件夹列表
- **文件对话框** - 集成系统文件对话框
- **滚动支持** - 支持大量文件夹的滚动显示
- **信号通知** - 提供文件夹变化的信号通知

核心组件
--------

FolderListDialog
~~~~~~~~~~~~~~~~

文件夹列表对话框，提供完整的文件夹管理功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.folder_list_dialog import FolderListDialog
   from PySide6.QtWidgets import QApplication
   
   # 创建文件夹列表对话框
   folder_dialog = FolderListDialog(
       folderPaths=["/path/to/folder1", "/path/to/folder2"],
       title="选择文件夹",
       content="请选择要处理的文件夹：",
       parent=parent
   )
   
   # 连接信号
   folder_dialog.folderChanged.connect(on_folders_changed)
   
   # 显示对话框
   folder_dialog.exec()

**主要信号：**
- ``folderChanged`` - 文件夹列表变化信号

FolderCard
~~~~~~~~~~

文件夹卡片，显示单个文件夹的信息。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.folder_list_dialog import FolderCard
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建文件夹卡片
   folder_card = FolderCard("/path/to/folder")
   
   # 连接信号
   folder_card.clicked.connect(on_folder_clicked)

AddFolderCard
~~~~~~~~~~~~~

添加文件夹卡片，提供添加新文件夹的功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.folder_list_dialog import AddFolderCard
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建添加文件夹卡片
   add_folder_card = AddFolderCard()
   
   # 连接信号
   add_folder_card.clicked.connect(on_add_folder)

实际应用
--------

基本文件夹列表对话框
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.folder_list_dialog import FolderListDialog
   from qfluentwidgets import PushButton, CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicFolderListDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.show_dialog_btn = PushButton("选择文件夹")
           
           # 显示选中的文件夹
           self.selected_folders_label = Label("未选择文件夹")
           self.selected_folders_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(self.show_dialog_btn)
           layout.addWidget(self.selected_folders_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_dialog_btn.clicked.connect(self.show_folder_dialog)
       
       def show_folder_dialog(self):
           """显示文件夹列表对话框"""
           # 初始文件夹列表
           initial_folders = [
               "/home/user/Documents",
               "/home/user/Downloads"
           ]
           
           folder_dialog = FolderListDialog(
               folderPaths=initial_folders,
               title="选择文件夹",
               content="请选择要处理的文件夹：",
               parent=self
           )
           
           # 连接信号
           folder_dialog.folderChanged.connect(self.on_folders_changed)
           
           # 显示对话框
           folder_dialog.exec()
       
       def on_folders_changed(self, folders):
           """文件夹变化处理"""
           if folders:
               folder_text = "\n".join(folders[:5])  # 最多显示5个
               if len(folders) > 5:
                   folder_text += f"\n... 还有 {len(folders) - 5} 个文件夹"
               
               self.selected_folders_label.setText(f"已选择 {len(folders)} 个文件夹:\n{folder_text}")
           else:
               self.selected_folders_label.setText("未选择文件夹")

项目文件夹管理器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.folder_list_dialog import FolderListDialog
   from qfluentwidgets import PushButton, CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   import os
   
   class ProjectFolderManager(CardWidget):
       """项目文件夹管理器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.project_folders = []
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("项目文件夹管理")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           self.select_folders_btn = PushButton("选择项目文件夹")
           self.show_folders_btn = PushButton("显示当前文件夹")
           self.clear_folders_btn = PushButton("清空文件夹")
           
           # 显示当前文件夹
           self.current_folders_label = Label("未选择项目文件夹")
           self.current_folders_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addWidget(self.select_folders_btn)
           layout.addWidget(self.show_folders_btn)
           layout.addWidget(self.clear_folders_btn)
           layout.addWidget(self.current_folders_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.select_folders_btn.clicked.connect(self.select_project_folders)
           self.show_folders_btn.clicked.connect(self.show_current_folders)
           self.clear_folders_btn.clicked.connect(self.clear_project_folders)
       
       def select_project_folders(self):
           """选择项目文件夹"""
           # 默认项目文件夹
           default_folders = [
               os.path.expanduser("~/Documents"),
               os.path.expanduser("~/Desktop")
           ]
           
           folder_dialog = FolderListDialog(
               folderPaths=self.project_folders,
               title="选择项目文件夹",
               content="请选择要包含在项目中的文件夹：",
               parent=self
           )
           
           # 连接信号
           folder_dialog.folderChanged.connect(self.on_project_folders_changed)
           
           # 显示对话框
           folder_dialog.exec()
       
       def on_project_folders_changed(self, folders):
           """项目文件夹变化处理"""
           self.project_folders = folders
           self.update_folder_display()
       
       def show_current_folders(self):
           """显示当前文件夹"""
           self.update_folder_display()
       
       def clear_project_folders(self):
           """清空项目文件夹"""
           self.project_folders = []
           self.update_folder_display()
       
       def update_folder_display(self):
           """更新文件夹显示"""
           if self.project_folders:
               folder_count = len(self.project_folders)
               folder_list = "\n".join(self.project_folders[:3])
               if folder_count > 3:
                   folder_list += f"\n... 还有 {folder_count - 3} 个文件夹"
               
               self.current_folders_label.setText(
                   f"项目文件夹 ({folder_count}个):\n{folder_list}"
               )
           else:
               self.current_folders_label.setText("未选择项目文件夹")

高级用法
--------

自定义文件夹列表对话框
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.folder_list_dialog import FolderListDialog, FolderCard, AddFolderCard
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   import os
   
   class CustomFolderListDialog(FolderListDialog):
       """自定义文件夹列表对话框"""
       
       def __init__(self, folderPaths, title, content, parent):
           super().__init__(folderPaths, title, content, parent)
           self.setup_custom_ui()
       
       def setup_custom_ui(self):
           """设置自定义界面"""
           # 添加文件夹数量显示
           self.folder_count_label = QLabel(f"当前文件夹数量: {len(self.folderPaths)}")
           self.folder_count_label.setAlignment(Qt.AlignCenter)
           
           # 添加到布局
           self.vBoxLayout.insertWidget(2, self.folder_count_label)
           self.vBoxLayout.insertSpacing(3, 12)
       
       def update_folder_count(self):
           """更新文件夹数量显示"""
           self.folder_count_label.setText(f"当前文件夹数量: {len(self.folderPaths)}")
       
       def __showFileDialog(self):
           """重写文件对话框显示"""
           # 调用父类方法
           super().__showFileDialog()
           # 更新数量显示
           self.update_folder_count()
       
       def __showDeleteFolderCardDialog(self, card):
           """重写删除文件夹对话框"""
           # 调用父类方法
           super().__showDeleteFolderCardDialog(card)
           # 更新数量显示
           self.update_folder_count()
   
   class CustomFolderDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义文件夹对话框")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建触发按钮
           self.show_custom_dialog_btn = PushButton("显示自定义对话框")
           
           # 显示结果
           self.result_label = Label("未选择文件夹")
           
           layout.addWidget(title_label)
           layout.addWidget(self.show_custom_dialog_btn)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.show_custom_dialog_btn.clicked.connect(self.show_custom_dialog)
       
       def show_custom_dialog(self):
           """显示自定义对话框"""
           initial_folders = [
               os.path.expanduser("~/Documents"),
               os.path.expanduser("~/Downloads")
           ]
           
           custom_dialog = CustomFolderListDialog(
               folderPaths=initial_folders,
               title="自定义文件夹选择",
               content="请选择需要的文件夹：",
               parent=self
           )
           
           # 连接信号
           custom_dialog.folderChanged.connect(self.on_folders_changed)
           
           # 显示对话框
           custom_dialog.exec()
       
       def on_folders_changed(self, folders):
           """文件夹变化处理"""
           if folders:
               self.result_label.setText(f"选择了 {len(folders)} 个文件夹")
           else:
               self.result_label.setText("未选择文件夹")

文件夹验证管理器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.folder_list_dialog import FolderListDialog
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   import os
   
   class FolderValidationManager(CardWidget):
       """文件夹验证管理器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.validated_folders = []
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("文件夹验证管理器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           self.select_folders_btn = PushButton("选择并验证文件夹")
           self.validate_btn = PushButton("验证当前文件夹")
           self.clear_btn = PushButton("清空")
           
           # 显示验证结果
           self.validation_result_label = Label("未选择文件夹")
           self.validation_result_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addWidget(self.select_folders_btn)
           layout.addWidget(self.validate_btn)
           layout.addWidget(self.clear_btn)
           layout.addWidget(self.validation_result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.select_folders_btn.clicked.connect(self.select_and_validate_folders)
           self.validate_btn.clicked.connect(self.validate_current_folders)
           self.clear_btn.clicked.connect(self.clear_folders)
       
       def select_and_validate_folders(self):
           """选择并验证文件夹"""
           folder_dialog = FolderListDialog(
               folderPaths=self.validated_folders,
               title="选择文件夹",
               content="请选择要验证的文件夹：",
               parent=self
           )
           
           # 连接信号
           folder_dialog.folderChanged.connect(self.on_folders_selected)
           
           # 显示对话框
           folder_dialog.exec()
       
       def on_folders_selected(self, folders):
           """文件夹选择处理"""
           self.validated_folders = folders
           self.validate_folders()
       
       def validate_current_folders(self):
           """验证当前文件夹"""
           self.validate_folders()
       
       def validate_folders(self):
           """验证文件夹"""
           if not self.validated_folders:
               self.validation_result_label.setText("未选择文件夹")
               return
           
           valid_folders = []
           invalid_folders = []
           
           for folder_path in self.validated_folders:
               if os.path.exists(folder_path) and os.path.isdir(folder_path):
                   valid_folders.append(folder_path)
               else:
                   invalid_folders.append(folder_path)
           
           # 显示验证结果
           result_text = f"验证结果:\n"
           result_text += f"有效文件夹: {len(valid_folders)}个\n"
           result_text += f"无效文件夹: {len(invalid_folders)}个\n"
           
           if valid_folders:
               result_text += "\n有效文件夹:\n"
               result_text += "\n".join(valid_folders[:3])
               if len(valid_folders) > 3:
                   result_text += f"\n... 还有 {len(valid_folders) - 3} 个"
           
           if invalid_folders:
               result_text += "\n\n无效文件夹:\n"
               result_text += "\n".join(invalid_folders[:3])
               if len(invalid_folders) > 3:
                   result_text += f"\n... 还有 {len(invalid_folders) - 3} 个"
           
           self.validation_result_label.setText(result_text)
       
       def clear_folders(self):
           """清空文件夹"""
           self.validated_folders = []
           self.validation_result_label.setText("未选择文件夹")

最佳实践
--------

1. **路径验证** - 在使用前验证文件夹路径的有效性
2. **用户体验** - 提供清晰的文件夹选择界面
3. **性能考虑** - 避免选择过多文件夹影响性能
4. **错误处理** - 正确处理无效的文件夹路径
5. **信号连接** - 及时连接和处理文件夹变化信号

注意事项
--------

- 文件夹路径需要使用绝对路径
- 大量文件夹可能影响界面性能
- 文件对话框需要正确处理用户取消操作
- 文件夹删除需要用户确认
- 路径格式需要考虑不同操作系统的差异

相关模块
--------

- :doc:`components.dialog_box.dialog` - 标准对话框
- :doc:`components.dialog_box.mask_dialog_base` - 遮罩对话框基类
- :doc:`components.widgets.scroll_area` - 滚动区域组件
