Image Utils 图像工具模块
=========================

Image Utils 模块提供图像处理和颜色分析工具，包括高斯模糊、主色提取、颜色空间转换等功能。
该模块主要用于图像背景处理和主题色彩提取，确保界面视觉效果的一致性。

主要功能
--------

- **高斯模糊** - 创建模糊背景效果
- **主色提取** - 从图像中提取主要颜色
- **颜色空间转换** - RGB/HSV颜色空间转换
- **图像格式转换** - QImage/QPixmap与PIL图像互转
- **色彩分析** - 分析图像的色彩丰富度

核心函数
--------

gaussianBlur()
~~~~~~~~~~~~~

高斯模糊处理，创建模糊背景效果。

.. code-block:: python

   from qfluentwidgets.common.image_utils import gaussianBlur
   from PySide6.QtGui import QPixmap
   
   # 基本模糊
   blurred_pixmap = gaussianBlur("image.jpg")
   
   # 自定义模糊参数
   blurred_pixmap = gaussianBlur(
       "image.jpg", 
       blurRadius=25,      # 模糊半径
       brightFactor=1.2,   # 亮度因子
       blurPicSize=(800, 600)  # 模糊处理尺寸
   )
   
   # 处理QPixmap
   original_pixmap = QPixmap("image.jpg")
   blurred_pixmap = gaussianBlur(original_pixmap)

**参数说明：**
- ``image`` - 图像路径或QPixmap对象
- ``blurRadius`` - 模糊半径，默认为18
- ``brightFactor`` - 亮度因子，默认为1
- ``blurPicSize`` - 模糊处理尺寸，用于减少计算量

fromqpixmap()
~~~~~~~~~~~~~

将QImage/QPixmap转换为PIL图像。

.. code-block:: python

   from qfluentwidgets.common.image_utils import fromqpixmap
   from PySide6.QtGui import QPixmap, QImage
   from PIL import Image
   
   # 转换QPixmap
   qpixmap = QPixmap("image.jpg")
   pil_image = fromqpixmap(qpixmap)
   
   # 转换QImage
   qimage = QImage("image.jpg")
   pil_image = fromqpixmap(qimage)
   
   # 使用PIL处理
   pil_image = pil_image.resize((200, 200), Image.ANTIALIAS)
   pil_image = pil_image.convert('L')  # 转为灰度

DominantColor
~~~~~~~~~~~~~

主色提取类，从图像中提取主要颜色。

.. code-block:: python

   from qfluentwidgets.common.image_utils import DominantColor
   
   # 提取主色
   dominant_color = DominantColor.getDominantColor("image.jpg")
   print(f"主色: {dominant_color}")  # (r, g, b)
   
   # 处理资源图像
   resource_color = DominantColor.getDominantColor(":/images/background.jpg")

**特点：**
- 自动调整色彩亮度
- 过滤过于接近黑色的颜色
- 按色彩丰富度排序
- 异常处理保护

颜色空间转换
------------

rgb2hsv()
~~~~~~~~~~

将RGB颜色转换为HSV颜色空间。

.. code-block:: python

   from qfluentwidgets.common.image_utils import DominantColor
   
   # RGB转HSV
   r, g, b = 255, 0, 0  # 红色
   h, s, v = DominantColor.rgb2hsv((r, g, b))
   print(f"HSV: ({h}, {s}, {v})")  # (0, 1, 1)

hsv2rgb()
~~~~~~~~~~

将HSV颜色转换为RGB颜色空间。

.. code-block:: python

   from qfluentwidgets.common.image_utils import DominantColor
   
   # HSV转RGB
   h, s, v = 120, 1, 1  # 绿色
   r, g, b = DominantColor.hsv2rgb(h, s, v)
   print(f"RGB: ({r}, {g}, {b})")  # (0, 255, 0)

colorfulness()
~~~~~~~~~~~~~~

计算颜色的丰富度。

.. code-block:: python

   from qfluentwidgets.common.image_utils import DominantColor
   
   # 计算色彩丰富度
   richness = DominantColor.colorfulness(255, 0, 0)    # 红色
   richness = DominantColor.colorfulness(128, 128, 128)  # 灰色
   
   print(f"色彩丰富度: {richness}")

实际应用
--------

