Folder List Setting Card 文件夹列表设置卡片模块
============================================

Folder List Setting Card 模块提供文件夹列表设置功能，支持文件夹管理和配置保存。
该模块提供现代化的文件夹管理界面，支持添加、删除和文件夹选择。

主要功能
--------

- **文件夹列表** - 提供文件夹列表的管理功能
- **配置集成** - 支持配置项的自动保存和加载
- **文件对话框** - 集成文件夹选择对话框
- **确认删除** - 支持删除前的确认提示
- **展开卡片** - 继承展开卡片的功能

核心组件
--------

FolderListSettingCard
~~~~~~~~~~~~~~~~~~~~

文件夹列表设置卡片，提供完整的文件夹管理功能。

.. code-block:: python

   from qfluentwidgets.components.settings import FolderListSettingCard
   from qfluentwidgets.common.config import ConfigItem
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建文件夹配置项
   folder_config = ConfigItem("App", "DownloadFolders", ["C:/Downloads"])
   
   # 创建文件夹列表设置卡片
   folder_card = FolderListSettingCard(
       configItem=folder_config,
       title="下载文件夹",
       content="管理文件下载位置",
       directory="C:/Downloads"
   )
   
   # 连接文件夹变化信号
   folder_card.folderChanged.connect(self.on_folders_changed)

**主要信号：**
- ``folderChanged`` - 文件夹列表变化信号

**主要方法：**
- ``setValue()`` - 设置文件夹列表
- ``value()`` - 获取当前文件夹列表

FolderItem
~~~~~~~~~~

文件夹项，表示单个文件夹条目。

.. code-block:: python

   from qfluentwidgets.components.settings import FolderItem
   
   # 创建文件夹项
   folder_item = FolderItem(
       folder="C:/Downloads",
       parent=parent_widget
   )

**主要信号：**
- ``removed`` - 移除信号

实际应用
--------

基本文件夹列表设置
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import FolderListSettingCard
   from qfluentwidgets.common.config import ConfigItem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicFolderListWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("文件夹列表设置示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建文件夹配置项
           self.folder_config = ConfigItem("App", "DownloadFolders", ["C:/Downloads"])
           
           # 创建文件夹列表设置卡片
           self.folder_card = FolderListSettingCard(
               configItem=self.folder_config,
               title="下载文件夹",
               content="管理文件下载位置",
               directory="C:/Downloads"
           )
           
           # 显示当前文件夹
           self.current_label = Label("当前文件夹: C:/Downloads")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.folder_card)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.folder_card.folderChanged.connect(self.on_folders_changed)
       
       def on_folders_changed(self, folders):
           """文件夹列表变化处理"""
           if folders:
               folder_list = ", ".join(folders)
               self.current_label.setText(f"当前文件夹: {folder_list}")
           else:
               self.current_label.setText("当前文件夹: 无")

