from __future__ import annotations

from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtCore import QItemSelectionModel

from qfluentwidgets import TableView
from qfluentwidgets.components.widgets.menu import RoundMenu, MenuAnimationType

from app.common.icon import Icon
from app.core.managers.signal_manager import signalManager
from app.models.remote_file_model import RemoteFileEntry


class RemoteFileTableView(TableView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAlternatingRowColors(True)
        self.setShowGrid(False)
        self.verticalHeader().hide()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(lambda p: self._show_context_menu(p))
        self.doubleClicked.connect(lambda i: self._on_double_clicked(i))

    def selected_entries(self):
        if not self.model() or not self.selectionModel():
            return []
        entries = []
        for idx in self.selectionModel().selectedRows():
            entry = self.model().data(idx, Qt.UserRole)
            if isinstance(entry, RemoteFileEntry) and not entry.is_parent:
                entries.append(entry)
        return entries

    def _on_double_clicked(self, index):
        if not index.isValid() or not self.model():
            return
        entry = self.model().data(index, Qt.UserRole)
        if isinstance(entry, RemoteFileEntry) and (entry.is_parent or entry.is_dir):
            signalManager.emit("remoteFileEnterRequested", entry)

    def _show_context_menu(self, pos: QPoint):
        view_index = self.indexAt(pos)
        if view_index.isValid() and self.selectionModel():
            if not self.selectionModel().isSelected(view_index):
                self.selectionModel().select(
                    view_index,
                    QItemSelectionModel.ClearAndSelect | QItemSelectionModel.Rows,
                )

        selected = self.selected_entries()
        has_archive = any(self._is_archive(e.name) for e in selected)

        menu = RoundMenu(parent=self)
        menu.setItemHeight(32)

        download_action = QAction(QIcon(Icon.REMOTE_FILE_DOWNLOAD.path(theme=None)), self.tr("下载"), menu)
        delete_action = QAction(QIcon(Icon.REMOTE_FILE_DELETE.path(theme=None)), self.tr("删除"), menu)
        compress_action = QAction(QIcon(Icon.REMOTE_FILE_COMPRESS.path(theme=None)), self.tr("压缩"), menu)
        decompress_action = QAction(QIcon(Icon.REMOTE_FILE_ARCHIVE.path(theme=None)), self.tr("解压"), menu)
        upload_action = QAction(QIcon(Icon.REMOTE_FILE_UPLOAD.path(theme=None)), self.tr("上传"), menu)
        refresh_action = QAction(QIcon(Icon.REMOTE_FILE_REFRESH.path(theme=None)), self.tr("刷新"), menu)

        download_action.setEnabled(bool(selected))
        delete_action.setEnabled(bool(selected))
        compress_action.setEnabled(bool(selected))
        decompress_action.setVisible(has_archive)

        download_action.triggered.connect(lambda: signalManager.emit("remoteFileOperationRequested", "download"))
        delete_action.triggered.connect(lambda: signalManager.emit("remoteFileOperationRequested", "delete"))
        compress_action.triggered.connect(lambda: signalManager.emit("remoteFileOperationRequested", "compress"))
        decompress_action.triggered.connect(lambda: signalManager.emit("remoteFileOperationRequested", "decompress"))
        upload_action.triggered.connect(lambda: signalManager.emit("remoteFileOperationRequested", "upload"))
        refresh_action.triggered.connect(lambda: signalManager.emit("remoteFileOperationRequested", "refresh"))

        menu.addAction(download_action)
        menu.addAction(delete_action)
        menu.addAction(compress_action)
        if has_archive:
            menu.addAction(decompress_action)
        menu.addSeparator()
        menu.addAction(upload_action)
        menu.addAction(refresh_action)

        global_pos = self.viewport().mapToGlobal(pos)
        menu.exec(global_pos, aniType=MenuAnimationType.DROP_DOWN)

    def _is_archive(self, name: str) -> bool:
        lower = name.lower()
        return lower.endswith((".zip", ".tar", ".tgz", ".tar.gz"))