背景模糊效果
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.image_utils import gaussianBlur
   from qfluentwidgets import BackgroundMaskWidget, FluentIcon
   from PySide6.QtGui import QPixmap
   
   class BlurredBackgroundWidget(BackgroundMaskWidget):
       def __init__(self, image_path):
           super().__init__()
           self.set_blurred_background(image_path)
       
       def set_blurred_background(self, image_path):
           """设置模糊背景"""
           # 创建模糊背景
           blurred_pixmap = gaussianBlur(
               image_path,
               blurRadius=30,
               brightFactor=0.8,
               blurPicSize=(1920, 1080)
           )
           
           # 设置背景
           self.setBackground(blurred_pixmap)
   
   # 使用
   widget = BlurredBackgroundWidget("background.jpg")

主题色彩提取
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.image_utils import DominantColor
   from qfluentwidgets.common.color import FluentThemeColor
   from PySide6.QtGui import QColor
   
   class ThemeColorExtractor:
       def __init__(self):
           self.cache = {}
       
       def extract_theme_color(self, image_path):
           """提取主题色彩"""
           if image_path in self.cache:
               return self.cache[image_path]
           
           # 提取主色
           dominant_color = DominantColor.getDominantColor(image_path)
           qcolor = QColor(*dominant_color)
           
           # 缓存结果
           self.cache[image_path] = qcolor
           return qcolor
       
       def apply_theme_color(self, image_path, widget):
           """应用主题色彩到控件"""
           theme_color = self.extract_theme_color(image_path)
           
           # 应用到控件样式
           widget.setStyleSheet(f"""
               QWidget {{
                   background-color: {theme_color.name()};
                   color: white;
               }}
           """)
   
   # 使用
   extractor = ThemeColorExtractor()
   extractor.apply_theme_color("album_cover.jpg", widget)

图像处理管道
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.image_utils import gaussianBlur, fromqpixmap, DominantColor
   from PySide6.QtGui import QPixmap, QImage
   from PIL import Image, ImageEnhance
   
   class ImageProcessor:
       def __init__(self):
           pass
       
       def create_thumbnail(self, image_path, size=(200, 200)):
           """创建缩略图"""
           # 转换为PIL图像
           qpixmap = QPixmap(image_path)
           pil_image = fromqpixmap(qpixmap)
           
           # 创建缩略图
           pil_image.thumbnail(size, Image.ANTIALIAS)
           
           # 转换回QPixmap
           return QPixmap.fromImage(QImage(pil_image))
       
       def enhance_image(self, image_path, brightness=1.2, contrast=1.1):
           """增强图像"""
           qpixmap = QPixmap(image_path)
           pil_image = fromqpixmap(qpixmap)
           
           # 亮度增强
           enhancer = ImageEnhance.Brightness(pil_image)
           pil_image = enhancer.enhance(brightness)
           
           # 对比度增强
           enhancer = ImageEnhance.Contrast(pil_image)
           pil_image = enhancer.enhance(contrast)
           
           return QPixmap.fromImage(QImage(pil_image))
       
       def create_blurred_thumbnail(self, image_path, size=(200, 200)):
           """创建模糊缩略图"""
           # 先创建缩略图
           thumbnail = self.create_thumbnail(image_path, size)
           
           # 应用模糊
           blurred = gaussianBlur(thumbnail, blurRadius=10, brightFactor=1.0)
           
           return blurred
   
   # 使用
   processor = ImageProcessor()
   thumbnail = processor.create_thumbnail("image.jpg")
   enhanced = processor.enhance_image("image.jpg")
   blurred_thumb = processor.create_blurred_thumbnail("image.jpg")

色彩分析工具
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.image_utils import DominantColor
   import matplotlib.pyplot as plt
   
   class ColorAnalyzer:
       def __init__(self, image_path):
           self.image_path = image_path
           self.dominant_color = DominantColor.getDominantColor(image_path)
       
       def analyze_color_distribution(self):
           """分析颜色分布"""
           # 这里可以扩展更复杂的颜色分析
           r, g, b = self.dominant_color
           
           # 计算颜色属性
           brightness = (r + g + b) / 3
           saturation = max(r, g, b) - min(r, g, b)
           
           return {
               'dominant_color': self.dominant_color,
               'brightness': brightness,
               'saturation': saturation,
               'is_warm': r > b,  # 暖色调判断
               'colorfulness': DominantColor.colorfulness(r, g, b)
           }
       
       def suggest_theme(self):
           """建议主题颜色"""
           analysis = self.analyze_color_distribution()
           
           r, g, b = self.dominant_color
           brightness = analysis['brightness']
           
           # 根据主色和亮度建议主题
           if brightness > 200:
               return "light"  # 亮色主题
           elif brightness < 50:
               return "dark"   # 暗色主题
           else:
               return "auto"   # 自动主题
       
       def create_color_palette(self, num_colors=5):
           """创建调色板"""
           # 这里可以扩展创建完整调色板的功能
           base_color = self.dominant_color
           palette = [base_color]
           
           # 生成互补色、类似色等
           h, s, v = DominantColor.rgb2hsv(base_color)
           
           # 互补色
           complementary_h = (h + 180) % 360
           complementary = DominantColor.hsv2rgb(complementary_h, s, v)
           palette.append(complementary)
           
           return palette
   
   # 使用
   analyzer = ColorAnalyzer("image.jpg")
   analysis = analyzer.analyze_color_distribution()
   theme = analyzer.suggest_theme()
   palette = analyzer.create_color_palette()

