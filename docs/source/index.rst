.. PySide6-Fluent-Widgets 中文文档主文件

.. raw:: html

   <p align="center">
      <img width="18%" align="center" src="./_static/logo.png" alt="logo">
   </p>

   <h1 align="center">
      PySide6-Fluent-Widgets
   </h1>

   <hr/>

   <p align="center">
      基于 PySide6 的 Fluent Design 风格组件库
   </p>

   <p align="center">
      <a style="text-decoration:none">
         <img src="https://img.shields.io/badge/Platform-Win32%20|%20Linux%20|%20macOS-blue?color=#4ec820" alt="Platform Win32 | Linux | macOS"/>
      </a>

      <a style="text-decoration:none">
         <img src="https://static.pepy.tech/personalized-badge/pyqt-fluent-widgets?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads" alt="Download"/>
      </a>

      <a style="text-decoration:none">
         <img src="https://img.shields.io/badge/License-LGPLv3-blue?color=#4ec820" alt="LGPLv3"/>
      </a>
   </p>

   <p align="center">
      <img src="./_static/Interface.jpg" alt="Interface">
   </p>


欢迎使用 PySide6-Fluent-Widgets 中文文档！
==========================================

本文档将为您介绍 PySide6-Fluent-Widgets 的所有功能特性和最佳实践。

.. toctree::
   :maxdepth: 2
   :caption: 目录

   introduction
   architecture
   api/index
   components/index
   code_examples/index

项目介绍
--------

PySide6-Fluent-Widgets 是一个基于 PySide6 的 Fluent Design 风格组件库。
它提供了丰富的现代化 UI 组件，帮助开发者快速构建美观的应用程序。

主要特性
--------

* **现代化设计**: 采用 Microsoft Fluent Design 设计语言
* **丰富组件**: 提供按钮、输入框、对话框、导航等常用组件
* **主题支持**: 支持亮色/暗色主题切换
* **易于使用**: 简洁的 API 设计，易于集成到现有项目
* **中文友好**: 完整的中文文档和示例

快速开始
--------

.. code-block:: python

   from qfluentwidgets import *
   from PySide6.QtWidgets import QApplication, QMainWindow

   app = QApplication([])
   window = QMainWindow()
   
   # 创建一个按钮
   button = PushButton('点击我')
   window.setCentralWidget(button)
   
   window.show()
   app.exec()

目录结构
--------

* :doc:`introduction` - 项目介绍和快速开始
* :doc:`architecture` - 架构概览
* :doc:`api/index` - API 参考文档
* :doc:`components/index` - 组件使用指南
* :doc:`code_examples/index` - 示例代码

索引和表格
----------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
