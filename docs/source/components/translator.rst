Translator 翻译模块
====================

Translator 模块提供国际化翻译功能，支持多语言界面本地化。
该模块基于PySide6的QTranslator，为Fluent Widgets提供内置的翻译支持。

主要功能
--------

- **多语言支持** - 支持多种语言的界面翻译
- **自动加载** - 根据系统语言自动加载翻译文件
- **资源管理** - 使用Qt资源系统管理翻译文件
- **继承扩展** - 继承QTranslator提供额外功能
- **简单易用** - 提供简洁的API接口

核心组件
--------

FluentTranslator
~~~~~~~~~~~~~~~~

Fluent Widgets翻译器，继承自QTranslator。

.. code-block:: python

   from qfluentwidgets.common.translator import FluentTranslator
   from PySide6.QtCore import QLocale, QApplication
   from PySide6.QtWidgets import QWidget
   
   # 创建翻译器
   translator = FluentTranslator()
   
   # 使用指定语言
   chinese_translator = FluentTranslator(QLocale.Chinese)
   english_translator = FluentTranslator(QLocale.English)
   
   # 安装翻译器到应用
   app = QApplication.instance()
   app.installTranslator(translator)

**主要方法：**
- ``__init__()`` - 创建翻译器
- ``load()`` - 加载翻译文件

实际应用
--------

