Flow Layout 流式布局模块
=============================

Flow Layout 模块提供流式布局功能，支持自动换行和移动动画。
该模块允许子控件在水平方向上排列，当空间不足时自动换行，并支持平滑的移动动画效果。

主要功能
--------

- **流式排列** - 支持子控件在水平方向上的流式排列
- **自动换行** - 当空间不足时自动换行到下一行
- **移动动画** - 支持控件位置变化的平滑动画
- **间距控制** - 支持水平和垂直间距的独立设置
- **紧凑模式** - 支持隐藏控件时的紧凑布局模式

核心组件
--------

FlowLayout
~~~~~~~~~~

流式布局，提供自动换行和动画功能。

.. code-block:: python

   from qfluentwidgets.components.layout.flow_layout import FlowLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QWidget
   from PySide6.QtCore import QEasingCurve
   
   # 创建流式布局
   flow_layout = FlowLayout(needAni=True, isTight=False)
   
   # 设置动画参数
   flow_layout.setAnimation(300, QEasingCurve.OutCubic)
   
   # 添加子控件
   label1 = Label("标签1")
   label2 = Label("标签2")
   button1 = PushButton("按钮1")
   
   flow_layout.addWidget(label1)
   flow_layout.addWidget(label2)
   flow_layout.addWidget(button1)
   
   # 设置到父控件
   widget = QWidget()
   widget.setLayout(flow_layout)

**主要方法：**
- ``addWidget()`` - 添加子控件
- ``setAnimation()`` - 设置动画参数
- ``setVerticalSpacing()`` - 设置垂直间距
- ``setHorizontalSpacing()`` - 设置水平间距
- ``removeWidget()`` - 移除子控件

实际应用
--------

基本流式布局
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.flow_layout import FlowLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   
   class BasicFlowLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 创建流式布局容器
           flow_widget = QWidget()
           flow_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 8px;")
           
           # 创建流式布局
           self.flow_layout = FlowLayout(needAni=False)
           flow_widget.setLayout(self.flow_layout)
           
           # 添加子控件
           items = [
               "Python", "JavaScript", "TypeScript", "React", "Vue.js",
               "Django", "Flask", "FastAPI", "Node.js", "Express",
               "Docker", "Kubernetes", "AWS", "Azure", "GCP"
           ]
           
           for item in items:
               label = Label(item)
               label.setStyleSheet("""
                   background-color: #e3f2fd; 
                   color: #1976d2; 
                   padding: 8px 12px; 
                   border-radius: 16px;
                   margin: 2px;
               """)
               self.flow_layout.addWidget(label)
           
           # 设置间距
           self.flow_layout.setVerticalSpacing(8)
           self.flow_layout.setHorizontalSpacing(8)
           self.flow_layout.setContentsMargins(12, 12, 12, 12)
           
           main_layout.addWidget(flow_widget)
           self.setLayout(main_layout)

