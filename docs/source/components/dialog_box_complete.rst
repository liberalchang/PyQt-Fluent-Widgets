对话框组件 (Dialog Box)
=======================

本节介绍 PySide6-Fluent-Widgets 中的对话框相关组件。

ColorDialog
-----------

颜色选择对话框。

.. code-block:: python

   from qfluentwidgets import ColorDialog
   from PySide6.QtGui import QColor

   # 创建颜色对话框
   dialog = ColorDialog(self)
   dialog.setWindowTitle('选择颜色')
   
   # 设置默认颜色
   dialog.setColor(QColor('#0078d4'))
   
   # 显示对话框
   if dialog.exec():
       color = dialog.selectedColor()
       print(f'选择颜色: {color.name()}')

Dialog
-----

基础对话框组件。

.. code-block:: python

   from qfluentwidgets import Dialog

   # 创建对话框
   dialog = Dialog('标题', '这是对话框内容', self)
   dialog.yesButton.setText('确定')
   dialog.cancelButton.setText('取消')
   
   # 显示对话框
   if dialog.exec():
       print('用户点击确定')

MessageBox
---------

消息框组件。

.. code-block:: python

   from qfluentwidgets import MessageBox

   # 创建消息框
   box = MessageBox(
       '提示',
       '这是一个消息框',
       self
   )
   
   # 显示消息框
   if box.exec():
       print('用户确认')

FolderListDialog
----------------

文件夹列表对话框。

.. code-block:: python

   from qfluentwidgets import FolderListDialog

   # 创建文件夹列表对话框
   dialog = FolderListDialog('选择文件夹', self)
   dialog.setFolderMode()
   
   # 显示对话框
   if dialog.exec():
       folder = dialog.getFolder()
       print(f'选择文件夹: {folder}')

MessageDialog
-------------

消息对话框。

.. code-block:: python

   from qfluentwidgets import MessageDialog

   # 创建消息对话框
   dialog = MessageDialog('消息', '这是消息内容', self)
   
   # 显示对话框
   if dialog.exec():
       print('用户确认消息')

MessageBoxBase
--------------

消息框基类。

