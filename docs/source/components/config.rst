Config 配置管理模块
====================

Config 模块提供完整的配置管理系统，支持类型安全的配置项、验证器、序列化器和持久化存储。
该模块确保应用配置的一致性和可靠性，提供灵活的配置管理方案。

主要功能
--------

- **类型安全配置** - 支持多种数据类型的配置项
- **配置验证** - 内置多种验证器确保数据有效性
- **序列化支持** - 自动序列化和反序列化配置值
- **持久化存储** - 自动保存和加载配置文件
- **信号通知** - 配置变化时自动通知相关组件

核心组件
--------

Theme
~~~~~

主题枚举，定义应用的主题模式。

.. code-block:: python

   from qfluentwidgets.common.config import Theme
   
   # 主题类型
   theme = Theme.LIGHT     # 亮色主题
   theme = Theme.DARK      # 暗色主题
   theme = Theme.AUTO      # 跟随系统主题

**使用示例：**

.. code-block:: python

   from qfluentwidgets import setTheme, Theme
   
   # 设置主题
   setTheme(Theme.DARK)
   setTheme(Theme.LIGHT)
   setTheme(Theme.AUTO)

WindowEffect
~~~~~~~~~~~~

窗口效果枚举，定义窗口的视觉效果。

.. code-block:: python

   from qfluentwidgets.common.config import WindowEffect
   
   # 窗口效果
   effect = WindowEffect.MICA       # 云母效果
   effect = WindowEffect.ACRYLIC    # 亚克力效果
   effect = WindowEffect.DISABLE    # 禁用效果

ConfigValidator
~~~~~~~~~~~~~~

配置验证器基类，提供配置值验证接口。

.. code-block:: python

   from qfluentwidgets.common.config import ConfigValidator
   
   class CustomValidator(ConfigValidator):
       def validate(self, value):
           """验证值是否合法"""
           return isinstance(value, str) and len(value) > 0
       
       def correct(self, value):
           """修正非法值"""
           return value if self.validate(value) else "default"

内置验证器
----------

RangeValidator
~~~~~~~~~~~~~~

范围验证器，确保数值在指定范围内。

.. code-block:: python

   from qfluentwidgets.common.config import RangeValidator
   
   # 创建范围验证器
   validator = RangeValidator(0, 100)  # 0-100的范围
   
   # 验证值
   is_valid = validator.validate(50)   # True
   is_valid = validator.validate(150)  # False
   
   # 修正值
   corrected = validator.correct(150)  # 100
   corrected = validator.correct(-10)  # 0

OptionsValidator
~~~~~~~~~~~~~~~

选项验证器，确保值在预定义选项中。

.. code-block:: python

   from qfluentwidgets.common.config import OptionsValidator
   
   # 创建选项验证器
   validator = OptionsValidator(["small", "medium", "large"])
   
   # 验证值
   is_valid = validator.validate("medium")  # True
   is_valid = validator.validate("extra")  # False
   
   # 修正值
   corrected = validator.correct("extra")  # "small" (第一个选项)

BoolValidator
~~~~~~~~~~~~~

布尔值验证器，专门用于布尔类型配置。

.. code-block:: python

   from qfluentwidgets.common.config import BoolValidator
   
   validator = BoolValidator()
   
   is_valid = validator.validate(True)   # True
   is_valid = validator.validate("yes")  # False
   
   corrected = validator.correct("yes")  # False

FolderValidator
~~~~~~~~~~~~~~~

文件夹验证器，确保文件夹路径存在。

.. code-block:: python

   from qfluentwidgets.common.config import FolderValidator
   
   validator = FolderValidator()
   
   # 验证文件夹是否存在
   is_valid = validator.validate("/path/to/folder")
   
   # 自动创建文件夹
   corrected = validator.correct("/new/path")  # 创建并返回路径

FolderListValidator
~~~~~~~~~~~~~~~~~~~

文件夹列表验证器，验证多个文件夹路径。

.. code-block:: python

   from qfluentwidgets.common.config import FolderListValidator
   
   validator = FolderListValidator()
   
   folders = ["/path1", "/path2", "/path3"]
   is_valid = validator.validate(folders)
   
   # 过滤存在的文件夹
   corrected = validator.correct(folders)