动画流式布局
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.flow_layout import FlowLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   from PySide6.QtCore import QEasingCurve
   
   class AnimatedFlowLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 控制按钮
           button_layout = QVBoxLayout()
           
           self.add_btn = PushButton("添加标签")
           self.remove_btn = PushButton("移除标签")
           self.clear_btn = PushButton("清空标签")
           
           button_layout.addWidget(self.add_btn)
           button_layout.addWidget(self.remove_btn)
           button_layout.addWidget(self.clear_btn)
           
           # 流式布局容器
           self.flow_widget = QWidget()
           self.flow_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")
           
           # 创建动画流式布局
           self.flow_layout = FlowLayout(needAni=True, isTight=False)
           self.flow_layout.setAnimation(400, QEasingCurve.OutCubic)
           self.flow_widget.setLayout(self.flow_layout)
           
           # 添加初始标签
           self.add_initial_tags()
           
           # 设置间距
           self.flow_layout.setVerticalSpacing(10)
           self.flow_layout.setHorizontalSpacing(10)
           self.flow_layout.setContentsMargins(15, 15, 15, 15)
           
           # 布局
           content_layout = QVBoxLayout()
           content_layout.addLayout(button_layout)
           content_layout.addWidget(self.flow_widget)
           
           main_layout.addLayout(content_layout)
           self.setLayout(main_layout)
       
       def setup_connections(self):
           """设置连接"""
           self.add_btn.clicked.connect(self.add_random_tag)
           self.remove_btn.clicked.connect(self.remove_random_tag)
           self.clear_btn.clicked.connect(self.clear_tags)
       
       def add_initial_tags(self):
           """添加初始标签"""
           initial_tags = ["重要", "紧急", "待处理", "已完成"]
           colors = ["#ff6b6b", "#f39c12", "#3498db", "#27ae60"]
           
           for tag, color in zip(initial_tags, colors):
               label = Label(tag)
               label.setStyleSheet(f"""
                   background-color: {color}; 
                   color: white; 
                   padding: 6px 12px; 
                   border-radius: 15px;
                   font-weight: bold;
               """)
               self.flow_layout.addWidget(label)
       
       def add_random_tag(self):
           """添加随机标签"""
           import random
           
           tags = ["新任务", "高优先级", "低优先级", "审核中", "已发布", "草稿", "归档"]
           colors = ["#e74c3c", "#f39c12", "#3498db", "#9b59b6", "#1abc9c", "#2ecc71", "#95a5a6"]
           
           tag = random.choice(tags)
           color = random.choice(colors)
           
           label = Label(tag)
           label.setStyleSheet(f"""
               background-color: {color}; 
               color: white; 
               padding: 6px 12px; 
               border-radius: 15px;
               font-weight: bold;
           """)
           
           self.flow_layout.addWidget(label)
       
       def remove_random_tag(self):
           """移除随机标签"""
           if self.flow_layout.count() > 0:
               import random
               index = random.randint(0, self.flow_layout.count() - 1)
               item = self.flow_layout.itemAt(index)
               if item and item.widget():
                   self.flow_layout.removeWidget(item.widget())
                   item.widget().deleteLater()
       
       def clear_tags(self):
           """清空所有标签"""
           self.flow_layout.removeAllWidgets()

高级用法
--------

自定义流式布局
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.flow_layout import FlowLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget, QFrame
   from PySide6.QtCore import QEasingCurve, QTimer
   from PySide6.QtGui import QColor
   
   class CustomFlowLayout(FlowLayout):
       """自定义流式布局"""
       
       def __init__(self, parent=None, needAni=True, isTight=False):
           super().__init__(parent, needAni, isTight)
           self.widget_colors = {}
           self.color_palette = [
               QColor("#FF6B6B"), QColor("#4ECDC4"), QColor("#45B7D1"),
               QColor("#96CEB4"), QColor("#FFEAA7"), QColor("#DDA0DD")
           ]
       
       def addWidget(self, widget):
           """重写添加控件方法"""
           super().addWidget(widget)
           
           # 为控件设置随机颜色
           import random
           color = random.choice(self.color_palette)
           self.widget_colors[widget] = color
           
           # 设置样式
           widget.setStyleSheet(f"""
               background-color: {color.name()}; 
               color: white; 
               padding: 8px 16px; 
               border-radius: 20px;
               font-weight: bold;
               border: 2px solid transparent;
           """)
           
           # 添加悬停效果
           widget.installEventFilter(self)
       
       def eventFilter(self, obj, event):
           """事件过滤器处理悬停效果"""
           if obj in self.widget_colors:
               if event.type() == event.Type.Enter:
                   color = self.widget_colors[obj]
                   obj.setStyleSheet(f"""
                       background-color: {color.name()}; 
                       color: white; 
                       padding: 8px 16px; 
                       border-radius: 20px;
                       font-weight: bold;
                       border: 2px solid white;
                   """)
               elif event.type() == event.Type.Leave:
                   color = self.widget_colors[obj]
                   obj.setStyleSheet(f"""
                       background-color: {color.name()}; 
                       color: white; 
                       padding: 8px 16px; 
                       border-radius: 20px;
                       font-weight: bold;
                       border: 2px solid transparent;
                   """)
           
           return super().eventFilter(obj, event)
   
   class CustomFlowLayoutWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_timer()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 创建自定义流式布局容器
           flow_widget = QWidget()
           flow_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")
           
           # 创建自定义流式布局
           custom_layout = CustomFlowLayout(needAni=True)
           custom_layout.setAnimation(500, QEasingCurve.OutBack)
           flow_widget.setLayout(custom_layout)
           
           # 添加内容
           skills = [
               "Python", "JavaScript", "React", "Vue.js", "Node.js",
               "Docker", "Kubernetes", "AWS", "MongoDB", "PostgreSQL",
               "Redis", "Elasticsearch", "Git", "CI/CD", "Agile"
           ]
           
           for skill in skills:
               label = Label(skill)
               custom_layout.addWidget(label)
           
           # 设置布局属性
           custom_layout.setVerticalSpacing(12)
           custom_layout.setHorizontalSpacing(12)
           custom_layout.setContentsMargins(20, 20, 20, 20)
           
           main_layout.addWidget(flow_widget)
           self.setLayout(main_layout)
       
       def setup_timer(self):
           """设置定时器用于演示动态效果"""
           self.timer = QTimer()
           self.timer.timeout.connect(self.add_random_skill)
           self.timer.start(2000)  # 每2秒添加一个技能
       
       def add_random_skill(self):
           """动态添加技能标签"""
           flow_widget = self.findChild(QWidget)
           if flow_widget and flow_widget.layout():
               layout = flow_widget.layout()
               
               additional_skills = ["GraphQL", "TypeScript", "Rust", "Go", "Swift"]
               import random
               
               if layout.count() < 20:  # 限制最大数量
                   skill = random.choice(additional_skills)
                   label = Label(skill)
                   layout.addWidget(label)

