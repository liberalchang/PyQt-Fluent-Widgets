设置组件 (Settings)
===================

本节介绍 PySide6-Fluent-Widgets 中的设置相关组件。

SettingCard
-----------

基础设置卡片，用于显示设置项。

.. code-block:: python

   from qfluentwidgets import SettingCard, FluentIcon

   # 创建基础设置卡片
   card = SettingCard(
       icon=FluentIcon.SETTING,
       title='基本设置',
       content='配置应用程序的基本选项'
   )

SwitchSettingCard
-----------------

带开关的设置卡片，用于布尔类型设置。

.. code-block:: python

   from qfluentwidgets import SwitchSettingCard, FluentIcon

   # 创建开关设置卡片
   switch_card = SwitchSettingCard(
       icon=FluentIcon.BRIGHTNESS,
       title='启用通知',
       content='接收系统通知消息'
   )
   
   # 连接信号
   switch_card.checkedChanged.connect(lambda checked: print(f'通知状态: {checked}'))
   
   # 设置默认值
   switch_card.setChecked(True)

RangeSettingCard
----------------

带滑块的设置卡片，用于数值范围设置。

.. code-block:: python

   from qfluentwidgets import RangeSettingCard, FluentIcon

   # 创建范围设置卡片
   range_card = RangeSettingCard(
       icon=FluentIcon.VOLUME,
       title='音量',
       content='调整系统音量大小'
   )
   
   # 设置范围
   range_card.setRange(0, 100)
   range_card.setValue(50)
   
   # 连接信号
   range_card.valueChanged.connect(lambda value: print(f'音量: {value}'))

PushSettingCard
---------------

带按钮的设置卡片，用于触发操作。

.. code-block:: python

   from qfluentwidgets import PushSettingCard, FluentIcon

   # 创建按钮设置卡片
   push_card = PushSettingCard(
       icon=FluentIcon.DOWNLOAD,
       title='检查更新',
       content='检查应用程序更新'
   )
   
   # 连接信号
   push_card.clicked.connect(lambda: print('检查更新'))

PrimaryPushSettingCard
----------------------

带主要按钮的设置卡片，用于重要操作。

.. code-block:: python

   from qfluentwidgets import PrimaryPushSettingCard, FluentIcon

   # 创建主要按钮设置卡片
   primary_card = PrimaryPushSettingCard(
       icon=FluentIcon.SAVE,
       title='保存设置',
       content='保存所有配置更改'
   )
   
   # 连接信号
   primary_card.clicked.connect(lambda: print('保存设置'))

ColorSettingCard
----------------

带颜色选择器的设置卡片。

.. code-block:: python

   from qfluentwidgets import ColorSettingCard, FluentIcon

   # 创建颜色设置卡片
   color_card = ColorSettingCard(
       icon=FluentIcon.PALETTE,
       title='主题颜色',
       content='选择应用程序主题颜色'
   )
   
   # 设置默认颜色
   color_card.setValue('#0078d4')
   
   # 连接信号
   color_card.colorChanged.connect(lambda color: print(f'颜色: {color.name()}'))

ComboBoxSettingCard
-------------------

带下拉框的设置卡片。

.. code-block:: python

   from qfluentwidgets import ComboBoxSettingCard, FluentIcon

   # 创建下拉框设置卡片
   combo_card = ComboBoxSettingCard(
       icon=FluentIcon.LANGUAGE,
       title='语言设置',
       content='选择界面语言'
   )
   
   # 添加选项
   combo_card.addItems(['中文', 'English', '日本語'])
   combo_card.setCurrentText('中文')
   
   # 连接信号
   combo_card.currentTextChanged.connect(lambda text: print(f'语言: {text}'))

HyperlinkCard
------------

超链接卡片，用于导航到外部链接。

.. code-block:: python

   from qfluentwidgets import HyperlinkCard, FluentIcon

   # 创建超链接卡片
   link_card = HyperlinkCard(
       icon=FluentIcon.LINK,
       title='官方网站',
       content='访问项目主页',
       url='https://example.com'
   )

