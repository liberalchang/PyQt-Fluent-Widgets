from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import List

from PySide6.QtCore import QEvent, Qt, Signal, Slot
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QWidget,
    QVBoxLayout,
)

from qfluentwidgets import BodyLabel, InfoBar, InfoBarPosition, LineEdit, ScrollArea, SimpleCardWidget

from app.common.style_sheet import StyleSheet
from app.common.logger import logger
from app.core.managers.params_manager import paramsManager
from app.core.managers.signal_manager import signalManager
from app.core.services.carconnect.service import VehicleConnectionService
from app.models.remote_file_model import RemoteFileEntry, RemoteFileTableModel
from app.widgets.basic_input.remote_file_table_view import RemoteFileTableView
from app.views.dialogs.file_transfer_dialog import FileTransferDialog, FileTransferDirection


class FileManagerInterface(ScrollArea):
    _file_list_ready = Signal(object, str, bool, str)
    _operation_ready = Signal(str, bool, str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("fileManagerInterface")

        self.connection_service = VehicleConnectionService()
        self._executor = ThreadPoolExecutor(max_workers=2)

        self._current_path = ""
        self._last_good_path = ""
        self._busy = False

        self._build_ui()
        self._init_model()
        self._init_signals()
        self._load_style()

    def closeEvent(self, e):
        try:
            self._executor.shutdown(wait=False, cancel_futures=True)
        except TypeError:
            self._executor.shutdown(wait=False)
        except Exception:
            pass

        super().closeEvent(e)

    def _build_ui(self):
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)
        self.vBoxLayout.setContentsMargins(20, 20, 20, 20)
        self.vBoxLayout.setSpacing(12)

        self.pathCard = SimpleCardWidget(self.view)
        self.pathLayout = QVBoxLayout(self.pathCard)
        self.pathLayout.setContentsMargins(16, 16, 16, 16)
        self.pathLayout.setSpacing(10)

        self.pathRow = QWidget(self.pathCard)
        self.pathRowLayout = QHBoxLayout(self.pathRow)
        self.pathRowLayout.setContentsMargins(0, 0, 0, 0)
        self.pathRowLayout.setSpacing(10)

        self.pathLabel = BodyLabel(self.tr("文件路径"), self.pathRow)
        self.pathEdit = LineEdit(self.pathRow)
        self.pathEdit.setClearButtonEnabled(True)

        self.pathStatusDot = QFrame(self.pathRow)
        self.pathStatusDot.setObjectName("pathStatusDot")
        self.pathStatusDot.setFixedSize(10, 10)

        self.pathRowLayout.addWidget(self.pathLabel)
        self.pathRowLayout.addWidget(self.pathEdit, 1)
        self.pathRowLayout.addWidget(self.pathStatusDot)

        self.pathSeparator = QFrame(self.pathCard)
        self.pathSeparator.setObjectName("pathSeparator")
        self.pathSeparator.setFixedHeight(1)

        self.pathLayout.addWidget(self.pathRow)
        self.pathLayout.addWidget(self.pathSeparator)

        self.tableCard = SimpleCardWidget(self.view)
        self.tableLayout = QVBoxLayout(self.tableCard)
        self.tableLayout.setContentsMargins(12, 12, 12, 12)
        self.tableLayout.setSpacing(0)

        self.tableView = RemoteFileTableView(self.tableCard)
        self.tableLayout.addWidget(self.tableView)

        self.vBoxLayout.addWidget(self.pathCard)
        self.vBoxLayout.addWidget(self.tableCard, 1)

        self.setWidget(self.view)
        self.setWidgetResizable(True)

    def _init_model(self):
        self.fileModel = RemoteFileTableModel(self)
        self.tableView.setModel(self.fileModel)

        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSortIndicatorShown(True)

    def _init_signals(self):
        self._file_list_ready.connect(lambda l, p, s, m: self._on_file_list_ready(l, p, s, m))
        self._operation_ready.connect(lambda t, s, m: self._on_operation_ready(t, s, m))

        self.pathEdit.returnPressed.connect(lambda: self._on_path_entered())
        self.tableView.horizontalHeader().sortIndicatorChanged.connect(lambda i, o: self._on_sort_changed(i, o))

        signalManager.connect("vehicleConnectionChanged", self._on_vehicle_connection_changed)
        signalManager.connect("themeChanged", self._on_theme_changed)
        signalManager.connect("languageChanged", self._on_language_changed)
        signalManager.connect("remoteFileEnterRequested", self._on_enter_requested)
        signalManager.connect("remoteFileOperationRequested", self._on_operation_requested)

    def _load_style(self):
        StyleSheet.FILE_MANAGER_INTERFACE.apply(self)
        self._set_status("bad")

    @Slot(object)
    def _on_theme_changed(self, *_args):
        StyleSheet.FILE_MANAGER_INTERFACE.apply(self)

    @Slot(object)
    def _on_language_changed(self, *_args):
        self._retranslate_ui()

    @Slot(bool, str)
    def _on_vehicle_connection_changed(self, is_connected: bool, message: str):
        if not is_connected:
            self._apply_connected_state(False)
            return

        if self.isVisible():
            self._apply_connected_state(True)
            self._ensure_initialized_and_refresh()

    def showEvent(self, e):
        super().showEvent(e)
        is_connected = bool(paramsManager.get_memory("is_vehicle_connected", False))
        self._apply_connected_state(is_connected)
        self._ensure_initialized_and_refresh()

    def changeEvent(self, event: QEvent):
        super().changeEvent(event)
        if event.type() == QEvent.LanguageChange:
            self._retranslate_ui()

    def _retranslate_ui(self):
        self.pathLabel.setText(self.tr("文件路径"))
        self.fileModel.set_headers(
            [
                self.tr("名称"),
                self.tr("大小"),
                self.tr("修改时间"),
                self.tr("权限"),
                self.tr("拥有者"),
            ]
        )

    def _ensure_initialized_and_refresh(self):
        if not paramsManager.get_memory("is_vehicle_connected", False):
            return

        if not self._current_path:
            default_path = paramsManager.get_config("sshRemoteFolder", "/mooe/log")
            self._go_to_path(str(default_path))
            return

        self.refresh()

    def _apply_connected_state(self, is_connected: bool):
        """
        根据车辆连接状态更新UI组件的启用状态和路径指示灯
        
        状态指示灯 (PathStatusDot) 逻辑:
        1. 车辆已连接 (is_connected=True):
           - 如果 busy=True: 显示黄色 ("busy")
           - 否则，如果有有效的历史路径 (_last_good_path存在): 显示绿色 ("ok")
           - 否则 (没有有效历史路径): 显示黄色 ("busy")
           
        2. 车辆未连接 (is_connected=False):
           - 始终显示红色 ("bad")
        """
        self.pathEdit.setEnabled(is_connected and not self._busy)
        self.tableView.setEnabled(is_connected and not self._busy)
        if is_connected:
            if self._busy:
                self._set_status("busy")
            else:
                self._set_status("ok" if self._last_good_path else "busy")
        else:
            self._set_status("bad")

    def _set_busy(self, busy: bool):
        self._busy = busy
        if busy:
            self._set_status("busy")
        else:
            self._set_status("ok" if self._last_good_path else "bad")

        is_connected = bool(paramsManager.get_memory("is_vehicle_connected", False))
        self._apply_connected_state(is_connected)

    def _set_status(self, status: str):
        self.pathStatusDot.setProperty("status", status)
        self.pathStatusDot.style().unpolish(self.pathStatusDot)
        self.pathStatusDot.style().polish(self.pathStatusDot)
        self.pathStatusDot.update()

    def _show_error(self, title: str, content: str):
        InfoBar.error(
            title=title,
            content=content,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=2500,
            parent=self.window(),
        )

    def _show_success(self, title: str, content: str):
        InfoBar.success(
            title=title,
            content=content,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=1800,
            parent=self.window(),
        )

    @Slot()
    def _on_path_entered(self):
        text = self.pathEdit.text().strip()
        if not text:
            return
        self._go_to_path(text)

    @Slot(int, Qt.SortOrder)
    def _on_sort_changed(self, logical_index: int, order: Qt.SortOrder):
        self.fileModel.sort(logical_index, order)

    @Slot(RemoteFileEntry)
    def _on_enter_requested(self, entry: RemoteFileEntry):
        if self._busy or not paramsManager.get_memory("is_vehicle_connected", False):
            return

        if entry.is_parent:
            current = Path(self._current_path) if self._current_path else Path("/")
            parent_path = current.parent.as_posix()
            if parent_path == ".":
                parent_path = "/"
            self._go_to_path(parent_path)
            return

        self._go_to_path(entry.name)

    def refresh(self):
        if self._busy or not paramsManager.get_memory("is_vehicle_connected", False):
            return

        logger.debug("Refeshing file list...")
        self._set_busy(True)
        self._executor.submit(self._do_refresh)

    def _go_to_path(self, path: str):
        if self._busy or not paramsManager.get_memory("is_vehicle_connected", False):
            return

        logger.info(f"Navigating to path: {path}")
        self._set_busy(True)
        self._executor.submit(self._do_cd_and_refresh, path)

    def _do_cd_and_refresh(self, path: str):
        ok = self.connection_service.cd(path)
        if not ok:
            self._file_list_ready.emit([], self._current_path, False, self.tr("路径不可用"))
            return

        self._do_refresh()

    def _do_refresh(self):
        path = self.connection_service.pwd()
        entries = self.connection_service.ls(".")
        ok = bool(entries) or entries == []
        self._file_list_ready.emit(entries, path, ok, "")

    def _on_file_list_ready(self, raw_entries: object, path: str, ok: bool, message: str):
        """
        文件列表刷新完成的回调函数
        
        Args:
            raw_entries: 原始文件列表数据 (list of dict)
            path: 当前刷新成功的路径
            ok: 操作是否成功
            message: 错误信息 (如果失败)
        
        状态逻辑:
        - 失败 (ok=False):
            - 状态灯变红 ("bad")
            - 如果有上一次的有效路径，重置输入框显示为旧路径
        - 成功 (ok=True):
            - 更新当前路径 (_current_path) 和最后有效路径 (_last_good_path)
            - 状态灯变绿 ("ok")
            - 解析原始数据并更新表格模型 (RemoteFileTableModel)
        """
        self._set_busy(False)
        if not ok:
            logger.error(f"File list refresh failed: {message}")
            self._set_status("bad")
            if message:
                self._show_error(self.tr("错误"), message)
            if self._last_good_path:
                self.pathEdit.setText(self._last_good_path)
            return

        logger.debug(f"File list refresh success, path: {path}, entries: {len(raw_entries) if raw_entries else 0}")
        self._current_path = path
        self._last_good_path = path
        self.pathEdit.setText(path)
        self._set_status("ok")

        entries: List[RemoteFileEntry] = [
            RemoteFileEntry(
                name="..",
                is_dir=True,
                is_parent=True,
                size=None,
                mtime_text="",
                mtime_sort_key=None,
                permissions="",
                owner="",
            )
        ]

        for item in (raw_entries or []):
            if not isinstance(item, dict):
                continue
            name = str(item.get("name", "")).strip()
            if not name or name in (".", ".."):
                continue
            if " -> " in name:
                name = name.split(" -> ", 1)[0]

            permissions = str(item.get("permissions", ""))
            is_dir = bool(item.get("is_dir")) or permissions.startswith("d")

            size_val = None
            try:
                size_val = int(str(item.get("size", "")).strip())
            except Exception:
                size_val = None

            mtime_text = str(item.get("mtime") or "").strip()
            if not mtime_text:
                date = str(item.get("date") or "").strip()
                time_str = str(item.get("time") or "").strip()
                if date and time_str:
                    mtime_text = f"{date} {time_str}"

            mtime_dt = None
            if mtime_text:
                try:
                    mtime_dt = datetime.fromisoformat(mtime_text)
                except Exception:
                    mtime_dt = None

            user = str(item.get("user") or "").strip()
            group = str(item.get("group") or "").strip()
            owner = f"{user}:{group}" if user and group else user

            entries.append(
                RemoteFileEntry(
                    name=name,
                    is_dir=is_dir,
                    is_parent=False,
                    size=size_val,
                    mtime_text=mtime_text,
                    mtime_sort_key=mtime_dt,
                    permissions=permissions,
                    owner=owner,
                )
            )

        self.fileModel.set_headers(
            [
                self.tr("名称"),
                self.tr("大小"),
                self.tr("修改时间"),
                self.tr("权限"),
                self.tr("拥有者"),
            ]
        )
        self.fileModel.set_entries(entries)
        self.fileModel.sort(self.tableView.horizontalHeader().sortIndicatorSection(), self.tableView.horizontalHeader().sortIndicatorOrder())

    def _on_operation_requested(self, op: str):
        if not paramsManager.get_memory("is_vehicle_connected", False):
            return
        if self._busy:
            logger.warning(f"FileManager busy, ignoring operation: {op}")
            return

        logger.info(f"FileManager operation requested: {op}")

        if op == "refresh":
            self.refresh()
            return

        if op == "upload":
            self._start_upload()
            return

        selected = self.tableView.selected_entries()
        if not selected:
            logger.debug("No files selected for operation")
            return

        if op == "download":
            self._start_download(selected)
        elif op == "delete":
            self._start_delete(selected)
        elif op == "compress":
            self._start_compress(selected)
        elif op == "decompress":
            self._start_decompress(selected)

    def _start_upload(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, self.tr("选择本地文件"), "")
        if not file_paths:
            return

        tasks = []
        for local_path in file_paths:
            filename = os.path.basename(local_path)
            remote_path = f"{self._current_path.rstrip('/')}/{filename}" if self._current_path else filename
            tasks.append((local_path, remote_path))

        self._set_busy(True)
        dialog = FileTransferDialog(FileTransferDirection.UPLOAD, tasks, self)
        ok = bool(dialog.exec())
        self._set_busy(False)

        if ok:
            self._show_success(self.tr("上传"), self.tr("上传成功"))
            self.refresh()

    def _do_upload(self, file_paths: List[str]):
        ok_all = True
        for local_path in file_paths:
            filename = os.path.basename(local_path)
            remote_path = f"{self._current_path.rstrip('/')}/{filename}" if self._current_path else filename
            ok = self.connection_service.sftp_upload(local_path, remote_path)
            ok_all = ok_all and ok

        self._operation_ready.emit("upload", ok_all, "")

    def _start_download(self, entries: List[RemoteFileEntry]):
        local_dir = QFileDialog.getExistingDirectory(self, self.tr("选择本地保存目录"), "")
        if not local_dir:
            return

        has_dir = any(e.is_dir for e in entries)
        if has_dir:
            logger.info("Starting folder download (async)")
            self._set_busy(True)
            self._executor.submit(self._do_download, entries, local_dir)
            return

        tasks = []
        for entry in entries:
            remote_path = f"{self._current_path.rstrip('/')}/{entry.name}" if self._current_path else entry.name
            local_path = os.path.join(local_dir, entry.name)
            tasks.append((local_path, remote_path))

        logger.info(f"Starting file download dialog with {len(tasks)} tasks")
        self._set_busy(True)
        dialog = FileTransferDialog(FileTransferDirection.DOWNLOAD, tasks, self)
        
        logger.debug("Executing FileTransferDialog")
        ok = bool(dialog.exec())
        logger.debug(f"FileTransferDialog returned: {ok}")
        
        self._set_busy(False)

        if ok:
            logger.info("Download completed successfully, refreshing list")
            self._show_success(self.tr("下载"), self.tr("下载完成"))
            self.refresh()
        else:
            logger.info("Download canceled or failed")

    def _do_download(self, entries: List[RemoteFileEntry], local_dir: str):
        ok_all = True
        for entry in entries:
            remote_name = entry.name
            if entry.is_dir:
                archive_name = self._make_unique_remote_archive_name(f"{remote_name}.tar.gz")
                ok = self.connection_service.compress([remote_name], archive_name)
                if ok:
                    remote_archive_path = f"{self._current_path.rstrip('/')}/{archive_name}" if self._current_path else archive_name
                    ok = self.connection_service.sftp_download(remote_archive_path, os.path.join(local_dir, archive_name))
                    self.connection_service.rm(archive_name)
            else:
                remote_file_path = f"{self._current_path.rstrip('/')}/{remote_name}" if self._current_path else remote_name
                ok = self.connection_service.sftp_download(remote_file_path, os.path.join(local_dir, remote_name))
            ok_all = ok_all and ok

        self._operation_ready.emit("download", ok_all, "")

    def _start_delete(self, entries: List[RemoteFileEntry]):
        self._set_busy(True)
        self._executor.submit(self._do_delete, entries)

    def _do_delete(self, entries: List[RemoteFileEntry]):
        ok_all = True
        for entry in entries:
            ok_all = ok_all and self.connection_service.rm(entry.name)
        self._operation_ready.emit("delete", ok_all, "")

    def _start_compress(self, entries: List[RemoteFileEntry]):
        target = "archive.tar.gz"
        if len(entries) == 1:
            target = f"{entries[0].name}.tar.gz"

        target = self._make_unique_remote_archive_name(target)
        self._set_busy(True)
        self._executor.submit(self._do_compress, entries, target)

    def _do_compress(self, entries: List[RemoteFileEntry], target: str):
        ok = self.connection_service.compress([e.name for e in entries], target)
        self._operation_ready.emit("compress", ok, target)

    def _start_decompress(self, entries: List[RemoteFileEntry]):
        self._set_busy(True)
        self._executor.submit(self._do_decompress, entries)

    def _do_decompress(self, entries: List[RemoteFileEntry]):
        ok_all = True
        for entry in entries:
            if not self._is_supported_archive(entry.name):
                ok_all = False
                continue

            ok_all = ok_all and self.connection_service.decompress(entry.name, ".")

        self._operation_ready.emit("decompress", ok_all, "")

    def _on_operation_ready(self, op: str, ok: bool, payload: str):
        self._set_busy(False)
        if not ok:
            self._show_error(self.tr("操作失败"), self.tr("{op} 失败").format(op=op))
        else:
            if op == "delete":
                self._show_success(self.tr("删除"), self.tr("删除成功"))
            elif op == "compress":
                self._show_success(self.tr("压缩"), self.tr("压缩成功: {payload}").format(payload=payload))
            elif op == "decompress":
                self._show_success(self.tr("解压"), self.tr("解压成功"))
            elif op == "upload":
                self._show_success(self.tr("上传"), self.tr("上传成功"))
            elif op == "download":
                self._show_success(self.tr("下载"), self.tr("下载成功"))

        self.refresh()

    def _make_unique_remote_archive_name(self, base: str) -> str:
        existing = {e.name for e in self.fileModel.entries() if not e.is_parent}
        if base not in existing:
            return base

        stem = base
        suffix = ""
        if base.endswith(".tar.gz"):
            stem = base[:-7]
            suffix = ".tar.gz"
        elif "." in base:
            stem, suffix = base.rsplit(".", 1)
            suffix = f".{suffix}"

        for i in range(1, 1000):
            candidate = f"{stem}_{i}{suffix}"
            if candidate not in existing:
                return candidate

        return f"{stem}_{int(datetime.now().timestamp())}{suffix}"

    def _is_supported_archive(self, name: str) -> bool:
        lower = name.lower()
        return lower.endswith((".zip", ".tar.gz", ".tgz", ".tar"))
