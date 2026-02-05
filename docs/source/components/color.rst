Color 颜色管理模块
===================

Color 模块提供完整的颜色管理系统，基于 Fluent Design 设计规范。
该模块包含主题色彩、系统颜色和颜色工具函数，确保应用在不同主题下都有良好的视觉效果。

主要功能
--------

- **Fluent 主题色彩** - 完整的 Fluent Design 色彩规范
- **系统语义颜色** - 成功、警告、错误等状态颜色
- **主题自适应** - 自动适配亮色/暗色主题
- **颜色工具函数** - 颜色验证和回退机制
- **类型安全** - 使用枚举确保颜色一致性

核心组件
--------

FluentThemeColor
~~~~~~~~~~~~~~~

Fluent Design 主题色彩枚举，提供完整的色彩规范。

.. code-block:: python

   from qfluentwidgets.common.color import FluentThemeColor
   
   # 获取主题色彩
   blue = FluentThemeColor.DEFAULT_BLUE.color()
   gold = FluentThemeColor.GOLD.color()
   red = FluentThemeColor.RED.color()
   
   print(f"蓝色: {blue.name()}")
   print(f"金色: {gold.name()}")
   print(f"红色: {red.name()}")

**色彩分类：**

暖色系：
- ``YELLOW_GOLD`` - 金黄色 (#FFB900)
- ``GOLD`` - 金色 (#FF8C00)
- ``ORANGE_BRIGHT`` - 亮橙色 (#F7630C)
- ``ORANGE_DARK`` - 暗橙色 (#CA5010)
- ``RUST`` - 铁锈色 (#DA3B01)
- ``PALE_RUST`` - 淡铁锈色 (#EF6950)

红色系：
- ``BRICK_RED`` - 砖红色 (#D13438)
- ``MOD_RED`` - 现代红 (#FF4343)
- ``PALE_RED`` - 淡红色 (#E74856)
- ``RED`` - 红色 (#E81123)
- ``ROSE_BRIGHT`` - 亮玫瑰色 (#EA005E)
- ``ROSE`` - 玫瑰色 (#C30052)

紫色系：
- ``PLUM_LIGHT`` - 淡梅色 (#E3008C)
- ``PLUM`` - 梅色 (#BF0077)
- ``ORCHID_LIGHT`` - 淡兰花色 (#BF0077)
- ``ORCHID`` - 兰花色 (#9A0089)
- ``PURPLE_SHADOW`` - 紫影色 (#8E8CD8)
- ``PURPLE_SHADOW_DARK`` - 深紫影色 (#6B69D6)

蓝色系：
- ``DEFAULT_BLUE`` - 默认蓝色 (#0078D7)
- ``NAVY_BLUE`` - 海军蓝 (#0063B1)
- ``COOL_BLUE_BRIGHT`` - 亮冷蓝 (#0099BC)
- ``COOL_BLUR`` - 冷蓝模糊色 (#2D7D9A)
- ``STEAL_BLUE`` - 钢蓝色 (#68768A)
- ``METAL_BLUE`` - 金属蓝 (#515C6B)

绿色系：
- ``SEAFOAM`` - 海沫色 (#00B7C3)
- ``SEAFOAM_TEAL`` - 海沫青色 (#038387)
- ``MINT_LIGHT`` - 淡薄荷色 (#00B294)
- ``MINT_DARK`` - 深薄荷色 (#018574)
- ``TURF_GREEN`` - 草坪绿 (#00CC6A)
- ``SPORT_GREEN`` - 运动绿 (#10893E)
- ``MEADOW_GREEN`` - 草地绿 (#498205)
- ``GREEN`` - 绿色 (#107C10)

灰色系：
- ``GRAY`` - 灰色 (#7A7574)
- ``GRAY_BROWN`` - 灰褐色 (#5D5A58)
- ``OVERCAST`` - 阴天灰 (#767676)
- ``STORM`` - 风暴灰 (#4C4A48)
- ``BLUE_GRAY`` - 蓝灰色 (#69797E)
- ``GRAY_DARK`` - 深灰色 (#4A5459)

FluentSystemColor
~~~~~~~~~~~~~~~~~

系统语义颜色，用于表示不同的状态和含义。

.. code-block:: python

   from qfluentwidgets.common.color import FluentSystemColor, Theme
   
   # 获取成功状态颜色（自动适配主题）
   success_fg = FluentSystemColor.SUCCESS_FOREGROUND.color()
   success_bg = FluentSystemColor.SUCCESS_BACKGROUND.color()
   
   # 获取警告状态颜色
   caution_fg = FluentSystemColor.CAUTION_FOREGROUND.color()
   caution_bg = FluentSystemColor.CAUTION_BACKGROUND.color()
   
   # 获取错误状态颜色
   critical_fg = FluentSystemColor.CRITICAL_FOREGROUND.color()
   critical_bg = FluentSystemColor.CRITICAL_BACKGROUND.color()
   
   # 指定主题获取颜色
   success_dark = FluentSystemColor.SUCCESS_FOREGROUND.color(Theme.DARK)
   success_light = FluentSystemColor.SUCCESS_FOREGROUND.color(Theme.LIGHT)

**颜色类型：**

前景色（文字颜色）：
- ``SUCCESS_FOREGROUND`` - 成功前景色（亮色主题：#0f7b0f，暗色主题：#6ccb5f）
- ``CAUTION_FOREGROUND`` - 警告前景色（亮色主题：#9d5d00，暗色主题：#fce100）
- ``CRITICAL_FOREGROUND`` - 错误前景色（亮色主题：#c42b1c，暗色主题：#ff99a4）

背景色：
- ``SUCCESS_BACKGROUND`` - 成功背景色（亮色主题：#dff6dd，暗色主题：#393d1b）
- ``CAUTION_BACKGROUND`` - 警告背景色（亮色主题：#fff4ce，暗色主题：#433519）
- ``CRITICAL_BACKGROUND`` - 错误背景色（亮色主题：#fde7e9，暗色主题：#442726）

工具函数
--------

validColor()
~~~~~~~~~~~

验证颜色有效性，提供默认值回退。

.. code-block:: python

   from qfluentwidgets.common.color import validColor
   from PySide6.QtGui import QColor
   
   # 验证颜色
   valid_color = QColor("#FF0000")
   invalid_color = QColor()
   default_color = QColor("#000000")
   
   # 使用有效颜色
   result1 = validColor(valid_color, default_color)  # 返回 valid_color
   result2 = validColor(invalid_color, default_color)  # 返回 default_color

fallbackThemeColor()
~~~~~~~~~~~~~~~~~~

主题颜色回退机制。

.. code-block:: python

   from qfluentwidgets.common.color import fallbackThemeColor
   from PySide6.QtGui import QColor
   
   # 使用主题颜色作为回退
   custom_color = QColor("#invalid")
   result = fallbackThemeColor(custom_color)  # 返回当前主题色

autoFallbackThemeColor()
~~~~~~~~~~~~~~~~~~~~~~~

根据主题自动选择颜色。

.. code-block:: python

   from qfluentwidgets.common.color import autoFallbackThemeColor
   from PySide6.QtGui import QColor
   
   # 为不同主题设置不同颜色
   light_color = QColor("#FFFFFF")  # 亮色主题使用白色
   dark_color = QColor("#000000")   # 暗色主题使用黑色
   
   # 自动选择合适的颜色
   result = autoFallbackThemeColor(light_color, dark_color)

实际应用
--------

UI组件着色
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets import PushButton, InfoBar
   from qfluentwidgets.common.color import FluentThemeColor, FluentSystemColor
   
   # 使用主题色彩为按钮着色
   button = PushButton("重要操作")
   button.setStyleSheet(f"""
       PushButton {{
           background-color: {FluentThemeColor.DEFAULT_BLUE.value};
           color: white;
           border: none;
           border-radius: 4px;
           padding: 8px 16px;
       }}
   """)
   
   # 使用系统颜色显示状态信息
   InfoBar.success(
       title="操作成功",
       content="数据已保存",
       duration=2000
   )

状态指示器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets import InfoBadge, Label
   from qfluentwidgets.common.color import FluentSystemColor
   
   class StatusIndicator:
       def __init__(self):
           self.success_badge = InfoBadge()
           self.warning_badge = InfoBadge()
           self.error_badge = InfoBadge()
           
           # 设置状态颜色
           self.success_badge.setStyleSheet(
               f"background-color: {FluentSystemColor.SUCCESS_FOREGROUND.color().name()}"
           )
           self.warning_badge.setStyleSheet(
               f"background-color: {FluentSystemColor.CAUTION_FOREGROUND.color().name()}"
           )
           self.error_badge.setStyleSheet(
               f"background-color: {FluentSystemColor.CRITICAL_FOREGROUND.color().name()}"
           )
       
       def show_status(self, status_type):
           if status_type == "success":
               self.success_badge.show()
           elif status_type == "warning":
               self.warning_badge.show()
           elif status_type == "error":
               self.error_badge.show()

主题适配
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.color import FluentThemeColor, autoFallbackThemeColor
   from qfluentwidgets import setTheme, Theme
   
   class ThemeAwareWidget:
       def __init__(self):
           self.primary_color = FluentThemeColor.DEFAULT_BLUE.color()
           self.accent_color = FluentThemeColor.GOLD.color()
           
           # 自动适配主题的颜色
           self.text_color = autoFallbackThemeColor(
               QColor("#000000"),  # 亮色主题文字颜色
               QColor("#FFFFFF")   # 暗色主题文字颜色
           )
           
           self.update_colors()
       
       def update_colors(self):
           """更新颜色以适应当前主题"""
           self.setStyleSheet(f"""
               QWidget {{
                   color: {self.text_color.name()};
                   background-color: {self.primary_color.name()};
               }}
           """)
       
       def on_theme_changed(self):
           """主题变化时更新颜色"""
           self.update_colors()

颜色选择器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.color import FluentThemeColor
   from qfluentwidgets import ComboBox, QVBoxLayout, QWidget
   
   class ColorPicker(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建颜色选择下拉框
           self.color_combo = ComboBox()
           
           # 添加所有主题色彩
           for color in FluentThemeColor:
               self.color_combo.addItem(color.name, color)
           
           # 连接选择变化信号
           self.color_combo.currentTextChanged.connect(self.on_color_changed)
           
           layout.addWidget(self.color_combo)
           self.setLayout(layout)
       
       def on_color_changed(self, color_name):
           """颜色选择变化时的处理"""
           color = FluentThemeColor[color_name].color()
           self.setStyleSheet(f"background-color: {color.name()}")
           
           # 可以通过信号通知其他组件
           print(f"选择的颜色: {color_name} - {color.name()}")

最佳实践
--------

1. **使用枚举** - 始终通过枚举访问颜色，避免硬编码
2. **主题适配** - 使用系统颜色确保主题切换时的一致性
3. **语义化** - 根据语义选择颜色（成功、警告、错误）
4. **可访问性** - 确保颜色对比度符合可访问性标准
5. **回退机制** - 使用工具函数提供颜色回退

注意事项
--------

- 主题色彩基于 Fluent Design 规范
- 系统颜色会自动适配亮色/暗色主题
- 颜色值使用十六进制格式
- 在主题切换时需要更新相关组件的颜色

相关模块
--------

- :doc:`common.style_sheet` - 样式表管理
- :doc:`common.config` - 配置管理
- :doc:`components.widgets` - UI组件