ExpandSettingCard
-----------------

可展开的设置卡片，用于包含多个子设置。

.. code-block:: python

   from qfluentwidgets import ExpandSettingCard, FluentIcon, SwitchSettingCard

   # 创建可展开设置卡片
   expand_card = ExpandSettingCard(
       icon=FluentIcon.SETTING,
       title='高级设置',
       content='配置高级选项'
   )
   
   # 添加子设置
   switch1 = SwitchSettingCard(FluentIcon.WIFI, 'Wi-Fi', '启用无线网络')
   switch2 = SwitchSettingCard(FluentIcon.BLUETOOTH, '蓝牙', '启用蓝牙')
   
   expand_card.addWidget(switch1)
   expand_card.addWidget(switch2)

ExpandGroupSettingCard
----------------------

分组可展开设置卡片。

.. code-block:: python

   from qfluentwidgets import ExpandGroupSettingCard, FluentIcon, SwitchSettingCard

   # 创建分组可展开设置卡片
   group_card = ExpandGroupSettingCard(
       icon=FluentIcon.SETTING,
       title='网络设置',
       content='配置网络连接选项'
   )
   
   # 添加设置组
   group_card.addGroup('无线网络')
   group_card.addGroup('有线网络')
   
   # 添加设置项到组
   wifi_card = SwitchSettingCard(FluentIcon.WIFI, 'Wi-Fi', '启用无线网络')
   bluetooth_card = SwitchSettingCard(FluentIcon.BLUETOOTH, '蓝牙', '启用蓝牙')
   
   group_card.addWidget(wifi_card, '无线网络')
   group_card.addWidget(bluetooth_card, '无线网络')

FolderListSettingCard
----------------------

文件夹列表设置卡片。

.. code-block:: python

   from qfluentwidgets import FolderListSettingCard, FluentIcon

   # 创建文件夹列表设置卡片
   folder_card = FolderListSettingCard(
       icon=FluentIcon.FOLDER,
       title='下载文件夹',
       content='选择文件下载位置'
   )
   
   # 设置默认文件夹
   folder_card.setValue('C:/Downloads')
   
   # 连接信号
   folder_card.folderChanged.connect(lambda folder: print(f'文件夹: {folder}'))

OptionsSettingCard
-----------------

选项设置卡片，支持多个选项选择。

.. code-block:: python

   from qfluentwidgets import OptionsSettingCard, FluentIcon

   # 创建选项设置卡片
   options_card = OptionsSettingCard(
       icon=FluentIcon.DOCUMENT,
       title='文件格式',
       content='选择保存文件格式'
   )
   
   # 设置选项
   options_card.setOptions(['PDF', 'DOCX', 'TXT', 'HTML'])
   options_card.setValue('PDF')
   
   # 连接信号
   options_card.valueChanged.connect(lambda value: print(f'格式: {value}'))

CustomColorSettingCard
----------------------

自定义颜色设置卡片。

.. code-block:: python

   from qfluentwidgets import CustomColorSettingCard, FluentIcon

   # 创建自定义颜色设置卡片
   custom_color_card = CustomColorSettingCard(
       icon=FluentIcon.PALETTE,
       title='自定义颜色',
       content='选择自定义主题颜色'
   )
   
   # 设置颜色列表
   colors = ['#0078d4', '#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4']
   custom_color_card.setColors(colors)
   
   # 连接信号
   custom_color_card.colorChanged.connect(lambda color: print(f'自定义颜色: {color}'))

SettingCardGroup
----------------

设置卡片组，用于组织多个设置卡片。