ColorValidator
~~~~~~~~~~~~~~

颜色验证器，确保颜色值有效。

.. code-block:: python

   from qfluentwidgets.common.config import ColorValidator
   from PySide6.QtGui import QColor
   
   validator = ColorValidator("#FF0000")  # 默认红色
   
   is_valid = validator.validate("#00FF00")  # True
   is_valid = validator.validate("invalid")  # False
   
   corrected = validator.correct("invalid")  # 返回默认颜色

ConfigSerializer
~~~~~~~~~~~~~~~

配置序列化器基类，提供序列化接口。

.. code-block:: python

   from qfluentwidgets.common.config import ConfigSerializer
   
   class CustomSerializer(ConfigSerializer):
       def serialize(self, value):
           """序列化配置值"""
           return str(value)
       
       def deserialize(self, value):
           """反序列化配置值"""
           return int(value)

内置序列化器
----------

EnumSerializer
~~~~~~~~~~~~~

枚举序列化器，处理枚举类型的配置。

.. code-block:: python

   from qfluentwidgets.common.config import EnumSerializer, Theme
   
   serializer = EnumSerializer(Theme)
   
   # 序列化
   serialized = serializer.serialize(Theme.DARK)  # "Dark"
   
   # 反序列化
   deserialized = serializer.deserialize("Dark")  # Theme.DARK

ColorSerializer
~~~~~~~~~~~~~~

颜色序列化器，处理QColor类型的配置。

.. code-block:: python

   from qfluentwidgets.common.config import ColorSerializer
   from PySide6.QtGui import QColor
   
   serializer = ColorSerializer()
   
   color = QColor(255, 0, 0)
   
   # 序列化
   serialized = serializer.serialize(color)  # "#FFFF0000"
   
   # 反序列化
   deserialized = serializer.deserialize("#FFFF0000")  # QColor(255, 0, 0)

ConfigItem
~~~~~~~~~~

配置项类，表示单个配置项。

.. code-block:: python

   from qfluentwidgets.common.config import ConfigItem, RangeValidator
   
   # 创建配置项
   max_connections = ConfigItem(
       group="Network",
       name="maxConnections",
       default=10,
       validator=RangeValidator(1, 100),
       restart=False
   )
   
   # 获取值
   value = max_connections.value
   
   # 设置值
   max_connections.value = 20
   
   # 监听变化
   max_connections.valueChanged.connect(lambda v: print(f"新值: {v}"))

专用配置项
----------

RangeConfigItem
~~~~~~~~~~~~~~~

范围配置项，专门用于数值范围配置。

.. code-block:: python

   from qfluentwidgets.common.config import RangeConfigItem
   
   # 创建范围配置项
   volume = RangeConfigItem(
       group="Audio",
       name="volume",
       default=50,
       validator=RangeValidator(0, 100)
   )
   
   print(f"音量范围: {volume.range}")
   print(f"当前音量: {volume.value}")

OptionsConfigItem
~~~~~~~~~~~~~~~~~

选项配置项，专门用于多选一配置。

.. code-block:: python

   from qfluentwidgets.common.config import OptionsConfigItem
   
   # 创建选项配置项
   quality = OptionsConfigItem(
       group="Video",
       name="quality",
       default="HD",
       validator=OptionsValidator(["SD", "HD", "Full HD", "4K"])
   )
   
   print(f"可用选项: {quality.options}")
   print(f"当前质量: {quality.value}")

ColorConfigItem
~~~~~~~~~~~~~~~

颜色配置项，专门用于颜色配置。

.. code-block:: python

   from qfluentwidgets.common.config import ColorConfigItem
   
   # 创建颜色配置项
   theme_color = ColorConfigItem(
       group="Theme",
       name="primaryColor",
       default="#0078D7"
   )
   
   print(f"主题颜色: {theme_color.value.name()}")

QConfig
~~~~~~~

全局配置管理器，管理所有配置项。

