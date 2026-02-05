Screen 屏幕管理模块
====================

Screen 模块提供屏幕检测和几何信息获取功能，支持多显示器环境下的屏幕管理。
该模块主要用于获取当前鼠标所在屏幕的信息，确保窗口在正确的显示器上显示。

主要功能
--------

- **屏幕检测** - 获取当前鼠标所在的屏幕
- **几何信息** - 获取屏幕的几何尺寸和可用区域
- **多显示器支持** - 支持多显示器环境
- **可用区域** - 获取排除任务栏后的可用区域
- **回退机制** - 提供默认屏幕信息作为回退

核心函数
--------

getCurrentScreen()
~~~~~~~~~~~~~~~~~

获取当前鼠标所在的屏幕对象。

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreen
   from PySide6.QtGui import QScreen
   
   # 获取当前屏幕
   current_screen = getCurrentScreen()
   
   if current_screen:
       print(f"屏幕名称: {current_screen.name()}")
       print(f"屏幕尺寸: {current_screen.size().width()}x{current_screen.size().height()}")
       print(f"屏幕DPI: {current_screen.logicalDotsPerInch()}")
   else:
       print("未找到屏幕")

**特点：**
- 基于鼠标位置检测当前屏幕
- 支持多显示器环境
- 返回QScreen对象或None

getCurrentScreenGeometry()
~~~~~~~~~~~~~~~~~~~~~~~~~~

获取当前屏幕的几何信息。

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreenGeometry
   from PySide6.QtCore import QRect
   
   # 获取可用几何区域（排除任务栏）
   available_geometry = getCurrentScreenGeometry(avaliable=True)
   print(f"可用区域: {available_geometry.width()}x{available_geometry.height()}")
   print(f"可用位置: ({available_geometry.x()}, {available_geometry.y()})")
   
   # 获取完整几何区域
   full_geometry = getCurrentScreenGeometry(avaliable=False)
   print(f"完整区域: {full_geometry.width()}x{full_geometry.height()}")
   print(f"完整位置: ({full_geometry.x()}, {full_geometry.y()})")

**参数说明：**
- ``avaliable`` - 是否返回可用区域，默认为True
  - True: 返回排除任务栏后的可用区域
  - False: 返回完整的屏幕区域

实际应用
--------

窗口居中显示
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreenGeometry
   from PySide6.QtWidgets import QWidget, QMainWindow
   from PySide6.QtCore import QRect
   
   def center_window(window):
       """将窗口居中显示在当前屏幕"""
       # 获取当前屏幕几何信息
       screen_geometry = getCurrentScreenGeometry()
       
       # 获取窗口尺寸
       window_geometry = window.geometry()
       
       # 计算居中位置
       x = screen_geometry.x() + (screen_geometry.width() - window_geometry.width()) // 2
       y = screen_geometry.y() + (screen_geometry.height() - window_geometry.height()) // 2
       
       # 设置窗口位置
       window.move(x, y)
   
   # 使用示例
   window = QMainWindow()
   window.resize(800, 600)
   center_window(window)
   window.show()

