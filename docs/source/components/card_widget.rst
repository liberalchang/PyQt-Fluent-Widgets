CardWidget 卡片控件模块
======================

CardWidget 模块提供各种样式的卡片控件，包括基础卡片、简单卡片、悬浮卡片、卡片分隔符、标题卡片、卡片组和组标题卡片等。该模块实现了Fluent Design的卡片样式，提供丰富的视觉效果和交互体验。

主要功能
--------

- **多种卡片样式** - 支持基础、简单、悬浮等多种卡片样式
- **点击交互** - 支持卡片点击事件和悬浮效果
- **阴影效果** - 悬浮卡片提供动态阴影和位移动画
- **标题支持** - 标题卡片支持标题和内容区域分离
- **分组功能** - 支持卡片分组和组管理
- **图标支持** - 卡片组支持图标显示
- **分隔符** - 提供卡片内容分隔功能

核心组件
--------

CardWidget
~~~~~~~~~~

基础卡片控件，提供标准的卡片功能和点击交互。

.. code-block:: python

   from qfluentwidgets.components.widgets.card_widget import CardWidget
   
   # 创建基础卡片
   card = CardWidget(parent=parent)
   
   # 设置边框圆角
   card.setBorderRadius(8)
   
   # 启用点击功能
   card.setClickEnabled(True)
   
   # 连接点击信号
   card.clicked.connect(self.on_card_clicked)

**构造函数：**
- ``CardWidget(parent: QWidget = None)``

**主要方法：**
- ``setBorderRadius(radius: int)`` - 设置边框圆角
- ``getBorderRadius()`` - 获取边框圆角
- ``setClickEnabled(isEnabled: bool)`` - 设置是否启用点击
- ``isClickEnabled()`` - 获取点击启用状态

**信号：**
- ``clicked`` - 卡片被点击时发出

**属性：**
- ``borderRadius`` - 边框圆角（int）

SimpleCardWidget
~~~~~~~~~~~~~~~~

简单卡片控件，提供简洁的卡片样式，无悬浮效果。

.. code-block:: python

   from qfluentwidgets.components.widgets.card_widget import SimpleCardWidget
   
   # 创建简单卡片
   simple_card = SimpleCardWidget(parent=parent)
   simple_card.setBorderRadius(6)

**构造函数：**
- ``SimpleCardWidget(parent: QWidget = None)``

**特点：**
- 无悬浮效果
- 简洁的边框样式
- 适合静态内容展示

ElevatedCardWidget
~~~~~~~~~~~~~~~~~~

悬浮卡片控件，提供阴影效果和悬浮动画。

.. code-block:: python

   from qfluentwidgets.components.widgets.card_widget import ElevatedCardWidget
   
   # 创建悬浮卡片
   elevated_card = ElevatedCardWidget(parent=parent)
   
   # 卡片会自动应用悬浮效果：
   # - 鼠标悬浮时显示阴影
   # - 鼠标悬浮时向上移动3像素
   # - 点击时恢复原位置

**构造函数：**
- ``ElevatedCardWidget(parent: QWidget = None)``

**特点：**
- 自动阴影效果
- 悬浮位移动画
- 圆角默认为8像素
- 100ms的平滑动画

CardSeparator
~~~~~~~~~~~~~

卡片分隔符控件，用于在卡片内部创建分隔线。

.. code-block:: python

   from qfluentwidgets.components.widgets.card_widget import CardSeparator
   
   # 创建分隔符
   separator = CardSeparator(parent=parent)
   separator.setFixedHeight(3)

**构造函数：**
- ``CardSeparator(parent: QWidget = None)``

**特点：**
- 固定高度3像素
- 适应主题颜色的分隔线
- 适合卡片内容分组

HeaderCardWidget
~~~~~~~~~~~~~~~~

标题卡片控件，提供标题区域和内容区域的分离布局。

.. code-block:: python

   from qfluentwidgets.components.widgets.card_widget import HeaderCardWidget
   
   # 创建标题卡片
   header_card = HeaderCardWidget("设置", parent=parent)
   
   # 获取内容区域
   content_widget = header_card.view
   
   # 在内容区域添加控件
   layout = QVBoxLayout(content_widget)
   layout.addWidget(QLabel("这里是内容区域"))

**构造函数：**
- ``HeaderCardWidget(parent: QWidget = None)``
- ``HeaderCardWidget(title: str, parent: QWidget = None)``

**主要方法：**
- ``setTitle(title: str)`` - 设置标题
- ``getTitle()`` - 获取标题

**属性：**
- ``title`` - 卡片标题（str）

**布局结构：**
- ``headerView`` - 标题区域（48像素高度）
- ``separator`` - 分隔线
- ``view`` - 内容区域

CardGroupWidget
~~~~~~~~~~~~~~~

卡片组控件，提供图标、标题和内容的组合显示。

