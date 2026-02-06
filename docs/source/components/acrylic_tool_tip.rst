Acrylic Tool Tip 亚克力工具提示模块
====================================

Acrylic Tool Tip 模块提供亚克力风格的工具提示组件，支持透明效果和现代化设计。
该模块结合了亚克力视觉效果和工具提示功能，提供美观的信息提示界面。

主要功能
--------

- **亚克力效果** - 提供现代化的亚克力视觉效果
- **工具提示** - 支持标准的工具提示功能
- **自动显示** - 支持鼠标悬停自动显示
- **自定义容器** - 提供可定制的提示容器
- **事件过滤** - 支持工具提示事件过滤

核心组件
--------

AcrylicToolTip
~~~~~~~~~~~~~~

亚克力工具提示，提供标准的提示显示功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_tool_tip import AcrylicToolTip
   from qfluentwidgets import PushButton
   
   # 创建按钮
   button = PushButton("悬停查看提示")
   
   # 设置工具提示
   button.setToolTip("这是一个亚克力工具提示")
   
   # 创建亚克力工具提示
   tooltip = AcrylicToolTip(button.toolTip(), button.window())

AcrylicToolTipContainer
~~~~~~~~~~~~~~~~~~~~~~

亚克力工具提示容器，提供自定义的提示界面。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_tool_tip import AcrylicToolTipContainer
   from PySide6.QtWidgets import QVBoxLayout, QLabel
   
   # 创建自定义容器
   container = AcrylicToolTipContainer()
   
   # 添加自定义内容
   layout = QVBoxLayout(container)
   label = QLabel("自定义工具提示内容")
   layout.addWidget(label)

AcrylicToolTipFilter
~~~~~~~~~~~~~~~~~~~

亚克力工具提示过滤器，提供事件过滤功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_tool_tip import AcrylicToolTipFilter
   
   # 创建过滤器
   tooltip_filter = AcrylicToolTipFilter(parent_widget)
   parent_widget.installEventFilter(tooltip_filter)

实际应用
--------

