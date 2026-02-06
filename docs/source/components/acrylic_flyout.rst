Acrylic Flyout 亚克力弹出框模块
===================================

Acrylic Flyout 模块提供亚克力风格的弹出框组件，支持透明效果和现代化设计。
该模块结合了亚克力视觉效果和弹出框功能，提供美观的信息展示界面。

主要功能
--------

- **亚克力效果** - 提供现代化的亚克力视觉效果
- **弹出显示** - 支持多种动画类型的弹出效果
- **自定义视图** - 提供可定制的弹出框视图
- **图标支持** - 支持图标和图片显示
- **关闭控制** - 支持可关闭的弹出框

核心组件
--------

AcrylicFlyout
~~~~~~~~~~~~~

亚克力弹出框，提供标准的弹出显示功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_flyout import AcrylicFlyout
   from qfluentwidgets import PushButton
   from PySide6.QtCore import QPoint
   
   # 创建亚克力弹出框
   flyout = AcrylicFlyout.create(
       title="提示",
       content="这是一个亚克力弹出框示例",
       icon=None,
       target=button,
       parent=parent
   )

**主要方法：**
- ``create()`` - 创建并显示弹出框
- ``exec()`` - 执行弹出框显示

AcrylicFlyoutView
~~~~~~~~~~~~~~~~~

亚克力弹出框视图，提供自定义的视图界面。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_flyout import AcrylicFlyoutView
   from PySide6.QtWidgets import QVBoxLayout, QLabel
   
   # 创建自定义视图
   view = AcrylicFlyoutView(title="标题", content="内容", icon=None, isClosable=True)
   
   # 添加自定义控件
   layout = QVBoxLayout()
   custom_label = QLabel("自定义内容")
   layout.addWidget(custom_label)
   view.setLayout(layout)

AcrylicFlyoutViewBase
~~~~~~~~~~~~~~~~~~~~~

亚克力弹出框视图基类，提供基础的视图功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_flyout import AcrylicFlyoutViewBase
   
   # 创建自定义视图基类
   class CustomFlyoutView(AcrylicFlyoutViewBase):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 自定义界面设置
           pass

实际应用
--------

