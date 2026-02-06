Setting Card Group 设置卡片组模块
===================================

Setting Card Group 模块提供设置卡片分组功能，支持多个设置卡片的组织管理。
该模块提供现代化的设置卡片组界面，支持自动布局和大小调整。

主要功能
--------

- **卡片组** - 提供设置卡片的分组容器
- **自动布局** - 支持卡片的自动排列和布局
- **大小调整** - 根据内容自动调整组的大小
- **展开布局** - 集成展开布局功能
- **样式统一** - 提供统一的视觉风格

核心组件
--------

SettingCardGroup
~~~~~~~~~~~~~~

设置卡片组，提供完整的卡片分组功能。

.. code-block:: python

   from qfluentwidgets.components.settings import SettingCardGroup
   from qfluentwidgets.components.settings import SwitchSettingCard, RangeSettingCard
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建设置卡片组
   setting_group = SettingCardGroup("系统设置")
   
   # 添加设置卡片
   switch_card = SwitchSettingCard(FIF.BELL, "通知", "启用系统通知")
   range_card = RangeSettingCard(FIF.VOLUME, "音量", "调整系统音量")
   
   setting_group.addSettingCard(switch_card)
   setting_group.addSettingCard(range_card)

**主要方法：**
- ``addSettingCard()`` - 添加单个设置卡片
- ``addSettingCards()`` - 批量添加设置卡片
- ``adjustSize()`` - 调整组的大小

实际应用
--------

