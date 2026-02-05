Icon 图标管理模块
==================

Icon 模块提供完整的图标管理系统，支持Fluent Design图标、SVG图标、字体图标等多种图标类型。
该模块提供主题适配、颜色自动调整和图标引擎等功能，确保图标在不同主题下都有良好的显示效果。

主要功能
--------

- **Fluent Design图标** - 内置完整的Fluent Design图标集
- **SVG图标支持** - 支持自定义SVG图标
- **字体图标** - 支持字体图标渲染
- **主题适配** - 自动适配亮色/暗色主题
- **图标引擎** - 自定义图标引擎实现

核心组件
--------

FluentIcon
~~~~~~~~~~

Fluent Design图标枚举，提供标准化的图标集合。

.. code-block:: python

   from qfluentwidgets.common.icon import FluentIcon
   
   # 使用Fluent图标
   icon = FluentIcon.DOWNLOAD
   icon = FluentIcon.SETTING
   icon = FluentIcon.PLAY
   icon = FluentIcon.PAUSE
   
   # 创建QIcon
   qicon = QIcon(icon.path())

**主要图标分类：**

基础图标：
- ``DOWNLOAD`` - 下载
- ``UPLOAD`` - 上传
- ``DELETE`` - 删除
- ``EDIT`` - 编辑
- ``COPY`` - 复制
- ``SAVE`` - 保存

导航图标：
- ``LEFT_ARROW`` - 左箭头
- ``RIGHT_ARROW`` - 右箭头
- ``UP_ARROW`` - 上箭头
- ``DOWN_ARROW`` - 下箭头
- ``BACK`` - 返回
- ``FORWARD`` - 前进

媒体图标：
- ``PLAY`` - 播放
- ``PAUSE`` - 暂停
- ``STOP`` - 停止
- ``NEXT`` - 下一个
- ``PREVIOUS`` - 上一个
- ``VOLUME`` - 音量

系统图标：
- ``SETTING`` - 设置
- ``INFO`` - 信息
- ``WARNING`` - 警告
- ``ERROR`` - 错误
- ``SUCCESS`` - 成功
- ``HELP`` - 帮助

Icon
~~~~

图标包装类，将FluentIcon转换为QIcon。

.. code-block:: python

   from qfluentwidgets.common.icon import Icon, FluentIcon
   from qfluentwidgets import PushButton, Label
   
   # 创建图标
   download_icon = Icon(FluentIcon.DOWNLOAD)
   setting_icon = Icon(FluentIcon.SETTING)
   
   # 应用到控件
   button = PushButton("下载")
   button.setIcon(download_icon)
   
   label = Label("设置")
   label.setIcon(setting_icon)

FluentIconBase
~~~~~~~~~~~~~~

图标基类，提供图标的基础功能。

.. code-block:: python

   from qfluentwidgets.common.icon import FluentIconBase
   from qfluentwidgets.common.config import Theme
   
   class CustomIcon(FluentIconBase):
       def __init__(self, icon_name):
           self.icon_name = icon_name
       
       def icon(self, theme=Theme.AUTO):
           """返回指定主题的图标"""
           color = "black" if theme == Theme.LIGHT else "white"
           return QIcon(f"icons/{self.icon_name}_{color}.svg")
   
   # 使用自定义图标
   custom_icon = CustomIcon("my_icon")
   qicon = custom_icon.icon()

图标引擎
--------

FluentIconEngine
~~~~~~~~~~~~~~~~

Fluent图标引擎，提供主题适配和颜色调整。

.. code-block:: python

   from qfluentwidgets.common.icon import FluentIconEngine, FluentIcon
   
   # 创建图标引擎
   engine = FluentIconEngine(FluentIcon.DOWNLOAD)
   
   # 反转主题
   reverse_engine = FluentIconEngine(FluentIcon.DOWNLOAD, reverse=True)
   
   # 创建QIcon
   icon = QIcon(engine)

SvgIconEngine
~~~~~~~~~~~~~

SVG图标引擎，支持自定义SVG图标。