多显示器窗口管理
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreen, getCurrentScreenGeometry
   from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
   from PySide6.QtGui import QScreen
   
   class MultiMonitorWindow(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.update_screen_info()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 显示屏幕信息
           self.screen_label = QLabel()
           self.geometry_label = QLabel()
           
           # 按钮
           refresh_btn = QPushButton("刷新屏幕信息")
           refresh_btn.clicked.connect(self.update_screen_info)
           
           layout.addWidget(self.screen_label)
           layout.addWidget(self.geometry_label)
           layout.addWidget(refresh_btn)
           self.setLayout(layout)
       
       def update_screen_info(self):
           """更新屏幕信息"""
           current_screen = getCurrentScreen()
           screen_geometry = getCurrentScreenGeometry()
           
           if current_screen:
               screen_info = f"当前屏幕: {current_screen.name()}\n"
               screen_info += f"尺寸: {current_screen.size().width()}x{current_screen.size().height()}\n"
               screen_info += f"DPI: {current_screen.logicalDotsPerInch()}"
               self.screen_label.setText(screen_info)
           
           geometry_info = f"可用区域: {screen_geometry.width()}x{screen_geometry.height()}\n"
           geometry_info += f"位置: ({screen_geometry.x()}, {screen_geometry.y()})"
           self.geometry_label.setText(geometry_info)
   
   # 使用
   window = MultiMonitorWindow()
   window.show()

屏幕适配布局
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreenGeometry
   from PySide6.QtWidgets import QWidget, QVBoxLayout
   from PySide6.QtCore import QSize
   
   class AdaptiveLayout(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.adapt_to_screen()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           # 添加控件到布局
           self.setLayout(layout)
       
       def adapt_to_screen(self):
           """根据屏幕尺寸调整布局"""
           screen_geometry = getCurrentScreenGeometry()
           screen_width = screen_geometry.width()
           screen_height = screen_geometry.height()
           
           # 根据屏幕尺寸调整窗口大小
           if screen_width >= 1920:  # 大屏幕
               self.resize(1200, 800)
           elif screen_width >= 1366:  # 中等屏幕
               self.resize(1000, 700)
           else:  # 小屏幕
               self.resize(800, 600)
           
           # 居中显示
           self.center_on_screen()
       
       def center_on_screen(self):
           """在屏幕上居中显示"""
           screen_geometry = getCurrentScreenGeometry()
           x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2
           y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2
           self.move(x, y)
       
       def moveEvent(self, event):
           """窗口移动时更新"""
           super().moveEvent(event)
           # 可以在这里添加屏幕切换逻辑

弹出窗口定位
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreenGeometry
   from PySide6.QtWidgets import QDialog, QPushButton
   from PySide6.QtCore import QPoint, QRect
   
   class PopupDialog(QDialog):
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setup_ui()
           self.position_dialog()
       
       def setup_ui(self):
           self.setWindowTitle("弹出对话框")
           self.resize(400, 300)
       
       def position_dialog(self):
           """定位对话框"""
           if self.parent():
               # 相对于父窗口定位
               parent_geometry = self.parent().geometry()
               x = parent_geometry.x() + (parent_geometry.width() - self.width()) // 2
               y = parent_geometry.y() + (parent_geometry.height() - self.height()) // 2
           else:
               # 在当前屏幕居中
               screen_geometry = getCurrentScreenGeometry()
               x = screen_geometry.x() + (screen_geometry.width() - self.width()) // 2
               y = screen_geometry.y() + (screen_geometry.height() - self.height()) // 2
           
           self.move(x, y)
   
   def show_popup_at_cursor(parent=None):
       """在鼠标位置附近显示弹出窗口"""
       from PySide6.QtGui import QCursor
       
       popup = PopupDialog(parent)
       cursor_pos = QCursor.pos()
       screen_geometry = getCurrentScreenGeometry()
       
       # 计算弹出窗口位置（避免超出屏幕边界）
       x = cursor_pos.x() + 20
       y = cursor_pos.y() + 20
       
       # 确保窗口在屏幕内
       if x + popup.width() > screen_geometry.right():
           x = screen_geometry.right() - popup.width()
       if y + popup.height() > screen_geometry.bottom():
           y = screen_geometry.bottom() - popup.height()
       
       popup.move(x, y)
       popup.show()

高级用法
--------

屏幕变化监听
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreenGeometry
   from PySide6.QtWidgets import QApplication, QWidget
   from PySide6.QtCore import QObject, Signal
   
   class ScreenMonitor(QObject):
       """屏幕变化监听器"""
       
       screenChanged = Signal()
       
       def __init__(self):
           super().__init__()
           self.current_geometry = getCurrentScreenGeometry()
           self.setup_monitoring()
       
       def setup_monitoring(self):
           """设置监听"""
           # 监听屏幕变化
           app = QApplication.instance()
           if app:
               app.primaryScreenChanged.connect(self.on_screen_changed)
               
               # 监听所有屏幕
               for screen in app.screens():
                   screen.geometryChanged.connect(self.on_geometry_changed)
       
       def on_screen_changed(self, screen):
           """屏幕变化处理"""
           self.screenChanged.emit()
           self.current_geometry = getCurrentScreenGeometry()
       
       def on_geometry_changed(self):
           """几何变化处理"""
           new_geometry = getCurrentScreenGeometry()
           if new_geometry != self.current_geometry:
               self.current_geometry = new_geometry
               self.screenChanged.emit()
   
   # 使用屏幕监听器
   monitor = ScreenMonitor()
   
   class AdaptiveWidget(QWidget):
       def __init__(self):
           super().__init__()
           monitor.screenChanged.connect(self.adapt_layout)
       
       def adapt_layout(self):
           """适配布局"""
           screen_geometry = getCurrentScreenGeometry()
           # 根据屏幕变化调整布局
           pass

屏幕信息工具
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreen, getCurrentScreenGeometry
   from PySide6.QtWidgets import QApplication
   
   class ScreenInfo:
       """屏幕信息工具类"""
       
       @staticmethod
       def get_all_screens_info():
           """获取所有屏幕信息"""
           app = QApplication.instance()
           screens_info = []
           
           for i, screen in enumerate(app.screens()):
               info = {
                   'index': i,
                   'name': screen.name(),
                   'geometry': screen.geometry(),
                   'available_geometry': screen.availableGeometry(),
                   'dpi': screen.logicalDotsPerInch(),
                   'size': screen.size(),
                   'is_primary': screen == app.primaryScreen()
               }
               screens_info.append(info)
           
           return screens_info
       
       @staticmethod
       def get_current_screen_info():
           """获取当前屏幕信息"""
           current_screen = getCurrentScreen()
           if not current_screen:
               return None
           
           return {
               'name': current_screen.name(),
               'geometry': current_screen.geometry(),
               'available_geometry': current_screen.availableGeometry(),
               'dpi': current_screen.logicalDotsPerInch(),
               'size': current_screen.size(),
               'is_primary': current_screen == QApplication.primaryScreen()
           }
       
       @staticmethod
       def find_screen_by_name(name):
           """根据名称查找屏幕"""
           app = QApplication.instance()
           for screen in app.screens():
               if screen.name() == name:
                   return screen
           return None
       
       @staticmethod
       def get_screen_scale_factor(screen):
           """获取屏幕缩放因子"""
           if not screen:
               return 1.0
           
           # 基础DPI为96
           base_dpi = 96
           current_dpi = screen.logicalDotsPerInch()
           return current_dpi / base_dpi
   
   # 使用屏幕信息工具
   all_screens = ScreenInfo.get_all_screens_info()
   current_screen = ScreenInfo.get_current_screen_info()
   
   for screen_info in all_screens:
       print(f"屏幕 {screen_info['index']}: {screen_info['name']}")
       print(f"  尺寸: {screen_info['size'].width()}x{screen_info['size'].height()}")
       print(f"  主屏幕: {'是' if screen_info['is_primary'] else '否'}")

分辨率适配
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.screen import getCurrentScreenGeometry
   from PySide6.QtWidgets import QWidget
   from PySide6.QtCore import QSize
   
   class ResolutionAwareWidget(QWidget):
       """分辨率感知控件"""
       
       def __init__(self):
           super().__init__()
           self.base_size = QSize(800, 600)
           self.min_size = QSize(600, 400)
           self.max_size = QSize(1600, 1200)
           self.setup_ui()
           self.adapt_to_resolution()
       
       def setup_ui(self):
           """设置UI"""
           pass
       
       def adapt_to_resolution(self):
           """根据分辨率调整"""
           screen_geometry = getCurrentScreenGeometry()
           screen_width = screen_geometry.width()
           screen_height = screen_geometry.height()
           
           # 计算缩放因子
           scale_factor = min(
               screen_width / 1920,  # 基于1920x1080
               screen_height / 1080
           )
           scale_factor = max(0.5, min(2.0, scale_factor))  # 限制在0.5-2.0之间
           
           # 调整窗口大小
           new_width = int(self.base_size.width() * scale_factor)
           new_height = int(self.base_size.height() * scale_factor)
           
           new_width = max(self.min_size.width(), min(self.max_size.width(), new_width))
           new_height = max(self.min_size.height(), min(self.max_size.height(), new_height))
           
           self.resize(new_width, new_height)
           
           # 可以根据缩放因子调整字体大小等
           self.apply_scale_factor(scale_factor)
       
       def apply_scale_factor(self, scale_factor):
           """应用缩放因子"""
           # 调整字体大小
           base_font_size = 12
           new_font_size = int(base_font_size * scale_factor)
           new_font_size = max(8, min(24, new_font_size))
           
           font = self.font()
           font.setPixelSize(new_font_size)
           self.setFont(font)

最佳实践
--------

1. **多显示器支持** - 考虑多显示器环境下的窗口定位
2. **可用区域** - 使用可用区域而非完整区域避免被任务栏遮挡
3. **动态适配** - 监听屏幕变化并动态调整布局
4. **缩放支持** - 考虑DPI缩放对界面显示的影响
5. **回退机制** - 提供默认值处理异常情况

注意事项
--------

- 屏幕检测基于鼠标位置，可能不准确
- 多显示器环境下需要考虑屏幕边界
- DPI缩放会影响界面元素的显示大小
- 某些系统可能无法正确获取屏幕信息

相关模块
--------

- :doc:`common.config` - 配置管理
- :doc:`components.widgets` - UI组件
- :doc:`components.window` - 窗口管理
