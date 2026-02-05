Style Sheet 样式表模块
========================

Style Sheet 模块提供完整的样式表管理系统，支持主题切换、自定义样式和动态样式更新。
该模块是PySide6-Fluent-Widgets的核心样式系统，确保所有组件在不同主题下都有一致的视觉效果。

主要功能
--------

- **样式表管理** - 统一管理控件的样式表
- **主题切换** - 支持亮色/暗色主题切换
- **自定义样式** - 支持用户自定义样式
- **模板系统** - 提供样式表模板和变量替换
- **动态更新** - 支持样式的动态更新和监听

核心组件
--------

StyleSheetManager
~~~~~~~~~~~~~~~~~

样式表管理器，负责管理所有控件的样式表。

.. code-block:: python

   from qfluentwidgets.common.style_sheet import styleSheetManager, StyleSheetFile
   from qfluentwidgets import PushButton
   
   # 创建按钮
   button = PushButton("按钮")
   
   # 注册样式表
   styleSheetManager.register("custom.qss", button)
   
   # 获取控件的样式表源
   source = styleSheetManager.source(button)

**主要方法：**
- ``register()`` - 注册控件到管理器
- ``deregister()`` - 从管理器中移除控件
- ``source()`` - 获取控件的样式表源
- ``items()`` - 获取所有注册的控件

FluentStyleSheet
~~~~~~~~~~~~~~~~

Fluent样式表枚举，提供内置的样式表。

.. code-block:: python

   from qfluentwidgets.common.style_sheet import FluentStyleSheet
   
   # 使用内置样式表
   menu_style = FluentStyleSheet.MENU
   button_style = FluentStyleSheet.BUTTON
   card_style = FluentStyleSheet.CARD_WIDGET
   
   # 获取样式表路径
   style_path = menu_style.path()

**内置样式表：**
- ``MENU`` - 菜单样式
- ``BUTTON`` - 按钮样式
- ``CARD_WIDGET`` - 卡片控件样式
- ``SLIDER`` - 滑块样式
- ``CHECK_BOX`` - 复选框样式
- ``RADIO_BUTTON`` - 单选按钮样式

ThemeColor
~~~~~~~~~~

主题颜色枚举，定义主题色彩变量。

.. code-block:: python

   from qfluentwidgets.common.style_sheet import ThemeColor
   
   # 主题颜色
   ThemeColor.PRIMARY      # 主色调
   ThemeColor.SECONDARY    # 次要色调
   ThemeColor.BACKGROUND   # 背景色
   ThemeColor.SURFACE      # 表面色
   ThemeColor.TEXT_PRIMARY # 主要文本色
   ThemeColor.TEXT_SECONDARY # 次要文本色

样式表基类
----------

StyleSheetBase
~~~~~~~~~~~~~~

样式表基类，提供样式表的基础功能。

.. code-block:: python

   from qfluentwidgets.common.style_sheet import StyleSheetBase
   
   class CustomStyle(StyleSheetBase):
       def __init__(self, style_content):
           self.content = style_content
       
       def path(self, theme=None):
           return self.content
       
       def apply(self, widget, theme=None):
           widget.setStyleSheet(self.content)

StyleSheetFile
~~~~~~~~~~~~~~

样式表文件类，用于加载QSS文件。

.. code-block:: python

   from qfluentwidgets.common.style_sheet import StyleSheetFile
   
   # 加载样式表文件
   style_file = StyleSheetFile("styles/custom.qss")
   
   # 应用到控件
   style_file.apply(button)
   
   # 获取文件路径
   path = style_file.path()

CustomStyleSheet
~~~~~~~~~~~~~~~~

自定义样式表类，支持动态样式设置。

.. code-block:: python

   from qfluentwidgets.common.style_sheet import CustomStyleSheet
   
   # 创建自定义样式表
   custom_style = CustomStyleSheet()
   
   # 设置亮色主题样式
   custom_style.setLightStyleSheet("""
       QPushButton {
           background-color: #0078d4;
           color: white;
           border-radius: 4px;
       }
   """)
   
   # 设置暗色主题样式
   custom_style.setDarkStyleSheet("""
       QPushButton {
           background-color: #404040;
           color: white;
           border-radius: 4px;
       }
   """)

实际应用
--------

基本样式应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.style_sheet import styleSheetManager, StyleSheetFile
   from qfluentwidgets import PushButton, CardWidget
   
   class StyledWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_styles()
       
       def setup_ui(self):
           # 创建控件
           self.button = PushButton("点击我")
           self.layout.addWidget(self.button)
       
       def setup_styles(self):
           """设置样式"""
           # 注册按钮样式
           styleSheetManager.register(
               "button_style.qss", 
               self.button
           )
           
           # 注册卡片样式
           styleSheetManager.register(
               "card_style.qss", 
               self
           )