.. code-block:: python

   from qfluentwidgets.common.icon import SvgIconEngine
   
   # SVG内容
   svg_content = """
   <svg width="24" height="24" viewBox="0 0 24 24">
       <circle cx="12" cy="12" r="10" fill="currentColor"/>
   </svg>
   """
   
   # 创建SVG图标引擎
   engine = SvgIconEngine(svg_content)
   icon = QIcon(engine)

FontIconEngine
~~~~~~~~~~~~~~

字体图标引擎，支持字体图标渲染。

.. code-block:: python

   from qfluentwidgets.common.icon import FontIconEngine
   from PySide6.QtGui import QColor
   
   # 创建字体图标引擎
   engine = FontIconEngine(
       fontFamily="Material Icons",
       char="favorite",  # 图标字符
       color=QColor("#FF0000"),
       isBold=False
   )
   
   icon = QIcon(engine)

实际应用
--------

按钮图标
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.icon import Icon, FluentIcon
   from qfluentwidgets import PushButton, PrimaryPushButton, ToolButton
   
   # 基本按钮图标
   download_btn = PushButton("下载")
   download_btn.setIcon(Icon(FluentIcon.DOWNLOAD))
   
   # 主要按钮图标
   save_btn = PrimaryPushButton("保存")
   save_btn.setIcon(Icon(FluentIcon.SAVE))
   
   # 工具按钮
   refresh_btn = ToolButton()
   refresh_btn.setIcon(Icon(FluentIcon.SYNC))

菜单图标
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.icon import Icon, FluentIcon
   from qfluentwidgets import Menu, Action
   
   # 创建菜单
   menu = Menu()
   
   # 添加带图标的动作
   new_action = Action("新建", Icon(FluentIcon.ADD))
   open_action = Action("打开", Icon(FluentIcon.FOLDER))
   save_action = Action("保存", Icon(FluentIcon.SAVE))
   
   menu.addAction(new_action)
   menu.addAction(open_action)
   menu.addAction(save_action)

状态图标
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.icon import Icon, FluentIcon
   from qfluentwidgets import InfoBar, InfoBadge
   
   # 状态信息栏
   InfoBar.success(
       title="操作成功",
       content="文件已保存",
       icon=Icon(FluentIcon.SUCCESS),
       duration=2000
   )
   
   InfoBar.error(
       title="操作失败",
       content="文件保存失败",
       icon=Icon(FluentIcon.ERROR),
       duration=3000
   )
   
   # 状态徽章
   badge = InfoBadge()
   badge.setIcon(Icon(FluentIcon.CIRCLE))

自定义图标
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.icon import FluentIconBase, Icon
   from qfluentwidgets.common.config import Theme
   
   class CustomAppIcon(FluentIconBase):
       """自定义应用图标"""
       
       def __init__(self, icon_name, color_map=None):
           self.icon_name = icon_name
           self.color_map = color_map or {
               Theme.LIGHT: "#333333",
               Theme.DARK: "#FFFFFF"
           }
       
       def icon(self, theme=Theme.AUTO):
           """返回指定主题的图标"""
           if theme == Theme.AUTO:
               from qfluentwidgets.common.config import isDarkTheme
               theme = Theme.DARK if isDarkTheme() else Theme.LIGHT
           
           color = self.color_map.get(theme, "#333333")
           return QIcon(f"icons/{self.icon_name}_{color}.svg")
   
   # 使用自定义图标
   app_icon = CustomAppIcon("app_logo")
   logo_icon = Icon(app_icon)

主题适配图标
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.icon import FluentIconEngine, FluentIcon
   from qfluentwidgets.common.config import qconfig, Theme
   
   class ThemeAwareIcon:
       """主题感知图标"""
       
       def __init__(self, fluent_icon):
           self.fluent_icon = fluent_icon
           self.normal_icon = QIcon(FluentIconEngine(fluent_icon))
           self.reverse_icon = QIcon(FluentIconEngine(fluent_icon, reverse=True))
       
       def get_icon(self, reverse_theme=False):
           """获取图标"""
           if reverse_theme:
               return self.reverse_icon
           return self.normal_icon
       
       def update_theme(self):
           """更新主题"""
           # 主题变化时的处理
           pass
   
   # 使用主题适配图标
   theme_icon = ThemeAwareIcon(FluentIcon.SETTING)
   button.setIcon(theme_icon.get_icon())