.. code-block:: python

   from qfluentwidgets.common.config import qconfig, ConfigItem
   
   # 创建配置项
   app_name = ConfigItem("App", "name", "MyApp")
   app_version = ConfigItem("App", "version", "1.0.0")
   
   # 使用全局配置
   print(f"应用名称: {qconfig.get(app_name)}")
   print(f"应用版本: {qconfig.get(app_version)}")
   
   # 设置配置
   qconfig.set(app_name, "NewApp")
   
   # 保存配置
   qconfig.save()
   
   # 监听应用重启信号
   qconfig.appRestartSig.connect(lambda: print("需要重启应用"))

实际应用
--------

应用配置管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.config import (
       qconfig, ConfigItem, RangeConfigItem, 
       ColorConfigItem, OptionsConfigItem,
       Theme, WindowEffect
   )
   
   class AppConfig:
       # 主题配置
       theme = ConfigItem("Theme", "mode", Theme.AUTO)
       window_effect = ConfigItem("Window", "effect", WindowEffect.MICA)
       primary_color = ColorConfigItem("Theme", "primaryColor", "#0078D7")
       
       # 界面配置
       window_opacity = RangeConfigItem("Window", "opacity", 100, RangeValidator(50, 100))
       font_size = RangeConfigItem("Font", "size", 12, RangeValidator(8, 24))
       
       # 功能配置
       auto_save = ConfigItem("Features", "autoSave", True)
       recent_files_count = RangeConfigItem("Features", "recentFiles", 10, RangeValidator(0, 50))
       
       # 网络配置
       server_url = ConfigItem("Network", "serverUrl", "https://api.example.com")
       timeout = RangeConfigItem("Network", "timeout", 30, RangeValidator(5, 300))
   
   # 使用配置
   print(f"当前主题: {AppConfig.theme.value}")
   print(f"窗口透明度: {AppConfig.window_opacity.value}%")
   
   # 修改配置
   AppConfig.window_opacity.value = 80
   AppConfig.auto_save.value = True

配置界面集成
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets import (
       SwitchSettingCard, RangeSettingCard, 
       ComboBoxSettingCard, ColorSettingCard
   )
   
   def create_settings_interface():
       """创建设置界面"""
       
       # 自动保存开关
       auto_save_card = SwitchSettingCard(
           "自动保存",
           "编辑时自动保存文件",
           "qfluentwidgets.common.config.AppConfig.auto_save"
       )
       
       # 字体大小滑块
       font_size_card = RangeSettingCard(
           "字体大小",
           "调整界面字体大小",
           "qfluentwidgets.common.config.AppConfig.font_size"
       )
       
       # 主题颜色选择
       color_card = ColorSettingCard(
           "主题颜色",
           "选择应用的主题颜色",
           "qfluentwidgets.common.config.AppConfig.primary_color"
       )
       
       return [auto_save_card, font_size_card, color_card]

配置文件管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.config import qconfig
   import json
   
   def export_config():
       """导出配置到文件"""
       config_data = {}
       
       # 收集所有配置项
       for item in qconfig.items:
           config_data[f"{item.group}.{item.name}"] = item.value
       
       # 保存到文件
       with open("config_export.json", "w", encoding="utf-8") as f:
           json.dump(config_data, f, indent=2, ensure_ascii=False)
   
   def import_config(file_path):
       """从文件导入配置"""
       with open(file_path, "r", encoding="utf-8") as f:
           config_data = json.load(f)
       
       # 应用配置
       for key, value in config_data.items():
           group, name = key.split(".", 1)
           
           # 查找对应的配置项
           for item in qconfig.items:
               if item.group == group and item.name == name:
                   item.value = value
                   break
       
       # 保存配置
       qconfig.save()

最佳实践
--------

1. **分组管理** - 使用有意义的分组名称组织配置项
2. **类型安全** - 使用适当的验证器和序列化器
3. **默认值** - 为所有配置项提供合理的默认值
4. **文档说明** - 为配置项提供清晰的说明
5. **版本兼容** - 考虑配置文件的版本兼容性

注意事项
--------

- 配置文件自动保存在用户目录
- 配置项名称应该唯一且有意义
- 复杂类型需要自定义序列化器
- 重启标记的配置项修改后需要重启应用

相关模块
--------

- :doc:`common.style_sheet` - 样式表管理
- :doc:`common.color` - 颜色管理
- :doc:`components.settings` - 设置组件
