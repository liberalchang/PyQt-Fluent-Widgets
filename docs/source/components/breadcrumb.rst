Breadcrumb 面包屑导航模块
=============================

Breadcrumb 模块提供面包屑导航功能，支持层级导航和省略显示。
该模块提供现代化的面包屑导航界面，支持点击导航和自动省略功能。

主要功能
--------

- **层级导航** - 支持多层级路径导航
- **点击导航** - 支持点击面包屑项进行导航
- **自动省略** - 空间不足时自动省略中间项
- **悬停效果** - 提供鼠标悬停的视觉反馈
- **选中状态** - 高亮显示当前所在层级

核心组件
--------

BreadcrumbBar
~~~~~~~~~~~~

面包屑导航栏，提供完整的导航功能。

.. code-block:: python

   from qfluentwidgets.components.navigation.breadcrumb import BreadcrumbBar
   from qfluentwidgets import CardWidget
   
   # 创建面包屑导航栏
   breadcrumb_bar = BreadcrumbBar()
   
   # 添加导航项
   breadcrumb_bar.addItem("home", "首页")
   breadcrumb_bar.addItem("products", "产品")
   breadcrumb_bar.addItem("details", "详情")
   
   # 连接信号
   breadcrumb_bar.currentItemChanged.connect(on_navigation_changed)

**主要信号：**
- ``currentItemChanged`` - 当前项变化信号
- ``currentIndexChanged`` - 当前索引变化信号

**主要方法：**
- ``addItem()`` - 添加导航项
- ``setCurrentItem()`` - 设置当前项
- ``clear()`` - 清空所有项
- ``popItem()`` - 弹出最后一项

BreadcrumbItem
~~~~~~~~~~~~~~

面包屑项，表示单个导航项。

.. code-block:: python

   from qfluentwidgets.components.navigation.breadcrumb import BreadcrumbItem
   
   # 创建面包屑项
   item = BreadcrumbItem(routeKey="home", text="首页", index=0)
   
   # 设置选中状态
   item.setSelected(True)
   
   # 设置文本
   item.setText("新的文本")

实际应用
--------

