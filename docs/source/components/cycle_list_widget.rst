CycleListWidget 循环列表控件模块
===============================

CycleListWidget 模块提供循环滚动列表控件，支持循环滚动、平滑动画和键盘导航。该模块实现了现代化的循环列表样式，提供流畅的用户体验。

主要功能
--------

- **循环滚动** - 支持无限循环滚动列表项
- **平滑动画** - 提供流畅的滚动动画效果
- **键盘导航** - 支持上下键导航
- **鼠标滚轮** - 支持鼠标滚轮滚动
- **滚动按钮** - 提供上下滚动按钮
- **自动重复** - 支持按钮自动重复功能
- **自适应动画** - 根据操作速度调整动画效果

核心组件
--------

CycleListWidget
~~~~~~~~~~~~~~~

循环列表控件，提供循环滚动的列表功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.cycle_list_widget import CycleListWidget
   from PySide6.QtCore import QSize
   from PySide6.QtCore import Qt
   
   # 创建循环列表
   items = ["选项1", "选项2", "选项3", "选项4", "选项5"]
   item_size = QSize(200, 40)
   
   cycle_list = CycleListWidget(items, item_size, Qt.AlignCenter, parent=parent)
   
   # 设置选中项
   cycle_list.setSelectedItem("选项3")
   
   # 连接信号
   cycle_list.currentItemChanged.connect(self.on_current_item_changed)

**构造函数：**
- ``CycleListWidget(items: Iterable, itemSize: QSize, align=Qt.AlignCenter, parent=None)``

**参数说明：**
- ``items`` - 要添加的项列表
- ``itemSize`` - 每项的尺寸
- ``align`` - 文本对齐方式
- ``parent`` - 父控件

**主要方法：**
- ``setItems(items: list)`` - 设置列表项
- ``setSelectedItem(text: str)`` - 设置选中项
- ``scrollUp()`` - 向上滚动一项
- ``scrollDown()`` - 向下滚动一项
- ``scrollToItem(item, hint)`` - 滚动到指定项
- ``setScrollButtonRepeatEnabled(isEnabled: bool)`` - 设置按钮自动重复
- ``currentItem()`` - 获取当前项
- ``currentIndex()`` - 获取当前索引
- ``setCurrentIndex(index: int)`` - 设置当前索引

**信号：**
- ``currentItemChanged(item)`` - 当前项变化时发出

**特点：**
- 自动检测是否需要循环滚动
- 平滑的滚动动画
- 支持键盘和鼠标操作
- 智能的滚动按钮显示

ScrollButton
~~~~~~~~~~~~

滚动按钮控件，用于列表的上下滚动。

.. code-block:: python

   from qfluentwidgets.components.widgets.cycle_list_widget import ScrollButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建滚动按钮（通常由CycleListWidget自动管理）
   up_button = ScrollButton(FIF.CARE_UP_SOLID, parent=parent)
   down_button = ScrollButton(FIF.CARE_DOWN_SOLID, parent=parent)

**构造函数：**
- ``ScrollButton(icon: FluentIcon, parent=None)``

**特点：**
- 专门为滚动设计的按钮样式
- 支持按下状态视觉反馈
- 适应主题颜色
- 通常不需要直接使用

使用示例
--------

基础循环列表示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
   from PySide6.QtCore import QSize, Qt
   from qfluentwidgets.components.widgets.cycle_list_widget import CycleListWidget
   
   class CycleListDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建数据
           colors = ["红色", "橙色", "黄色", "绿色", "蓝色", "靛色", "紫色"]
           
           # 创建循环列表
           self.cycle_list = CycleListWidget(
               colors, 
               QSize(150, 35), 
               Qt.AlignCenter, 
               self
           )
           
           # 状态显示标签
           self.status_label = QLabel("当前选择: 无", self)
           
           # 连接信号
           self.cycle_list.currentItemChanged.connect(self.on_item_changed)
           
           # 添加到布局
           layout.addWidget(QLabel("颜色选择器："))
           layout.addWidget(self.cycle_list)
           layout.addWidget(self.status_label)
           
       def on_item_changed(self, item):
           if item:
               self.status_label.setText(f"当前选择: {item.text()}")
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       demo = CycleListDemo()
       demo.show()
       sys.exit(app.exec())

