Acrylic Label 亚克力标签模块
=================================

Acrylic Label 模块提供亚克力风格的标签控件，支持模糊背景、纹理效果和自定义颜色。
该模块实现了Windows Fluent Design中的亚克力材质效果，提供现代化的视觉体验。

主要功能
--------

- **亚克力效果** - 实现Windows Fluent Design的亚克力材质
- **模糊背景** - 支持高斯模糊背景效果
- **纹理叠加** - 提供噪声纹理增强视觉效果
- **自定义颜色** - 支持自定义色调和亮度颜色
- **异步处理** - 使用线程处理模糊效果避免界面卡顿
- **画笔支持** - 提供亚克力画笔用于自定义绘制

核心组件
--------

checkAcrylicAvailability
~~~~~~~~~~~~~~~~~~~~~~~

检查亚克力效果可用性函数。

.. code-block:: python

   from qfluentwidgets.components.widgets.acrylic_label import checkAcrylicAvailability
   
   # 检查亚克力效果是否可用
   is_available = checkAcrylicAvailability()
   
   if is_available:
       print("亚克力效果可用")
   else:
       print("亚克力效果不可用，请安装完整版")

BlurCoverThread
~~~~~~~~~~~~~~

模糊处理线程，用于异步处理图像模糊效果。

.. code-block:: python

   from qfluentwidgets.components.widgets.acrylic_label import BlurCoverThread
   from PySide6.QtCore import QObject
   
   class BlurProcessor(QObject):
       def __init__(self):
           super().__init__()
           self.blur_thread = BlurCoverThread()
           self.blur_thread.blurFinished.connect(self.on_blur_finished)
       
       def process_image(self, image_path):
           """处理图像模糊"""
           self.blur_thread.blur(
               imagePath=image_path,
               blurRadius=8,
               maxSize=(450, 450)
           )
       
       def on_blur_finished(self, pixmap):
           """模糊完成处理"""
           print("模糊处理完成")
           # 使用处理后的pixmap

**主要信号：**
- ``blurFinished`` - 模糊处理完成信号

**主要方法：**
- ``blur()`` - 开始模糊处理

AcrylicTextureLabel
~~~~~~~~~~~~~~~~~~

亚克力纹理标签，提供纯亚克力纹理效果。

.. code-block:: python

   from qfluentwidgets.components.widgets.acrylic_label import AcrylicTextureLabel
   from PySide6.QtGui import QColor
   
   # 创建亚克力纹理标签
   texture_label = AcrylicTextureLabel(
       tintColor=QColor(255, 255, 255, 120),
       luminosityColor=QColor(255, 255, 255, 20),
       noiseOpacity=0.03,
       parent=parent
   )
   
   # 设置色调颜色
   texture_label.setTintColor(QColor(200, 200, 255, 150))

**主要方法：**
- ``setTintColor()`` - 设置色调颜色

AcrylicLabel
~~~~~~~~~~~~

亚克力标签，支持图像模糊和亚克力效果。

.. code-block:: python

   from qfluentwidgets.components.widgets.acrylic_label import AcrylicLabel
   from PySide6.QtGui import QColor
   
   # 创建亚克力标签
   acrylic_label = AcrylicLabel(
       blurRadius=30,
       tintColor=QColor(255, 255, 255, 120),
       luminosityColor=QColor(255, 255, 255, 10),
       maxBlurSize=(800, 600),
       parent=parent
   )
   
   # 设置图像
   acrylic_label.setImage("path/to/image.jpg")
   
   # 设置色调颜色
   acrylic_label.setTintColor(QColor(200, 200, 255, 150))

**主要方法：**
- ``setImage()`` - 设置要模糊的图像
- ``setTintColor()`` - 设置色调颜色

AcrylicBrush
~~~~~~~~~~~~

亚克力画笔，用于在自定义控件上绘制亚克力效果。