主题切换
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.style_sheet import setTheme, Theme
   from qfluentwidgets import ToggleButton, SwitchButton
   
   class ThemeSwitcher(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           layout = QHBoxLayout()
           
           # 主题切换按钮
           self.theme_switch = ToggleButton("暗色主题")
           self.theme_switch.checkedChanged.connect(self.toggle_theme)
           
           layout.addWidget(self.theme_switch)
           self.setLayout(layout)
       
       def toggle_theme(self, checked):
           """切换主题"""
           if checked:
               setTheme(Theme.DARK, save=True)
           else:
               setTheme(Theme.LIGHT, save=True)

动态样式更新
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.style_sheet import CustomStyleSheet, styleSheetManager
   from PySide6.QtWidgets import QPushButton
   from PySide6.QtCore import QObject, Signal
   
   class DynamicStyleManager(QObject):
       """动态样式管理器"""
       
       styleChanged = Signal(str)
       
       def __init__(self):
           super().__init__()
           self.custom_styles = {}
       
       def create_dynamic_style(self, widget, style_name):
           """创建动态样式"""
           custom_style = CustomStyleSheet()
           
           # 设置样式
           custom_style.setLightStyleSheet(self.get_light_style(style_name))
           custom_style.setDarkStyleSheet(self.get_dark_style(style_name))
           
           # 注册到管理器
           styleSheetManager.register(custom_style, widget)
           
           # 保存引用
           self.custom_styles[widget] = custom_style
           
           return custom_style
       
       def update_style(self, widget, style_name):
           """更新样式"""
           if widget in self.custom_styles:
               custom_style = self.custom_styles[widget]
               custom_style.setLightStyleSheet(self.get_light_style(style_name))
               custom_style.setDarkStyleSheet(self.get_dark_style(style_name))
               
               # 触发重新应用样式
               widget.style().unpolish(widget)
               widget.style().polish(widget)
               widget.update()
               
               self.styleChanged.emit(style_name)
       
       def get_light_style(self, style_name):
           """获取亮色主题样式"""
           styles = {
               "primary": """
                   QPushButton {
                       background-color: #0078d4;
                       color: white;
                       border: none;
                       padding: 8px 16px;
                       border-radius: 4px;
                   }
               """,
               "secondary": """
                   QPushButton {
                       background-color: #f3f2f1;
                       color: #323130;
                       border: 1px solid #d2d0ce;
                       padding: 8px 16px;
                       border-radius: 4px;
                   }
               """
           }
           return styles.get(style_name, "")
       
       def get_dark_style(self, style_name):
           """获取暗色主题样式"""
           styles = {
               "primary": """
                   QPushButton {
                       background-color: #404040;
                       color: white;
                       border: none;
                       padding: 8px 16px;
                       border-radius: 4px;
                   }
               """,
               "secondary": """
                   QPushButton {
                       background-color: #292929;
                       color: white;
                       border: 1px solid #3d3d3d;
                       padding: 8px 16px;
                       border-radius: 4px;
                   }
               """
           }
           return styles.get(style_name, "")

高级用法
--------

样式表模板
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.style_sheet import QssTemplate, applyThemeColor
   
   # 创建样式表模板
   template_str = """
   QPushButton {
       background-color: --ThemeColorPrimary;
       color: --ThemeColorTextPrimary;
       border: 1px solid --ThemeColorBorder;
       padding: 8px 16px;
       border-radius: 4px;
       font-family: --FontFamilies;
   }
   
   QPushButton:hover {
       background-color: --ThemeColorPrimaryHover;
   }
   """
   
   # 应用主题颜色
   themed_qss = applyThemeColor(template_str)
   
   # 应用到控件
   button.setStyleSheet(themed_qss)

样式表组合
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.style_sheet import StyleSheetCompose, StyleSheetFile, CustomStyleSheet
   
   # 组合多个样式表
   base_style = StyleSheetFile("base.qss")
   custom_style = CustomStyleSheet()
   custom_style.setLightStyleSheet("/* 自定义亮色样式 */")
   
   # 创建组合样式
   composed_style = StyleSheetCompose([base_style, custom_style])
   
   # 应用到控件
   composed_style.apply(widget)

样式表监听
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.style_sheet import CustomStyleSheetWatcher
   from PySide6.QtCore import QEvent
   
   class StyleWatcher(QObject):
       """样式表监听器"""
       
       def __init__(self, widget):
           super().__init__()
           self.widget = widget
           self.setup_watcher()
       
       def setup_watcher(self):
           """设置监听器"""
           self.watcher = CustomStyleSheetWatcher(self.widget)
           self.widget.installEventFilter(self.watcher)
       
       def on_style_changed(self):
           """样式变化时的处理"""
           print("样式表已更新")
           # 可以在这里添加样式变化后的处理逻辑

性能优化
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.style_sheet import styleSheetManager
   from PySide6.QtWidgets import QWidget
   
   class OptimizedStyleWidget(QWidget):
       def __init__(self):
           super().__init__()
           self.style_cache = {}
           self.setup_optimized_style()
       
       def setup_optimized_style(self):
           """设置优化的样式"""
           # 预编译样式表
           self.precompile_styles()
       
       def precompile_styles(self):
           """预编译样式表"""
           styles = [
               "light_button.qss",
               "dark_button.qss",
               "light_card.qss",
               "dark_card.qss"
           ]
           
           for style in styles:
               # 预加载样式表
               if style not in self.style_cache:
                   with open(style, 'r', encoding='utf-8') as f:
                       self.style_cache[style] = f.read()
       
       def get_cached_style(self, style_name):
           """获取缓存的样式"""
           return self.style_cache.get(style_name, "")
       
       def apply_cached_style(self, widget, style_name):
           """应用缓存的样式"""
           style_content = self.get_cached_style(style_name)
           if style_content:
               widget.setStyleSheet(style_content)

最佳实践
--------

1. **样式分离** - 将样式表分离到独立的QSS文件中
2. **主题一致性** - 确保所有组件在不同主题下的一致性
3. **性能考虑** - 避免频繁的样式表更新
4. **缓存机制** - 对常用样式表进行缓存
5. **模块化设计** - 将样式表按功能模块化

注意事项
--------

- 样式表更新会影响控件性能
- 复杂的样式选择器会降低渲染性能
- 主题切换时需要重新应用所有样式表
- 自定义样式应该与内置样式保持一致

相关模块
--------

- :doc:`common.color` - 颜色管理
- :doc:`common.config` - 配置管理
- :doc:`common.font` - 字体管理
- :doc:`components.widgets` - UI组件