.. code-block:: python

   from qfluentwidgets.components.widgets.card_widget import CardGroupWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建卡片组
   group = CardGroupWidget(FIF.SETTING, "系统设置", "配置系统参数", parent=parent)
   
   # 添加自定义控件
   button = QPushButton("打开设置")
   group.addWidget(button)
   
   # 修改内容
   group.setTitle("新标题")
   group.setContent("新描述")

**构造函数：**
- ``CardGroupWidget(icon: str | FluentIconBase | QIcon, title: str, content: str, parent: QWidget = None)``

**主要方法：**
- ``setTitle(title: str)`` - 设置标题
- ``title()`` - 获取标题
- ``setContent(content: str)`` - 设置内容描述
- ``content()`` - 获取内容描述
- ``setIcon(icon: str | FluentIconBase | QIcon)`` - 设置图标
- ``icon()`` - 获取图标
- ``setIconSize(size: QSize)`` - 设置图标大小
- ``addWidget(widget: QWidget, stretch=0)`` - 添加控件
- ``setSeparatorVisible(isVisible: bool)`` - 设置分隔符可见性
- ``isSeparatorVisible()`` - 获取分隔符可见性

GroupHeaderCardWidget
~~~~~~~~~~~~~~~~~~~~~

组标题卡片控件，用于管理多个CardGroupWidget的容器。

.. code-block:: python

   from qfluentwidgets.components.widgets.card_widget import GroupHeaderCardWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建组标题卡片
   group_card = GroupHeaderCardWidget("应用程序", parent=parent)
   
   # 添加分组
   group1 = group_card.addGroup(FIF.BROWSER, "浏览器", "打开网页浏览器", QPushButton("启动"))
   group2 = group_card.addGroup(FIF.MAIL, "邮件", "查看邮件", QPushButton("打开"))
   
   # 获取分组数量
   count = group_card.groupCount()

**构造函数：**
- ``GroupHeaderCardWidget(parent: QWidget = None)``
- ``GroupHeaderCardWidget(title: str, parent: QWidget = None)``

**主要方法：**
- ``addGroup(icon, title: str, content: str, widget: QWidget, stretch=0)`` - 添加分组
- ``groupCount()`` - 获取分组数量

**addGroup参数说明：**
- ``icon`` - 分组图标
- ``title`` - 分组标题
- ``content`` - 分组描述
- ``widget`` - 要添加的控件
- ``stretch`` - 布局拉伸因子

**特点：**
- 自动管理分组之间的分隔符
- 继承HeaderCardWidget的所有功能
- 支持动态添加分组

使用示例
--------

完整的使用示例，展示如何创建一个设置界面：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
   from qfluentwidgets.components.widgets.card_widget import (
       ElevatedCardWidget, HeaderCardWidget, GroupHeaderCardWidget
   )
   from qfluentwidgets import FluentIcon as FIF
   
   class SettingsWindow(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建悬浮卡片作为欢迎区域
           welcome_card = ElevatedCardWidget(self)
           welcome_layout = QVBoxLayout(welcome_card)
           welcome_layout.addWidget(QLabel("欢迎使用设置面板"))
           welcome_layout.addWidget(QLabel("在这里可以配置应用程序的各项参数"))
           
           # 创建组标题卡片
           settings_card = GroupHeaderCardWidget("系统设置", self)
           
           # 添加设置分组
           settings_card.addGroup(
               FIF.SETTING, "常规设置", "基本配置选项", 
               QPushButton("打开设置")
           )
           settings_card.addGroup(
               FIF.POWER_BUTTON, "电源管理", "电源和睡眠设置", 
               QPushButton("电源选项")
           )
           settings_card.addGroup(
               FIF.NETWORK, "网络设置", "网络连接配置", 
               QPushButton("网络设置")
           )
           
           # 添加到布局
           layout.addWidget(welcome_card)
           layout.addWidget(settings_card)
           layout.addStretch()
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       window = SettingsWindow()
       window.show()
       sys.exit(app.exec())

样式自定义
----------

所有卡片控件都支持通过样式表进行自定义：

.. code-block:: python

   # 自定义卡片样式
   card = CardWidget()
   card.setStyleSheet("""
       CardWidget {
           background-color: rgba(255, 255, 255, 0.1);
           border: 1px solid rgba(255, 255, 255, 0.2);
       }
       CardWidget:hover {
           background-color: rgba(255, 255, 255, 0.15);
       }
   """)

注意事项
--------

1. **性能考虑** - ElevatedCardWidget的动画效果可能影响性能，在大量使用时需注意
2. **主题适配** - 所有卡片控件自动适配深色/浅色主题
3. **布局管理** - HeaderCardWidget和GroupHeaderCardWidget内部使用固定布局，添加控件时注意布局约束
4. **点击区域** - CardWidget的点击事件覆盖整个卡片区域
5. **圆角设置** - 边框圆角会影响绘制性能，建议使用合理的数值

相关组件
--------

- :doc:`button` - 按钮控件，常与卡片配合使用
- :doc:`label` - 标签控件，用于卡片内容显示
- :doc:`icon` - 图标控件，用于卡片图标显示