.. code-block:: python

   from qfluentwidgets import MessageBoxBase

   # 创建自定义消息框
   class CustomMessageBox(MessageBoxBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           # 添加自定义内容
           self.addContent(QLabel('自定义内容'))

MaskDialogBase
--------------

遮罩对话框基类。

.. code-block:: python

   from qfluentwidgets import MaskDialogBase

   # 创建遮罩对话框
   class CustomMaskDialog(MaskDialogBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           # 添加自定义内容
           self.addContent(QLabel('遮罩对话框内容'))

DropDownColorPalette
-------------------

下拉颜色面板。

.. code-block:: python

   from qfluentwidgets import DropDownColorPalette

   # 创建下拉颜色面板
   palette = DropDownColorPalette()
   palette.addColor('#0078d4')
   palette.addColor('#ff6b6b')
   
   # 连接信号
   palette.colorChanged.connect(lambda color: print(f'选择颜色: {color}'))

ColorPalette
------------

颜色面板。

.. code-block:: python

   from qfluentwidgets import ColorPalette

   # 创建颜色面板
   palette = ColorPalette()
   palette.addColor('#0078d4')
   palette.addColor('#ff6b6b')
   palette.addColor('#4ecdc4')

ColorButton
-----------

颜色按钮。

.. code-block:: python

   from qfluentwidgets import ColorButton

   # 创建颜色按钮
   color_btn = ColorButton()
   color_btn.setColor('#0078d4')
   
   # 连接信号
   color_btn.colorChanged.connect(lambda color: print(f'颜色变化: {color}'))

ColorDialogButton
-----------------

颜色对话框按钮。

.. code-block:: python

   from qfluentwidgets import ColorDialogButton

   # 创建颜色对话框按钮
   dialog_btn = ColorDialogButton()
   dialog_btn.setColor('#0078d4')
   
   # 连接信号
   dialog_btn.colorChanged.connect(lambda color: print(f'对话框选择颜色: {color}'))

CircleColorButton
----------------

圆形颜色按钮。

.. code-block:: python

   from qfluentwidgets import CircleColorButton

   # 创建圆形颜色按钮
   circle_btn = CircleColorButton()
   circle_btn.setColor('#0078d4')
   
   # 连接信号
   circle_btn.colorChanged.connect(lambda color: print(f'圆形按钮颜色: {color}'))

ScreenColorButton
-----------------

屏幕颜色选择按钮。

.. code-block:: python

   from qfluentwidgets import ScreenColorButton

   # 创建屏幕颜色选择按钮
   screen_btn = ScreenColorButton()
   
   # 连接信号
   screen_btn.colorChanged.connect(lambda color: print(f'屏幕选择颜色: {color}'))

CircleColorPicker
-----------------

圆形颜色选择器。

.. code-block:: python

   from qfluentwidgets import CircleColorPicker

   # 创建圆形颜色选择器
   picker = CircleColorPicker()
   picker.addColor('#0078d4')
   picker.addColor('#ff6b6b')
   
   # 连接信号
   picker.colorChanged.connect(lambda color: print(f'圆形选择器颜色: {color}'))

CircleColorItem
---------------

圆形颜色项。

.. code-block:: python

   from qfluentwidgets import CircleColorItem

   # 创建圆形颜色项
   color_item = CircleColorItem('#0078d4')
   color_item.setFixedSize(30, 30)

ScreenColorPicker
-----------------

屏幕颜色选择器。

.. code-block:: python

   from qfluentwidgets import ScreenColorPicker

   # 创建屏幕颜色选择器
   picker = ScreenColorPicker()
   
   # 连接信号
   picker.colorChanged.connect(lambda color: print(f'屏幕选择器颜色: {color}'))

完整示例
--------

下面是一个完整的对话框组件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QPushButton, QLabel, QGroupBox)
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   from qfluentwidgets import *

   class DialogDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('对话框组件示例')
           self.resize(800, 600)
           
           # 创建界面
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           layout.setSpacing(20)
           layout.setContentsMargins(20, 20, 20, 20)
           
           # 添加标题
           title = SubtitleLabel('对话框组件示例')
           layout.addWidget(title)
           
           # 添加各种对话框组件
           self.add_dialog_group(layout)
           self.add_color_dialog_group(layout)
           self.add_color_button_group(layout)

       def add_dialog_group(self, layout):
           """添加对话框组"""
           group = QGroupBox('对话框组件')
           group_layout = QVBoxLayout(group)
           
           # 基础对话框按钮
           dialog_btn = PrimaryPushButton('基础对话框')
           dialog_btn.clicked.connect(self.show_basic_dialog)
           group_layout.addWidget(dialog_btn)
           
           # 消息框按钮
           messagebox_btn = PushButton('消息框')
           messagebox_btn.clicked.connect(self.show_messagebox)
           group_layout.addWidget(messagebox_btn)
           
           # 文件夹对话框按钮
           folder_btn = PushButton('文件夹对话框')
           folder_btn.clicked.connect(self.show_folder_dialog)
           group_layout.addWidget(folder_btn)
           
           # 消息对话框按钮
           message_dialog_btn = PushButton('消息对话框')
           message_dialog_btn.clicked.connect(self.show_message_dialog)
           group_layout.addWidget(message_dialog_btn)
           
           layout.addWidget(group)

       def add_color_dialog_group(self, layout):
           """添加颜色对话框组"""
           group = QGroupBox('颜色对话框')
           group_layout = QVBoxLayout(group)
           
           # 颜色对话框按钮
           color_dialog_btn = PrimaryPushButton('颜色对话框')
           color_dialog_btn.clicked.connect(self.show_color_dialog)
           group_layout.addWidget(color_dialog_btn)
           
           # 下拉颜色面板
           palette_label = QLabel('下拉颜色面板:')
           group_layout.addWidget(palette_label)
           
           self.dropdown_palette = DropDownColorPalette()
           self.dropdown_palette.addColor('#0078d4')
           self.dropdown_palette.addColor('#ff6b6b')
           self.dropdown_palette.addColor('#4ecdc4')
           self.dropdown_palette.addColor('#45b7d1')
           self.dropdown_palette.colorChanged.connect(self.on_palette_color_changed)
           group_layout.addWidget(self.dropdown_palette)
           
           # 颜色面板
           palette_label2 = QLabel('颜色面板:')
           group_layout.addWidget(palette_label2)
           
           self.color_palette = ColorPalette()
           self.color_palette.addColor('#0078d4')
           self.color_palette.addColor('#ff6b6b')
           self.color_palette.addColor('#4ecdc4')
           self.color_palette.addColor('#45b7d1')
           self.color_palette.colorChanged.connect(self.on_color_palette_changed)
           group_layout.addWidget(self.color_palette)
           
           layout.addWidget(group)

       def add_color_button_group(self, layout):
           """添加颜色按钮组"""
           group = QGroupBox('颜色按钮')
           group_layout = QVBoxLayout(group)
           
           # 颜色按钮
           color_btn = ColorButton()
           color_btn.setColor('#0078d4')
           color_btn.colorChanged.connect(self.on_color_button_changed)
           group_layout.addWidget(color_btn)
           
           # 颜色对话框按钮
           color_dialog_btn = ColorDialogButton()
           color_dialog_btn.setColor('#ff6b6b')
           color_dialog_btn.colorChanged.connect(self.on_color_dialog_button_changed)
           group_layout.addWidget(color_dialog_btn)
           
           # 圆形颜色按钮
           circle_btn = CircleColorButton()
           circle_btn.setColor('#4ecdc4')
           circle_btn.colorChanged.connect(self.on_circle_button_changed)
           group_layout.addWidget(circle_btn)
           
           # 屏幕颜色按钮
           screen_btn = ScreenColorButton()
           screen_btn.colorChanged.connect(self.on_screen_button_changed)
           group_layout.addWidget(screen_btn)
           
           # 圆形颜色选择器
           picker_label = QLabel('圆形颜色选择器:')
           group_layout.addWidget(picker_label)
           
           circle_picker = CircleColorPicker()
           circle_picker.addColor('#0078d4')
           circle_picker.addColor('#ff6b6b')
           circle_picker.addColor('#4ecdc4')
           circle_picker.addColor('#45b7d1')
           circle_picker.colorChanged.connect(self.on_circle_picker_changed)
           group_layout.addWidget(circle_picker)
           
           layout.addWidget(group)

       def show_basic_dialog(self):
           """显示基础对话框"""
           dialog = Dialog('基础对话框', '这是一个基础的对话框示例，用于展示基本功能。', self)
           dialog.yesButton.setText('确定')
           dialog.cancelButton.setText('取消')
           
           if dialog.exec():
               InfoBar.success('用户点击确定', parent=self)
           else:
               InfoBar.info('用户点击取消', parent=self)

       def show_messagebox(self):
           """显示消息框"""
           box = MessageBox('消息框', '这是一个消息框示例，用于显示重要信息。', self)
           
           if box.exec():
               InfoBar.success('用户确认消息', parent=self)

       def show_folder_dialog(self):
           """显示文件夹对话框"""
           dialog = FolderListDialog('选择文件夹', self)
           dialog.setFolderMode()
           
           if dialog.exec():
               folder = dialog.getFolder()
               InfoBar.success(f'选择文件夹: {folder}', parent=self)

       def show_message_dialog(self):
           """显示消息对话框"""
           dialog = MessageDialog('消息对话框', '这是一个消息对话框示例，用于显示详细消息。', self)
           
           if dialog.exec():
               InfoBar.success('用户确认消息', parent=self)

       def show_color_dialog(self):
           """显示颜色对话框"""
           dialog = ColorDialog(self)
           dialog.setWindowTitle('选择颜色')
           dialog.setColor(QColor('#0078d4'))
           
           if dialog.exec():
               color = dialog.selectedColor()
               InfoBar.success(f'选择颜色: {color.name()}', parent=self)

       def on_palette_color_changed(self, color):
           """下拉面板颜色变化"""
           InfoBar.info(f'下拉面板选择颜色: {color.name()}', parent=self)

       def on_color_palette_changed(self, color):
           """颜色面板颜色变化"""
           InfoBar.info(f'颜色面板选择: {color.name()}', parent=self)

       def on_color_button_changed(self, color):
           """颜色按钮变化"""
           InfoBar.info(f'颜色按钮: {color.name()}', parent=self)

       def on_color_dialog_button_changed(self, color):
           """颜色对话框按钮变化"""
           InfoBar.info(f'颜色对话框按钮: {color.name()}', parent=self)

       def on_circle_button_changed(self, color):
           """圆形按钮变化"""
           InfoBar.info(f'圆形按钮: {color.name()}', parent=self)

       def on_screen_button_changed(self, color):
           """屏幕按钮变化"""
           InfoBar.info(f'屏幕选择颜色: {color.name()}', parent=self)

       def on_circle_picker_changed(self, color):
           """圆形选择器变化"""
           InfoBar.info(f'圆形选择器: {color.name()}', parent=self)

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = DialogDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **对话框选择**: 
   - Dialog 适合自定义内容对话框
   - MessageBox 适合简单确认操作
   - ColorDialog 专门用于颜色选择
   - FolderListDialog 用于文件夹选择

2. **用户体验**: 
   - 提供清晰的标题和内容
   - 合理设置按钮文本
   - 处理用户取消操作

3. **颜色组件**: 
   - ColorButton 适合内联颜色选择
   - ColorDialogButton 适合打开颜色对话框
   - CircleColorPicker 适合预设颜色选择

4. **样式一致性**: 
   - 保持对话框风格统一
   - 合理设置对话框大小
   - 提供适当的视觉反馈
