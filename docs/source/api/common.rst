Common 模块 API
================

Common 模块是 PySide6-Fluent-Widgets 的基础设施，提供整个组件库的基础功能。
这些基础功能确保了所有组件的一致性和可扩展性。

主要功能：
- 动画引擎和过渡效果
- 颜色管理和主题系统
- 配置管理和持久化
- 图标管理和资源加载
- 样式表管理和主题切换
- 国际化支持

使用方法：
.. code-block:: python

   from qfluentwidgets.common import qconfig, Theme, setTheme, FluentIcon
   
   # 主题管理
   setTheme(Theme.DARK)
   
   # 配置管理
   qconfig.set('theme_color', '#0078d4')
   
   # 图标使用
   icon = FluentIcon.SETTING

.. automodule:: qfluentwidgets.common
   :members:
   :undoc-members:
   :show-inheritance:

Animation
---------

动画引擎模块，提供平滑的过渡效果和动画功能。

主要功能：
- AnimationBase：动画基类
- FluentAnimation：Fluent 风格动画
- 各种动画效果：平移、缩放、透明度、旋转等

支持缓动函数和动画链，提供流畅的用户体验。

.. automodule:: qfluentwidgets.common.animation
   :members:
   :undoc-members:
   :show-inheritance:

Color
-----

颜色管理模块，实现主题色彩系统。

主要功能：
- Fluent Design 色彩规范
- 亮色/暗色主题自动切换
- 自定义主题色支持
- 颜色对比度计算

确保应用在不同主题下都有良好的视觉效果。

.. automodule:: qfluentwidgets.common.color
   :members:
   :undoc-members:
   :show-inheritance:

Config
------

配置管理模块，提供应用配置的持久化存储。

主要功能：
- qconfig：全局配置对象
- 多种配置类型：字符串、数字、颜色、文件夹等
- 配置验证和序列化
- 自动保存和加载

支持配置文件的导入导出，便于用户迁移设置。

.. automodule:: qfluentwidgets.common.config
   :members:
   :undoc-members:
   :show-inheritance:

Icon
----

图标管理模块，提供统一的图标加载和管理。

主要功能：
- FluentIcon：内置图标集合
- 多尺寸和主题适配
- 图标缓存和按需加载
- 自定义图标支持

提供完整的 Fluent Design 图标库，支持 SVG 和位图格式。

.. automodule:: qfluentwidgets.common.icon
   :members:
   :undoc-members:
   :show-inheritance:

Style Sheet
-----------

样式表管理模块，实现 QSS 样式的动态管理。

主要功能：
- FluentStyleSheet：样式表管理器
- 动态样式切换
- 主题样式自动应用
- 自定义样式支持

确保所有组件的视觉一致性，支持运行时样式切换。

.. automodule:: qfluentwidgets.common.style_sheet
   :members:
   :undoc-members:
   :show-inheritance:

Font
----

字体管理模块，提供字体检测和加载功能。

主要功能：
- 系统字体检测
- 自定义字体配置
- 字体回退机制
- 多语言字体支持

确保应用在不同系统上都有良好的字体显示效果。

.. automodule:: qfluentwidgets.common.font
   :members:
   :undoc-members:
   :show-inheritance:

Image Utils
-----------

.. automodule:: qfluentwidgets.common.image_utils
   :members:
   :undoc-members:
   :show-inheritance:

Router
------

.. automodule:: qfluentwidgets.common.router
   :members:
   :undoc-members:
   :show-inheritance:

Screen
------

.. automodule:: qfluentwidgets.common.screen
   :members:
   :undoc-members:
   :show-inheritance:

Smooth Scroll
-------------

.. automodule:: qfluentwidgets.common.smooth_scroll
   :members:
   :undoc-members:
   :show-inheritance:

Theme Listener
--------------

.. automodule:: qfluentwidgets.common.theme_listener
   :members:
   :undoc-members:
   :show-inheritance:

Translator
----------

.. automodule:: qfluentwidgets.common.translator
   :members:
   :undoc-members:
   :show-inheritance:
