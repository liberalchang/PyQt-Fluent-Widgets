表格组件 (Table Widgets)
=======================

本节介绍 PySide6-Fluent-Widgets 中的表格相关组件。

TableWidget
-----------

基础表格控件，提供现代化的表格显示功能。

.. code-block:: python

   from qfluentwidgets import TableWidget
   from PySide6.QtWidgets import QTableWidgetItem

   # 创建表格
   table = TableWidget()
   
   # 设置列数和行数
   table.setColumnCount(3)
   table.setRowCount(5)
   
   # 设置表头
   table.setHorizontalHeaderLabels(['姓名', '年龄', '职业'])
   
   # 添加数据
   table.setItem(0, 0, QTableWidgetItem('张三'))
   table.setItem(0, 1, QTableWidgetItem('25'))
   table.setItem(0, 2, QTableWidgetItem('工程师'))
   
   # 设置选择模式
   table.setSelectionBehavior(TableWidget.SelectRows)
   table.setSelectionMode(TableWidget.SingleSelection)

SortableTableWidget
-------------------

可排序的表格控件，支持点击表头进行排序。

.. code-block:: python

   from qfluentwidgets import SortableTableWidget
   from PySide6.QtWidgets import QTableWidgetItem

   # 创建可排序表格
   table = SortableTableWidget()
   
   # 设置列数和行数
   table.setColumnCount(4)
   table.setRowCount(10)
   
   # 设置表头
   table.setHorizontalHeaderLabels(['编号', '姓名', '年龄', '部门'])
   
   # 添加数据
   data = [
       (1, '张三', 25, '技术部'),
       (2, '李四', 30, '市场部'),
       (3, '王五', 28, '人事部'),
       (4, '赵六', 35, '财务部'),
   ]
   
   for row, (id, name, age, dept) in enumerate(data):
       table.setItem(row, 0, QTableWidgetItem(str(id)))
       table.setItem(row, 1, QTableWidgetItem(name))
       table.setItem(row, 2, QTableWidgetItem(str(age)))
       table.setItem(row, 3, QTableWidgetItem(dept))
   
   # 连接排序信号
   table.sortRequested.connect(lambda column, order: print(f'排序: 列{column}, 顺序{order}'))

TableView
---------

表格视图控件，使用模型/视图架构。

.. code-block:: python

   from qfluentwidgets import TableView
   from PySide6.QtCore import QAbstractTableModel, Qt

   class TableModel(QAbstractTableModel):
       """表格模型"""
       
       def __init__(self, data):
           super().__init__()
           self._data = data
           self._headers = ['姓名', '年龄', '城市']

       def rowCount(self, parent=None):
           return len(self._data)

       def columnCount(self, parent=None):
           return len(self._headers)

       def data(self, index, role=Qt.DisplayRole):
           if role == Qt.DisplayRole:
               return self._data[index.row()][index.column()]
           return None

       def headerData(self, section, orientation, role=Qt.DisplayRole):
           if orientation == Qt.Horizontal and role == Qt.DisplayRole:
               return self._headers[section]
           return None

   # 创建数据和模型
   data = [
       ['张三', 25, '北京'],
       ['李四', 30, '上海'],
       ['王五', 28, '广州'],
   ]
   
   model = TableModel(data)
   
   # 创建表格视图
   table = TableView()
   table.setModel(model)

SortableTableView
-----------------

可排序的表格视图，支持点击表头排序。

.. code-block:: python

   from qfluentwidgets import SortableTableView
   from PySide6.QtCore import QAbstractTableModel, Qt

   class SortableTableModel(QAbstractTableModel):
       """可排序表格模型"""
       
       def __init__(self, data):
           super().__init__()
           self._data = data
           self._headers = ['姓名', '年龄', '部门', '薪资']
           self._sort_column = -1
           self._sort_order = Qt.AscendingOrder

       def rowCount(self, parent=None):
           return len(self._data)

       def columnCount(self, parent=None):
           return len(self._headers)

       def data(self, index, role=Qt.DisplayRole):
           if role == Qt.DisplayRole:
               return str(self._data[index.row()][index.column()])
           return None

       def headerData(self, section, orientation, role=Qt.DisplayRole):
           if orientation == Qt.Horizontal and role == Qt.DisplayRole:
               return self._headers[section]
           return None

       def sort(self, column, order=Qt.AscendingOrder):
           """排序数据"""
           self.layoutAboutToBeChanged.emit()
           
           self._sort_column = column
           self._sort_order = order
           
           # 排序逻辑
           self._data.sort(key=lambda x: x[column], reverse=(order == Qt.DescendingOrder))
           
           self.layoutChanged.emit()

   # 创建数据和模型
   data = [
       ['张三', 25, '技术部', 15000],
       ['李四', 30, '市场部', 12000],
       ['王五', 28, '人事部', 8000],
       ['赵六', 35, '财务部', 10000],
   ]
   
   model = SortableTableModel(data)
   
   # 创建可排序表格视图
   table = SortableTableView()
   table.setModel(model)
   
   # 连接排序信号
   table.sortRequested.connect(model.sort)

高级功能
--------