高级用法
--------

批量图像处理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.image_utils import gaussianBlur, DominantColor
   import os
   from concurrent.futures import ThreadPoolExecutor
   
   class BatchImageProcessor:
       def __init__(self, max_workers=4):
           self.max_workers = max_workers
       
       def process_batch(self, image_paths, output_dir):
           """批量处理图像"""
           os.makedirs(output_dir, exist_ok=True)
           
           with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
               futures = []
               
               for image_path in image_paths:
                   future = executor.submit(
                       self._process_single_image, 
                       image_path, 
                       output_dir
                   )
                   futures.append(future)
               
               # 等待所有任务完成
               results = [future.result() for future in futures]
           
           return results
       
       def _process_single_image(self, image_path, output_dir):
           """处理单个图像"""
           try:
               # 创建模糊版本
               blurred = gaussianBlur(image_path, blurRadius=20)
               blurred_path = os.path.join(
                   output_dir, 
                   f"blurred_{os.path.basename(image_path)}"
               )
               blurred.save(blurred_path)
               
               # 提取主色
               dominant_color = DominantColor.getDominantColor(image_path)
               
               return {
                   'original': image_path,
                   'blurred': blurred_path,
                   'dominant_color': dominant_color,
                   'status': 'success'
               }
           
           except Exception as e:
               return {
                   'original': image_path,
                   'status': 'error',
                   'error': str(e)
               }
   
   # 使用
   processor = BatchImageProcessor()
   image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
   results = processor.process_batch(image_paths, "output")

实时图像处理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.image_utils import gaussianBlur, DominantColor
   from PySide6.QtCore import QTimer, QThread, Signal
   from PySide6.QtGui import QPixmap
   
   class ImageProcessingThread(QThread):
       processed = Signal(QPixmap)
       color_extracted = Signal(tuple)
       
       def __init__(self, image_path):
           super().__init__()
           self.image_path = image_path
       
       def run(self):
           # 处理图像
           blurred = gaussianBlur(self.image_path)
           self.processed.emit(blurred)
           
           # 提取颜色
           color = DominantColor.getDominantColor(self.image_path)
           self.color_extracted.emit(color)
   
   class RealTimeImageProcessor:
       def __init__(self):
           self.current_thread = None
       
       def process_image(self, image_path):
           """处理图像（异步）"""
           if self.current_thread and self.current_thread.isRunning():
               self.current_thread.quit()
               self.current_thread.wait()
           
           self.current_thread = ImageProcessingThread(image_path)
           self.current_thread.processed.connect(self.on_image_processed)
           self.current_thread.color_extracted.connect(self.on_color_extracted)
           self.current_thread.start()
       
       def on_image_processed(self, pixmap):
           """图像处理完成"""
           # 更新UI显示模糊图像
           pass
       
       def on_color_extracted(self, color):
           """颜色提取完成"""
           # 更新UI显示主色
           pass

最佳实践
--------

1. **性能优化** - 使用适当的模糊尺寸减少计算量
2. **缓存机制** - 缓存处理结果避免重复计算
3. **异常处理** - 使用异常处理装饰器保护关键函数
4. **批量处理** - 使用多线程处理大量图像
5. **内存管理** - 及时释放大图像对象

注意事项
--------

- 高斯模糊计算量较大，建议设置合适的处理尺寸
- 主色提取依赖于ColorThief库，需要正确安装
- 资源图像（以:开头）无法提取主色
- 颜色转换函数使用标准算法，可能存在精度误差

相关模块
--------

- :doc:`common.color` - 颜色管理
- :doc:`common.exception_handler` - 异常处理
- :doc:`components.widgets` - UI组件
