Expand Setting Card 展开设置卡片模块
========================================

Expand Setting Card 模块提供可展开的设置卡片功能，支持分组和动画效果。
该模块提供现代化的展开设置界面，支持分组管理和平滑动画。

主要功能
--------

- **展开卡片** - 提供可展开/折叠的设置卡片
- **分组管理** - 支持设置项的分组管理
- **动画效果** - 支持展开/折叠的平滑动画
- **分隔符** - 提供组间分隔符
- **简单分组** - 支持简化的分组设置卡片

核心组件
--------

ExpandSettingCard
~~~~~~~~~~~~~~~~

可展开的设置卡片，提供基础的展开功能。

.. code-block:: python

   from qfluentwidgets.components.settings import ExpandSettingCard
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建展开设置卡片
   expand_card = ExpandSettingCard(
       icon=FIF.SETTING,
       title="高级设置",
       content="配置高级选项"
   )
   
   # 添加子控件
   expand_card.addWidget(child_widget)

ExpandGroupSettingCard
~~~~~~~~~~~~~~~~~~~~

分组展开设置卡片，支持分组管理。

.. code-block:: python

   from qfluentwidgets.components.settings import ExpandGroupSettingCard
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建分组展开设置卡片
   group_card = ExpandGroupSettingCard(
       icon=FIF.SETTING,
       title="网络设置",
       content="配置网络连接选项"
   )
   
   # 添加分组
   group = group_card.addGroup(
       icon=FIF.WIFI,
       title="无线网络",
       content="Wi-Fi连接设置",
       widget=widget
   )

SimpleExpandGroupSettingCard
~~~~~~~~~~~~~~~~~~~~~~~~~~

简单分组展开设置卡片，提供简化的分组功能。

.. code-block:: python

   from qfluentwidgets.components.settings import SimpleExpandGroupSettingCard
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建简单分组展开设置卡片
   simple_card = SimpleExpandGroupSettingCard(
       icon=FIF.SETTING,
       title="系统设置",
       content="配置系统选项"
   )

实际应用
--------

