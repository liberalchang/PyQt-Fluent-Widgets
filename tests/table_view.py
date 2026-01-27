# coding: utf-8
from typing import List, Union, Optional, Callable
from dataclasses import dataclass
from datetime import datetime
import os

from PySide6.QtCore import Qt, QMargins, QModelIndex, QItemSelectionModel, Property, QRectF, QEvent, Signal
from PySide6.QtGui import QHelpEvent, QPainter, QColor, QKeyEvent, QPalette, QBrush, QIcon, QFont
from PySide6.QtWidgets import (QAbstractItemView, QStyledItemDelegate, QApplication, QStyleOptionViewItem,
                             QTableView, QTableWidget, QWidget, QTableWidgetItem, QStyle,
                             QStyleOptionButton, QStyleFactory, QHeaderView, QHBoxLayout, QLabel)

from .check_box import CheckBoxIcon
from ...common.font import getFont
from ...common.color import autoFallbackThemeColor
from ...common.style_sheet import isDarkTheme, FluentStyleSheet, updateDynamicStyle, setCustomStyleSheet
from .line_edit import LineEdit
from .scroll_bar import SmoothScrollDelegate
from .tool_tip import ItemViewToolTipDelegate, ItemViewToolTipType
from ...common.icon import AntDesignIcon as AIF


class TableItemDelegate(QStyledItemDelegate):

    def __init__(self, parent: QTableView):
        super().__init__(parent)
        self.margin = 2
        self.hoverRow = -1
        self.pressedRow = -1
        self.selectedRows = set()
        self.lightCheckedColor = QColor()
        self.darkCheckedColor = QColor()

        if isinstance(parent, QTableView):
            self.tooltipDelegate = ItemViewToolTipDelegate(parent, 100, ItemViewToolTipType.TABLE)
        else:
            self.tooltipDelegate = ItemViewToolTipDelegate(parent, 100, ItemViewToolTipType.LIST)

    def setHoverRow(self, row: int):
        self.hoverRow = row

    def setPressedRow(self, row: int):
        self.pressedRow = row

    def setSelectedRows(self, indexes: List[QModelIndex]):
        self.selectedRows.clear()
        for index in indexes:
            self.selectedRows.add(index.row())
            if index.row() == self.pressedRow:
                self.pressedRow = -1

    def sizeHint(self, option, index):
        # increase original sizeHint to accommodate space needed for border
        size = super().sizeHint(option, index)
        size = size.grownBy(QMargins(0, self.margin, 0, self.margin))
        return size

    def createEditor(self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex) -> QWidget:
        lineEdit = LineEdit(parent)
        lineEdit.setProperty("transparent", False)
        lineEdit.setStyle(QApplication.style())
        lineEdit.setText(option.text)
        lineEdit.setClearButtonEnabled(True)
        return lineEdit

    def updateEditorGeometry(self, editor: QWidget, option: QStyleOptionViewItem, index: QModelIndex):
        rect = option.rect
        y = rect.y() + (rect.height() - editor.height()) // 2
        x, w = max(8, rect.x()), rect.width()
        if index.column() == 0:
            w -= 8

        editor.setGeometry(x, y, w, rect.height())

    def setCheckedColor(self, light, dark):
        """ set the color of indicator in checked status

        Parameters
        ----------
        light, dark: str | QColor | Qt.GlobalColor
            color in light/dark theme mode
        """
        self.lightCheckedColor = QColor(light)
        self.darkCheckedColor = QColor(dark)
        self.parent().viewport().update()

    def _drawBackground(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        """ draw row background """
        r = 5
        if index.column() == 0:
            rect = option.rect.adjusted(4, 0, r + 1, 0)
            painter.drawRoundedRect(rect, r, r)
        elif index.column() == index.model().columnCount(index.parent()) - 1:
            rect = option.rect.adjusted(-r - 1, 0, -4, 0)
            painter.drawRoundedRect(rect, r, r)
        else:
            rect = option.rect.adjusted(-1, 0, 1, 0)
            painter.drawRect(rect)

    def _drawIndicator(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        """ draw indicator """
        y, h = option.rect.y(), option.rect.height()
        ph = round(0.35*h if self.pressedRow == index.row() else 0.257*h)
        painter.setBrush(autoFallbackThemeColor(self.lightCheckedColor, self.darkCheckedColor))
        painter.drawRoundedRect(4, ph + y, 3, h - 2*ph, 1.5, 1.5)

    def initStyleOption(self, option: QStyleOptionViewItem, index: QModelIndex):
        super().initStyleOption(option, index)

        # font
        option.font = index.data(Qt.FontRole) or getFont(13)

        # text color
        textColor = Qt.white if isDarkTheme() else Qt.black
        textBrush = index.data(Qt.ForegroundRole)   # type: QBrush
        if textBrush is not None:
            textColor = QBrush(textBrush).color()

        option.palette.setColor(QPalette.Text, textColor)
        option.palette.setColor(QPalette.HighlightedText, textColor)

    def paint(self, painter, option, index):
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)

        # set clipping rect of painter to avoid painting outside the borders
        painter.setClipping(True)
        painter.setClipRect(option.rect)

        # call original paint method where option.rect is adjusted to account for border
        option.rect.adjust(0, self.margin, 0, -self.margin)

        # draw highlight background
        isHover = self.hoverRow == index.row()
        isPressed = self.pressedRow == index.row()
        isAlternate = index.row() % 2 == 0 and self.parent().alternatingRowColors()
        isDark = isDarkTheme()

        c = 255 if isDark else 0
        alpha = 0

        if index.row() not in self.selectedRows:
            if isPressed:
                alpha = 9 if isDark else 6
            elif isHover:
                alpha = 12
            elif isAlternate:
                alpha = 5
        else:
            if isPressed:
                alpha = 15 if isDark else 9
            elif isHover:
                alpha = 25
            else:
                alpha = 17

        if index.data(Qt.ItemDataRole.BackgroundRole):
            painter.setBrush(index.data(Qt.ItemDataRole.BackgroundRole))
        else:
            painter.setBrush(QColor(c, c, c, alpha))

        self._drawBackground(painter, option, index)

        # draw indicator
        if index.row() in self.selectedRows and index.column() == 0 and self.parent().horizontalScrollBar().value() == 0:
            self._drawIndicator(painter, option, index)

        if index.data(Qt.CheckStateRole) is not None:
            self._drawCheckBox(painter, option, index)

        painter.restore()
        super().paint(painter, option, index)

    def _drawCheckBox(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        painter.save()
        checkState = Qt.CheckState(index.data(Qt.ItemDataRole.CheckStateRole))

        isDark = isDarkTheme()

        r = 4.5
        x = option.rect.x() + 15
        y = option.rect.center().y() - 9.5
        rect = QRectF(x, y, 19, 19)

        if checkState == Qt.CheckState.Unchecked:
            painter.setBrush(QColor(0, 0, 0, 26) if isDark else QColor(0, 0, 0, 6))
            painter.setPen(QColor(255, 255, 255, 142) if isDark else QColor(0, 0, 0, 122))
            painter.drawRoundedRect(rect, r, r)
        else:
            color = autoFallbackThemeColor(self.lightCheckedColor, self.darkCheckedColor)
            painter.setPen(color)
            painter.setBrush(color)
            painter.drawRoundedRect(rect, r, r)

            if checkState == Qt.CheckState.Checked:
                CheckBoxIcon.ACCEPT.render(painter, rect)
            else:
                CheckBoxIcon.PARTIAL_ACCEPT.render(painter, rect)

        painter.restore()

    def helpEvent(self, event: QHelpEvent, view: QAbstractItemView, option: QStyleOptionViewItem, index: QModelIndex) -> bool:
        return self.tooltipDelegate.helpEvent(event, view, option, index)



class TableBase:
    """ Table base class """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delegate = TableItemDelegate(self)
        self.scrollDelagate = SmoothScrollDelegate(self)
        self._isSelectRightClickedRow = False

        # set style sheet
        FluentStyleSheet.TABLE_VIEW.apply(self)

        self.setShowGrid(False)
        self.setMouseTracking(True)
        self.setAlternatingRowColors(True)
        self.setItemDelegate(self.delegate)
        self.setSelectionBehavior(TableWidget.SelectRows)
        self.horizontalHeader().setHighlightSections(False)
        self.verticalHeader().setHighlightSections(False)
        self.verticalHeader().setDefaultSectionSize(38)

        self.entered.connect(lambda i: self._setHoverRow(i.row()))
        self.pressed.connect(lambda i: self._setPressedRow(i.row()))
        self.verticalHeader().sectionClicked.connect(self.selectRow)

    def setBorderVisible(self, isVisible: bool):
        """ set the visibility of border """
        self.setProperty("isBorderVisible", isVisible)
        updateDynamicStyle(self)

    def setBorderRadius(self, radius: int):
        """ set the radius of border """
        qss = f"QTableView{{border-radius: {radius}px}}"
        setCustomStyleSheet(self, qss, qss)

    def setCheckedColor(self, light, dark):
        """ set the color in checked status

        Parameters
        ----------
        light, dark: str | QColor | Qt.GlobalColor
            color in light/dark theme mode
        """
        self.delegate.setCheckedColor(light, dark)

    def _setHoverRow(self, row: int):
        """ set hovered row """
        self.delegate.setHoverRow(row)
        self.viewport().update()

    def _setPressedRow(self, row: int):
        """ set pressed row """
        if self.selectionMode() == QTableView.SelectionMode.NoSelection:
            return

        self.delegate.setPressedRow(row)
        self.viewport().update()

    def _setSelectedRows(self, indexes: List[QModelIndex]):
        if self.selectionMode() == QTableView.SelectionMode.NoSelection:
            return

        self.delegate.setSelectedRows(indexes)
        self.viewport().update()

    def leaveEvent(self, e):
        QTableView.leaveEvent(self, e)
        self._setHoverRow(-1)

    def resizeEvent(self, e):
        QTableView.resizeEvent(self, e)
        self.viewport().update()

    def keyPressEvent(self, e: QKeyEvent):
        QTableView.keyPressEvent(self, e)
        self.updateSelectedRows()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton or self._isSelectRightClickedRow:
            return QTableView.mousePressEvent(self, e)

        index = self.indexAt(e.pos())
        if index.isValid():
            self._setPressedRow(index.row())

        QWidget.mousePressEvent(self, e)

    def mouseReleaseEvent(self, e):
        QTableView.mouseReleaseEvent(self, e)
        self.updateSelectedRows()

        if self.indexAt(e.pos()).row() < 0 or e.button() == Qt.RightButton:
            self._setPressedRow(-1)

    def setItemDelegate(self, delegate: TableItemDelegate):
        self.delegate = delegate
        super().setItemDelegate(delegate)

    def selectAll(self):
        QTableView.selectAll(self)
        self.updateSelectedRows()

    def selectRow(self, row: int):
        QTableView.selectRow(self, row)
        self.updateSelectedRows()

    def clearSelection(self):
        QTableView.clearSelection(self)
        self.updateSelectedRows()

    def setCurrentIndex(self, index: QModelIndex):
        QTableView.setCurrentIndex(self, index)
        self.updateSelectedRows()

    def updateSelectedRows(self):
        self._setSelectedRows(self.selectedIndexes())


class TableWidget(TableBase, QTableWidget):
    """ Table widget """

    def __init__(self, parent=None):
        super().__init__(parent)
        updateDynamicStyle(self)

    def setCurrentCell(self, row: int, column: int, command=None):
        self.setCurrentItem(self.item(row, column), command)

    def setCurrentItem(self, item: QTableWidgetItem, command=None):
        if not command:
            super().setCurrentItem(item)
        else:
            super().setCurrentItem(item, command)

        self.updateSelectedRows()

    def isSelectRightClickedRow(self):
        return self._isSelectRightClickedRow

    def setSelectRightClickedRow(self, isSelect: bool):
        self._isSelectRightClickedRow = isSelect

    selectRightClickedRow = Property(bool, isSelectRightClickedRow, setSelectRightClickedRow)


class SortableHeaderView(QHeaderView):
    """ 支持排序的表头视图 """
    
    sortRequested = Signal(int, object)  # 列索引，排序顺序（可能为None）
    
    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super().__init__(orientation, parent)
        self._sort_column = -1
        self._sort_order = Qt.AscendingOrder
        self.setSectionsClickable(True)
        self.sectionClicked.connect(self._on_section_clicked)
        
        # 启用排序指示器
        self.setSortIndicatorShown(True)
        
        # 设置对象名称以便QSS样式应用
        self.setObjectName("SortableHeaderView")
        
        # 强制应用样式
        self.setStyleSheet("""
            SortableHeaderView::section {
                background-color: rgba(240, 240, 240, 0.8);
                color: rgb(51, 51, 51);
                padding-left: 12px;
                padding-right: 12px;
                padding-top: 6px;
                padding-bottom: 6px;
                border: 1px solid rgba(0, 0, 0, 15);
                font: bold 13px --FontFamilies;
            }
            SortableHeaderView::section:hover {
                background-color: rgba(232, 232, 232, 0.9);
            }
            SortableHeaderView::section:pressed {
                background-color: rgba(216, 216, 216, 0.9);
            }
        """)
        
    def _on_section_clicked(self, logical_index: int):
        """ 表头点击事件 """
        print(f"[DEBUG] 表头点击: 列 {logical_index}")
        
        if logical_index == self._sort_column:
            # 同一列，循环切换排序顺序：降序 -> 升序 -> 无排序
            if self._sort_order == Qt.DescendingOrder:
                new_order = Qt.AscendingOrder
                print(f"[DEBUG] 切换到升序: {new_order}")
            elif self._sort_order == Qt.AscendingOrder:
                new_order = None  # 无排序状态
                print(f"[DEBUG] 切换到无排序: {new_order}")
            else:
                new_order = Qt.DescendingOrder
                print(f"[DEBUG] 切换到降序: {new_order}")
        else:
            # 不同列，默认降序
            new_order = Qt.DescendingOrder
            print(f"[DEBUG] 新列排序: {new_order}")
            
        self.sortRequested.emit(logical_index, new_order)
        
    def paintSection(self, painter, rect, logical_index):
        """ 自定义绘制表头，显示排序图标 """
        super().paintSection(painter, rect, logical_index)
        
        # 如果是当前排序列，绘制排序图标
        if logical_index == self._sort_column and self._sort_column >= 0:
            # 选择图标
            if self._sort_column == -1:
                # 无排序状态
                icon = AIF.MINUS.icon()
            elif self._sort_order == Qt.AscendingOrder:
                icon = AIF.UP.icon()
            elif self._sort_order == Qt.DescendingOrder:
                icon = AIF.DOWN.icon()
            else:
                icon = AIF.MINUS.icon()
            
            # 计算图标位置（右侧）
            icon_size = 16
            margin = 8
            icon_rect = rect.adjusted(
                rect.width() - icon_size - margin, 
                (rect.height() - icon_size) // 2,
                -margin, 
                -(rect.height() - icon_size) // 2
            )
            
            # 绘制图标
            painter.save()
            icon.paint(painter, icon_rect)
            painter.restore()
            
            print(f"[DEBUG] 绘制排序图标: 列 {logical_index}, 顺序 {self._sort_order}")
        
    def setSortIndicator(self, column: int, order):
        """ 设置排序指示器 """
        print(f"[DEBUG] 设置排序指示器: 列 {column}, 顺序 {order}")
        self._sort_column = column
        self._sort_order = order if order is not None else Qt.AscendingOrder
        super().setSortIndicator(column, order if order is not None else Qt.AscendingOrder)
        self.viewport().update()  # 重绘表头
        
    def getSortColumn(self) -> int:
        """ 获取当前排序列 """
        return self._sort_column
        
    def getSortOrder(self) -> Qt.SortOrder:
        """ 获取当前排序顺序 """
        return self._sort_order


class SortableTableMixin:
    """ 可排序表格混入类 """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sort_column = -1
        self._sort_order = Qt.AscendingOrder
        self._sort_key_functions = {}  # 自定义排序键函数
        self._original_data = None  # 保存原始数据
        
        # 排序缓存系统 - 优化版本
        self._sort_cache = {}  # {column: {'unsorted': [], 'ascending': [], 'descending': []}}
        self._data_version = 0  # 数据版本号，用于检测数据变化
        self._cache_version = {}  # 缓存版本号 {column: version}
        
        self._setup_sortable_header()
        
    def _setup_sortable_header(self):
        """ 设置可排序表头 """
        if hasattr(self, 'horizontalHeader'):
            header = SortableHeaderView(Qt.Horizontal, self)
            header.sortRequested.connect(self._handle_sort_request)
            self.setHorizontalHeader(header)
            
    def _handle_sort_request(self, column: int, order):
        """ 处理排序请求 """
        print(f"[DEBUG] 处理排序请求: 列 {column}, 顺序 {order}")
        
        if order is None:
            # 无排序状态，恢复原始顺序
            print("[DEBUG] 恢复原始顺序")
            self._restore_original_order()
        else:
            self._sort_column = column
            self._sort_order = order
            self._sort_data()
        
    def setSortKeyFunction(self, column: int, key_func: Callable):
        """ 设置列的自定义排序键函数 """
        self._sort_key_functions[column] = key_func
        
    def _get_sort_key(self, row_data: dict, column: int):
        """ 获取排序键 """
        # 如果有自定义排序函数，使用自定义函数
        if column in self._sort_key_functions:
            sort_func = self._sort_key_functions[column]
            # 检查是否是get_file_sort_key函数，如果是，需要传递column参数
            if sort_func.__name__ == 'get_file_sort_key':
                return sort_func(row_data, column)
            else:
                return sort_func(row_data)
            
        # 默认排序逻辑
        value = row_data.get(column, "")
        
        # 文件类型排序
        if column == 0:  # 名称列，同时考虑文件类型
            name = str(value)
            is_dir = row_data.get('_is_dir', False)
            dir_priority = 0 if is_dir else 1
            return (dir_priority, name.lower())
            
        # 大小排序
        elif column == 1:  # 大小列
            if isinstance(value, (int, float)):
                return value
            # 尝试从字符串解析大小
            size_str = str(value).upper()
            if 'B' in size_str:
                try:
                    if 'KB' in size_str:
                        return float(size_str.replace('KB', '').strip()) * 1024
                    elif 'MB' in size_str:
                        return float(size_str.replace('MB', '').strip()) * 1024 * 1024
                    elif 'GB' in size_str:
                        return float(size_str.replace('GB', '').strip()) * 1024 * 1024 * 1024
                    else:
                        return float(size_str.replace('B', '').strip())
                except ValueError:
                    return 0
            return 0
            
        # 日期排序
        elif column == 2:  # 日期列
            if isinstance(value, datetime):
                return value
            # 尝试解析日期字符串
            date_str = str(value)
            try:
                # 常见日期格式
                for fmt in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d']:
                    try:
                        return datetime.strptime(date_str, fmt)
                    except ValueError:
                        continue
            except ValueError:
                pass
            return datetime.min
            
        # 其他列按字符串排序
        return str(value).lower()
        
    def _sort_data(self):
        """ 排序数据 - 子类需要实现 """
        raise NotImplementedError("子类必须实现 _sort_data 方法")
        
    def getSortColumn(self) -> int:
        """ 获取当前排序列 """
        return self._sort_column
        
    def getSortOrder(self) -> Qt.SortOrder:
        """ 获取当前排序顺序 """
        return self._sort_order


class SortableTableWidget(SortableTableMixin, TableWidget):
    """ 可排序的表格控件 """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._row_data = {}  # 存储每行的原始数据
        
    def setRowCount(self, rows: int):
        """ 设置行数 """
        super().setRowCount(rows)
        # 更新行数据字典
        current_rows = self._row_data.copy()
        self._row_data = {}
        for row in range(rows):
            if row in current_rows:
                self._row_data[row] = current_rows[row]
            else:
                self._row_data[row] = {}
                
    def setItem(self, row: int, column: int, item: QTableWidgetItem):
        """ 设置表格项 """
        super().setItem(row, column, item)
        # 更新行数据
        if row not in self._row_data:
            self._row_data[row] = {}
        self._row_data[row][column] = item.text()
        
        # 存储额外的排序信息
        if column == 0:  # 名称列
            # 检查是否为目录（这里简化处理，实际可能需要更复杂的逻辑）
            name = item.text()
            is_dir = name.endswith('/') or '.' not in name
            self._row_data[row]['_is_dir'] = is_dir
            
        # 只有在非排序重排时才增加版本号和清除缓存
        if not hasattr(self, '_is_rearranging') or not self._is_rearranging:
            self._data_version += 1
            # 只有数据变化（增加/删除）才清除缓存，排序不清除缓存
            self._invalidate_data_cache()
        
        # 自动保存原始数据（如果还没有保存）
        if self._original_data is None and self._is_table_fully_populated():
            self._save_original_data()
    
    def _is_table_fully_populated(self):
        """ 检查表格是否已完全填充 """
        # 简单检查：如果有数据且行数大于0，认为表格已填充
        if self.rowCount() == 0:
            return False
        
        # 检查至少第一行有数据
        for col in range(self.columnCount()):
            if self.item(0, col):
                return True
        
        return False
    
    def _invalidate_data_cache(self):
        """ 清除数据缓存（数据变化时） """
        self._sort_cache.clear()
        self._cache_version.clear()
    
    def _invalidate_sort_cache(self):
        """ 清除排序缓存（可选，一般不调用） """
        self._sort_cache.clear()
        self._cache_version.clear()
    
    def _get_cached_sort_order(self, column: int):
        """ 获取缓存的排序结果 - 基于原始数据的下标映射 """
        if column not in self._sort_cache:
            return None
        
        # 检查原始数据是否存在
        if self._original_data is None:
            return None
        
        return self._sort_cache[column]
    
    def _cache_sort_order(self, column: int, unsorted_order: list, ascending_order: list, descending_order: list):
        """ 缓存排序结果 - 基于原始数据的下标映射 """
        # 只有在原始数据状态下才缓存
        if self._original_data is None:
            return
        
        self._sort_cache[column] = {
            'unsorted': unsorted_order,      # 原始顺序下标
            'ascending': ascending_order,    # 升序顺序下标  
            'descending': descending_order   # 降序顺序下标
        }
        self._cache_version[column] = self._data_version
    
    def _compute_sort_orders(self, column: int):
        """ 计算并缓存所有排序顺序 - 基于原始数据的下标映射 """
        print(f"[DEBUG] 计算列 {column} 的排序顺序")
        
        # 基于原始数据计算排序
        if self._original_data is None:
            print("[DEBUG] 原始数据不存在，无法计算排序")
            return [], [], []
        
        # 获取原始数据的排序键
        sort_keys = []
        for row_idx, row_data in self._original_data.items():
            sort_key = self._get_sort_key(row_data, column)
            sort_keys.append((row_idx, sort_key))
            print(f"[DEBUG] 原始数据行 {row_idx}: 排序键={sort_key}, 值={row_data.get(column, '')}")
        
        # 按排序键排序（升序）
        sorted_ascending = sorted(sort_keys, key=lambda x: x[1])
        ascending_order = [item[0] for item in sorted_ascending]
        
        # 降序就是升序的反转
        descending_order = ascending_order[::-1]
        
        # 未排序顺序就是原始顺序
        unsorted_order = list(self._original_data.keys())
        unsorted_order.sort()  # 确保顺序一致
        
        print(f"[DEBUG] 基于原始数据计算结果:")
        print(f"  原始顺序: {unsorted_order}")
        print(f"  升序顺序: {ascending_order}")
        print(f"  降序顺序: {descending_order}")
        
        # 缓存结果 - 基于原始数据的下标映射
        self._cache_sort_order(column, unsorted_order, ascending_order, descending_order)
        
        return unsorted_order, ascending_order, descending_order
    
    def _save_original_data(self):
        print("[DEBUG] 保存原始数据")
        self._original_data = {}
        for row in range(self.rowCount()):
            if self.item(row, 0):  # 只保存有数据的行
                self._original_data[row] = {}
                for col in range(self.columnCount()):
                    if self.item(row, col):
                        self._original_data[row][col] = self.item(row, col).text()
                # 复制其他属性
                if row in self._row_data:
                    for key, value in self._row_data[row].items():
                        if not isinstance(key, int):  # 跳过列数据
                            self._original_data[row][key] = value
        print(f"[DEBUG] 保存的原始数据: {self._original_data}")
    
    def saveOriginalData(self):
        """ 手动保存原始数据 """
        self._save_original_data()
                            
    def _restore_original_order(self):
        """ 恢复原始顺序 """
        print("[DEBUG] 开始恢复原始顺序")
        
        if self._original_data is None:
            print("[DEBUG] 没有原始数据可恢复")
            return
            
        # 重置排序状态
        self._sort_column = -1
        self._sort_order = Qt.AscendingOrder
        
        # 清空表格
        self.clearContents()
        self.setRowCount(len(self._original_data))
        
        # 按原始顺序恢复数据
        new_row_data = {}
        for row, data in self._original_data.items():
            for col, text in data.items():
                if isinstance(col, int):  # 只处理列数据
                    item = QTableWidgetItem(text)
                    # 直接设置项目，不调用setItem避免递归
                    super().setItem(row, col, item)
                    
            # 复制行数据
            new_row_data[row] = data.copy()
            
        self._row_data = new_row_data
        
        print("[DEBUG] 原始顺序恢复完成")
        print(f"[DEBUG] 恢复后的数据:")
        for row in range(self.rowCount()):
            if self.item(row, 0):
                name = self.item(row, 0).text()
                size = self.item(row, 1).text() if self.item(row, 1) else "N/A"
                print(f"  行 {row}: {name} - {size}")
        
        # 更新表头排序指示器
        if hasattr(self, 'horizontalHeader'):
            header = self.horizontalHeader()
            if isinstance(header, SortableHeaderView):
                header.setSortIndicator(-1, Qt.AscendingOrder)
            
    def _sort_data(self):
        """ 高性能排序表格数据 """
        print(f"[DEBUG] 开始排序数据: 列 {self._sort_column}, 顺序 {self._sort_order}")
        
        if self._sort_column < 0:
            print("[DEBUG] 排序列无效，退出排序")
            return
        
        # 尝试从缓存获取排序结果
        cached_order = self._get_cached_sort_order(self._sort_column)
        
        if cached_order:
            print(f"[DEBUG] 使用缓存排序结果，列 {self._sort_column}")
            unsorted_order = cached_order['unsorted']
            ascending_order = cached_order['ascending']
            descending_order = cached_order['descending']
        else:
            print(f"[DEBUG] 计算新的排序结果，列 {self._sort_column}")
            unsorted_order, ascending_order, descending_order = self._compute_sort_orders(self._sort_column)
        
        # 根据排序顺序选择对应的行顺序
        if self._sort_order == Qt.AscendingOrder:
            sorted_rows = ascending_order
        elif self._sort_order == Qt.DescendingOrder:
            sorted_rows = descending_order
        else:
            sorted_rows = unsorted_order
        
        print(f"[DEBUG] 选择的排序顺序: {sorted_rows}")
        
        # 高效数据重排
        self._rearrange_data_fast(sorted_rows)
        
        # 更新表头排序指示器
        if hasattr(self, 'horizontalHeader'):
            header = self.horizontalHeader()
            if isinstance(header, SortableHeaderView):
                header.setSortIndicator(self._sort_column, self._sort_order)
                
        print("[DEBUG] 排序完成")
    
    def _rearrange_data_fast(self, sorted_rows: list):
        """ 高效数据重排 - 基于原始数据的下标映射 """
        print(f"[DEBUG] 开始高效数据重排，目标顺序: {sorted_rows}")
        
        # 标记正在重排，避免清除缓存
        self._is_rearranging = True
        
        # 基于原始数据构建排序后的数据
        sorted_data = []
        for row_idx in sorted_rows:
            if row_idx in self._original_data:
                sorted_data.append(self._original_data[row_idx])
            else:
                print(f"[DEBUG] 警告: 原始数据中找不到行 {row_idx}")
        
        # 清空表格并重新设置行数
        self.clearContents()
        self.setRowCount(len(sorted_data))
        
        # 按新顺序放回数据
        new_row_data = {}
        
        for new_row, row_data in enumerate(sorted_data):
            print(f"新行 {new_row} <- 原始数据行 {sorted_rows[new_row]}: {row_data.get(0, '')}")
            for col in range(self.columnCount()):
                if col in row_data:
                    item = QTableWidgetItem(row_data[col])
                    # 直接设置项目，不调用setItem避免递归
                    super().setItem(new_row, col, item)
                    print(f"设置项目: 行 {new_row}, 列 {col}, 值={row_data[col]}")
                    
            # 创建新的行数据
            new_row_data[new_row] = row_data.copy()
            
        self._row_data = new_row_data
        
        # 结束重排标记
        self._is_rearranging = False
        
        print("数据重排完成，验证结果:")
        for row in range(self.rowCount()):
            if self.item(row, 0):
                name = self.item(row, 0).text()
                size = self.item(row, 1).text() if self.item(row, 1) else "N/A"
                print(f"验证行 {row}: {name} - {size}")


class TableView(TableBase, QTableView):
    """ Table view """
    
    def __init__(self, parent=None):
        super().__init__(parent)

    def isSelectRightClickedRow(self):
        return self._isSelectRightClickedRow

    def setSelectRightClickedRow(self, isSelect: bool):
        self._isSelectRightClickedRow = isSelect

    selectRightClickedRow = Property(bool, isSelectRightClickedRow, setSelectRightClickedRow)


class SortableTableView(SortableTableMixin, TableView):
    """ 可排序的表格视图 """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def _sort_data(self):
        """ 排序模型数据 """
        if self._sort_column < 0 or not self.model():
            return
            
        # 让模型处理排序
        self.model().sort(self._sort_column, self._sort_order)
        
        # 更新表头排序指示器
        if hasattr(self, 'horizontalHeader'):
            header = self.horizontalHeader()
            if isinstance(header, SortableHeaderView):
                header.setSortIndicator(self._sort_column, self._sort_order)


# 文件管理专用的排序函数
def get_file_sort_key(file_info: dict, column: int):
    """ 文件管理排序键函数 """
    name = file_info.get('name', '')
    is_dir = file_info.get('is_dir', False)
    size = file_info.get('size', 0)
    mtime = file_info.get('mtime', datetime.min)
    
    # 目录优先
    dir_priority = 0 if is_dir else 1
    
    if column == 0:  # 名称列
        return (dir_priority, name.lower())
    elif column == 1:  # 大小列
        return (dir_priority, size if isinstance(size, (int, float)) else 0)
    elif column == 2:  # 日期列
        return (dir_priority, mtime if isinstance(mtime, datetime) else datetime.min)
    else:
        # 其他列
        value = file_info.get(str(column), '')
        return (dir_priority, str(value).lower())


def create_file_sort_adapter(column: int):
    """创建文件排序函数适配器"""
    def adapter(file_info: dict):
        return get_file_sort_key(file_info, column)
    return adapter


# 为现有类添加排序功能的便捷函数
def make_table_sortable(table, sort_key_func: Callable = None):
    """ 使现有表格支持排序 """
    if isinstance(table, TableWidget):
        # 创建新的可排序表格并复制数据
        sortable_table = SortableTableWidget(table.parent())
        
        # 复制表头
        sortable_table.setColumnCount(table.columnCount())
        for col in range(table.columnCount()):
            header_item = table.horizontalHeaderItem(col)
            if header_item:
                sortable_table.setHorizontalHeaderItem(col, QTableWidgetItem(header_item))
                
        # 复制数据
        sortable_table.setRowCount(table.rowCount())
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    sortable_table.setItem(row, col, QTableWidgetItem(item))
                    
        # 设置自定义排序函数
        if sort_key_func:
            sortable_table.setSortKeyFunction(0, sort_key_func)
            
        return sortable_table
        
    elif isinstance(table, TableView):
        # 为TableView添加排序功能
        if hasattr(table, 'model') and table.model():
            # 创建新的可排序视图
            sortable_view = SortableTableView(table.parent())
            sortable_view.setModel(table.model())
            
            if sort_key_func:
                sortable_view.setSortKeyFunction(0, sort_key_func)
                
            return sortable_view
            
    return table
