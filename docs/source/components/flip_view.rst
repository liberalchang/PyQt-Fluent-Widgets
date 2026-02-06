FlipView 翻页视图控件模块
========================

FlipView 模块提供Fluent Design风格的翻页视图控件，支持水平和垂直方向的图片浏览。该模块实现了现代化的图片展示效果，提供流畅的翻页动画和交互体验。

主要功能
--------

- **双向支持** - 支持水平和垂直翻页方向
- **图片展示** - 专门为图片展示优化的视图控件
- **平滑动画** - 提供流畅的翻页滚动动画
- **导航按钮** - 智能显示的前进/后退按钮
- **滚轮支持** - 支持鼠标滚轮翻页
- **懒加载** - 支持图片的延迟加载
- **圆角支持** - 可配置的图片圆角效果
- **宽高比控制** - 支持多种宽高比模式

核心组件
--------

FlipView
~~~~~~~~

翻页视图控件，提供图片的翻页浏览功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.flip_view import FlipView
   from PySide6.QtCore import Qt, QSize
   from PySide6.QtGui import QImage
   
   # 创建水平翻页视图
   flip_view = FlipView(Qt.Horizontal, parent=parent)
   
   # 设置图片尺寸
   flip_view.setItemSize(QSize(480, 270))
   
   # 添加图片
   flip_view.addImage("image1.jpg")
   flip_view.addImage("image2.jpg")
   flip_view.addImage(QImage("image3.png"))
   
   # 连接信号
   flip_view.currentIndexChanged.connect(self.on_index_changed)

**构造函数：**
- ``FlipView(parent: QWidget = None)``
- ``FlipView(orient: Qt.Orientation, parent: QWidget = None)``

**主要方法：**
- ``addImage(image: Union[QImage, QPixmap, str])`` - 添加单个图片
- ``addImages(images: List[Union[QImage, QPixmap, str]], targetSize: QSize = None)`` - 批量添加图片
- ``setItemImage(index: int, image, targetSize: QSize = None)`` - 设置指定索引的图片
- ``itemImage(index: int, load=True)`` - 获取指定索引的图片
- ``setItemSize(size: QSize)`` - 设置图片尺寸
- ``setBorderRadius(radius: int)`` - 设置圆角半径
- ``setAspectRatioMode(mode: Qt.AspectRatioMode)`` - 设置宽高比模式
- ``scrollPrevious()`` - 翻到上一页
- ``scrollNext()`` - 翻到下一页
- ``setCurrentIndex(index: int)`` - 设置当前索引
- ``currentIndex()`` - 获取当前索引

**信号：**
- ``currentIndexChanged(index: int)`` - 当前索引变化时发出

**属性：**
- ``itemSize`` - 图片尺寸（QSize）
- ``borderRadius`` - 圆角半径（int）
- ``aspectRatioMode`` - 宽高比模式（Qt.AspectRatioMode）

**宽高比模式：**
- ``Qt.IgnoreAspectRatio`` - 忽略宽高比，拉伸填充
- ``Qt.KeepAspectRatio`` - 保持宽高比
- ``Qt.KeepAspectRatioByExpanding`` - 保持宽高比并扩展

HorizontalFlipView
~~~~~~~~~~~~~~~~~

水平翻页视图控件，专门用于水平方向的图片浏览。

.. code-block:: python

   from qfluentwidgets.components.widgets.flip_view import HorizontalFlipView
   
   # 创建水平翻页视图
   horizontal_view = HorizontalFlipView(parent=parent)
   
   # 添加图片
   images = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]
   horizontal_view.addImages(images)

**构造函数：**
- ``HorizontalFlipView(parent: QWidget = None)``

**特点：**
- 默认水平布局
- 左右导航按钮
- 支持水平滚轮翻页

VerticalFlipView
~~~~~~~~~~~~~~~~

垂直翻页视图控件，专门用于垂直方向的图片浏览。

.. code-block:: python

   from qfluentwidgets.components.widgets.flip_view import VerticalFlipView
   
   # 创建垂直翻页视图
   vertical_view = VerticalFlipView(parent=parent)
   
   # 添加图片
   images = ["banner1.jpg", "banner2.jpg", "banner3.jpg"]
   vertical_view.addImages(images)

**构造函数：**
- ``VerticalFlipView(parent: QWidget = None)``

**特点：**
- 默认垂直布局
- 上下导航按钮
- 支持垂直滚轮翻页

FlipImageDelegate
~~~~~~~~~~~~~~~~~

翻页视图的图片委托，负责图片的绘制和渲染。

.. code-block:: python

   from qfluentwidgets.components.widgets.flip_view import FlipImageDelegate
   
   # 委托通常由FlipView自动管理
   # 可以通过FlipView的delegate属性访问
   
   delegate = flip_view.delegate
   delegate.setBorderRadius(8)

**主要方法：**
- ``setBorderRadius(radius: int)`` - 设置圆角半径
- ``itemSize(index: int)`` - 获取指定项的尺寸

**特点：**
- 支持圆角绘制
- 智能图片裁剪
- 懒加载优化
- 平滑渲染效果