.. code-block:: python

   from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush
   from PySide6.QtGui import QColor, QPainterPath
   from PySide6.QtWidgets import QWidget
   
   class CustomAcrylicWidget(QWidget):
       def __init__(self):
           super().__init__()
           
           # 创建亚克力画笔
           self.acrylic_brush = AcrylicBrush(
               device=self,
               blurRadius=30,
               tintColor=QColor(255, 255, 255, 120),
               luminosityColor=QColor(255, 255, 255, 10),
               noiseOpacity=0.03
           )
       
       def paintEvent(self, event):
           # 绘制亚克力效果
           self.acrylic_brush.paint()
       
       def set_background(self, image_path):
           """设置背景图像"""
           self.acrylic_brush.setImage(image_path)
       
       def set_clip_path(self, path):
           """设置裁剪路径"""
           self.acrylic_brush.setClipPath(path)

**主要方法：**
- ``setBlurRadius()`` - 设置模糊半径
- ``setTintColor()`` - 设置色调颜色
- ``setLuminosityColor()`` - 设置亮度颜色
- ``grabImage()`` - 从屏幕抓取图像
- ``setImage()`` - 设置图像
- ``setClipPath()`` - 设置裁剪路径
- ``paint()`` - 绘制亚克力效果
- ``isAvailable()`` - 检查亚克力是否可用

实际应用
--------

