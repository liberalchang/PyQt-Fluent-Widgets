CheckBox 复选框控件模块
======================

CheckBox 模块提供Fluent Design风格的复选框控件，支持多种状态显示、自定义颜色和主题适配。该模块实现了现代化的复选框样式，提供流畅的交互动画和视觉效果。

主要功能
--------

- **多种状态支持** - 支持普通、悬浮、按下、选中、禁用等多种状态
- **三态复选框** - 支持全选、部分选中、未选中三种状态
- **自定义颜色** - 支持自定义选中状态和文本颜色
- **主题适配** - 自动适配深色/浅色主题
- **流畅动画** - 提供状态切换的平滑过渡效果
- **图标支持** - 内置选中状态的矢量图标

核心组件
--------

CheckBox
~~~~~~~~

Fluent Design风格的复选框控件，提供丰富的交互状态和自定义选项。

.. code-block:: python

   from qfluentwidgets.components.widgets.check_box import CheckBox
   
   # 创建基础复选框
   check_box = CheckBox("启用通知", parent=parent)
   
   # 设置选中状态
   check_box.setChecked(True)
   
   # 连接状态变化信号
   check_box.stateChanged.connect(self.on_check_box_changed)

**构造函数：**
- ``CheckBox(parent: QWidget = None)``
- ``CheckBox(text: str, parent: QWidget = None)``

**主要方法：**
- ``setCheckedColor(light, dark)`` - 设置选中状态的颜色
- ``setTextColor(light, dark)`` - 设置文本颜色
- ``setChecked(checked: bool)`` - 设置选中状态（继承自QCheckBox）
- ``isChecked()`` - 获取选中状态（继承自QCheckBox）
- ``setCheckState(state)`` - 设置三态状态（继承自QCheckBox）
- ``checkState()`` - 获取三态状态（继承自QCheckBox）

**信号：**
- ``stateChanged(state)`` - 状态变化时发出（继承自QCheckBox）
- ``clicked()`` - 点击时发出（继承自QCheckBox）
- ``toggled(checked)`` - 选中状态切换时发出（继承自QCheckBox）

**颜色自定义方法：**

.. code-block:: python

   # 设置选中状态的背景色
   check_box.setCheckedColor("#0078d4", "#4080d6")  # 浅色主题色，深色主题色
   
   # 设置文本颜色
   check_box.setTextColor("#000000", "#ffffff")  # 浅色主题色，深色主题色

**三态复选框使用：**

.. code-block:: python

   # 启用三态模式
   check_box.setTristate(True)
   
   # 设置部分选中状态
   check_box.setCheckState(Qt.PartiallyChecked)

CheckBoxIcon
~~~~~~~~~~~~

复选框图标枚举，定义了不同状态的图标。

.. code-block:: python

   from qfluentwidgets.components.widgets.check_box import CheckBoxIcon
   
   # 图标类型（通常不需要直接使用）
   CheckBoxIcon.ACCEPT        # 全选图标
   CheckBoxIcon.PARTIAL_ACCEPT  # 部分选中图标

**图标类型：**
- ``ACCEPT`` - 全选状态的勾选图标
- ``PARTIAL_ACCEPT`` - 部分选中状态的图标

CheckBoxState
~~~~~~~~~~~~~

复选框状态枚举，定义了所有可能的交互状态。

.. code-block:: python

   from qfluentwidgets.components.widgets.check_box import CheckBoxState
   
   # 状态常量（通常不需要直接使用）
   CheckBoxState.NORMAL           # 普通状态
   CheckBoxState.HOVER           # 悬浮状态
   CheckBoxState.PRESSED         # 按下状态
   CheckBoxState.CHECKED         # 选中状态
   CheckBoxState.CHECKED_HOVER   # 选中悬浮状态
   CheckBoxState.CHECKED_PRESSED # 选中按下状态
   CheckBoxState.DISABLED        # 禁用状态
   CheckBoxState.CHECKED_DISABLED # 选中禁用状态

**状态说明：**
- ``NORMAL`` - 未选中的普通状态
- ``HOVER`` - 鼠标悬浮时的状态
- ``PRESSED`` - 鼠标按下时的状态
- ``CHECKED`` - 已选中的普通状态
- ``CHECKED_HOVER`` - 选中且鼠标悬浮的状态
- ``CHECKED_PRESSED`` - 选中且鼠标按下的状态
- ``DISABLED`` - 禁用状态下的未选中状态
- ``CHECKED_DISABLED`` - 禁用状态下的选中状态

使用示例
--------

