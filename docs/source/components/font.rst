Font 字体管理模块
==================

Font 模块提供完整的字体管理系统，支持字体族设置、字体创建和样式表生成。
该模块确保应用在不同平台上都有一致的字体显示效果，支持中英文混合显示。

主要功能
--------

- **字体族管理** - 统一设置应用字体族
- **字体创建** - 创建标准化的字体对象
- **样式表生成** - 将字体转换为QSS样式表
- **配置持久化** - 支持字体配置的保存和加载
- **跨平台支持** - 自动适配不同操作系统的字体

核心函数
--------

setFontFamilies()
~~~~~~~~~~~~~~~~

设置应用使用的字体族。

.. code-block:: python

   from qfluentwidgets.common.font import setFontFamilies
   
   # 设置字体族
   setFontFamilies(['Segoe UI', 'Microsoft YaHei', 'PingFang SC'])
   
   # 保存到配置文件
   setFontFamilies(['Arial', 'SimHei'], save=True)

**参数说明：**
- ``families`` - 字体族名称列表，按优先级排序
- ``save`` - 是否保存到配置文件，默认为False

**默认字体族：**
- Windows: Segoe UI, Microsoft YaHei, PingFang SC
- macOS: PingFang SC, Helvetica Neue, Arial
- Linux: Ubuntu, Noto Sans CJK, Arial

fontFamilies()
~~~~~~~~~~~~~

获取当前设置的字体族。

.. code-block:: python

   from qfluentwidgets.common.font import fontFamilies
   
   # 获取字体族列表
   families = fontFamilies()
   print(f"当前字体族: {families}")

setFont()
~~~~~~~~~

为控件设置字体。

.. code-block:: python

   from qfluentwidgets.common.font import setFont
   from qfluentwidgets import PushButton, Label
   from PySide6.QtGui import QFont
   
   # 创建控件
   button = PushButton("按钮")
   label = Label("标签")
   
   # 设置字体
   setFont(button, fontSize=16, weight=QFont.Bold)
   setFont(label, fontSize=12, weight=QFont.Normal)

**参数说明：**
- ``widget`` - 要设置字体的控件
- ``fontSize`` - 字体像素大小，默认为14
- ``weight`` - 字体粗细，默认为QFont.Normal

getFont()
~~~~~~~~~

创建字体对象。

.. code-block:: python

   from qfluentwidgets.common.font import getFont
   from PySide6.QtGui import QFont
   
   # 创建不同大小的字体
   small_font = getFont(fontSize=12)
   medium_font = getFont(fontSize=14)
   large_font = getFont(fontSize=18)
   
   # 创建不同粗细的字体
   bold_font = getFont(fontSize=14, weight=QFont.Bold)
   light_font = getFont(fontSize=14, weight=QFont.Light)

fontStyleSheet()
~~~~~~~~~~~~~~~~

将字体对象转换为QSS样式表。

.. code-block:: python

   from qfluentwidgets.common.font import getFont, fontStyleSheet
   
   # 创建字体
   font = getFont(fontSize=16, weight=QFont.Bold)
   
   # 生成样式表
   font_qss = fontStyleSheet(font)
   print(f"字体样式表: {font_qss}")
   
   # 应用到控件
   widget.setStyleSheet(f"""
       QLabel {{
           {font_qss}
           color: #333333;
       }}
   """)

实际应用
--------

全局字体设置
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.font import setFontFamilies, getFont
   from qfluentwidgets import setTheme, Theme
   import sys
   
   def setup_application_font():
       """设置应用全局字体"""
       
       # 根据平台设置合适的字体族
       if sys.platform == 'win32':
           families = ['Microsoft YaHei UI', 'Microsoft YaHei', 'Segoe UI']
       elif sys.platform == 'darwin':
           families = ['PingFang SC', 'Helvetica Neue', 'Arial']
       else:
           families = ['Noto Sans CJK SC', 'Ubuntu', 'Arial']
       
       setFontFamilies(families, save=True)
       print(f"已设置字体族: {families}")
   
   def get_theme_font():
       """根据主题获取合适的字体"""
       from qfluentwidgets.common.config import qconfig
       
       # 亮色主题使用正常粗细
       if qconfig.theme == Theme.LIGHT:
           return getFont(fontSize=14, weight=QFont.Normal)
       # 暗色主题使用稍粗的字体
       else:
           return getFont(fontSize=14, weight=QFont.Medium)