基本亚克力弹出框
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_flyout import AcrylicFlyout
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicAcrylicFlyoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.info_btn = PushButton("显示信息")
           self.warning_btn = PushButton("显示警告")
           self.success_btn = PushButton("显示成功")
           
           layout.addWidget(self.info_btn)
           layout.addWidget(self.warning_btn)
           layout.addWidget(self.success_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.info_btn.clicked.connect(self.show_info_flyout)
           self.warning_btn.clicked.connect(self.show_warning_flyout)
           self.success_btn.clicked.connect(self.show_success_flyout)
       
       def show_info_flyout(self):
           """显示信息弹出框"""
           AcrylicFlyout.create(
               title="信息提示",
               content="这是一条信息提示，用于向用户展示一般性的信息。",
               icon=None,
               target=self.info_btn,
               parent=self
           )
       
       def show_warning_flyout(self):
           """显示警告弹出框"""
           from qfluentwidgets.common.icon import FluentIcon as FIF
           
           AcrylicFlyout.create(
               title="警告提示",
               content="请注意，此操作可能存在风险，建议在操作前仔细阅读相关说明。",
               icon=FIF.WARNING,
               target=self.warning_btn,
               parent=self
           )
       
       def show_success_flyout(self):
           """显示成功弹出框"""
           from qfluentwidgets.common.icon import FluentIcon as FIF
           
           AcrylicFlyout.create(
               title="成功提示",
               content="操作已成功完成！系统已保存所有更改。",
               icon=FIF.CIRCLE_CHECK,
               target=self.success_btn,
               parent=self
           )

可关闭弹出框
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_flyout import AcrylicFlyout
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class ClosableFlyoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.long_content_btn = PushButton("显示长内容")
           self.closable_btn = PushButton("显示可关闭")
           self.position_btn = PushButton("指定位置")
           
           layout.addWidget(self.long_content_btn)
           layout.addWidget(self.closable_btn)
           layout.addWidget(self.position_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.long_content_btn.clicked.connect(self.show_long_content)
           self.closable_btn.clicked.connect(self.show_closable)
           self.position_btn.clicked.connect(self.show_positioned)
       
       def show_long_content(self):
           """显示长内容弹出框"""
           long_content = (
               "这是一个长内容的弹出框示例。AcrylicFlyout组件支持自动文本换行功能，"
               "能够很好地处理较长的文本内容。当文本内容超过弹出框的宽度限制时，"
               "系统会自动进行换行处理，确保文本内容能够完整显示。"
               "这种设计使得弹出框能够适应不同长度的文本内容，"
               "为用户提供更好的阅读体验。"
           )
           
           AcrylicFlyout.create(
               title="详细说明",
               content=long_content,
               icon=FIF.INFO,
               isClosable=True,
               target=self.long_content_btn,
               parent=self
           )
       
       def show_closable(self):
           """显示可关闭弹出框"""
           AcrylicFlyout.create(
               title="可关闭提示",
               content="这是一个可以手动关闭的弹出框。点击右上角的关闭按钮即可关闭。",
               icon=FIF.CLOSE,
               isClosable=True,
               target=self.closable_btn,
               parent=self
           )
       
       def show_positioned(self):
           """显示指定位置的弹出框"""
           from PySide6.QtCore import QPoint
           
           # 指定弹出位置
           pos = self.position_btn.mapToParent(QPoint(0, -50))
           
           AcrylicFlyout.create(
               title="位置提示",
               content="这个弹出框显示在指定位置。",
               icon=FIF.LOCATION,
               isClosable=True,
               target=pos,
               parent=self
           )

高级用法
--------

自定义弹出框视图
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_flyout import AcrylicFlyoutView, AcrylicFlyout
   from qfluentwidgets import PushButton, CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class CustomFlyoutView(AcrylicFlyoutView):
       """自定义弹出框视图"""
       
       def __init__(self, title, content, icon=None, image=None, isClosable=False):
           super().__init__(title, content, icon, image, isClosable)
           self.setup_custom_ui()
       
       def setup_custom_ui(self):
           """设置自定义界面"""
           # 创建自定义布局
           custom_layout = QVBoxLayout()
           
           # 添加自定义控件
           custom_label = Label("这是自定义添加的内容")
           custom_label.setStyleSheet("padding: 10px; font-weight: bold;")
           
           # 添加按钮
           button_layout = QHBoxLayout()
           
           from qfluentwidgets import PrimaryPushButton, PushButton
           
           self.ok_btn = PrimaryPushButton("确定")
           self.cancel_btn = PushButton("取消")
           
           button_layout.addStretch()
           button_layout.addWidget(self.ok_btn)
           button_layout.addWidget(self.cancel_btn)
           
           custom_layout.addWidget(custom_label)
           custom_layout.addLayout(button_layout)
           
           # 添加到现有布局
           self.vBoxLayout.addLayout(custom_layout)
   
   class CustomFlyoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.custom_btn = PushButton("显示自定义弹出框")
           
           layout.addWidget(self.custom_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.custom_btn.clicked.connect(self.show_custom_flyout)
       
       def show_custom_flyout(self):
           """显示自定义弹出框"""
           # 创建自定义视图
           custom_view = CustomFlyoutView(
               title="自定义弹出框",
               content="这是一个使用自定义视图的弹出框。",
               icon=FIF.SETTING,
               isClosable=True
           )
           
           # 连接按钮信号
           custom_view.ok_btn.clicked.connect(lambda: print("用户点击了确定"))
           custom_view.cancel_btn.clicked.connect(lambda: print("用户点击了取消"))
           
           # 创建弹出框
           flyout = AcrylicFlyout.make(
               view=custom_view,
               target=self.custom_btn,
               parent=self
           )
           
           custom_view.closed.connect(flyout.close)
           flyout.exec(self.custom_btn.mapToGlobal(QPoint(0, -50)))

动画类型弹出框
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_flyout import AcrylicFlyout
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from qfluentwidgets.widgets.flyout import FlyoutAnimationType
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AnimationFlyoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建不同动画类型的按钮
           self.pull_up_btn = PushButton("向上弹出")
           self.pull_down_btn = PushButton("向下弹出")
           self.fade_in_btn = PushButton("淡入效果")
           
           layout.addWidget(self.pull_up_btn)
           layout.addWidget(self.pull_down_btn)
           layout.addWidget(self.fade_in_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.pull_up_btn.clicked.connect(self.show_pull_up)
           self.pull_down_btn.clicked.connect(self.show_pull_down)
           self.fade_in_btn.clicked.connect(self.show_fade_in)
       
       def show_pull_up(self):
           """显示向上弹出动画"""
           AcrylicFlyout.create(
               title="向上弹出",
               content="这个弹出框使用向上滑出的动画效果。",
               icon=FIF.UP_ARROW,
               isClosable=True,
               target=self.pull_up_btn,
               parent=self,
               aniType=FlyoutAnimationType.PULL_UP
           )
       
       def show_pull_down(self):
           """显示向下弹出动画"""
           AcrylicFlyout.create(
               title="向下弹出",
               content="这个弹出框使用向下滑出的动画效果。",
               icon=FIF.DOWN_ARROW,
               isClosable=True,
               target=self.pull_down_btn,
               parent=self,
               aniType=FlyoutAnimationType.PULL_DOWN
           )
       
       def show_fade_in(self):
           """显示淡入动画"""
           AcrylicFlyout.create(
               title="淡入效果",
               content="这个弹出框使用淡入的动画效果。",
               icon=FIF.BRIGHTNESS,
               isClosable=True,
               target=self.fade_in_btn,
               parent=self,
               aniType=FlyoutAnimationType.FADE_IN
           )

图片弹出框
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_flyout import AcrylicFlyout
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from qfluentwidgets.common.icon import FluentIcon as FIF
   from PySide6.QtGui import QPixmap
   
   class ImageFlyoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建触发按钮
           self.image_btn = PushButton("显示图片弹出框")
           self.avatar_btn = PushButton("显示头像弹出框")
           
           layout.addWidget(self.image_btn)
           layout.addWidget(self.avatar_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.image_btn.clicked.connect(self.show_image_flyout)
           self.avatar_btn.clicked.connect(self.show_avatar_flyout)
       
       def show_image_flyout(self):
           """显示图片弹出框"""
           # 创建示例图片
           pixmap = QPixmap(100, 100)
           pixmap.fill(FIF.PHOTO.color())
           
           AcrylicFlyout.create(
               title="图片展示",
               content="这是一个包含图片的弹出框示例。",
               icon=FIF.IMAGE,
               image=pixmap,
               isClosable=True,
               target=self.image_btn,
               parent=self
           )
       
       def show_avatar_flyout(self):
           """显示头像弹出框"""
           # 创建头像图片
           avatar_pixmap = QPixmap(80, 80)
           avatar_pixmap.fill(FIF.PERSON.color())
           
           AcrylicFlyout.create(
               title="用户信息",
               content="张三\n高级开发工程师\nPython专家",
               icon=FIF.PERSON,
               image=avatar_pixmap,
               isClosable=True,
               target=self.avatar_btn,
               parent=self
           )

最佳实践
--------

1. **内容简洁** - 弹出框内容要简洁明了，突出重点
2. **位置合理** - 选择合适的弹出位置避免遮挡重要内容
3. **动画效果** - 合理使用动画效果提升用户体验
4. **关闭控制** - 为长时间显示的弹出框提供关闭按钮
5. **图标使用** - 使用合适的图标增强信息传达

注意事项
--------

- 亚克力效果需要正确的背景支持
- 弹出框会自动调整大小适应内容
- 长文本内容会自动换行处理
- 图片需要合适的尺寸和格式
- 动画效果可能影响性能，需要合理使用

相关模块
--------

- :doc:`components.material.acrylic_widget` - 亚克力控件基类
- :doc:`components.widgets.flyout` - 标准弹出框
- :doc:`components.widgets.menu` - 菜单组件