ScrollButton
~~~~~~~~~~~~

滚动按钮控件，用于翻页导航。

.. code-block:: python

   from qfluentwidgets.components.widgets.flip_view import ScrollButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建滚动按钮（通常由FlipView自动管理）
   prev_button = ScrollButton(FIF.CARE_LEFT_SOLID, parent=parent)
   next_button = ScrollButton(FIF.CARE_RIGHT_SOLID, parent=parent)

**主要方法：**
- ``fadeIn()`` - 淡入显示
- ``fadeOut()`` - 淡出隐藏
- ``isTransparent()`` - 检查是否透明

**特点：**
- 平滑的透明度动画
- 智能显示/隐藏逻辑
- 适应主题颜色
- 悬浮状态响应

使用示例
--------

基础图片浏览器示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
   from PySide6.QtCore import Qt, QSize
   from PySide6.QtGui import QImage
   from qfluentwidgets.components.widgets.flip_view import FlipView
   
   class ImageGallery(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建翻页视图
           self.flip_view = FlipView(Qt.Horizontal, self)
           self.flip_view.setItemSize(QSize(600, 400))
           self.flip_view.setBorderRadius(12)
           
           # 添加示例图片（这里使用占位符）
           images = [
               "landscape1.jpg",
               "landscape2.jpg", 
               "landscape3.jpg",
               "portrait1.jpg",
               "portrait2.jpg"
           ]
           
           self.flip_view.addImages(images)
           
           # 信息显示标签
           self.info_label = QLabel("图片 1 / 5", self)
           self.info_label.setAlignment(Qt.AlignCenter)
           
           # 连接信号
           self.flip_view.currentIndexChanged.connect(self.on_index_changed)
           
           # 添加到布局
           layout.addWidget(self.flip_view)
           layout.addWidget(self.info_label)
           
       def on_index_changed(self, index):
           total = self.flip_view.count()
           self.info_label.setText(f"图片 {index + 1} / {total}")
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       gallery = ImageGallery()
       gallery.show()
       sys.exit(app.exec())

产品展示示例：

.. code-block:: python

   from PySide6.QtWidgets import QHBoxLayout, QPushButton
   from qfluentwidgets.components.widgets.button import PrimaryPushButton
   
   class ProductShowcase(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建产品展示翻页视图
           self.product_view = FlipView(Qt.Horizontal, self)
           self.product_view.setItemSize(QSize(400, 300))
           self.product_view.setBorderRadius(8)
           self.product_view.setAspectRatioMode(Qt.KeepAspectRatio)
           
           # 添加产品图片
           products = [
               "product1.jpg",
               "product2.jpg",
               "product3.jpg",
               "product4.jpg",
               "product5.jpg"
           ]
           
           self.product_view.addImages(products)
           
           # 控制按钮
           control_layout = QHBoxLayout()
           
           self.prev_btn = QPushButton("上一个", self)
           self.next_btn = QPushButton("下一个", self)
           self.auto_btn = PrimaryPushButton("自动播放", self)
           
           # 连接信号
           self.prev_btn.clicked.connect(self.product_view.scrollPrevious)
           self.next_btn.clicked.connect(self.product_view.scrollNext)
           self.auto_btn.clicked.connect(self.toggle_auto_play)
           
           self.product_view.currentIndexChanged.connect(self.update_buttons)
           
           control_layout.addWidget(self.prev_btn)
           control_layout.addWidget(self.next_btn)
           control_layout.addStretch()
           control_layout.addWidget(self.auto_btn)
           
           # 产品信息
           self.product_info = QLabel("产品信息显示区域", self)
           self.product_info.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(self.product_view)
           layout.addLayout(control_layout)
           layout.addWidget(self.product_info)
           
           # 初始化状态
           self.update_buttons(0)
           self.auto_play_timer = None
           
       def toggle_auto_play(self):
           if self.auto_play_timer:
               self.auto_play_timer.stop()
               self.auto_play_timer.deleteLater()
               self.auto_play_timer = None
               self.auto_btn.setText("自动播放")
           else:
               from PySide6.QtCore import QTimer
               self.auto_play_timer = QTimer(self)
               self.auto_play_timer.timeout.connect(self.auto_next)
               self.auto_play_timer.start(3000)  # 3秒切换
               self.auto_btn.setText("停止播放")
               
       def auto_next(self):
           current = self.product_view.currentIndex()
           total = self.product_view.count()
           next_index = (current + 1) % total
           self.product_view.setCurrentIndex(next_index)
           
       def update_buttons(self, index):
           total = self.product_view.count()
           self.prev_btn.setEnabled(index > 0)
           self.next_btn.setEnabled(index < total - 1)
           
           # 更新产品信息
           product_names = ["产品 A", "产品 B", "产品 C", "产品 D", "产品 E"]
           if index < len(product_names):
               self.product_info.setText(f"{product_names[index]} - {index + 1}/{total}")

垂直横幅展示示例：

.. code-block:: python

   from qfluentwidgets.components.widgets.flip_view import VerticalFlipView
   
   class BannerShowcase(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QHBoxLayout(self)
           
           # 创建垂直翻页视图作为侧边栏横幅
           self.banner_view = VerticalFlipView(self)
           self.banner_view.setItemSize(QSize(200, 120))
           self.banner_view.setBorderRadius(6)
           self.banner_view.setFixedWidth(220)
           
           # 添加横幅图片
           banners = [
               "banner1.jpg",
               "banner2.jpg",
               "banner3.jpg",
               "banner4.jpg"
           ]
           
           self.banner_view.addImages(banners)
           
           # 主内容区域
           self.content_area = QLabel("主要内容区域", self)
           self.content_area.setStyleSheet("""
               QLabel {
                   background-color: rgba(255, 255, 255, 0.1);
                   border: 1px solid rgba(255, 255, 255, 0.2);
                   border-radius: 8px;
                   padding: 20px;
               }
           """)
           
           layout.addWidget(self.banner_view)
           layout.addWidget(self.content_area, 1)

动态图片加载示例：

.. code-block:: python

   from PySide6.QtCore import QThread, Signal
   import requests
   from io import BytesIO
   
   class ImageLoader(QThread):
       imageLoaded = Signal(QImage, str)
       
       def __init__(self, url, name):
           super().__init__()
           self.url = url
           self.name = name
           
       def run(self):
           try:
               response = requests.get(self.url)
               image = QImage()
               image.loadFromData(response.content)
               self.imageLoaded.emit(image, self.name)
           except Exception as e:
               print(f"加载图片失败: {e}")
   
   class DynamicFlipView(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建翻页视图
           self.flip_view = FlipView(Qt.Horizontal, self)
           self.flip_view.setItemSize(QSize(500, 350))
           self.flip_view.setBorderRadius(10)
           
           # 状态标签
           self.status_label = QLabel("正在加载图片...", self)
           
           layout.addWidget(self.flip_view)
           layout.addWidget(self.status_label)
           
           # 加载网络图片
           self.load_network_images()
           
       def load_network_images(self):
           # 示例图片URL（实际使用时替换为真实URL）
           image_urls = [
               ("https://example.com/image1.jpg", "图片1"),
               ("https://example.com/image2.jpg", "图片2"),
               ("https://example.com/image3.jpg", "图片3")
           ]
           
           self.loaded_count = 0
           self.total_count = len(image_urls)
           
           for url, name in image_urls:
               loader = ImageLoader(url, name)
               loader.imageLoaded.connect(self.on_image_loaded)
               loader.start()
               
       def on_image_loaded(self, image, name):
           self.flip_view.addImage(image)
           self.loaded_count += 1
           self.status_label.setText(f"已加载 {self.loaded_count}/{self.total_count} 张图片")

样式自定义
----------

可以通过样式表自定义翻页视图的外观：

.. code-block:: python

   # 自定义FlipView样式
   flip_view = FlipView()
   flip_view.setStyleSheet("""
       FlipView {
           background-color: rgba(255, 255, 255, 0.05);
           border: 1px solid rgba(255, 255, 255, 0.1);
           border-radius: 12px;
           padding: 8px;
       }
       FlipView::item {
           background-color: transparent;
           border: none;
           margin: 4px;
           border-radius: 8px;
       }
       FlipView::item:hover {
           background-color: rgba(255, 255, 255, 0.1);
       }
       FlipView::item:selected {
           border: 2px solid rgba(0, 120, 212, 0.8);
       }
   """)

自定义滚动按钮样式：

.. code-block:: python

   # 通过FlipView的按钮属性自定义样式
   flip_view.preButton.setStyleSheet("""
       ScrollButton {
           background-color: rgba(255, 255, 255, 0.9);
           border: none;
           border-radius: 6px;
       }
       ScrollButton:hover {
           background-color: rgba(0, 120, 212, 0.8);
       }
   """)
   
   flip_view.nextButton.setStyleSheet("""
       ScrollButton {
           background-color: rgba(255, 255, 255, 0.9);
           border: none;
           border-radius: 6px;
       }
       ScrollButton:hover {
           background-color: rgba(0, 120, 212, 0.8);
       }
   """)

注意事项
--------

1. **图片格式** - 支持常见图片格式：JPG、PNG、BMP、GIF等
2. **内存管理** - 大量图片时注意内存使用，建议使用适当的图片尺寸
3. **懒加载** - 使用字符串路径时支持懒加载，提高初始加载速度
4. **宽高比** - 根据需要选择合适的宽高比模式
5. **性能优化** - 对于大量图片，考虑分页加载或虚拟化技术
6. **动画性能** - 滚动动画持续时间可通过scrollBar.setScrollAnimation()调整
7. **按钮显示** - 导航按钮会根据当前位置和悬浮状态智能显示/隐藏
8. **图片路径** - 使用相对路径时确保路径正确，建议使用绝对路径

相关组件
--------

- :doc:`list_widget` - 列表控件，FlipView的基类
- :doc:`scroll_bar` - 滚动条控件，用于平滑滚动
- :doc:`button` - 按钮控件，ScrollButton的基类
- :doc:`image` - 图片控件，用于图片处理和显示
