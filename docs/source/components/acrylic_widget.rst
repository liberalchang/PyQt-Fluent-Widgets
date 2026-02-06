Acrylic Widget 亚克力控件基类模块
===================================

Acrylic Widget 模块提供亚克力控件的基类，支持透明效果和现代化设计。
该模块为其他亚克力组件提供基础功能，包括亚克力画刷和绘制逻辑。

主要功能
--------

- **亚克力效果** - 提供现代化的亚克力视觉效果
- **基类支持** - 为其他亚克力组件提供基础功能
- **主题适配** - 自动适配亮色/暗色主题
- **绘制逻辑** - 提供统一的亚克力绘制方法
- **裁剪路径** - 支持自定义的裁剪路径

核心组件
--------

AcrylicWidget
~~~~~~~~~~~~~

亚克力控件基类，提供基础的亚克力功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_widget import AcrylicWidget
   from PySide6.QtWidgets import QWidget
   
   # 创建自定义亚克力控件
   class CustomAcrylicWidget(AcrylicWidget, QWidget):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def acrylicClipPath(self):
           """定义亚克力裁剪路径"""
           from PySide6.QtGui import QPainterPath
           from PySide6.QtCore import QRectF
           
           path = QPainterPath()
           path.addRoundedRect(QRectF(self.rect()), 10, 10)
           return path

**主要方法：**
- ``acrylicClipPath()`` - 定义亚克力裁剪路径
- ``_drawAcrylic()`` - 绘制亚克力效果
- ``_updateAcrylicColor()`` - 更新亚克力颜色

实际应用
--------