控件字体管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.font import setFont, getFont, fontStyleSheet
   from qfluentwidgets import PushButton, Label, CardWidget
   from PySide6.QtGui import QFont
   
   class StyledWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           
       def setup_ui(self):
           # 标题标签
           title = Label("标题")
           setFont(title, fontSize=18, weight=QFont.Bold)
           
           # 正文标签
           content = Label("这是正文内容")
           setFont(content, fontSize=14, weight=QFont.Normal)
           
           # 按钮
           button = PushButton("确定")
           setFont(button, fontSize=12, weight=QFont.Normal)
           
           # 使用样式表设置字体
           subtitle = Label("副标题")
           subtitle_font = getFont(fontSize=16, weight=QFont.Medium)
           subtitle.setStyleSheet(f"""
               QLabel {{
                   {fontStyleSheet(subtitle_font)}
                   color: #666666;
                   margin: 8px 0;
               }}
           """)

动态字体调整
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.font import setFont, getFont
   from qfluentwidgets import Slider, Label, QVBoxLayout, QWidget
   
   class FontAdjustWidget(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 字体大小滑块
           self.size_slider = Slider()
           self.size_slider.setRange(8, 32)
           self.size_slider.setValue(14)
           self.size_slider.valueChanged.connect(self.update_font_size)
           
           # 示例标签
           self.sample_label = Label("示例文本")
           setFont(self.sample_label, fontSize=14)
           
           layout.addWidget(self.size_slider)
           layout.addWidget(self.sample_label)
           self.setLayout(layout)
       
       def update_font_size(self, size):
           """更新字体大小"""
           setFont(self.sample_label, fontSize=size)

字体主题适配
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.font import getFont, fontStyleSheet
   from qfluentwidgets.common.config import qconfig, Theme
   
   class ThemeAwareFont:
       def __init__(self):
           self.update_font()
           qconfig.themeChanged.connect(self.update_font)
           
       def update_font(self):
           """根据主题更新字体"""
           if qconfig.theme == Theme.DARK:
               # 暗色主题使用稍粗的字体
               self.title_font = getFont(fontSize=18, weight=QFont.Medium)
               self.body_font = getFont(fontSize=14, weight=QFont.Normal)
           else:
               # 亮色主题使用正常粗细
               self.title_font = getFont(fontSize=18, weight=QFont.Normal)
               self.body_font = getFont(fontSize=14, weight=QFont.Normal)
       
       def get_title_style(self):
           """获取标题样式"""
           return f"""
               QLabel {{
                   {fontStyleSheet(self.title_font)}
                   color: #333333;
               }}
           """
       
       def get_body_style(self):
           """获取正文样式"""
           return f"""
               QLabel {{
                   {fontStyleSheet(self.body_font)}
                   color: #666666;
               }}
           """

字体配置管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.font import setFontFamilies, fontFamilies
   from qfluentwidgets.common.config import qconfig
   import json
   
   def export_font_config():
       """导出字体配置"""
       config = {
           'font_families': fontFamilies(),
           'font_size': qconfig.get(qconfig.fontSize),
           'font_weight': qconfig.get(qconfig.fontWeight)
       }
       
       with open('font_config.json', 'w', encoding='utf-8') as f:
           json.dump(config, f, indent=2, ensure_ascii=False)
   
   def import_font_config(file_path):
       """导入字体配置"""
       with open(file_path, 'r', encoding='utf-8') as f:
           config = json.load(f)
       
       # 应用字体配置
       setFontFamilies(config['font_families'], save=True)
       qconfig.set(qconfig.fontSize, config['font_size'])
       qconfig.set(qconfig.fontWeight, config['font_weight'])

最佳实践
--------

1. **字体族选择** - 选择跨平台兼容性好的字体族
2. **字体大小** - 使用像素大小而非点大小确保一致性
3. **字体粗细** - 根据内容层次选择合适的字体粗细
4. **配置保存** - 重要的字体配置应该保存到配置文件
5. **主题适配** - 根据主题调整字体样式

注意事项
--------

- 字体族按优先级排序，系统会使用第一个可用的字体
- 像素大小在不同DPI下可能需要调整
- 字体粗细在不同平台上的显示效果可能不同
- 中文字体通常需要比英文字体更大的字号

相关模块
--------

- :doc:`common.config` - 配置管理
- :doc:`common.style_sheet` - 样式表管理
- :doc:`components.widgets` - UI组件