基本亚克力标签应用
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.widgets.acrylic_label import AcrylicLabel
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   
   class BasicAcrylicWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_acrylic()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("基本亚克力标签应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.image_btn = PushButton("设置图像")
           self.color_btn = PushButton("更改颜色")
           self.clear_btn = PushButton("清除图像")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.image_btn)
           header_layout.addWidget(self.color_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建亚克力标签
           self.acrylic_label = AcrylicLabel(
               blurRadius=25,
               tintColor=QColor(255, 255, 255, 100),
               luminosityColor=QColor(255, 255, 255, 15),
               maxBlurSize=(600, 400),
               parent=self
           )
           self.acrylic_label.setFixedSize(600, 400)
           self.acrylic_label.setAlignment(Qt.AlignCenter)
           self.acrylic_label.setText("亚克力标签示例")
           
           # 显示当前状态
           self.status_label = Label("状态: 亚克力标签已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.acrylic_label)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_acrylic(self):
           """设置亚克力效果"""
           self.current_color_index = 0
           self.colors = [
               QColor(255, 255, 255, 100),  # 白色
               QColor(100, 200, 255, 100),  # 蓝色
               QColor(255, 100, 100, 100),  # 红色
               QColor(100, 255, 100, 100),  # 绿色
               QColor(255, 255, 100, 100),  # 黄色
           ]
           
           self.status_label.setText("状态: 亚克力标签已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.image_btn.clicked.connect(self.set_image)
           self.color_btn.clicked.connect(self.change_color)
           self.clear_btn.clicked.connect(self.clear_image)
       
       def set_image(self):
           """设置图像"""
           # 这里应该使用文件对话框选择图像
           # 示例使用占位符
           image_path = "path/to/sample/image.jpg"
           
           try:
               self.acrylic_label.setImage(image_path)
               self.status_label.setText(f"状态: 已设置图像 {image_path}")
           except Exception as e:
               self.status_label.setText(f"状态: 设置图像失败: {str(e)}")
       
       def change_color(self):
           """更改颜色"""
           self.current_color_index = (self.current_color_index + 1) % len(self.colors)
           color = self.colors[self.current_color_index]
           
           self.acrylic_label.setTintColor(color)
           
           color_name = ["白色", "蓝色", "红色", "绿色", "黄色"][self.current_color_index]
           self.status_label.setText(f"状态: 已更改为{color_name}色调")
       
       def clear_image(self):
           """清除图像"""
           self.acrylic_label.setImage("")
           self.acrylic_label.setText("亚克力标签示例")
           self.status_label.setText("状态: 已清除图像")

高级亚克力画笔应用
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush, checkAcrylicAvailability
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor, QPainter, QPainterPath
   
   class AdvancedAcrylicWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_acrylic()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级亚克力画笔应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.blur_btn = PushButton("调整模糊")
           self.color_btn = PushButton("更改颜色")
           self.shape_btn = PushButton("更改形状")
           self.grab_btn = PushButton("抓取背景")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.blur_btn)
           header_layout.addWidget(self.color_btn)
           header_layout.addWidget(self.shape_btn)
           header_layout.addWidget(self.grab_btn)
           
           # 创建自定义亚克力控件
           self.acrylic_widget = CustomAcrylicWidget(parent=self)
           self.acrylic_widget.setFixedSize(600, 400)
           
           # 显示当前状态
           self.status_label = Label("状态: 高级亚克力画笔已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.acrylic_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_acrylic(self):
           """设置亚克力画笔"""
           # 检查可用性
           if not checkAcrylicAvailability():
               self.status_label.setText("状态: 亚克力效果不可用")
               return
           
           self.current_blur = 30
           self.current_color_index = 0
           self.current_shape_index = 0
           
           self.colors = [
               QColor(255, 255, 255, 120),
               QColor(100, 200, 255, 120),
               QColor(255, 100, 100, 120),
           ]
           
           self.status_label.setText("状态: 高级亚克力画笔已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.blur_btn.clicked.connect(self.adjust_blur)
           self.color_btn.clicked.connect(self.change_color)
           self.shape_btn.clicked.connect(self.change_shape)
           self.grab_btn.clicked.connect(self.grab_background)
       
       def adjust_blur(self):
           """调整模糊半径"""
           # 循环切换模糊半径
           blur_values = [15, 30, 45, 60]
           current_index = blur_values.index(self.current_blur)
           self.current_blur = blur_values[(current_index + 1) % len(blur_values)]
           
           self.acrylic_widget.acrylic_brush.setBlurRadius(self.current_blur)
           self.status_label.setText(f"状态: 模糊半径已调整为 {self.current_blur}")
       
       def change_color(self):
           """更改颜色"""
           self.current_color_index = (self.current_color_index + 1) % len(self.colors)
           color = self.colors[self.current_color_index]
           
           self.acrylic_widget.acrylic_brush.setTintColor(color)
           
           color_name = ["白色", "蓝色", "红色"][self.current_color_index]
           self.status_label.setText(f"状态: 已更改为{color_name}色调")
       
       def change_shape(self):
           """更改形状"""
           self.current_shape_index = (self.current_shape_index + 1) % 3
           
           # 创建不同的裁剪路径
           path = QPainterPath()
           
           if self.current_shape_index == 0:  # 矩形
               path.addRect(50, 50, 500, 300)
           elif self.current_shape_index == 1:  # 圆形
               path.addEllipse(150, 100, 300, 200)
           else:  # 圆角矩形
               path.addRoundedRect(50, 50, 500, 300, 30, 30)
           
           self.acrylic_widget.acrylic_brush.setClipPath(path)
           
           shape_name = ["矩形", "圆形", "圆角矩形"][self.current_shape_index]
           self.status_label.Text(f"状态: 已更改为{shape_name}形状")
       
       def grab_background(self):
           """抓取背景"""
           try:
               # 获取控件位置
               widget_rect = self.acrylic_widget.rect()
               global_rect = self.acrylic_widget.mapToGlobal(widget_rect.topLeft())
               grab_rect = QRect(global_rect, widget_rect.size())
               
               # 抓取屏幕图像
               self.acrylic_widget.acrylic_brush.grabImage(grab_rect)
               self.status_label.setText("状态: 已抓取背景图像")
           except Exception as e:
               self.status_label.setText(f"状态: 抓取背景失败: {str(e)}")


   class CustomAcrylicWidget(QWidget):
       """自定义亚克力控件"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           
           # 创建亚克力画笔
           self.acrylic_brush = AcrylicBrush(
               device=self,
               blurRadius=30,
               tintColor=QColor(255, 255, 255, 120),
               luminosityColor=QColor(255, 255, 255, 10),
               noiseOpacity=0.03
           )
           
           # 设置默认背景
           self.acrylic_brush.setImage("path/to/background.jpg")
       
       def paintEvent(self, event):
           """绘制事件"""
           # 绘制亚克力效果
           self.acrylic_brush.paint()

亚克力纹理应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.widgets.acrylic_label import AcrylicTextureLabel
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   
   class AcrylicTextureWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_texture()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("亚克力纹理应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.color_btn = PushButton("更改颜色")
           self.opacity_btn = PushButton("调整透明度")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.color_btn)
           header_layout.addWidget(self.opacity_btn)
           
           # 创建亚克力纹理标签
           self.texture_label = AcrylicTextureLabel(
               tintColor=QColor(255, 255, 255, 120),
               luminosityColor=QColor(255, 255, 255, 20),
               noiseOpacity=0.03,
               parent=self
           )
           self.texture_label.setFixedSize(600, 400)
           
           # 显示当前状态
           self.status_label = Label("状态: 亚克力纹理已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.texture_label)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_texture(self):
           """设置纹理效果"""
           self.current_color_index = 0
           self.current_opacity = 0.03
           
           self.colors = [
               QColor(255, 255, 255, 120),  # 白色
               QColor(100, 200, 255, 120),  # 蓝色
               QColor(255, 100, 100, 120),  # 红色
               QColor(100, 255, 100, 120),  # 绿色
           ]
           
           self.status_label.setText("状态: 亚克力纹理已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.color_btn.clicked.connect(self.change_color)
           self.opacity_btn.clicked.connect(self.adjust_opacity)
       
       def change_color(self):
           """更改颜色"""
           self.current_color_index = (self.current_color_index + 1) % len(self.colors)
           color = self.colors[self.current_color_index]
           
           self.texture_label.setTintColor(color)
           
           color_name = ["白色", "蓝色", "红色", "绿色"][self.current_color_index]
           self.status_label.setText(f"状态: 已更改为{color_name}纹理")
       
       def adjust_opacity(self):
           """调整透明度"""
           # 循环切换透明度
           opacity_values = [0.01, 0.03, 0.05, 0.08, 0.1]
           current_index = opacity_values.index(self.current_opacity)
           self.current_opacity = opacity_values[(current_index + 1) % len(opacity_values)]
           
           # 重新创建纹理标签以更新透明度
           self.texture_label = AcrylicTextureLabel(
               tintColor=self.colors[self.current_color_index],
               luminosityColor=QColor(255, 255, 255, 20),
               noiseOpacity=self.current_opacity,
               parent=self
           )
           self.texture_label.setFixedSize(600, 400)
           
           # 更新布局
           # 这里需要重新添加到布局中
           
           self.status_label.Text(f"状态: 透明度已调整为 {self.current_opacity}")

最佳实践
--------

1. **可用性检查** - 使用前检查亚克力效果是否可用
2. **性能优化** - 合理设置模糊半径和图像尺寸
3. **异步处理** - 使用BlurCoverThread避免界面卡顿
4. **颜色搭配** - 选择合适的色调和亮度颜色
5. **内存管理** - 及时释放不需要的图像资源

注意事项
--------

- 需要安装完整版才能使用亚克力效果
- 模糊处理可能消耗较多计算资源
- 大图像处理时建议设置maxBlurSize限制
- 噪声纹理需要相应的资源文件
- 在某些系统上可能不支持亚克力效果
- 透明度设置会影响整体视觉效果

相关模块
--------

- :doc:`components.widgets.label` - 标签控件
- :doc:`common.image_utils` - 图像处理工具
- :doc:`common.screen` - 屏幕相关工具
- :doc:`common.style_sheet` - 样式表