基本面包屑导航
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.breadcrumb import BreadcrumbBar
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicBreadcrumbWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("面包屑导航示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建面包屑导航栏
           self.breadcrumb_bar = BreadcrumbBar()
           
           # 添加导航项
           self.breadcrumb_bar.addItem("home", "首页")
           self.breadcrumb_bar.addItem("category", "分类")
           self.breadcrumb_bar.addItem("product", "产品")
           self.breadcrumb_bar.addItem("details", "详情")
           
           # 显示当前路径
           self.path_label = Label("当前路径: 首页 > 分类 > 产品 > 详情")
           self.path_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.breadcrumb_bar)
           layout.addWidget(self.path_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.breadcrumb_bar.currentItemChanged.connect(self.on_navigation_changed)
       
       def on_navigation_changed(self, route_key):
           """导航变化处理"""
           # 构建路径显示
           path_items = []
           for i in range(self.breadcrumb_bar.currentIndex() + 1):
               item = self.breadcrumb_bar.itemAt(i)
               if item:
                   path_items.append(item.text)
           
           path_text = " > ".join(path_items)
           self.path_label.setText(f"当前路径: {path_text}")

动态面包屑导航
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.breadcrumb import BreadcrumbBar
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   
   class DynamicBreadcrumbWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态面包屑导航")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_level_btn = PushButton("添加层级")
           self.go_deeper_btn = PushButton("进入子级")
           self.go_up_btn = PushButton("返回上级")
           self.clear_btn = PushButton("清空路径")
           
           button_layout.addWidget(self.add_level_btn)
           button_layout.addWidget(self.go_deeper_btn)
           button_layout.addWidget(self.go_up_btn)
           button_layout.addWidget(self.clear_btn)
           
           # 创建面包屑导航栏
           self.breadcrumb_bar = BreadcrumbBar()
           
           # 显示当前信息
           self.info_label = Label("当前层级: 首页")
           self.info_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.breadcrumb_bar)
           layout.addWidget(self.info_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.add_level_btn.clicked.connect(self.add_level)
           self.go_deeper_btn.clicked.connect(self.go_deeper)
           self.go_up_btn.clicked.connect(self.go_up)
           self.clear_btn.clicked.connect(self.clear_path)
           
           self.breadcrumb_bar.currentItemChanged.connect(self.on_navigation_changed)
       
       def add_level(self):
           """添加层级"""
           import random
           
           levels = [
               ("settings", "设置"),
               ("profile", "个人资料"),
               ("documents", "文档"),
               ("images", "图片"),
               ("downloads", "下载")
           ]
           
           route_key, text = random.choice(levels)
           self.breadcrumb_bar.addItem(route_key, text)
       
       def go_deeper(self):
           """进入子级"""
           current_item = self.breadcrumb_bar.currentItem()
           if current_item:
               # 模拟进入子级
               sub_text = f"{current_item.text}_子级"
               sub_route = f"{current_item.routeKey}_sub"
               self.breadcrumb_bar.addItem(sub_route, sub_text)
       
       def go_up(self):
           """返回上级"""
           self.breadcrumb_bar.popItem()
       
       def clear_path(self):
           """清空路径"""
           self.breadcrumb_bar.clear()
       
       def on_navigation_changed(self, route_key):
           """导航变化处理"""
           current_item = self.breadcrumb_bar.currentItem()
           if current_item:
               self.info_label.setText(f"当前层级: {current_item.text}")
           else:
               self.info_label.setText("当前层级: 无")

高级用法
--------

文件系统导航
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.breadcrumb import BreadcrumbBar
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import QDir
   
   class FileSystemBreadcrumbWidget(CardWidget):
       """文件系统导航"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.current_path = QDir.homePath()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("文件系统导航")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.home_btn = PushButton("主页")
           self.documents_btn = PushButton("文档")
           self.downloads_btn = PushButton("下载")
           self.back_btn = PushButton("后退")
           
           button_layout.addWidget(self.home_btn)
           button_layout.addWidget(self.documents_btn)
           button_layout.addWidget(self.downloads_btn)
           button_layout.addWidget(self.back_btn)
           
           # 创建面包屑导航栏
           self.breadcrumb_bar = BreadcrumbBar()
           
           # 显示当前路径
           self.path_label = Label(f"当前路径: {self.current_path}")
           self.path_label.setStyleSheet("padding: 10px;")
           self.path_label.setWordWrap(True)
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout)
           layout.addWidget(self.breadcrumb_bar)
           layout.addWidget(self.path_label)
           self.setLayout(layout)
           
           # 初始化路径
           self.update_breadcrumb()
       
       def setup_connections(self):
           """设置连接"""
           self.home_btn.clicked.connect(self.go_home)
           self.documents_btn.clicked.connect(self.go_documents)
           self.downloads_btn.clicked.connect(self.go_downloads)
           self.back_btn.clicked.connect(self.go_back)
           
           self.breadcrumb_bar.currentItemChanged.connect(self.on_navigation_changed)
       
       def go_home(self):
           """跳转到主页"""
           self.current_path = QDir.homePath()
           self.update_breadcrumb()
       
       def go_documents(self):
           """跳转到文档目录"""
           self.current_path = QDir.homePath() + "/Documents"
           self.update_breadcrumb()
       
       def go_downloads(self):
           """跳转到下载目录"""
           self.current_path = QDir.homePath() + "/Downloads"
           self.update_breadcrumb()
       
       def go_back(self):
           """后退到上级目录"""
           current_dir = QDir(self.current_path)
           if current_dir.cdUp():
               self.current_path = current_dir.absolutePath()
               self.update_breadcrumb()
       
       def update_breadcrumb(self):
           """更新面包屑导航"""
           # 清空现有项
           self.breadcrumb_bar.clear()
           
           # 解析路径
           path_parts = self.current_path.replace("\\", "/").split("/")
           path_parts = [part for part in path_parts if part]  # 移除空字符串
           
           # 添加根目录
           self.breadcrumb_bar.addItem("root", "/")
           
           # 添加路径层级
           current_path = ""
           for i, part in enumerate(path_parts):
               current_path += "/" + part
               route_key = f"level_{i}"
               self.breadcrumb_bar.addItem(route_key, part)
       
       def on_navigation_changed(self, route_key):
           """导航变化处理"""
           current_item = self.breadcrumb_bar.currentItem()
           if current_item:
               # 重建完整路径
               path_parts = []
               for i in range(self.breadcrumb_bar.currentIndex() + 1):
                   item = self.breadcrumb_bar.itemAt(i)
                   if item and item.routeKey != "root":
                       path_parts.append(item.text)
               
               if path_parts:
                   reconstructed_path = "/" + "/".join(path_parts)
                   self.current_path = reconstructed_path
                   self.path_label.setText(f"当前路径: {self.current_path}")

电商导航
~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.breadcrumb import BreadcrumbBar
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   
   class EcommerceBreadcrumbWidget(CardWidget):
       """电商导航"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("电商导航")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 分类按钮
           category_layout = QHBoxLayout()
           
           self.electronics_btn = PushButton("电子产品")
           self.clothing_btn = PushButton("服装")
           self.books_btn = PushButton("图书")
           self.home_btn = PushButton("家居")
           
           category_layout.addWidget(self.electronics_btn)
           category_layout.addWidget(self.clothing_btn)
           category_layout.addWidget(self.books_btn)
           category_layout.addWidget(self.home_btn)
           
           # 创建面包屑导航栏
           self.breadcrumb_bar = BreadcrumbBar()
           
           # 显示当前分类
           self.category_label = Label("当前分类: 首页")
           self.category_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(category_layout)
           layout.addWidget(self.breadcrumb_bar)
           layout.addWidget(self.category_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.electronics_btn.clicked.connect(self.show_electronics)
           self.clothing_btn.clicked.connect(self.show_clothing)
           self.books_btn.clicked.connect(self.show_books)
           self.home_btn.clicked.connect(self.show_home)
           
           self.breadcrumb_bar.currentItemChanged.connect(self.on_navigation_changed)
       
       def show_electronics(self):
           """显示电子产品分类"""
           self.breadcrumb_bar.clear()
           self.breadcrumb_bar.addItem("home", "首页")
           self.breadcrumb_bar.addItem("electronics", "电子产品")
           self.breadcrumb_bar.setCurrentItem("electronics")
       
       def show_clothing(self):
           """显示服装分类"""
           self.breadcrumb_bar.clear()
           self.breadcrumb_bar.addItem("home", "首页")
           self.breadcrumb_bar.addItem("clothing", "服装")
           self.breadcrumb_bar.setCurrentItem("clothing")
       
       def show_books(self):
           """显示图书分类"""
           self.breadcrumb_bar.clear()
           self.breadcrumb_bar.addItem("home", "首页")
           self.breadcrumb_bar.addItem("books", "图书")
           self.breadcrumb_bar.setCurrentItem("books")
       
       def show_home(self):
           """显示首页"""
           self.breadcrumb_bar.clear()
           self.breadcrumb_bar.addItem("home", "首页")
           self.breadcrumb_bar.setCurrentItem("home")
       
       def on_navigation_changed(self, route_key):
           """导航变化处理"""
           current_item = self.breadcrumb_bar.currentItem()
           if current_item:
               self.category_label.setText(f"当前分类: {current_item.text}")

自定义面包屑样式
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.navigation.breadcrumb import BreadcrumbBar, BreadcrumbItem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QFont
   
   class CustomBreadcrumbItem(BreadcrumbItem):
       """自定义面包屑项"""
       
       def __init__(self, route_key, text, index, parent=None):
           super().__init__(route_key, text, index, parent)
           self.setup_custom_style()
       
       def setup_custom_style(self):
           """设置自定义样式"""
           # 设置字体
           font = QFont()
           font.setFamily("Microsoft YaHei")
           font.setPointSize(12)
           font.setBold(True)
           self.setFont(font)
           
           # 设置间距
           self.setSpacing(8)
   
   class CustomBreadcrumbBar(BreadcrumbBar):
       """自定义面包屑栏"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_custom_style()
       
       def addItem(self, route_key, text):
           """重写添加项方法"""
           if route_key in self.itemMap:
               return
           
           # 使用自定义面包屑项
           item = CustomBreadcrumbItem(route_key, text, len(self.items), self)
           item.clicked.connect(lambda: self.setCurrentItem(route_key))
           
           self.itemMap[route_key] = item
           self.items.append(item)
           item.setFont(self.font())
           item.setSpacing(self.spacing)
           
           self.setFixedHeight(max(i.height() for i in self.items))
           self.setCurrentItem(route_key)
           self.updateGeometry()
   
   class CustomBreadcrumbWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义面包屑导航")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建自定义面包屑导航栏
           self.breadcrumb_bar = CustomBreadcrumbBar()
           
           # 添加导航项
           self.breadcrumb_bar.addItem("home", "🏠 首页")
           self.breadcrumb_bar.addItem("products", "📦 产品")
           self.breadcrumb_bar.addItem("category", "📂 分类")
           self.breadcrumb_bar.addItem("details", "📄 详情")
           
           # 显示当前路径
           self.path_label = Label("当前路径: 🏠 首页 > 📦 产品 > 📂 分类 > 📄 详情")
           self.path_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.breadcrumb_bar)
           layout.addWidget(self.path_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.breadcrumb_bar.currentItemChanged.connect(self.on_navigation_changed)
       
       def on_navigation_changed(self, route_key):
           """导航变化处理"""
           # 构建路径显示
           path_items = []
           for i in range(self.breadcrumb_bar.currentIndex() + 1):
               item = self.breadcrumb_bar.itemAt(i)
               if item:
                   path_items.append(item.text)
           
           path_text = " > ".join(path_items)
           self.path_label.setText(f"当前路径: {path_text}")

最佳实践
--------

1. **层级清晰** - 确保面包屑层级关系清晰明确
2. **路径合理** - 提供合理的导航路径和返回功能
3. **空间管理** - 合理处理空间不足时的省略显示
4. **交互友好** - 提供清晰的点击和悬停反馈
5. **状态同步** - 保持导航状态与实际内容同步

注意事项
--------

- 面包屑项会根据空间自动省略显示
- 点击面包屑项会自动跳转到对应层级
- 省略的项可以通过省略按钮访问
- 需要正确设置routeKey用于导航逻辑
- 大量层级可能影响性能

相关模块
--------

- :doc:`components.navigation.navigation_bar` - 导航栏
- :doc:`components.navigation.navigation_panel` - 导航面板
- :doc:`components.widgets.menu` - 菜单组件