基本展开设置卡片
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import ExpandSettingCard
   from qfluentwidgets.components.settings import SwitchSettingCard
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicExpandWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("展开设置卡片示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建展开设置卡片
           self.expand_card = ExpandSettingCard(
               icon=FIF.SETTING,
               title="高级设置",
               content="配置高级选项"
           )
           
           # 添加子设置
           self.add_child_settings()
           
           # 显示当前状态
           self.status_label = Label("状态: 已折叠")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.expand_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def add_child_settings(self):
           """添加子设置"""
           # Wi-Fi 设置
           wifi_card = SwitchSettingCard(
               FIF.WIFI, "Wi-Fi", "启用无线网络"
           )
           wifi_card.setChecked(True)
           
           # 蓝牙设置
           bluetooth_card = SwitchSettingCard(
               FIF.BLUETOOTH, "蓝牙", "启用蓝牙"
           )
           
           # 位置服务
           location_card = SwitchSettingCard(
               FIF.LOCATION, "位置服务", "启用位置服务"
           )
           
           self.expand_card.addWidget(wifi_card)
           self.expand_card.addWidget(bluetooth_card)
           self.expand_card.addWidget(location_card)
       
       def setup_connections(self):
           """设置连接"""
           # 监听展开状态变化
           self.expand_card.installEventFilter(self)
       
       def eventFilter(self, obj, e):
           """事件过滤器"""
           if obj is self.expand_card and e.type() == e.Type.Resize:
               is_expanded = self.expand_card.isExpand
               self.status_label.setText(f"状态: {'已展开' if is_expanded else '已折叠'}")
           
           return super().eventFilter(obj, e)

分组展开设置卡片
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import ExpandGroupSettingCard
   from qfluentwidgets.components.settings import SwitchSettingCard, RangeSettingCard
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class GroupExpandWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("分组展开设置卡片示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建分组展开设置卡片
           self.group_card = ExpandGroupSettingCard(
               icon=FIF.GLOBE,
               title="网络设置",
               content="配置网络连接选项"
           )
           
           # 添加分组
           self.add_network_groups()
           
           # 显示当前状态
           self.status_label = Label("状态: 已折叠")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.group_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def add_network_groups(self):
           """添加网络分组"""
           # 无线网络组
           wifi_switch = SwitchSettingCard(
               FIF.WIFI, "Wi-Fi", "启用无线网络"
           )
           wifi_switch.setChecked(True)
           
           wifi_group = self.group_card.addGroup(
               icon=FIF.WIFI,
               title="无线网络",
               content="Wi-Fi连接设置",
               widget=wifi_switch
           )
           
           # 有线网络组
           ethernet_switch = SwitchSettingCard(
               FIF.ETHERNET, "以太网", "启用有线网络"
           )
           
           ethernet_group = self.group_card.addGroup(
               icon=FIF.ETHERNET,
               title="有线网络",
               content="以太网连接设置",
               widget=ethernet_switch
           )
           
           # VPN组
           vpn_switch = SwitchSettingCard(
               FIF.SHIELD, "VPN", "启用VPN连接"
               )
           
           vpn_group = self.group_card.addGroup(
               icon=FIF.SHIELD,
               title="VPN",
               content="虚拟专用网络设置",
               widget=vpn_switch
           )
       
       def setup_connections(self):
           """设置连接"""
           # 监听展开状态变化
           self.group_card.installEventFilter(self)
       
       def eventFilter(self, obj, e):
           """事件过滤器"""
           if obj is self.group_card and e.type() == e.Type.Resize:
               is_expanded = self.group_card.isExpand
               self.status_label.setText(f"状态: {'已展开' if is_expanded else '已折叠'}")
           
           return super().eventFilter(obj, e)

高级用法
--------

动态分组展开设置
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import ExpandGroupSettingCard
   from qfluentwidgets.components.settings import SwitchSettingCard, RangeSettingCard
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class DynamicGroupExpandWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("动态分组展开设置")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.add_group_btn = PushButton("添加分组")
           self.remove_group_btn = PushButton("移除分组")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.add_group_btn)
           header_layout.addWidget(self.remove_group_btn)
           
           # 创建分组展开设置卡片
           self.group_card = ExpandGroupSettingCard(
               icon=FIF.SETTING,
               title="动态设置",
               content="动态管理设置分组"
           )
           
           # 添加初始分组
           self.add_initial_groups()
           
           # 显示当前状态
           self.status_label = Label("状态: 已折叠")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.group_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def add_initial_groups(self):
           """添加初始分组"""
           self.groups = []
           
           # 性能组
           performance_switch = SwitchSettingCard(
               FIF.SPEED, "性能模式", "启用高性能模式"
           )
           
           performance_group = self.group_card.addGroup(
               icon=FIF.SPEED,
               title="性能",
               content="系统性能设置",
               widget=performance_switch
           )
           self.groups.append(performance_group)
           
           # 电源组
           power_range = RangeSettingCard(
               FIF.BATTERY, "电源管理", "调整电源设置"
           )
           power_range.setRange(0, 100)
           power_range.setValue(80)
           
           power_group = self.group_card.addGroup(
               icon=FIF.BATTERY,
               title="电源",
               content="电源管理设置",
               widget=power_range
           )
           self.groups.append(power_group)
       
       def setup_connections(self):
           """设置连接"""
           self.add_group_btn.clicked.connect(self.add_group)
           self.remove_group_btn.clicked.connect(self.remove_group)
           
           # 监听展开状态变化
           self.group_card.installEventFilter(self)
       
       def add_group(self):
           """添加分组"""
           import random
           
           group_options = [
               ("安全", FIF.SHIELD, "安全设置"),
               ("隐私", FIF.LOCK, "隐私设置"),
               ("备份", FIF.SAVE, "备份设置"),
               ("同步", FIF.SYNC, "同步设置")
           ]
           
           title, icon, content = random.choice(group_options)
           
           # 创建开关设置
           switch_card = SwitchSettingCard(icon, title, content)
           switch_card.setChecked(random.choice([True, False]))
           
           # 添加到分组卡片
           group = self.group_card.addGroup(
               icon=icon,
               title=title,
               content=content,
               widget=switch_card
           )
           
           self.groups.append(group)
           self.status_label.setText(f"已添加分组: {title}")
       
       def remove_group(self):
           """移除分组"""
           if not self.groups:
               self.status_label.setText("没有可移除的分组")
               return
           
           # 移除最后一个分组
           group = self.groups.pop()
           self.group_card.removeGroupWidget(group)
           self.status_label.setText(f"已移除分组")
       
       def eventFilter(self, obj, e):
           """事件过滤器"""
           if obj is self.group_card and e.type() == e.Type.Resize:
               is_expanded = self.group_card.isExpand
               self.status_label.setText(f"状态: {'已展开' if is_expanded else '已折叠'}")
           
           return super().eventFilter(obj, e)

简单展开设置卡片
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import SimpleExpandGroupSettingCard
   from qfluentwidgets.components.settings import SwitchSettingCard, RangeSettingCard
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class SimpleExpandWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("简单展开设置卡片示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建简单展开设置卡片
           self.simple_card = SimpleExpandGroupSettingCard(
               icon=FIF.SETTING,
               title="系统设置",
               content="配置系统选项"
           )
           
           # 添加设置项
           self.add_simple_settings()
           
           # 显示当前状态
           self.status_label = Label("状态: 已折叠")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.simple_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def add_simple_settings(self):
           """添加简单设置"""
           # 通知设置
           notification_switch = SwitchSettingCard(
               FIF.BELL, "通知", "启用系统通知"
           )
           notification_switch.setChecked(True)
           
           # 音量设置
           volume_range = RangeSettingCard(
               FIF.VOLUME, "音量", "调整系统音量"
           )
           volume_range.setRange(0, 100)
           volume_range.setValue(50)
           
           # 亮度设置
           brightness_range = RangeSettingCard(
               FIF.BRIGHTNESS, "亮度", "调整屏幕亮度"
           )
           brightness_range.setRange(0, 100)
           brightness_range.setValue(75)
           
           self.simple_card.addWidget(notification_switch)
           self.simple_card.addWidget(volume_range)
           self.simple_card.addWidget(brightness_range)
       
       def setup_connections(self):
           """设置连接"""
           # 监听展开状态变化
           self.simple_card.installEventFilter(self)
       
       def eventFilter(self, obj, e):
           """事件过滤器"""
           if obj is self.simple_card and e.type() == e.Type.Resize:
               is_expanded = self.simple_card.isExpand
               self.status_label.setText(f"状态: {'已展开' if is_expanded else '已折叠'}")
           
           return super().eventFilter(obj, e)

最佳实践
--------

1. **分组组织** - 合理组织设置项的分组结构
2. **动画效果** - 合理使用展开/折叠动画
3. **状态管理** - 正确管理展开/折叠状态
4. **布局优化** - 优化展开区域的布局和间距
5. **用户体验** - 提供清晰的展开指示和反馈

注意事项
--------

- 展开设置卡片会自动处理动画效果
- 分组卡片会自动添加分隔符
- 简单展开卡片适合少量设置项
- 动态添加/移除分组需要正确管理引用
- 展开状态会影响卡片的高度和布局
- 需要正确处理事件过滤器

相关模块
--------

- :doc:`components.settings.setting_card` - 设置卡片
- :doc:`components.settings.custom_color_setting_card` - 自定义颜色设置卡片
- :doc:`components.widgets.scroll_area` - 滚动区域
- :doc:`common.animation` - 动画组件