基本翻译设置
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.translator import FluentTranslator
   from PySide6.QtCore import QLocale, QApplication
   from PySide6.QtWidgets import QApplication, QWidget
   import sys
   
   class InternationalizedApp(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_translator()
           self.setup_ui()
       
       def setup_translator(self):
           """设置翻译器"""
           # 获取应用实例
           app = QApplication.instance()
           
           # 创建并安装翻译器
           self.translator = FluentTranslator()
           app.installTranslator(self.translator)
       
       def setup_ui(self):
           """设置UI"""
           from qfluentwidgets import PushButton, Label
           
           layout = QVBoxLayout()
           
           # 使用可翻译的文本
           self.button = PushButton(self.tr("Click Me"))
           self.label = Label(self.tr("Hello, World!"))
           
           layout.addWidget(self.button)
           layout.addWidget(self.label)
           self.setLayout(layout)
       
       def change_language(self, locale):
           """切换语言"""
           app = QApplication.instance()
           
           # 移除旧翻译器
           app.removeTranslator(self.translator)
           
           # 创建新翻译器
           self.translator = FluentTranslator(locale)
           app.installTranslator(self.translator)
           
           # 重新设置UI文本
           self.retranslate_ui()
       
       def retranslate_ui(self):
           """重新翻译UI"""
           self.button.setText(self.tr("Click Me"))
           self.label.setText(self.tr("Hello, World!"))

多语言切换
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.translator import FluentTranslator
   from qfluentwidgets import ComboBox, PushButton, FluentIcon
   from PySide6.QtCore import QLocale, QApplication
   
   class LanguageSwitcher(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_translator()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 语言选择下拉框
           self.language_combo = ComboBox()
           self.language_combo.addItems([
               "English",
               "中文",
               "日本語",
               "Español"
           ])
           self.language_combo.currentTextChanged.connect(self.change_language)
           
           # 测试按钮
           self.test_button = PushButton()
           self.test_button.setText(self.tr("Test Button"))
           
           layout.addWidget(self.language_combo)
           layout.addWidget(self.test_button)
           self.setLayout(layout)
       
       def setup_translator(self):
           """设置翻译器"""
           self.app = QApplication.instance()
           self.translator = FluentTranslator()
           self.app.installTranslator(self.translator)
           
           # 语言映射
           self.language_map = {
               "English": QLocale.English,
               "中文": QLocale.Chinese,
               "日本語": QLocale.Japanese,
               "Español": QLocale.Spanish
           }
       
       def change_language(self, language_text):
           """切换语言"""
           locale = self.language_map.get(language_text, QLocale.English)
           
           # 移除旧翻译器
           self.app.removeTranslator(self.translator)
           
           # 创建新翻译器
           self.translator = FluentTranslator(locale)
           self.app.installTranslator(self.translator)
           
           # 重新翻译UI
           self.retranslate_ui()
       
       def retranslate_ui(self):
           """重新翻译UI"""
           self.test_button.setText(self.tr("Test Button"))

高级用法
--------

自定义翻译器
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.translator import FluentTranslator
   from PySide6.QtCore import QLocale, QTranslator
   import os
   
   class CustomTranslator(FluentTranslator):
       """自定义翻译器"""
       
       def __init__(self, locale=None, parent=None):
           super().__init__(locale, parent)
           self.custom_translations = {}
           self.load_custom_translations()
       
       def load_custom_translations(self):
           """加载自定义翻译"""
           # 加载自定义翻译文件
           custom_qm_path = "translations/custom.qm"
           if os.path.exists(custom_qm_path):
               self.load(custom_qm_path)
       
       def add_custom_translation(self, source_text, translation):
           """添加自定义翻译"""
           self.custom_translations[source_text] = translation
       
       def translate(self, context, source_text, disambiguation=None, n=-1):
           """重写翻译方法"""
           # 先尝试自定义翻译
           if source_text in self.custom_translations:
               return self.custom_translations[source_text]
           
           # 使用默认翻译
           return super().translate(context, source_text, disambiguation, n)
   
   # 使用自定义翻译器
   custom_translator = CustomTranslator(QLocale.Chinese)
   custom_translator.add_custom_translation("Custom Text", "自定义文本")

动态翻译加载
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.translator import FluentTranslator
   from PySide6.QtCore import QLocale, QCoreApplication
   import requests
   
   class DynamicTranslator(FluentTranslator):
       """动态翻译器"""
       
       def __init__(self, locale=None, parent=None):
           super().__init__(locale, parent)
           self.online_translations = {}
           self.load_online_translations()
       
       def load_online_translations(self):
           """加载在线翻译"""
           # 这里可以实现从服务器加载翻译的逻辑
           # 示例：从API获取翻译
           try:
               translations = self.fetch_translations_from_api()
               self.online_translations.update(translations)
           except Exception as e:
               print(f"加载在线翻译失败: {e}")
       
       def fetch_translations_from_api(self):
           """从API获取翻译"""
           # 示例API调用
           api_url = "https://api.example.com/translations"
           params = {
               'locale': self.locale.name(),
               'module': 'qfluentwidgets'
           }
           
           response = requests.get(api_url, params=params)
           if response.status_code == 200:
               return response.json()
           return {}
       
       def translate(self, context, source_text, disambiguation=None, n=-1):
           """重写翻译方法"""
           # 先尝试在线翻译
           key = f"{context}:{source_text}"
           if key in self.online_translations:
               return self.online_translations[key]
           
           # 使用默认翻译
           return super().translate(context, source_text, disambiguation, n)

翻译管理器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.translator import FluentTranslator
   from PySide6.QtCore import QLocale, QCoreApplication, QObject, Signal
   
   class TranslationManager(QObject):
       """翻译管理器"""
       
       languageChanged = Signal(QLocale)
       
       def __init__(self):
           super().__init__()
           self.current_locale = QLocale()
           self.translator = None
           self.available_languages = {}
           self.setup_available_languages()
       
       def setup_available_languages(self):
           """设置可用语言"""
           self.available_languages = {
               'en': QLocale.English,
               'zh_CN': QLocale.Chinese,
               'ja': QLocale.Japanese,
               'es': QLocale.Spanish,
               'fr': QLocale.French,
               'de': QLocale.German
           }
       
       def set_language(self, locale):
           """设置语言"""
           if locale == self.current_locale:
               return
           
           app = QCoreApplication.instance()
           
           # 移除旧翻译器
           if self.translator:
               app.removeTranslator(self.translator)
           
           # 安装新翻译器
           self.translator = FluentTranslator(locale)
           app.installTranslator(self.translator)
           
           self.current_locale = locale
           self.languageChanged.emit(locale)
       
       def set_language_by_code(self, language_code):
           """通过语言代码设置语言"""
           locale = self.available_languages.get(language_code, QLocale.English)
           self.set_language(locale)
       
       def get_current_language(self):
           """获取当前语言"""
           return self.current_locale
       
       def get_available_languages(self):
           """获取可用语言列表"""
           return list(self.available_languages.keys())
       
       def is_language_available(self, language_code):
           """检查语言是否可用"""
           return language_code in self.available_languages
       
       def get_language_name(self, language_code):
           """获取语言名称"""
           locale = self.available_languages.get(language_code)
           if locale:
               return locale.nativeLanguageName()
           return language_code

最佳实践
--------

1. **资源管理** - 正确管理翻译器的生命周期
2. **性能优化** - 避免频繁切换语言
3. **错误处理** - 处理翻译文件加载失败的情况
4. **用户体验** - 提供语言切换的反馈
5. **测试覆盖** - 测试所有支持的语言

注意事项
--------

- 翻译文件必须正确打包到Qt资源中
- 翻译器安装后需要重新设置UI文本
- 某些语言可能需要特殊的字体支持
- 翻译文件的大小会影响应用启动时间
- 动态翻译可能影响应用性能

相关模块
--------

- :doc:`common.config` - 配置管理
- :doc:`components.widgets` - UI组件
- :doc:`components.window` - 窗口管理
