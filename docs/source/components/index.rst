组件使用指南
=============

本节详细介绍各个组件的使用方法和最佳实践。

.. toctree::
   :maxdepth: 2
   :caption: 组件指南

   animation
   auto_wrap
   chart_resource
   color
   config
   exception_handler
   font
   icon
   image_utils
   overload
   router
   screen
   smooth_scroll
   style_sheet
   theme_listener
   translator
   echarts_widget
   calendar_picker
   calendar_view
   date_picker
   fast_calendar_view
   picker_base
   time_picker
   circle_color_picker
   color_dialog
   color_palette
   color_picker_button
   dialog
   folder_list_dialog
   mask_dialog_base
   message_box_base
   message_dialog
   screen_color_picker
   expand_layout
   flow_layout
   splitter
   v_box_layout
   acrylic_combo_box
   acrylic_flyout
   acrylic_line_edit
   acrylic_menu
   acrylic_tool_tip
   acrylic_widget
   acrylic_label
   breadcrumb
   navigation_bar
   navigation_interface
   navigation_panel
   navigation_widget
   pivot
   segmented_widget
   top_navigation_bar
   custom_color_setting_card
   expand_setting_card
   folder_list_setting_card
   options_setting_card
   setting_card
   setting_card_group
   vispy
   vispy_drawing
   coordinate_system
   data_models
   drawing_canvas
   drawing_visuals
   drawing_widget
   interaction_manager
   layer_manager
   selection_manager
   drawing_view
   vispy_canvas
   vispy_visuals
   vispy_widget
   button
   widgets_complete
   navigation_complete
   dialog_box_complete
   settings
   material_complete
   charts_complete
   date_time_complete
   layout_complete
   vispy_complete
   multimedia_complete
   table
   window

使用原则
--------

1. **导入组件**: 从 `qfluentwidgets` 导入需要的组件
2. **创建实例**: 像普通 Qt 组件一样创建实例
3. **设置属性**: 使用属性方法或 QSS 设置样式
4. **连接信号**: 使用 Qt 的信号槽机制处理交互
5. **布局管理**: 使用 Qt 布局管理器组织组件

基本示例
--------

.. code-block:: python

   from qfluentwidgets import PushButton, LineEdit, ProgressBar
   from PySide6.QtWidgets import QVBoxLayout, QWidget

   # 创建组件
   button = PushButton('点击我')
   line_edit = LineEdit()
   progress_bar = ProgressBar()

   # 设置属性
   button.setFixedSize(120, 32)
   line_edit.setPlaceholderText('请输入文本')
   progress_bar.setValue(50)

   # 连接信号
   button.clicked.connect(lambda: print('按钮被点击'))

   # 布局
   layout = QVBoxLayout()
   layout.addWidget(button)
   layout.addWidget(line_edit)
   layout.addWidget(progress_bar)

   widget = QWidget()
   widget.setLayout(layout)

主题适配
--------

所有组件都自动适配主题变化：

.. code-block:: python

   from qfluentwidgets import setTheme, Theme

   # 设置主题
   setTheme(Theme.DARK)  # 暗色主题
   setTheme(Theme.LIGHT) # 亮色主题
   setTheme(Theme.AUTO)  # 跟随系统

自定义样式
--------

可以通过 QSS 自定义组件样式：

.. code-block:: python

   # 自定义按钮样式
   button.setStyleSheet("""
       PushButton {
           background-color: #0078d4;
           color: white;
           border: none;
           border-radius: 4px;
       }
       PushButton:hover {
           background-color: #106ebe;
       }
       PushButton:pressed {
           background-color: #005a9e;
       }
   """)

国际化支持
--------

组件支持中文显示：

.. code-block:: python

   from PySide6.QtCore import QLocale

   # 设置中文本地化
   QLocale.setDefault(QLocale.Chinese)

   # 组件会自动使用中文文本
   button = PushButton('确定')
   cancel_button = PushButton('取消')