基础使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
   from PySide6.QtCore import Qt
   from qfluentwidgets.components.widgets.check_box import CheckBox
   
   class SettingsWindow(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 创建基础复选框
           check1 = CheckBox("启用自动更新", self)
           check1.setChecked(True)
           check1.stateChanged.connect(self.on_auto_update_changed)
           
           # 创建三态复选框
           check2 = CheckBox("选择所有项目", self)
           check2.setTristate(True)
           check2.setCheckState(Qt.PartiallyChecked)
           
           # 自定义颜色的复选框
           check3 = CheckBox("高级模式", self)
           check3.setCheckedColor("#ff6b35", "#ff8c42")  # 橙色主题
           check3.setTextColor("#333333", "#cccccc")
           
           # 禁用状态的复选框
           check4 = CheckBox("已禁用选项", self)
           check4.setEnabled(False)
           
           # 添加到布局
           layout.addWidget(QLabel("系统设置："))
           layout.addWidget(check1)
           layout.addWidget(check2)
           layout.addWidget(check3)
           layout.addWidget(check4)
           
       def on_auto_update_changed(self, state):
           if state == Qt.Checked:
               print("自动更新已启用")
           elif state == Qt.Unchecked:
               print("自动更新已禁用")
           elif state == Qt.PartiallyChecked:
               print("自动更新部分启用")
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       window = SettingsWindow()
       window.show()
       sys.exit(app.exec())

批量操作示例：

.. code-block:: python

   from PySide6.QtWidgets import QHBoxLayout
   from qfluentwidgets.components.widgets.check_box import CheckBox
   
   class BatchSelection(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QVBoxLayout(self)
           
           # 全选复选框
           self.select_all = CheckBox("全选", self)
           self.select_all.stateChanged.connect(self.on_select_all_changed)
           
           # 子项复选框
           self.check_boxes = []
           items = ["选项A", "选项B", "选项C", "选项D"]
           
           for item in items:
               check = CheckBox(item, self)
               check.stateChanged.connect(self.on_item_changed)
               self.check_boxes.append(check)
               layout.addWidget(check)
           
           layout.insertWidget(0, self.select_all)
           
       def on_select_all_changed(self, state):
           """全选状态变化"""
           for check in self.check_boxes:
               check.setChecked(state == Qt.Checked)
               
       def on_item_changed(self):
           """子项状态变化，更新全选状态"""
           checked_count = sum(1 for check in self.check_boxes if check.isChecked())
           total_count = len(self.check_boxes)
           
           if checked_count == 0:
               self.select_all.setCheckState(Qt.Unchecked)
           elif checked_count == total_count:
               self.select_all.setCheckState(Qt.Checked)
           else:
               self.select_all.setCheckState(Qt.PartiallyChecked)

样式自定义
----------

可以通过样式表进一步自定义复选框的外观：

.. code-block:: python

   # 自定义复选框样式
   check_box = CheckBox("自定义样式", self)
   check_box.setStyleSheet("""
       CheckBox {
           font-size: 14px;
           font-weight: 500;
           spacing: 8px;
       }
       CheckBox::indicator {
           width: 18px;
           height: 18px;
           border-radius: 4px;
       }
   """)

主题颜色配置：

.. code-block:: python

   # 配置主题色
   check_box.setCheckedColor(
       QColor(0, 120, 212),   # 浅色主题：蓝色
       QColor(64, 128, 214)    # 深色主题：浅蓝色
   )
   
   check_box.setTextColor(
       QColor(32, 32, 32),     # 浅色主题：深灰色
       QColor(255, 255, 255)   # 深色主题：白色
   )

注意事项
--------

1. **三态模式** - 使用 ``setTristate(True)`` 启用三态模式后，可以通过 ``setCheckState()`` 设置部分选中状态
2. **颜色设置** - ``setCheckedColor()`` 和 ``setTextColor()`` 需要同时提供浅色和深色主题的颜色值
3. **状态监听** - 使用 ``stateChanged`` 信号监听所有状态变化，包括三态变化
4. **性能考虑** - 复选框的状态变化会触发重绘，大量使用时注意性能影响
5. **可访问性** - 确保为复选框设置适当的文本标签，支持屏幕阅读器

相关组件
--------

- :doc:`button` - 按钮控件，常与复选框配合使用
- :doc:`radio_button` - 单选按钮控件，用于互斥选择
- :doc:`toggle_button` - 切换按钮控件，提供类似功能
- :doc:`switch_button` - 开关按钮控件，现代化的开关样式