基本亚克力工具提示
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_tool_tip import AcrylicToolTip
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicAcrylicToolTipWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           from qfluentwidgets import Label
           title_label = Label("亚克力工具提示示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建带工具提示的按钮
           info_btn = PushButton("信息按钮")
           info_btn.setToolTip("这是一个信息提示，用于向用户展示一般性的信息。")
           
           warning_btn = PushButton("警告按钮")
           warning_btn.setToolTip("这是一个警告提示，提醒用户注意潜在的问题。")
           
           error_btn = PushButton("错误按钮")
           error_btn.setToolTip("这是一个错误提示，指示出现了错误情况。")
           
           help_btn = PushButton("帮助按钮")
           help_btn.setToolTip("这是一个帮助提示，提供相关的帮助信息。")
           
           layout.addWidget(title_label)
           layout.addWidget(info_btn)
           layout.addWidget(warning_btn)
           layout.addWidget(error_btn)
           layout.addWidget(help_btn)
           self.setLayout(layout)

自定义工具提示
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_tool_tip import AcrylicToolTip, AcrylicToolTipContainer
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout, QLabel
   from PySide6.QtCore import Qt
   
   class CustomToolTipWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_tooltips()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           from qfluentwidgets import Label
           title_label = Label("自定义工具提示示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建按钮
           self.user_btn = PushButton("用户信息")
           self.settings_btn = PushButton("设置选项")
           self.status_btn = PushButton("系统状态")
           
           layout.addWidget(title_label)
           layout.addWidget(self.user_btn)
           layout.addWidget(self.settings_btn)
           layout.addWidget(self.status_btn)
           self.setLayout(layout)
       
       def setup_tooltips(self):
           """设置自定义工具提示"""
           # 用户信息工具提示
           user_tooltip = self.create_custom_tooltip(
               "用户信息",
               "姓名: 张三\n邮箱: zhangsan@example.com\n角色: 管理员"
           )
           self.user_btn.setToolTip(user_tooltip)
           
           # 设置选项工具提示
           settings_tooltip = self.create_custom_tooltip(
               "设置选项",
               "• 主题设置\n• 语言设置\n• 字体设置\n• 快捷键设置"
           )
           self.settings_btn.setToolTip(settings_tooltip)
           
           # 系统状态工具提示
           status_tooltip = self.create_custom_tooltip(
               "系统状态",
               "CPU使用率: 45%\n内存使用率: 62%\n磁盘使用率: 78%"
           )
           self.status_btn.setToolTip(status_tooltip)
       
       def create_custom_tooltip(self, title, content):
           """创建自定义工具提示"""
           # 创建自定义容器
           container = AcrylicToolTipContainer()
           container.setStyleSheet("padding: 8px;")
           
           # 添加内容
           layout = QVBoxLayout(container)
           layout.setContentsMargins(0, 0, 0, 0)
           layout.setSpacing(4)
           
           # 标题
           title_label = QLabel(title)
           title_label.setStyleSheet("font-weight: bold; color: #333;")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 内容
           content_label = QLabel(content)
           content_label.setStyleSheet("color: #666;")
           content_label.setWordWrap(True)
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           
           return container

高级用法
--------

动态工具提示
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_tool_tip import AcrylicToolTip
   from qfluentwidgets import PushButton, CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import QTimer
   
   class DynamicToolTipWidget(CardWidget):
       """动态工具提示示例"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_timer()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态工具提示")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建按钮
           self.time_btn = PushButton("当前时间")
           self.memory_btn = PushButton("内存使用")
           self.network_btn = PushButton("网络状态")
           
           layout.addWidget(title_label)
           layout.addWidget(self.time_btn)
           layout.addWidget(self.memory_btn)
           layout.addWidget(self.network_btn)
           self.setLayout(layout)
       
       def setup_timer(self):
           """设置定时器更新工具提示"""
           self.timer = QTimer()
           self.timer.timeout.connect(self.update_tooltips)
           self.timer.start(1000)  # 每秒更新一次
       
       def update_tooltips(self):
           """更新工具提示内容"""
           from datetime import datetime
           import random
           
           # 时间工具提示
           current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           self.time_btn.setToolTip(f"当前时间: {current_time}")
           
           # 内存使用工具提示
           memory_usage = random.randint(30, 80)
           self.memory_btn.setToolTip(f"内存使用率: {memory_usage}%")
           
           # 网络状态工具提示
           network_status = random.choice(["连接正常", "连接缓慢", "连接断开"])
           self.network_btn.setToolTip(f"网络状态: {network_status}")

富文本工具提示
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_tool_tip import AcrylicToolTip, AcrylicToolTipContainer
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout, QLabel
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QTextDocument
   
   class RichTextToolTipWidget(CardWidget):
       """富文本工具提示示例"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_tooltips()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           from qfluentwidgets import Label
           title_label = Label("富文本工具提示")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建按钮
           self.html_btn = PushButton("HTML提示")
           self.format_btn = PushButton("格式化文本")
           self.link_btn = PushButton("链接提示")
           
           layout.addWidget(title_label)
           layout.addWidget(self.html_btn)
           layout.addWidget(self.format_btn)
           layout.addWidget(self.link_btn)
           self.setLayout(layout)
       
       def setup_tooltips(self):
           """设置富文本工具提示"""
           # HTML工具提示
           html_tooltip = self.create_html_tooltip()
           self.html_btn.setToolTip(html_tooltip)
           
           # 格式化文本工具提示
           format_tooltip = self.create_format_tooltip()
           self.format_btn.setToolTip(format_tooltip)
           
           # 链接工具提示
           link_tooltip = self.create_link_tooltip()
           self.link_btn.setToolTip(link_tooltip)
       
       def create_html_tooltip(self):
           """创建HTML工具提示"""
           container = AcrylicToolTipContainer()
           container.setStyleSheet("padding: 8px;")
           
           layout = QVBoxLayout(container)
           layout.setContentsMargins(0, 0, 0, 0)
           
           # HTML内容
           html_label = QLabel()
           html_label.setText("""
               <div style='text-align: center;'>
                   <h3 style='color: #2196F3; margin: 5px 0;'>HTML提示</h3>
                   <p style='color: #666; margin: 5px 0;'>
                       这是<b>HTML格式</b>的工具提示<br>
                       支持<font color='#E91E63'>颜色</font>和
                       <font size='4'>大小</font>设置
                   </p>
               </div>
           """)
           html_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(html_label)
           return container
       
       def create_format_tooltip(self):
           """创建格式化文本工具提示"""
           container = AcrylicToolTipContainer()
           container.setStyleSheet("padding: 8px;")
           
           layout = QVBoxLayout(container)
           layout.setContentsMargins(0, 0, 0, 0)
           
           # 格式化内容
           format_label = QLabel()
           format_label.setText("""
               <div>
                   <h4 style='color: #4CAF50; margin: 3px 0;'>格式化文本</h4>
                   <p style='margin: 3px 0;'>
                       <span style='background: #FFF3E0; padding: 2px 4px; border-radius: 3px;'>高亮</span>
                       <span style='text-decoration: underline; color: #2196F3;'>下划线</span>
                       <span style='font-style: italic; color: #9C27B0;'>斜体</span>
                   </p>
               </div>
           """)
           
           layout.addWidget(format_label)
           return container
       
       def create_link_tooltip(self):
           """创建链接工具提示"""
           container = AcrylicToolTipContainer()
           container.setStyleSheet("padding: 8px;")
           
           layout = QVBoxLayout(container)
           layout.setContentsMargins(0, 0, 0, 0)
           
           # 链接内容
           link_label = QLabel()
           link_label.setText("""
               <div>
                   <h4 style='color: #FF9800; margin: 3px 0;'>相关链接</h4>
                   <p style='margin: 3px 0;'>
                       <a href='#' style='color: #2196F3; text-decoration: none;'>📚 文档</a><br>
                       <a href='#' style='color: #4CAF50; text-decoration: none;'>💬 社区</a><br>
                       <a href='#' style='color: #9C27B0; text-decoration: none;'>🐛 问题反馈</a>
                   </p>
               </div>
           """)
           link_label.setOpenExternalLinks(True)
           
           layout.addWidget(link_label)
           return container

工具提示过滤器
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_tool_tip import AcrylicToolTipFilter
   from qfluentwidgets import PushButton, CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   class ToolTipFilterWidget(CardWidget):
       """工具提示过滤器示例"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_filter()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           from qfluentwidgets import Label
           title_label = Label("工具提示过滤器")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建按钮
           self.filter_btn = PushButton("过滤提示")
           self.normal_btn = PushButton("普通提示")
           
           layout.addWidget(title_label)
           layout.addWidget(self.filter_btn)
           layout.addWidget(self.normal_btn)
           self.setLayout(layout)
       
       def setup_filter(self):
           """设置过滤器"""
           # 为过滤按钮安装过滤器
           tooltip_filter = AcrylicToolTipFilter(self.filter_btn)
           self.filter_btn.installEventFilter(tooltip_filter)
           
           # 设置工具提示
           self.filter_btn.setToolTip("这是一个经过过滤的工具提示")
           self.normal_btn.setToolTip("这是一个普通的工具提示")

最佳实践
--------

1. **内容简洁** - 工具提示内容要简洁明了，突出重点
2. **显示时机** - 合理设置工具提示的显示延迟和持续时间
3. **样式一致** - 保持与应用整体风格的一致性
4. **位置合理** - 确保工具提示不会遮挡重要内容
5. **性能考虑** - 避免过于复杂的工具提示影响性能

注意事项
--------

- 亚克力效果需要正确的背景支持
- 工具提示会自动根据内容调整大小
- 富文本内容需要正确处理HTML标签
- 过滤器需要正确安装到目标控件
- 长文本内容需要考虑换行显示

相关模块
--------

- :doc:`components.material.acrylic_widget` - 亚克力控件基类
- :doc:`components.widgets.tool_tip` - 标准工具提示
- :doc:`components.widgets.menu` - 菜单组件