音乐播放列表示例：

.. code-block:: python

   from PySide6.QtWidgets import QHBoxLayout
   from qfluentwidgets import FluentIcon as FIF
   
   class MusicPlayer(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 歌曲列表
           songs = [
               "歌曲1 - 艺术家A",
               "歌曲2 - 艺术家B", 
               "歌曲3 - 艺术家C",
               "歌曲4 - 艺术家D",
               "歌曲5 - 艺术家E",
               "歌曲6 - 艺术家F",
               "歌曲7 - 艺术家G",
               "歌曲8 - 艺术家H"
           ]
           
           # 创建循环列表
           self.song_list = CycleListWidget(
               songs,
               QSize(200, 40),
               Qt.AlignLeft,
               self
           )
           
           # 控制按钮
           control_layout = QHBoxLayout()
           
           from qfluentwidgets.components.widgets.button import PushButton
           
           self.play_btn = PushButton(FIF.PLAY, "播放", self)
           self.next_btn = PushButton(FIF.NEXT, "下一首", self)
           self.prev_btn = PushButton(FIF.PREVIOUS, "上一首", self)
           
           # 连接信号
           self.song_list.currentItemChanged.connect(self.on_song_changed)
           self.play_btn.clicked.connect(self.toggle_play)
           self.next_btn.clicked.connect(self.next_song)
           self.prev_btn.clicked.connect(self.prev_song)
           
           control_layout.addWidget(self.prev_btn)
           control_layout.addWidget(self.play_btn)
           control_layout.addWidget(self.next_btn)
           
           # 当前播放信息
           self.now_playing = QLabel("未播放", self)
           
           # 添加到布局
           layout.addWidget(QLabel("播放列表："))
           layout.addWidget(self.song_list)
           layout.addLayout(control_layout)
           layout.addWidget(self.now_playing)
           
           # 设置默认选择
           self.song_list.setSelectedItem("歌曲1 - 艺术家A")
           
       def on_song_changed(self, item):
           if item:
               self.now_playing.setText(f"正在播放: {item.text()}")
               
       def toggle_play(self):
           if self.play_btn.text() == "播放":
               self.play_btn.setText("暂停")
               self.play_btn.setIcon(FIF.PAUSE)
           else:
               self.play_btn.setText("播放")
               self.play_btn.setIcon(FIF.PLAY)
               
       def next_song(self):
           self.song_list.scrollDown()
           
       def prev_song(self):
           self.song_list.scrollUp()

时间选择器示例：

.. code-block:: python

   class TimeSelector(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QHBoxLayout(self)
           
           # 小时选择
           hours = [f"{i:02d}" for i in range(24)]
           self.hour_list = CycleListWidget(
               hours,
               QSize(60, 35),
               Qt.AlignCenter,
               self
           )
           
           # 分钟选择
           minutes = [f"{i:02d}" for i in range(60)]
           self.minute_list = CycleListWidget(
               minutes,
               QSize(60, 35),
               Qt.AlignCenter,
               self
           )
           
           # 秒钟选择
           seconds = [f"{i:02d}" for i in range(60)]
           self.second_list = CycleListWidget(
               seconds,
               QSize(60, 35),
               Qt.AlignCenter,
               self
           )
           
           # 分隔符标签
           colon1 = QLabel(":", self)
           colon2 = QLabel(":", self)
           colon1.setStyleSheet("font-size: 24px; font-weight: bold;")
           colon2.setStyleSheet("font-size: 24px; font-weight: bold;")
           
           # 当前时间显示
           self.time_label = QLabel("00:00:00", self)
           self.time_label.setStyleSheet("font-size: 18px; font-weight: bold;")
           
           # 连接信号
           self.hour_list.currentItemChanged.connect(self.update_time)
           self.minute_list.currentItemChanged.connect(self.update_time)
           self.second_list.currentItemChanged.connect(self.update_time)
           
           # 添加到布局
           layout.addWidget(self.hour_list)
           layout.addWidget(colon1)
           layout.addWidget(self.minute_list)
           layout.addWidget(colon2)
           layout.addWidget(self.second_list)
           layout.addStretch()
           layout.addWidget(self.time_label)
           
           # 设置当前时间
           import datetime
           now = datetime.datetime.now()
           self.hour_list.setSelectedItem(f"{now.hour:02d}")
           self.minute_list.setSelectedItem(f"{now.minute:02d}")
           self.second_list.setSelectedItem(f"{now.second:02d}")
           
       def update_time(self, item=None):
           hour = self.hour_list.currentItem().text() if self.hour_list.currentItem() else "00"
           minute = self.minute_list.currentItem().text() if self.minute_list.currentItem() else "00"
           second = self.second_list.currentItem().text() if self.second_list.currentItem() else "00"
           
           self.time_label.setText(f"{hour}:{minute}:{second}")

自定义样式示例：

.. code-block:: python

   class CustomCycleList(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建自定义样式的循环列表
           items = ["项目 A", "项目 B", "项目 C", "项目 D", "项目 E"]
           
           self.cycle_list = CycleListWidget(
               items,
               QSize(180, 45),
               Qt.AlignLeft,
               self
           )
           
           # 应用自定义样式
           self.cycle_list.setStyleSheet("""
               CycleListWidget {
                   background-color: rgba(255, 255, 255, 0.05);
                   border: 1px solid rgba(255, 255, 255, 0.1);
                   border-radius: 8px;
                   padding: 4px;
               }
               QListWidget::item {
                   background-color: transparent;
                   border: none;
                   padding: 8px 12px;
                   margin: 2px;
                   border-radius: 4px;
                   color: white;
               }
               QListWidget::item:hover {
                   background-color: rgba(255, 255, 255, 0.1);
               }
               QListWidget::item:selected {
                   background-color: rgba(0, 120, 212, 0.3);
                   color: white;
               }
               QToolButton {
                   background-color: rgba(255, 255, 255, 0.1);
                   border: none;
                   border-radius: 4px;
                   width: 100%;
               }
               QToolButton:hover {
                   background-color: rgba(255, 255, 255, 0.2);
               }
               QToolButton:pressed {
                   background-color: rgba(255, 255, 255, 0.3);
               }
           """)
           
           # 设置滚动按钮重复
           self.cycle_list.setScrollButtonRepeatEnabled(True)
           
           layout.addWidget(self.cycle_list)

高级功能示例：

.. code-block:: python

   class AdvancedCycleList(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建大量数据的循环列表
           import random
           import string
           
           # 生成100个随机项目
           items = []
           for i in range(100):
               item_text = f"项目 {i+1} - {''.join(random.choices(string.ascii_letters, k=5))}"
               items.append(item_text)
           
           self.cycle_list = CycleListWidget(
               items,
               QSize(250, 35),
               Qt.AlignLeft,
               self
           )
           
           # 控制面板
           control_layout = QHBoxLayout()
           
           from qfluentwidgets.components.widgets.button import PushButton
           from qfluentwidgets.components.widgets.line_edit import LineEdit
           
           # 搜索框
           self.search_box = LineEdit(self)
           self.search_box.setPlaceholderText("搜索项目...")
           self.search_box.textChanged.connect(self.search_items)
           
           # 控制按钮
           random_btn = PushButton("随机选择", self)
           random_btn.clicked.connect(self.random_select)
           
           first_btn = PushButton("第一个", self)
           first_btn.clicked.connect(lambda: self.cycle_list.setSelectedItem(items[0]))
           
           last_btn = PushButton("最后一个", self)
           last_btn.clicked.connect(lambda: self.cycle_list.setSelectedItem(items[-1]))
           
           control_layout.addWidget(self.search_box)
           control_layout.addWidget(random_btn)
           control_layout.addWidget(first_btn)
           control_layout.addWidget(last_btn)
           
           # 信息显示
           self.info_label = QLabel("项目总数: 100", self)
           
           # 连接信号
           self.cycle_list.currentItemChanged.connect(self.on_item_changed)
           
           layout.addWidget(QLabel("大数据循环列表："))
           layout.addWidget(self.cycle_list)
           layout.addLayout(control_layout)
           layout.addWidget(self.info_label)
           
       def search_items(self, text):
           """搜索并跳转到匹配项"""
           if not text:
               return
               
           # 在原始项目中搜索
           for i, item in enumerate(self.cycle_list.originItems):
               if text.lower() in str(item).lower():
                   self.cycle_list.setSelectedItem(str(item))
                   break
                   
       def random_select(self):
           """随机选择一个项目"""
           import random
           random_item = random.choice(self.cycle_list.originItems)
           self.cycle_list.setSelectedItem(str(random_item))
           
       def on_item_changed(self, item):
           if item:
               index = self.cycle_list.currentIndex()
               total = len(self.cycle_list.originItems)
               self.info_label.setText(f"当前: {item.text()} | 索引: {index} | 总数: {total}")

样式自定义
----------

可以通过样式表自定义循环列表的外观：

.. code-block:: python

   # 自定义循环列表样式
   cycle_list = CycleListWidget(items, QSize(200, 40))
   cycle_list.setStyleSheet("""
       CycleListWidget {
           background-color: rgba(30, 30, 30, 0.8);
           border: 2px solid rgba(0, 120, 212, 0.5);
           border-radius: 10px;
           outline: none;
       }
       QListWidget::item {
           background-color: transparent;
           border: none;
           padding: 10px 15px;
           margin: 1px;
           border-radius: 6px;
           color: #ffffff;
           font-size: 14px;
       }
       QListWidget::item:hover {
           background-color: rgba(0, 120, 212, 0.3);
       }
       QListWidget::item:selected {
           background-color: rgba(0, 120, 212, 0.6);
           color: white;
       }
       QToolButton {
           background: rgba(255, 255, 255, 0.1);
           border: none;
           border-radius: 6px;
           margin: 2px;
       }
       QToolButton:hover {
           background: rgba(255, 255, 255, 0.2);
       }
       QToolButton:pressed {
           background: rgba(255, 255, 255, 0.3);
       }
   """)

自定义滚动动画：

.. code-block:: python

   # 调整滚动动画持续时间
   cycle_list.scrollDuration = 300  # 毫秒

   # 自定义滚动按钮重复设置
   cycle_list.setScrollButtonRepeatEnabled(True)
   cycle_list.upButton.setAutoRepeatDelay(300)   # 首次延迟
   cycle_list.upButton.setAutoRepeatInterval(100) # 重复间隔
   cycle_list.downButton.setAutoRepeatDelay(300)
   cycle_list.downButton.setAutoRepeatInterval(100)

注意事项
--------

1. **循环模式** - 当项目数量超过可见数量时自动启用循环滚动
2. **性能考虑** - 大量项目时建议使用虚拟化或分页加载
3. **项尺寸** - 所有项应使用相同的尺寸以确保正确的滚动效果
4. **动画性能** - 自定义动画持续时间时注意性能影响
5. **键盘导航** - 支持上下键，确保控件有焦点以接收键盘事件
6. **滚动按钮** - 按钮会在鼠标悬浮时显示，离开时隐藏
7. **项选择** - 使用setSelectedItem()方法设置选中项，会自动滚动到中心位置

相关组件
--------

- :doc:`list_widget` - 列表控件，CycleListWidget的基类
- :doc:`scroll_area` - 滚动区域控件
- :doc:`button` - 按钮控件，ScrollButton的基类