自定义委托
~~~~~~~~~~

可以自定义单元格的显示和编辑方式。

.. code-block:: python

   from qfluentwidgets import TableWidget, TableItemDelegate
   from PySide6.QtWidgets import QComboBox

   class CustomDelegate(TableItemDelegate):
       """自定义委托"""
       
       def createEditor(self, parent, option, index):
           # 为特定列创建不同的编辑器
           if index.column() == 2:  # 第三列使用下拉框
               combo = QComboBox(parent)
               combo.addItems(['技术部', '市场部', '人事部', '财务部'])
               return combo
           else:
               return super().createEditor(parent, option, index)

   # 使用自定义委托
   table = TableWidget()
   table.setItemDelegate(CustomDelegate(table))

右键菜单
~~~~~~~~

为表格添加右键菜单功能。

.. code-block:: python

   from PySide6.QtWidgets import QMenu

   class TableWidgetWithMenu(TableWidget):
       """带右键菜单的表格"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           self.setContextMenuPolicy(Qt.CustomContextMenu)
           self.customContextMenuRequested.connect(self.show_context_menu)

       def show_context_menu(self, pos):
           """显示右键菜单"""
           menu = QMenu(self)
           
           # 添加菜单项
           add_action = menu.addAction('添加行')
           delete_action = menu.addAction('删除行')
           menu.addSeparator()
           copy_action = menu.addAction('复制')
           paste_action = menu.addAction('粘贴')
           
           # 获取点击的位置
           item = self.itemAt(pos)
           
           # 连接信号
           add_action.triggered.connect(self.add_row)
           if item:
               delete_action.triggered.connect(lambda: self.delete_row(item.row()))
               copy_action.triggered.connect(lambda: self.copy_row(item.row()))

           # 显示菜单
           menu.exec_(self.mapToGlobal(pos))

       def add_row(self):
           """添加行"""
           row_count = self.rowCount()
           self.setRowCount(row_count + 1)

       def delete_row(self, row):
           """删除行"""
           self.removeRow(row)

       def copy_row(self, row):
           """复制行"""
           # 实现复制逻辑
           pass

搜索和过滤
~~~~~~~~~~

实现表格数据的搜索和过滤功能。

.. code-block:: python

   from PySide6.QtCore import QSortFilterProxyModel

   class FilterableTableView(SortableTableView):
       """可过滤的表格视图"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           
           # 创建代理模型
           self.proxy_model = QSortFilterProxyModel()
           self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
           self.proxy_model.setFilterKeyColumn(-1)  # 搜索所有列
           
           # 设置模型
           self.setModel(self.proxy_model)

       def set_source_model(self, model):
           """设置源模型"""
           self.proxy_model.setSourceModel(model)

       def filter_data(self, text):
           """过滤数据"""
           self.proxy_model.setFilterString(text)

   # 使用示例
   table = FilterableTableView()
   model = SortableTableModel(data)
   table.set_source_model(model)
   
   # 搜索框
   search_box = LineEdit()
   search_box.textChanged.connect(table.filter_data)

样式自定义
--------

可以通过 QSS 自定义表格样式：

.. code-block:: python

   # 自定义表格样式
   table.setStyleSheet("""
       TableWidget {
           background-color: white;
           border: 1px solid #e1e1e1;
           border-radius: 8px;
           gridline-color: #f0f0f0;
       }
       
       TableWidget::item {
           padding: 8px;
           border: none;
       }
       
       TableWidget::item:hover {
           background-color: #f5f5f5;
       }
       
       TableWidget::item:selected {
           background-color: #0078d4;
           color: white;
       }
       
       QHeaderView::section {
           background-color: #f8f9fa;
           padding: 8px;
           border: none;
           border-right: 1px solid #e1e1e1;
           border-bottom: 1px solid #e1e1e1;
           font-weight: bold;
       }
       
       QHeaderView::section:hover {
           background-color: #e9ecef;
       }
   """)

完整示例
--------