图标资源管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.icon import FluentIcon
   import json
   
   def export_icon_config():
       """导出图标配置"""
       icon_config = {
           'toolbar_icons': [
               FluentIcon.NEW.value,
               FluentIcon.OPEN.value,
               FluentIcon.SAVE.value
           ],
           'status_icons': [
               FluentIcon.SUCCESS.value,
               FluentIcon.ERROR.value,
               FluentIcon.WARNING.value
           ]
       }
       
       with open('icon_config.json', 'w', encoding='utf-8') as f:
           json.dump(icon_config, f, indent=2, ensure_ascii=False)
   
   def create_icon_toolbar(icon_list):
       """根据配置创建图标工具栏"""
       from qfluentwidgets import ToolBar, ToolButton
       
       toolbar = ToolBar()
       
       for icon_name in icon_list:
           icon = getattr(FluentIcon, icon_name, None)
           if icon:
               button = ToolButton()
               button.setIcon(Icon(icon))
               toolbar.addWidget(button)
       
       return toolbar

高级用法
--------

图标组合
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.icon import Icon, FluentIcon
   from PySide6.QtGui import QPainter, QPixmap
   from PySide6.QtCore import QSize
   
   def create_combined_icon(icon1, icon2, size=24):
       """组合两个图标"""
       pixmap = QPixmap(size, size)
       pixmap.fill(Qt.transparent)
       
       painter = QPainter(pixmap)
       
       # 绘制第一个图标
       icon1.paint(painter, QRect(0, 0, size//2, size), Qt.AlignCenter)
       
       # 绘制第二个图标
       icon2.paint(painter, QRect(size//2, 0, size//2, size), Qt.AlignCenter)
       
       painter.end()
       
       return QIcon(pixmap)
   
   # 使用组合图标
   combined = create_combined_icon(
       Icon(FluentIcon.DOWNLOAD),
       Icon(FluentIcon.ARROW_DOWN)
   )

动态图标
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.icon import Icon, FluentIcon
   from PySide6.QtCore import QTimer, Property
   from PySide6.QtGui import QIconEngine
   
   class AnimatedIconEngine(QIconEngine):
       """动画图标引擎"""
       
       def __init__(self, icons):
           super().__init__()
           self.icons = icons
           self.current_index = 0
           self.timer = QTimer()
           self.timer.timeout.connect(self.next_frame)
           self.timer.start(200)  # 200ms切换一次
       
       def next_frame(self):
           """切换到下一帧"""
           self.current_index = (self.current_index + 1) % len(self.icons)
       
       def paint(self, painter, rect, mode, state):
           current_icon = self.icons[self.current_index]
           current_icon.paint(painter, rect, Qt.AlignCenter, mode, state)
       
       def clone(self):
           return AnimatedIconEngine(self.icons)
   
   # 创建动画图标
   loading_icons = [
       Icon(FluentIcon.LOADING_1),
       Icon(FluentIcon.LOADING_2),
       Icon(FluentIcon.LOADING_3)
   ]
   
   animated_icon = QIcon(AnimatedIconEngine(loading_icons))

最佳实践
--------

1. **图标选择** - 使用语义化的图标，确保用户理解
2. **尺寸一致** - 保持图标尺寸的一致性
3. **主题适配** - 确保图标在不同主题下都清晰可见
4. **性能考虑** - 避免使用过于复杂的SVG图标
5. **可访问性** - 为图标提供文本描述

注意事项
--------

- 图标资源必须正确打包到QRC资源文件中
- 不同主题下图标颜色会自动调整
- 自定义图标需要提供亮色和暗色版本
- 图标引擎会影响图标的渲染性能

相关模块
--------

- :doc:`common.config` - 配置管理
- :doc:`components.widgets` - UI组件
- :doc:`common.color` - 颜色管理