基本亚克力控件
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_widget import AcrylicWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QPainterPath, QRectF
   from PySide6.QtCore import Qt
   
   class BasicAcrylicWidget(AcrylicWidget):
       """基本亚克力控件"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           """设置界面"""
           layout = QVBoxLayout(self)
           
           # 添加标签
           title_label = Label("亚克力控件")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")
           title_label.setAlignment(Qt.AlignCenter)
           
           content_label = Label("这是一个亚克力控件示例")
           content_label.setStyleSheet("color: white; padding: 10px;")
           content_label.setAlignment(Qt.AlignCenter)
           content_label.setWordWrap(True)
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           layout.addStretch()
       
       def acrylicClipPath(self):
           """定义圆角矩形裁剪路径"""
           path = QPainterPath()
           path.addRoundedRect(QRectF(self.rect()), 12, 12)
           return path
   
   class BasicAcrylicWidgetDemo(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("基本亚克力控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建亚克力控件
           acrylic_widget = BasicAcrylicWidget()
           acrylic_widget.setFixedSize(300, 150)
           
           layout.addWidget(title_label)
           layout.addWidget(acrylic_widget, alignment=Qt.AlignCenter)
           self.setLayout(layout)

圆形亚克力控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_widget import AcrylicWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QPainterPath, QRectF
   from PySide6.QtCore import Qt
   
   class CircularAcrylicWidget(AcrylicWidget):
       """圆形亚克力控件"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           """设置界面"""
           layout = QVBoxLayout(self)
           
           # 添加图标标签
           icon_label = Label("🎨")
           icon_label.setStyleSheet("font-size: 32px; color: white;")
           icon_label.setAlignment(Qt.AlignCenter)
           
           # 添加文本标签
           text_label = Label("设计")
           text_label.setStyleSheet("font-size: 14px; color: white; font-weight: bold;")
           text_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(icon_label)
           layout.addWidget(text_label)
           layout.addStretch()
       
       def acrylicClipPath(self):
           """定义圆形裁剪路径"""
           path = QPainterPath()
           rect = self.rect()
           center_x = rect.center().x()
           center_y = rect.center().y()
           radius = min(rect.width(), rect.height()) // 2 - 2
           
           path.addEllipse(center_x - radius, center_y - radius, 
                         radius * 2, radius * 2)
           return path
   
   class CircularAcrylicWidgetDemo(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("圆形亚克力控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建圆形亚克力控件
           circular_widget = CircularAcrylicWidget()
           circular_widget.setFixedSize(120, 120)
           
           layout.addWidget(title_label)
           layout.addWidget(circular_widget, alignment=Qt.AlignCenter)
           self.setLayout(layout)

高级用法
--------

自定义形状亚克力控件
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_widget import AcrylicWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QPainterPath, QRectF
   from PySide6.QtCore import Qt
   
   class StarAcrylicWidget(AcrylicWidget):
       """星形亚克力控件"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           """设置界面"""
           layout = QVBoxLayout(self)
           
           # 添加星形标签
           star_label = Label("⭐")
           star_label.setStyleSheet("font-size: 24px; color: white;")
           star_label.setAlignment(Qt.AlignCenter)
           
           # 添加文本标签
           text_label = Label("收藏")
           text_label.setStyleSheet("font-size: 12px; color: white;")
           text_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(star_label)
           layout.addWidget(text_label)
           layout.addStretch()
       
       def acrylicClipPath(self):
           """定义星形裁剪路径"""
           path = QPainterPath()
           rect = self.rect()
           center_x = rect.center().x()
           center_y = rect.center().y()
           size = min(rect.width(), rect.height()) // 2 - 5
           
           # 创建五角星路径
           import math
           points = []
           for i in range(10):
               angle = math.pi * i / 5 - math.pi / 2
               if i % 2 == 0:
                   # 外顶点
                   x = center_x + size * math.cos(angle)
                   y = center_y + size * math.sin(angle)
               else:
                   # 内顶点
                   x = center_x + size * 0.4 * math.cos(angle)
                   y = center_y + size * 0.4 * math.sin(angle)
               points.append((x, y))
           
           path.moveTo(points[0][0], points[0][1])
           for x, y in points[1:]:
               path.lineTo(x, y)
           path.closeSubpath()
           
           return path
   
   class StarAcrylicWidgetDemo(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("星形亚克力控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建星形亚克力控件
           star_widget = StarAcrylicWidget()
           star_widget.setFixedSize(100, 100)
           
           layout.addWidget(title_label)
           layout.addWidget(star_widget, alignment=Qt.AlignCenter)
           self.setLayout(layout)

动态亚克力控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_widget import AcrylicWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QPainterPath, QRectF
   from PySide6.QtCore import Qt, QTimer
   
   class DynamicAcrylicWidget(AcrylicWidget):
       """动态亚克力控件"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
           self.setup_animation()
       
       def setup_ui(self):
           """设置界面"""
           layout = QVBoxLayout(self)
           
           # 添加动态标签
           self.status_label = Label("就绪")
           self.status_label.setStyleSheet("font-size: 14px; color: white; font-weight: bold;")
           self.status_label.setAlignment(Qt.AlignCenter)
           
           # 添加计数标签
           self.count_label = Label("0")
           self.count_label.setStyleSheet("font-size: 24px; color: white;")
           self.count_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(self.status_label)
           layout.addWidget(self.count_label)
           layout.addStretch()
       
       def setup_animation(self):
           """设置动画"""
           self.counter = 0
           self.timer = QTimer()
           self.timer.timeout.connect(self.update_content)
           self.timer.start(1000)  # 每秒更新一次
       
       def update_content(self):
           """更新内容"""
           self.counter += 1
           self.count_label.setText(str(self.counter))
           
           # 根据计数器更新状态
           if self.counter < 10:
               self.status_label.setText("初始化")
           elif self.counter < 30:
               self.status_label.setText("处理中")
           elif self.counter < 50:
               self.status_label.setText("即将完成")
           else:
               self.status_label.setText("已完成")
               self.timer.stop()
       
       def acrylicClipPath(self):
           """定义动态变化的裁剪路径"""
           path = QPainterPath()
           rect = self.rect()
           
           # 根据计数器调整圆角大小
           if self.counter < 10:
               radius = 20
           elif self.counter < 30:
               radius = 15
           elif self.counter < 50:
               radius = 10
           else:
               radius = 5
           
           path.addRoundedRect(QRectF(rect), radius, radius)
           return path
   
   class DynamicAcrylicWidgetDemo(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态亚克力控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建动态亚克力控件
           dynamic_widget = DynamicAcrylicWidget()
           dynamic_widget.setFixedSize(200, 120)
           
           # 控制按钮
           from qfluentwidgets import PushButton
           
           self.restart_btn = PushButton("重新开始")
           self.restart_btn.clicked.connect(dynamic_widget.setup_animation)
           
           layout.addWidget(title_label)
           layout.addWidget(dynamic_widget, alignment=Qt.AlignCenter)
           layout.addWidget(self.restart_btn, alignment=Qt.AlignCenter)
           self.setLayout(layout)

渐变亚克力控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_widget import AcrylicWidget
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QPainterPath, QRectF, QLinearGradient, QColor
   from PySide6.QtCore import Qt
   
   class GradientAcrylicWidget(AcrylicWidget):
       """渐变亚克力控件"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
       
       def setup_ui(self):
           """设置界面"""
           layout = QVBoxLayout(self)
           
           # 添加标题标签
           title_label = Label("渐变效果")
           title_label.setStyleSheet("font-size: 16px; color: white; font-weight: bold;")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 添加内容标签
           content_label = Label("支持渐变背景的亚克力控件")
           content_label.setStyleSheet("color: white; padding: 10px;")
           content_label.setAlignment(Qt.AlignCenter)
           content_label.setWordWrap(True)
           
           layout.addWidget(title_label)
           layout.addWidget(content_label)
           layout.addStretch()
       
       def acrylicClipPath(self):
           """定义渐变裁剪路径"""
           path = QPainterPath()
           rect = self.rect()
           
           # 创建椭圆形路径
           path.addEllipse(QRectF(rect.adjusted(5, 5, -5, -5)))
           return path
       
       def paintEvent(self, event):
           """重写绘制事件添加渐变背景"""
           from PySide6.QtGui import QPainter
           
           painter = QPainter(self)
           painter.setRenderHints(QPainter.Antialiasing)
           
           # 绘制渐变背景
           gradient = QLinearGradient(0, 0, self.width(), self.height())
           gradient.setColorAt(0.0, QColor(255, 107, 107, 200))
           gradient.setColorAt(0.5, QColor(78, 205, 196, 200))
           gradient.setColorAt(1.0, QColor(69, 183, 209, 200))
           
           painter.setBrush(gradient)
           painter.setPen(Qt.NoPen)
           
           # 使用裁剪路径
           path = self.acrylicClipPath()
           if not path.isEmpty():
               painter.setClipPath(path)
               painter.drawPath(path)
           
           # 调用父类绘制亚克力效果
           super().paintEvent(event)
   
   class GradientAcrylicWidgetDemo(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("渐变亚克力控件示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建渐变亚克力控件
           gradient_widget = GradientAcrylicWidget()
           gradient_widget.setFixedSize(250, 150)
           
           layout.addWidget(title_label)
           layout.addWidget(gradient_widget, alignment=Qt.AlignCenter)
           self.setLayout(layout)

最佳实践
--------

1. **路径定义** - 正确定义acrylicClipPath方法
2. **性能优化** - 避免过于复杂的裁剪路径
3. **主题适配** - 利用内置的主题适配功能
4. **绘制顺序** - 正确处理亚克力效果和自定义绘制
5. **尺寸考虑** - 考虑不同尺寸下的显示效果

注意事项
--------

- 亚克力效果需要正确的背景支持
- acrylicClipPath方法必须正确实现
- 复杂的裁剪路径可能影响性能
- 主题变化时会自动更新颜色
- 继承时需要正确调用父类方法

相关模块
--------

- :doc:`components.material.acrylic_label` - 亚克力标签
- :doc:`components.widgets.acrylic_label` - 亚克力标签组件
- :doc:`components.material.acrylic_menu` - 亚克力菜单