基本设置卡片组
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import SettingCardGroup
   from qfluentwidgets.components.settings import (
       SwitchSettingCard, RangeSettingCard, PushSettingCard
   )
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicSettingGroupWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("设置卡片组示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建设置卡片组
           self.setting_group = SettingCardGroup("系统设置")
           
           # 添加设置卡片
           self.add_setting_cards()
           
           # 显示当前状态
           self.status_label = Label("状态: 已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.setting_group)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def add_setting_cards(self):
           """添加设置卡片"""
           # 通知设置
           notification_card = SwitchSettingCard(
               FIF.BELL, "通知", "启用系统通知"
           )
           notification_card.setChecked(True)
           
           # 音量设置
           volume_card = RangeSettingCard(
               FIF.VOLUME, "音量", "调整系统音量"
           )
           volume_card.setRange(0, 100)
           volume_card.setValue(50)
           
           # 亮度设置
           brightness_card = RangeSettingCard(
               FIF.BRIGHTNESS, "亮度", "调整屏幕亮度"
           )
           brightness_card.setRange(0, 100)
           brightness_card.setValue(75)
           
           self.setting_group.addSettingCard(notification_card)
           self.setting_group.addSettingCard(volume_card)
           self.setting_group.addSettingCard(brightness_card)
       
       def setup_connections(self):
           """设置连接"""
           # 这里可以连接各种信号
           pass

高级设置卡片组
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import SettingCardGroup
   from qfluentwidgets.components.settings import (
       SwitchSettingCard, RangeSettingCard, ColorSettingCard, ComboBoxSettingCard
   )
   from qfluentwidgets.common.config import ConfigItem, RangeConfigItem, ColorConfigItem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AdvancedSettingGroupWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级设置卡片组")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.add_card_btn = PushButton("添加卡片")
           self.clear_btn = PushButton("清空卡片")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.add_card_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建多个设置卡片组
           self.create_setting_groups()
           
           # 显示当前状态
           self.status_label = Label("状态: 已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.system_group)
           layout.addWidget(self.appearance_group)
           layout.addWidget(self.network_group)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_setting_groups(self):
           """创建多个设置卡片组"""
           # 系统设置组
           self.system_group = SettingCardGroup("系统设置")
           self.add_system_cards()
           
           # 外观设置组
           self.appearance_group = SettingCardGroup("外观设置")
           self.add_appearance_cards()
           
           # 网络设置组
           self.network_group = SettingCardGroup("网络设置")
           self.add_network_cards()
       
       def add_system_cards(self):
           """添加系统设置卡片"""
           # 性能模式
           performance_card = SwitchSettingCard(
               FIF.SPEED, "性能模式", "启用高性能模式"
           )
           
           # 电源管理
           power_card = RangeSettingCard(
               FIF.BATTERY, "电源管理", "调整电源设置"
           )
           power_card.setRange(0, 100)
           power_card.setValue(80)
           
           self.system_group.addSettingCard(performance_card)
           self.system_group.addSettingCard(power_card)
       
       def add_appearance_cards(self):
           """添加外观设置卡片"""
           # 主题颜色
           theme_card = ColorSettingCard(
               FIF.PALETTE, "主题颜色", "选择应用程序主题颜色"
           )
           
           # 字体大小
           font_card = RangeSettingCard(
               FIF.FONT, "字体大小", "调整界面字体大小"
           )
           font_card.setRange(8, 24)
           font_card.setValue(14)
           
           self.appearance_group.addSettingCard(theme_card)
           self.appearance_group.addSettingCard(font_card)
       
       def add_network_cards(self):
           """添加网络设置卡片"""
           # Wi-Fi设置
           wifi_card = SwitchSettingCard(
               FIF.WIFI, "Wi-Fi", "启用无线网络"
           )
           wifi_card.setChecked(True)
           
           # 蓝牙设置
           bluetooth_card = SwitchSettingCard(
               FIF.BLUETOOTH, "蓝牙", "启用蓝牙连接"
           )
           
           self.network_group.addSettingCard(wifi_card)
           self.network_group.addSettingCard(bluetooth_card)
       
       def setup_connections(self):
           """设置连接"""
           self.add_card_btn.clicked.connect(self.add_random_card)
           self.clear_btn.clicked.connect(self.clear_all_cards)
       
       def add_random_card(self):
           """添加随机卡片"""
           import random
           
           card_types = [
               ("通知", FIF.BELL),
               ("音量", FIF.VOLUME),
               ("亮度", FIF.BRIGHTNESS),
               ("主题", FIF.PALETTE)
           ]
           
           card_name, card_icon = random.choice(card_types)
           
           # 创建随机设置卡片
           if card_name == "通知":
               from qfluentwidgets.components.settings import SwitchSettingCard
               card = SwitchSettingCard(card_icon, f"随机{card_name}", f"随机{card_name}设置")
           elif card_name in ["音量", "亮度"]:
               from qfluentwidgets.components.settings import RangeSettingCard
               card = RangeSettingCard(card_icon, f"随机{card_name}", f"调整随机{card_name}")
               card.setRange(0, 100)
               card.setValue(random.randint(0, 100))
           else:
               from qfluentwidgets.components.settings import ColorSettingCard
               card = ColorSettingCard(card_icon, f"随机{card_name}", f"选择随机{card_name}")
           
           # 添加到第一个组
           self.system_group.addSettingCard(card)
           self.status_label.setText(f"已添加随机卡片: {card_name}")
       
       def clear_all_cards(self):
           """清空所有卡片"""
           # 清空所有组的卡片
           self.system_group = SettingCardGroup("系统设置")
           self.appearance_group = SettingCardGroup("外观设置")
           self.network_group = SettingCardGroup("网络设置")
           
           self.status_label.setText("已清空所有设置卡片")

动态设置卡片组
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import SettingCardGroup
   from qfluentwidgets.components.settings import SwitchSettingCard
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class DynamicSettingGroupWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("动态设置卡片组")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.add_group_btn = PushButton("添加组")
           self.add_card_btn = PushButton("添加卡片")
           self.remove_card_btn = PushButton("移除卡片")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.add_group_btn)
           header_layout.addWidget(self.add_card_btn)
           header_layout.addWidget(self.remove_card_btn)
           
           # 创建设置卡片组
           self.setting_group = SettingCardGroup("动态设置")
           
           # 添加初始卡片
           self.add_initial_cards()
           
           # 显示当前状态
           self.status_label = Label("状态: 已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.setting_group)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def add_initial_cards(self):
           """添加初始卡片"""
           card1 = SwitchSettingCard(FIF.SETTING, "设置1", "第一个设置项")
           card2 = SwitchSettingCard(FIF.SETTING, "设置2", "第二个设置项")
           
           self.setting_group.addSettingCard(card1)
           self.setting_group.addSettingCard(card2)
       
       def setup_connections(self):
           """设置连接"""
           self.add_group_btn.clicked.connect(self.add_new_group)
           self.add_card_btn.clicked.connect(self.add_new_card)
           self.remove_card_btn.clicked.connect(self.remove_last_card)
       
       def add_new_group(self):
           """添加新组"""
           # 创建新的设置卡片组
           new_group = SettingCardGroup(f"新组 {len(self.setting_groups) + 1}")
           
           # 添加一个卡片到新组
           new_card = SwitchSettingCard(FIF.ADD, "新设置", "新添加的设置项")
           new_group.addSettingCard(new_card)
           
           self.status_label.setText(f"已创建新组，包含 1 个卡片")
       
       def add_new_card(self):
           """添加新卡片"""
           card_count = len(self.setting_group.cardLayout.widgets())
           new_card = SwitchSettingCard(FIF.ADD, f"设置{card_count + 1}", f"第{card_count + 1}个设置项")
           
           self.setting_group.addSettingCard(new_card)
           self.status_label.setText(f"已添加新卡片，总计: {card_count + 1} 个")
       
       def remove_last_card(self):
           """移除最后一个卡片"""
           cards = self.setting_group.cardLayout.widgets()
           
           if cards:
               last_card = cards[-1]
               self.setting_group.cardLayout.removeWidget(last_card)
               last_card.deleteLater()
               
               self.status_label.setText(f"已移除最后一个卡片，剩余: {len(cards) - 1} 个")
           else:
               self.status_label.setText("没有可移除的卡片")

最佳实践
--------

1. **分组组织** - 合理组织设置卡片的分组结构
2. **布局管理** - 利用自动布局功能优化排列
3. **大小调整** - 让组件自动处理大小调整
4. **视觉统一** - 保持组内卡片的视觉一致性
5. **响应式设计** - 考虑不同屏幕尺寸下的显示效果

注意事项
--------

- 设置卡片组会自动处理卡片的布局和大小
- 卡片会按照添加顺序自动排列
- 组件会根据内容自动调整高度
- 适合大量设置卡片的组织管理
- 需要正确设置父窗口关系
- 支持动态添加和移除卡片

相关模块
--------

- :doc:`components.settings.setting_card` - 设置卡片
- :doc:`components.layout.expand_layout` - 展开布局
- :doc:`common.style_sheet` - 样式表
- :doc:`common.font` - 字体管理