.. code-block:: python

   from qfluentwidgets import (SettingCardGroup, SwitchSettingCard, 
                              RangeSettingCard, ComboBoxSettingCard, FluentIcon)

   # 创建设置卡片组
   group = SettingCardGroup('基本设置')
   
   # 添加设置卡片
   switch_card = SwitchSettingCard(
       FluentIcon.BRIGHTNESS, '启用通知', '接收系统通知消息'
   )
   
   range_card = RangeSettingCard(
       FluentIcon.VOLUME, '音量', '调整系统音量大小'
   )
   
   combo_card = ComboBoxSettingCard(
       FluentIcon.LANGUAGE, '语言', '选择界面语言'
   )
   
   group.addSettingCard(switch_card)
   group.addSettingCard(range_card)
   group.addSettingCard(combo_card)

配置管理
--------

使用配置系统管理设置：

.. code-block:: python

   from qfluentwidgets import qconfig, ConfigItem, OptionsConfigItem, RangeConfigItem

   # 定义配置项
   class AppConfig:
       # 布尔配置
       enable_notification = ConfigItem('App', 'EnableNotification', True)
       
       # 字符串配置
       language = ConfigItem('App', 'Language', 'zh_CN')
       
       # 选项配置
       theme = OptionsConfigItem('App', 'Theme', 'Light', ['Light', 'Dark', 'Auto'])
       
       # 范围配置
       volume = RangeConfigItem('App', 'Volume', 50, 0, 100)

   # 使用配置
   config = AppConfig()
   
   # 读取配置
   print(f'通知状态: {config.enable_notification.value}')
   print(f'语言: {config.language.value}')
   
   # 修改配置
   config.enable_notification.value = False
   config.language.value = 'en_US'
   
   # 保存配置
   qconfig.save()

完整示例
--------

下面是一个完整的设置界面示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                                QHBoxLayout, ScrollArea)
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class SettingsWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('设置界面示例')
           self.resize(600, 500)
           
           # 创建配置
           self.config = self.create_config()
           
           # 创建界面
           self.setup_ui()

       def create_config(self):
           """创建配置"""
           class Config:
               def __init__(self):
                   self.enable_notification = True
                   self.auto_update = False
                   self.volume = 50
                   self.language = '中文'
                   self.theme_color = '#0078d4'
                   self.download_folder = 'C:/Downloads'
           
           return Config()

       def setup_ui(self):
           """设置界面"""
           # 创建滚动区域
           scroll_area = ScrollArea()
           scroll_area.setWidgetResizable(True)
           scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
           
           # 创建主容器
           container = QWidget()
           container_layout = QVBoxLayout(container)
           container_layout.setSpacing(16)
           container_layout.setContentsMargins(20, 20, 20, 20)
           
           # 添加设置组
           self.add_general_settings(container_layout)
           self.add_appearance_settings(container_layout)
           self.add_network_settings(container_layout)
           self.add_storage_settings(container_layout)
           
           # 添加弹性空间
           container_layout.addStretch()
           
           scroll_area.setWidget(container)
           self.setCentralWidget(scroll_area)

       def add_general_settings(self, layout):
           """添加常规设置"""
           group = SettingCardGroup('常规设置')
           
           # 通知设置
           notification_card = SwitchSettingCard(
               FluentIcon.BELL, '启用通知', '接收系统通知消息'
           )
           notification_card.setChecked(self.config.enable_notification)
           notification_card.checkedChanged.connect(
               lambda checked: setattr(self.config, 'enable_notification', checked)
           )
           
           # 自动更新
           update_card = SwitchSettingCard(
               FluentIcon.SYNC, '自动更新', '自动检查并安装更新'
           )
           update_card.setChecked(self.config.auto_update)
           update_card.checkedChanged.connect(
               lambda checked: setattr(self.config, 'auto_update', checked)
           )
           
           # 音量设置
           volume_card = RangeSettingCard(
               FluentIcon.VOLUME, '音量', '调整系统音量大小'
           )
           volume_card.setRange(0, 100)
           volume_card.setValue(self.config.volume)
           volume_card.valueChanged.connect(
               lambda value: setattr(self.config, 'volume', value)
           )
           
           group.addSettingCard(notification_card)
           group.addSettingCard(update_card)
           group.addSettingCard(volume_card)
           
           layout.addWidget(group)

       def add_appearance_settings(self, layout):
           """添加外观设置"""
           group = SettingCardGroup('外观设置')
           
           # 语言设置
           language_card = ComboBoxSettingCard(
               FluentIcon.LANGUAGE, '语言', '选择界面语言'
           )
           language_card.addItems(['中文', 'English', '日本語'])
           language_card.setCurrentText(self.config.language)
           language_card.currentTextChanged.connect(
               lambda text: setattr(self.config, 'language', text)
           )
           
           # 主题颜色
           color_card = ColorSettingCard(
               FluentIcon.PALETTE, '主题颜色', '选择应用程序主题颜色'
           )
           color_card.setValue(self.config.theme_color)
           color_card.colorChanged.connect(
               lambda color: setattr(self.config, 'theme_color', color.name())
           )
           
           group.addSettingCard(language_card)
           group.addSettingCard(color_card)
           
           layout.addWidget(group)

       def add_network_settings(self, layout):
           """添加网络设置"""
           group = SettingCardGroup('网络设置')
           
           # 可展开的设置卡片
           expand_card = ExpandSettingCard(
               FluentIcon.GLOBE, '网络连接', '配置网络连接选项'
           )
           
           # Wi-Fi 设置
           wifi_card = SwitchSettingCard(
               FluentIcon.WIFI, 'Wi-Fi', '启用无线网络'
           )
           wifi_card.setChecked(True)
           
           # 蓝牙设置
           bluetooth_card = SwitchSettingCard(
               FluentIcon.BLUETOOTH, '蓝牙', '启用蓝牙'
           )
           
           expand_card.addWidget(wifi_card)
           expand_card.addWidget(bluetooth_card)
           
           group.addSettingCard(expand_card)
           
           layout.addWidget(group)

       def add_storage_settings(self, layout):
           """添加存储设置"""
           group = SettingCardGroup('存储设置')
           
           # 下载文件夹
           folder_card = FolderListSettingCard(
               FluentIcon.FOLDER, '下载文件夹', '选择文件下载位置'
           )
           folder_card.setValue(self.config.download_folder)
           folder_card.folderChanged.connect(
               lambda folder: setattr(self.config, 'download_folder', folder)
           )
           
           # 清理缓存
           clear_card = PrimaryPushSettingCard(
               FluentIcon.DELETE, '清理缓存', '删除临时文件和缓存'
           )
           clear_card.clicked.connect(self.clear_cache)
           
           group.addSettingCard(folder_card)
           group.addSettingCard(clear_card)
           
           layout.addWidget(group)

       def clear_cache(self):
           """清理缓存"""
           # 实现清理缓存逻辑
           InfoBar.success('缓存清理完成', parent=self)

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = SettingsWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **合理组织设置项**: 
   - 按功能分组设置
   - 使用清晰的标题和描述
   - 合理的默认值设置

2. **用户体验优化**: 
   - 提供即时反馈
   - 保存用户选择
   - 支持重置功能

3. **配置管理**: 
   - 使用配置系统持久化设置
   - 提供导入/导出功能
   - 支持配置验证

4. **界面设计**: 
   - 使用滚动区域处理大量设置
   - 合理的间距和布局
   - 响应式设计适配不同屏幕

样式自定义
--------

可以通过 QSS 自定义设置卡片样式：

.. code-block:: python

   # 自定义设置卡片样式
   setting_card.setStyleSheet("""
       SettingCard {
           background-color: white;
           border: 1px solid #e1e1e1;
           border-radius: 8px;
           margin: 4px;
       }
       
       SettingCard:hover {
           background-color: #f8f9fa;
           border-color: #0078d4;
       }
       
       SettingCard QLabel#titleLabel {
           color: #333333;
           font-size: 14px;
           font-weight: bold;
       }
       
       SettingCard QLabel#contentLabel {
           color: #666666;
           font-size: 12px;
       }
   """)
