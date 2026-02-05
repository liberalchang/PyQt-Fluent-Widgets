Theme Listener 主题监听模块
==============================

Theme Listener 模块提供系统主题变化监听功能，支持自动跟随系统主题切换。
该模块使用darkdetect库检测系统主题变化，并在主题变化时自动更新应用主题。

主要功能
--------

- **系统主题监听** - 监听系统主题变化
- **自动主题切换** - 自动跟随系统主题
- **跨平台支持** - 支持Windows、macOS、Linux
- **防抖处理** - 防止主题频繁切换
- **信号通知** - 主题变化时发送信号

核心组件
--------

SystemThemeListener
~~~~~~~~~~~~~~~~~~~

系统主题监听器，监听系统主题变化并自动切换应用主题。

.. code-block:: python

   from qfluentwidgets.common.theme_listener import SystemThemeListener
   from qfluentwidgets.common.config import qconfig, Theme
   
   # 创建主题监听器
   theme_listener = SystemThemeListener()
   
   # 连接主题变化信号
   theme_listener.systemThemeChanged.connect(on_theme_changed)
   
   # 启动监听
   theme_listener.start()

**主要信号：**
- ``systemThemeChanged`` - 系统主题变化信号

**主要方法：**
- ``run()`` - 运行监听器
- ``_onThemeChanged()`` - 处理主题变化

实际应用
--------

