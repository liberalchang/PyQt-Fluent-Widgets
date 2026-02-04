API 参考文档
=============

本节包含 PySide6-Fluent-Widgets 的完整 API 文档，按模块组织。

.. toctree::
   :maxdepth: 2
   :caption: API 文档

   common
   components
   window
   multimedia

模块概览
--------

common 模块
~~~~~~~~~~~

通用工具和基础类，提供整个组件库的基础功能。

* :doc:`common` - 通用模块 API 文档

components 模块
~~~~~~~~~~~~~~~

UI 组件模块，包含所有可视化组件。

* :doc:`components` - 组件模块 API 文档

window 模块
~~~~~~~~~~~

窗口相关组件。

* :doc:`window` - 窗口模块 API 文档

multimedia 模块
~~~~~~~~~~~~~~~

多媒体相关组件。

* :doc:`multimedia` - 多媒体模块 API 文档

API 设计原则
------------

* **一致性**: 所有组件遵循统一的 API 设计规范
* **简洁性**: 提供简单易用的接口
* **可扩展**: 支持自定义和扩展
* **类型安全**: 提供类型提示

命名规范
--------

* **类名**: 使用 PascalCase，如 `PushButton`
* **方法名**: 使用 camelCase，如 `setFixedSize()`
* **常量**: 使用 UPPER_CASE，如 `Theme.LIGHT`
* **属性**: 使用 camelCase，如 `themeColor`

信号和槽
--------

所有组件都遵循 Qt 的信号槽机制：

.. code-block:: python

   button.clicked.connect(lambda: print("按钮被点击"))
   slider.valueChanged.connect(lambda value: print(f"值变为: {value}"))

样式系统
--------

组件支持 QSS 样式表和 Fluent Design 主题：

.. code-block:: python

   # 使用 QSS
   button.setStyleSheet("PushButton { background-color: #0078d4; }")
   
   # 使用主题 API
   from qfluentwidgets import setThemeColor
   setThemeColor('#0078d4')