响应式流式布局
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.layout.flow_layout import FlowLayout
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QWidget
   from PySide6.QtCore import QTimer, QEasingCurve
   
   class ResponsiveFlowLayoutWidget(CardWidget):
       """响应式流式布局"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_timer()
       
       def setup_ui(self):
           # 创建主布局
           main_layout = QVBoxLayout()
           
           # 流式布局容器
           self.flow_widget = QWidget()
           self.flow_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 8px;")
           
           # 创建流式布局
           self.flow_layout = FlowLayout(needAni=True, isTight=True)
           self.flow_layout.setAnimation(300, QEasingCurve.OutCubic)
           self.flow_widget.setLayout(self.flow_layout)
           
           # 添加响应式内容
           self.add_responsive_content()
           
           # 设置布局属性
           self.flow_layout.setVerticalSpacing(8)
           self.flow_layout.setHorizontalSpacing(8)
           self.flow_layout.setContentsMargins(15, 15, 15, 15)
           
           main_layout.addWidget(self.flow_widget)
           self.setLayout(main_layout)
       
       def add_responsive_content(self):
           """添加响应式内容"""
           # 不同大小的内容
           contents = [
               ("小", "#3498db", 60),
               ("中等大小", "#e74c3c", 100),
               ("这是一个很长的标签内容", "#f39c12", 150),
               ("短", "#27ae60", 50),
               ("中等", "#9b59b6", 80),
               ("超长内容用于测试响应式布局效果", "#1abc9c", 200)
           ]
           
           for text, color, width in contents:
               label = Label(text)
               label.setFixedWidth(width)
               label.setStyleSheet(f"""
                   background-color: {color}; 
                   color: white; 
                   padding: 8px 12px; 
                   border-radius: 6px;
                   font-weight: bold;
               """)
               
               self.flow_layout.addWidget(label)
       
       def setup_timer(self):
           """设置定时器用于演示响应式效果"""
           self.timer = QTimer()
           self.timer.timeout.connect(self.update_content_visibility)
           self.timer.start(4000)  # 每4秒更新一次
       
       def update_content_visibility(self):
           """更新内容可见性以演示响应式效果"""
           if self.flow_layout.count() > 0:
               import random
               
               # 随机隐藏/显示一些控件
               for i in range(self.flow_layout.count()):
                   item = self.flow_layout.itemAt(i)
                   if item and item.widget():
                       # 随机决定是否显示
                       should_show = random.choice([True, False, True])  # 更倾向于显示
                       item.widget().setVisible(should_show)

最佳实践
--------

1. **动画效果** - 合理使用动画提升用户体验
2. **间距设置** - 根据内容调整合适的间距
3. **紧凑模式** - 在需要时使用紧凑模式节省空间
4. **性能优化** - 避免过多的控件影响性能
5. **响应式设计** - 考虑不同窗口尺寸下的显示效果

注意事项
--------

- 流式布局会根据可用空间自动换行
- 动画效果会增加一定的性能开销
- 紧凑模式下隐藏的控件不占用空间
- 大量子控件可能影响布局性能
- 需要合理设置间距以获得良好的视觉效果

相关模块
--------

- :doc:`components.layout.expand_layout` - 扩展布局
- :doc:`components.layout.splitter` - 分割器布局
- :doc:`components.layout.v_box_layout` - 垂直布局