高级文件夹列表设置
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import FolderListSettingCard
   from qfluentwidgets.common.config import ConfigItem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AdvancedFolderListWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级文件夹列表设置")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.reset_btn = PushButton("重置文件夹")
           self.export_btn = PushButton("导出列表")
           self.import_btn = PushButton("导入列表")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.reset_btn)
           header_layout.addWidget(self.export_btn)
           header_layout.addWidget(self.import_btn)
           
           # 创建多个文件夹配置
           self.create_folder_configs()
           
           # 创建文件夹列表设置卡片
           self.create_folder_cards()
           
           # 显示当前状态
           self.status_label = Label("状态: 就绪")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.download_card)
           layout.addWidget(self.music_card)
           layout.addWidget(self.picture_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_folder_configs(self):
           """创建文件夹配置项"""
           self.download_config = ConfigItem("App", "DownloadFolders", ["C:/Downloads"])
           self.music_config = ConfigItem("App", "MusicFolders", ["C:/Users/Music"])
           self.picture_config = ConfigItem("App", "PictureFolders", ["C:/Users/Pictures"])
       
       def create_folder_cards(self):
           """创建文件夹卡片"""
           self.download_card = FolderListSettingCard(
               configItem=self.download_config,
               title="下载文件夹",
               content="管理文件下载位置",
               directory="C:/Downloads"
           )
           
           self.music_card = FolderListSettingCard(
               configItem=self.music_config,
               title="音乐文件夹",
               content="管理音乐文件位置",
               directory="C:/Users/Music"
           )
           
           self.picture_card = FolderListSettingCard(
               configItem=self.picture_config,
               title="图片文件夹",
               content="管理图片文件位置",
               directory="C:/Users/Pictures"
           )
       
       def setup_connections(self):
           """设置连接"""
           self.reset_btn.clicked.connect(self.reset_folders)
           self.export_btn.clicked.connect(self.export_folders)
           self.import_btn.clicked.connect(self.import_folders)
           
           self.download_card.folderChanged.connect(self.on_download_folders_changed)
           self.music_card.folderChanged.connect(self.on_music_folders_changed)
           self.picture_card.folderChanged.connect(self.on_picture_folders_changed)
       
       def reset_folders(self):
           """重置文件夹"""
           self.download_config.value = ["C:/Downloads"]
           self.music_config.value = ["C:/Users/Music"]
           self.picture_config.value = ["C:/Users/Pictures"]
           self.status_label.setText("文件夹列表已重置")
       
       def export_folders(self):
           """导出文件夹列表"""
           folders = {
               "download": self.download_config.value,
               "music": self.music_config.value,
               "picture": self.picture_config.value
           }
           
           # 这里可以实现导出到文件的逻辑
           self.status_label.setText(f"文件夹列表已导出: {len(folders)} 个类别")
       
       def import_folders(self):
           """导入文件夹列表"""
           # 这里可以实现从文件导入的逻辑
           self.status_label.setText("文件夹列表导入功能待实现")
       
       def on_download_folders_changed(self, folders):
           """下载文件夹变化处理"""
           self.status_label.setText(f"下载文件夹已更新: {len(folders)} 个")
       
       def on_music_folders_changed(self, folders):
           """音乐文件夹变化处理"""
           self.status_label.setText(f"音乐文件夹已更新: {len(folders)} 个")
       
       def on_picture_folders_changed(self, folders):
           """图片文件夹变化处理"""
           self.status_label.setText(f"图片文件夹已更新: {len(folders)} 个")

动态文件夹管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import FolderListSettingCard
   from qfluentwidgets.common.config import ConfigItem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class DynamicFolderListWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("动态文件夹管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.add_default_btn = PushButton("添加默认文件夹")
           self.clear_all_btn = PushButton("清空所有")
           self.count_btn = PushButton("统计数量")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.add_default_btn)
           header_layout.addWidget(self.clear_all_btn)
           header_layout.addWidget(self.count_btn)
           
           # 创建文件夹配置项
           self.folder_config = ConfigItem("App", "ProjectFolders", [])
           
           # 创建文件夹列表设置卡片
           self.folder_card = FolderListSettingCard(
               configItem=self.folder_config,
               title="项目文件夹",
               content="管理项目文件位置",
               directory="C:/Projects"
           )
           
           # 显示当前状态
           self.status_label = Label("状态: 就绪")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.folder_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.add_default_btn.clicked.connect(self.add_default_folders)
           self.clear_all_btn.clicked.connect(self.clear_all_folders)
           self.count_btn.clicked.connect(self.count_folders)
           
           self.folder_card.folderChanged.connect(self.on_folders_changed)
       
       def add_default_folders(self):
           """添加默认文件夹"""
           default_folders = [
               "C:/Projects/Web",
               "C:/Projects/Desktop",
               "C:/Projects/Mobile",
               "C:/Projects/Backend"
           ]
           
           current_folders = self.folder_config.value.copy()
           for folder in default_folders:
               if folder not in current_folders:
                   current_folders.append(folder)
           
           self.folder_config.value = current_folders
           self.status_label.setText(f"已添加默认文件夹，总计: {len(current_folders)} 个")
       
       def clear_all_folders(self):
           """清空所有文件夹"""
           self.folder_config.value = []
           self.status_label.setText("已清空所有文件夹")
       
       def count_folders(self):
           """统计文件夹数量"""
           folders = self.folder_config.value
           total_count = len(folders)
           
           # 统计每个文件夹的文件数量（这里只是示例）
           file_counts = []
           for i, folder in enumerate(folders):
               # 模拟文件数量
               file_count = (i + 1) * 10
               file_counts.append(f"{folder}: {file_count} 个文件")
           
           count_info = f"总计: {total_count} 个文件夹\n" + "\n".join(file_counts)
           self.status_label.setText(count_info)
       
       def on_folders_changed(self, folders):
           """文件夹列表变化处理"""
           self.status_label.setText(f"文件夹列表已更新: {len(folders)} 个文件夹")

最佳实践
--------

1. **配置管理** - 正确使用ConfigItem进行配置管理
2. **默认目录** - 为文件夹选择设置合理的默认目录
3. **确认删除** - 提供删除前的确认提示
4. **路径验证** - 验证文件夹路径的有效性
5. **用户体验** - 提供清晰的操作反馈和状态显示

注意事项
--------

- 文件夹列表设置卡片会自动处理配置的保存和加载
- 文件对话框会过滤重复的文件夹路径
- 删除操作需要用户确认
- 展开卡片会根据内容自动调整高度
- 配置项需要正确初始化为列表类型
- 文件夹路径应该是绝对路径

相关模块
--------

- :doc:`components.settings.setting_card` - 设置卡片
- :doc:`components.settings.expand_setting_card` - 展开设置卡片
- :doc:`components.dialog_box.dialog` - 对话框
- :doc:`common.config` - 配置管理