下面是一个完整的表格使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                                QHBoxLayout, QPushButton, LineEdit, QLabel)
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class TableDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('表格组件示例')
           self.resize(800, 600)
           
           # 创建主界面
           self.setup_ui()
           
           # 初始化数据
           self.load_data()

       def setup_ui(self):
           """设置主界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 标题
           title = SubtitleLabel('可排序表格示例')
           layout.addWidget(title)
           
           # 搜索框
           search_layout = QHBoxLayout()
           search_label = QLabel('搜索:')
           self.search_box = LineEdit()
           self.search_box.setPlaceholderText('输入关键词搜索...')
           
           search_layout.addWidget(search_label)
           search_layout.addWidget(self.search_box)
           layout.addLayout(search_layout)
           
           # 创建表格
           self.table = SortableTableWidget()
           self.table.setColumnCount(5)
           self.table.setHorizontalHeaderLabels(['编号', '姓名', '年龄', '部门', '薪资'])
           
           # 设置表格属性
           self.table.setSelectionBehavior(TableWidget.SelectRows)
           self.table.setAlternatingRowColors(True)
           self.table.horizontalHeader().setStretchLastSection(True)
           
           layout.addWidget(self.table)
           
           # 操作按钮
           button_layout = QHBoxLayout()
           
           add_btn = PrimaryPushButton('添加行')
           delete_btn = PushButton('删除行')
           clear_btn = PushButton('清空')
           export_btn = PushButton('导出')
           
           button_layout.addWidget(add_btn)
           button_layout.addWidget(delete_btn)
           button_layout.addWidget(clear_btn)
           button_layout.addWidget(export_btn)
           button_layout.addStretch()
           
           layout.addLayout(button_layout)
           
           # 状态标签
           self.status_label = QLabel('就绪')
           layout.addWidget(self.status_label)
           
           # 连接信号
           self.search_box.textChanged.connect(self.filter_table)
           add_btn.clicked.connect(self.add_row)
           delete_btn.clicked.connect(self.delete_selected_row)
           clear_btn.clicked.connect(self.clear_table)
           export_btn.clicked.connect(self.export_data)
           self.table.sortRequested.connect(self.on_sort_requested)

       def load_data(self):
           """加载数据"""
           data = [
               (1, '张三', 25, '技术部', 15000),
               (2, '李四', 30, '市场部', 12000),
               (3, '王五', 28, '人事部', 8000),
               (4, '赵六', 35, '财务部', 10000),
               (5, '钱七', 27, '技术部', 13000),
               (6, '孙八', 32, '市场部', 11000),
               (7, '周九', 29, '人事部', 8500),
               (8, '吴十', 40, '财务部', 12000),
           ]
           
           self.table.setRowCount(len(data))
           
           for row, (id, name, age, dept, salary) in enumerate(data):
               self.table.setItem(row, 0, QTableWidgetItem(str(id)))
               self.table.setItem(row, 1, QTableWidgetItem(name))
               self.table.setItem(row, 2, QTableWidgetItem(str(age)))
               self.table.setItem(row, 3, QTableWidgetItem(dept))
               self.table.setItem(row, 4, QTableWidgetItem(str(salary)))
           
           self.status_label.setText(f'已加载 {len(data)} 条记录')

       def filter_table(self, text):
           """过滤表格"""
           for row in range(self.table.rowCount()):
               match = False
               for col in range(self.table.columnCount()):
                   item = self.table.item(row, col)
                   if item and text.lower() in item.text().lower():
                       match = True
                       break
               
               self.table.setRowHidden(row, not match)

       def add_row(self):
           """添加行"""
           row_count = self.table.rowCount()
           self.table.setRowCount(row_count + 1)
           
           # 添加默认数据
           new_id = row_count + 1
           self.table.setItem(row_count, 0, QTableWidgetItem(str(new_id)))
           self.table.setItem(row_count, 1, QTableWidgetItem('新员工'))
           self.table.setItem(row_count, 2, QTableWidgetItem('25'))
           self.table.setItem(row_count, 3, QTableWidgetItem('待分配'))
           self.table.setItem(row_count, 4, QTableWidgetItem('0'))
           
           self.status_label.setText(f'已添加第 {new_id} 行')

       def delete_selected_row(self):
           """删除选中行"""
           current_row = self.table.currentRow()
           if current_row >= 0:
               self.table.removeRow(current_row)
               self.status_label.setText(f'已删除第 {current_row + 1} 行')
           else:
               InfoBar.warning('请先选择要删除的行', parent=self)

       def clear_table(self):
           """清空表格"""
           self.table.setRowCount(0)
           self.status_label.setText('表格已清空')

       def export_data(self):
           """导出数据"""
           data = []
           headers = []
           
           # 获取表头
           for col in range(self.table.columnCount()):
               headers.append(self.table.horizontalHeaderItem(col).text())
           
           # 获取数据
           for row in range(self.table.rowCount()):
               if not self.table.isRowHidden(row):
                   row_data = []
                   for col in range(self.table.columnCount()):
                       item = self.table.item(row, col)
                       row_data.append(item.text() if item else '')
                   data.append(row_data)
           
           # 这里可以实现导出到文件的功能
           print('导出数据:', headers, data)
           InfoBar.success(f'导出成功，共 {len(data)} 条记录', parent=self)

       def on_sort_requested(self, column, order):
           """排序请求处理"""
           column_name = self.table.horizontalHeaderItem(column).text()
           order_text = '升序' if order == Qt.AscendingOrder else '降序'
           self.status_label.setText(f'按 {column_name} {order_text} 排序')

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = TableDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **选择合适的表格类型**:
   - 使用 TableWidget 处理简单数据
   - 使用 TableView 处理大量数据
   - 使用 SortableTableWidget/SortableTableView 需要排序功能

2. **性能优化**:
   - 大量数据时使用 TableView 而不是 TableWidget
   - 合理设置选择模式和选择行为
   - 使用代理模型进行数据过滤和排序

3. **用户体验**:
   - 提供搜索和过滤功能
   - 支持右键菜单操作
   - 添加状态提示信息
   - 支持键盘快捷键

4. **样式设计**:
   - 使用交替行颜色提高可读性
   - 自定义悬停和选中状态
   - 合理设置列宽和行高
   - 支持主题切换
