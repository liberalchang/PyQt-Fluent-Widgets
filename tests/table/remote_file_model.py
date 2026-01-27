from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QIcon

from app.common.icon import Icon


@dataclass(frozen=True)
class RemoteFileEntry:
    name: str
    is_dir: bool
    is_parent: bool
    size: Optional[int]
    mtime_text: str
    mtime_sort_key: Optional[datetime]
    permissions: str
    owner: str


class RemoteFileTableModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._headers: List[str] = ["名称", "大小", "修改时间", "权限", "拥有者"]
        self._entries: List[RemoteFileEntry] = []
        self._sort_column = 0
        self._sort_order = Qt.AscendingOrder

    def set_headers(self, headers: List[str]):
        self._headers = headers
        self.headerDataChanged.emit(Qt.Horizontal, 0, max(0, self.columnCount() - 1))

    def set_entries(self, entries: List[RemoteFileEntry]):
        self.beginResetModel()
        self._entries = list(entries)
        self.endResetModel()

    def entries(self) -> List[RemoteFileEntry]:
        return list(self._entries)

    def entry_at_row(self, row: int) -> Optional[RemoteFileEntry]:
        if row < 0 or row >= len(self._entries):
            return None
        return self._entries[row]

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return len(self._entries)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return 5

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if orientation != Qt.Horizontal:
            return super().headerData(section, orientation, role)
        if role != Qt.DisplayRole:
            return super().headerData(section, orientation, role)
        if 0 <= section < len(self._headers):
            return self._headers[section]
        return ""

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.NoItemFlags
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return None

        entry = self.entry_at_row(index.row())
        if not entry:
            return None

        col = index.column()
        if role == Qt.DisplayRole:
            if col == 0:
                return entry.name
            if col == 1:
                if entry.is_dir or entry.is_parent or entry.size is None:
                    return ""
                return self._format_size(entry.size)
            if col == 2:
                return entry.mtime_text
            if col == 3:
                return entry.permissions
            if col == 4:
                return entry.owner

        if role == Qt.DecorationRole and col == 0:
            icon_path = self._icon_path_for_entry(entry)
            return QIcon(icon_path)

        if role == Qt.TextAlignmentRole:
            if col in (1,):
                return int(Qt.AlignRight | Qt.AlignVCenter)
            return int(Qt.AlignLeft | Qt.AlignVCenter)

        if role == Qt.UserRole:
            return entry

        return None

    def sort(self, column: int, order: Qt.SortOrder = Qt.AscendingOrder):
        if not self._entries:
            return

        self.layoutAboutToBeChanged.emit()
        self._sort_column = column
        self._sort_order = order

        parent_entry = None
        rest = self._entries
        if self._entries and self._entries[0].is_parent:
            parent_entry = self._entries[0]
            rest = self._entries[1:]

        reverse = order == Qt.DescendingOrder
        rest.sort(key=lambda e: self._sort_key(e, column), reverse=reverse)

        self._entries = [parent_entry] + rest if parent_entry else rest
        self.layoutChanged.emit()

    def _sort_key(self, entry: RemoteFileEntry, column: int):
        if entry.is_parent:
            return (-1, "")

        dir_priority = 0 if entry.is_dir else 1
        if column == 0:
            return (dir_priority, entry.name.casefold())
        if column == 1:
            size = entry.size if entry.size is not None else 0
            return (dir_priority, size)
        if column == 2:
            dt = entry.mtime_sort_key or datetime.min
            return (dir_priority, dt)
        if column == 3:
            return (dir_priority, entry.permissions)
        if column == 4:
            return (dir_priority, entry.owner)
        return (dir_priority, entry.name.casefold())

    def _icon_path_for_entry(self, entry: RemoteFileEntry) -> str:
        if entry.is_parent:
            return Icon.REMOTE_FILE_PARENT.path(theme=None)
        if entry.is_dir:
            return Icon.REMOTE_FILE_FOLDER.path(theme=None)
        lower = entry.name.lower()
        if lower.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp")):
            return Icon.REMOTE_FILE_IMAGE.path(theme=None)
        if lower.endswith((".txt", ".md", ".log", ".json", ".yaml", ".yml", ".ini", ".cfg")):
            return Icon.REMOTE_FILE_TEXT.path(theme=None)
        if lower.endswith((".mp4", ".avi", ".mov", ".mkv")):
            return Icon.REMOTE_FILE_VIDEO.path(theme=None)
        if lower.endswith((".zip", ".tar", ".gz", ".tgz", ".tar.gz", ".7z", ".rar")):
            return Icon.REMOTE_FILE_ARCHIVE.path(theme=None)
        return Icon.REMOTE_FILE_FILE.path(theme=None)

    def _format_size(self, size: int) -> str:
        if size < 1024:
            return f"{size} B"
        if size < 1024 * 1024:
            return f"{size / 1024:.1f} KB"
        if size < 1024 * 1024 * 1024:
            return f"{size / (1024 * 1024):.1f} MB"
        return f"{size / (1024 * 1024 * 1024):.1f} GB"