基本主题监听
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.theme_listener import SystemThemeListener
   from qfluentwidgets.common.config import qconfig, Theme, setTheme
   from qfluentwidgets import FluentIcon, InfoBar
   from PySide6.QtWidgets import QApplication, QWidget
   
   class ThemeAwareWidget(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_theme_listener()
           self.setup_ui()
       
       def setup_theme_listener(self):
           """设置主题监听器"""
           self.theme_listener = SystemThemeListener()
           self.theme_listener.systemThemeChanged.connect(self.on_system_theme_changed)
           self.theme_listener.start()
       
       def setup_ui(self):
           """设置UI"""
           self.setWindowTitle("主题感知应用")
           self.resize(400, 300)
       
       def on_system_theme_changed(self):
           """系统主题变化处理"""
           current_theme = qconfig.theme
           theme_name = "暗色" if current_theme == Theme.DARK else "亮色"
           
           # 显示主题变化通知
           InfoBar.success(
               title="主题已切换",
               content=f"系统主题已切换为{theme_name}主题",
               icon=FluentIcon.BRIGHTNESS,
               duration=2000
           )
       
       def closeEvent(self, event):
           """关闭事件"""
           if hasattr(self, 'theme_listener'):
               self.theme_listener.requestInterruption()
               self.theme_listener.wait()
           event.accept()

自动主题切换
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.theme_listener import SystemThemeListener
   from qfluentwidgets.common.config import qconfig, Theme, setTheme
   from qfluentwidgets import SwitchButton, Label, QVBoxLayout, QWidget
   
   class AutoThemeWidget(QWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_theme_listener()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 主题模式开关
           self.auto_theme_switch = SwitchButton()
           self.auto_theme_switch.setChecked(
               qconfig.themeMode == Theme.AUTO
           )
           self.auto_theme_switch.checkedChanged.connect(self.toggle_auto_theme)
           
           # 当前主题显示
           self.theme_label = Label()
           self.update_theme_label()
           
           layout.addWidget(self.auto_theme_switch)
           layout.addWidget(self.theme_label)
           self.setLayout(layout)
       
       def setup_theme_listener(self):
           """设置主题监听器"""
           self.theme_listener = SystemThemeListener()
           self.theme_listener.systemThemeChanged.connect(self.on_system_theme_changed)
           self.theme_listener.start()
       
       def toggle_auto_theme(self, checked):
           """切换自动主题"""
           if checked:
               setTheme(Theme.AUTO, save=True)
               self.theme_listener.start()
           else:
               self.theme_listener.requestInterruption()
               self.theme_listener.wait()
               # 手动设置主题
               setTheme(Theme.LIGHT, save=True)
           
           self.update_theme_label()
       
       def on_system_theme_changed(self):
           """系统主题变化处理"""
           self.update_theme_label()
       
       def update_theme_label(self):
           """更新主题标签"""
           if qconfig.themeMode == Theme.AUTO:
               theme_name = "暗色" if qconfig.theme == Theme.DARK else "亮色"
               self.theme_label.setText(f"当前主题: 自动 ({theme_name})")
           else:
               theme_name = "暗色" if qconfig.theme == Theme.DARK else "亮色"
               self.theme_label.setText(f"当前主题: {theme_name}")
       
       def closeEvent(self, event):
           """关闭事件"""
           if hasattr(self, 'theme_listener'):
               self.theme_listener.requestInterruption()
               self.theme_listener.wait()
           event.accept()

高级用法
--------

自定义主题处理
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.theme_listener import SystemThemeListener
   from qfluentwidgets.common.config import qconfig, Theme
   from PySide6.QtCore import QObject, Signal
   
   class CustomThemeManager(QObject):
       """自定义主题管理器"""
       
       themeChanged = Signal(Theme)
       systemThemeChanged = Signal(Theme)
       
       def __init__(self):
           super().__init__()
           self.setup_listener()
           self.theme_history = []
       
       def setup_listener(self):
           """设置监听器"""
           self.listener = SystemThemeListener()
           self.listener.systemThemeChanged.connect(self.on_system_theme_changed)
           self.listener.start()
       
       def on_system_theme_changed(self):
           """系统主题变化处理"""
           current_theme = qconfig.theme
           
           # 记录主题历史
           self.theme_history.append({
               'theme': current_theme,
               'timestamp': QDateTime.currentDateTime(),
               'source': 'system'
           })
           
           # 发送信号
           self.systemThemeChanged.emit(current_theme)
           self.themeChanged.emit(current_theme)
           
           # 自定义处理逻辑
           self.handle_theme_change(current_theme)
       
       def handle_theme_change(self, theme):
           """处理主题变化"""
           # 可以在这里添加自定义的主题变化处理逻辑
           if theme == Theme.DARK:
               self.apply_dark_theme_adjustments()
           else:
               self.apply_light_theme_adjustments()
       
       def apply_dark_theme_adjustments(self):
           """应用暗色主题调整"""
           # 自定义暗色主题调整
           pass
       
       def apply_light_theme_adjustments(self):
           """应用亮色主题调整"""
           # 自定义亮色主题调整
           pass
       
       def get_theme_history(self):
           """获取主题历史"""
           return self.theme_history
       
       def stop(self):
           """停止监听"""
           self.listener.requestInterruption()
           self.listener.wait()

主题性能优化
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.theme_listener import SystemThemeListener
   from qfluentwidgets.common.config import qconfig, Theme
   from PySide6.QtCore import QTimer
   import time
   
   class OptimizedThemeListener:
       """优化的主题监听器"""
       
       def __init__(self):
           self.listener = SystemThemeListener()
           self.last_change_time = 0
           self.change_threshold = 2000  # 2秒防抖
           self.pending_change = False
           self.setup_listener()
       
       def setup_listener(self):
           """设置监听器"""
           self.listener.systemThemeChanged.connect(self.on_system_theme_changed)
           self.listener.start()
       
       def on_system_theme_changed(self):
           """系统主题变化处理（带防抖）"""
           current_time = time.time() * 1000
           
           # 防抖处理
           if current_time - self.last_change_time < self.change_threshold:
               if not self.pending_change:
                   self.pending_change = True
                   # 延迟处理
                   QTimer.singleShot(self.change_threshold, self.delayed_theme_change)
               return
           
           self.process_theme_change()
           self.last_change_time = current_time
       
       def delayed_theme_change(self):
           """延迟主题变化处理"""
           if self.pending_change:
               self.process_theme_change()
               self.pending_change = False
               self.last_change_time = time.time() * 1000
       
       def process_theme_change(self):
           """处理主题变化"""
           current_theme = qconfig.theme
           
           # 性能优化的主题更新
           self.optimized_theme_update(current_theme)
       
       def optimized_theme_update(self, theme):
           """优化的主题更新"""
           # 批量更新样式
           self.batch_update_styles(theme)
           
           # 延迟加载资源
           self.lazy_load_resources(theme)
       
       def batch_update_styles(self, theme):
           """批量更新样式"""
           # 实现批量样式更新逻辑
           pass
       
       def lazy_load_resources(self, theme):
           """延迟加载资源"""
           # 实现延迟资源加载逻辑
           pass
       
       def stop(self):
           """停止监听"""
           self.listener.requestInterruption()
           self.listener.wait()

跨平台主题检测
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.common.theme_listener import SystemThemeListener
   import sys
   import platform
   
   class CrossPlatformThemeManager:
       """跨平台主题管理器"""
       
       def __init__(self):
           self.platform = platform.system()
           self.setup_platform_listener()
       
       def setup_platform_listener(self):
           """设置平台特定的监听器"""
           if self.platform == "Windows":
               self.setup_windows_listener()
           elif self.platform == "Darwin":  # macOS
               self.setup_macos_listener()
           elif self.platform == "Linux":
               self.setup_linux_listener()
           else:
               print(f"不支持的平台: {self.platform}")
       
       def setup_windows_listener(self):
           """设置Windows监听器"""
           self.listener = SystemThemeListener()
           self.listener.systemThemeChanged.connect(self.on_theme_changed)
           self.listener.start()
       
       def setup_macos_listener(self):
           """设置macOS监听器"""
           self.listener = SystemThemeListener()
           self.listener.systemThemeChanged.connect(self.on_theme_changed)
           self.listener.start()
       
       def setup_linux_listener(self):
           """设置Linux监听器"""
           self.listener = SystemThemeListener()
           self.listener.systemThemeChanged.connect(self.on_theme_changed)
           self.listener.start()
       
       def on_theme_changed(self):
           """主题变化处理"""
           from qfluentwidgets.common.config import qconfig, Theme
           
           current_theme = qconfig.theme
           platform_name = self.get_platform_name()
           
           print(f"{platform_name} 系统主题已切换为: {current_theme.name}")
           
           # 平台特定的处理
           self.platform_specific_handling(current_theme)
       
       def get_platform_name(self):
           """获取平台名称"""
           platform_names = {
               "Windows": "Windows",
               "Darwin": "macOS",
               "Linux": "Linux"
           }
           return platform_names.get(self.platform, "未知")
       
       def platform_specific_handling(self, theme):
           """平台特定处理"""
           if self.platform == "Windows":
               self.windows_theme_handling(theme)
           elif self.platform == "Darwin":
               self.macos_theme_handling(theme)
           elif self.platform == "Linux":
               self.linux_theme_handling(theme)
       
       def windows_theme_handling(self, theme):
           """Windows特定处理"""
           # Windows特定的主题处理逻辑
           pass
       
       def macos_theme_handling(self, theme):
           """macOS特定处理"""
           # macOS特定的主题处理逻辑
           pass
       
       def linux_theme_handling(self, theme):
           """Linux特定处理"""
           # Linux特定的主题处理逻辑
           pass
       
       def stop(self):
           """停止监听"""
           if hasattr(self, 'listener'):
               self.listener.requestInterruption()
               self.listener.wait()

最佳实践
--------

1. **资源管理** - 及时停止监听器避免资源泄漏
2. **防抖处理** - 避免主题频繁切换造成的性能问题
3. **错误处理** - 处理主题检测失败的情况
4. **平台适配** - 针对不同平台进行特殊处理
5. **用户体验** - 提供主题变化的通知和反馈

注意事项
--------

- 依赖darkdetect库，需要正确安装
- 某些Linux发行版可能无法正确检测系统主题
- 监听器运行在独立线程中，需要注意线程安全
- 主题变化时可能需要重新加载资源
- 在应用关闭时需要正确停止监听器

相关模块
--------

- :doc:`common.config` - 配置管理
- :doc:`common.style_sheet` - 样式表管理
- :doc:`common.color` - 颜色管理
