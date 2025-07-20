"""
File explorer
"""
import os
from pathlib import Path

from PyQt6.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QFrame, QTreeWidget, QTreeWidgetItem, QVBoxLayout

from file_swirl.ui_components.styles import FILE_TREE
from file_swirl.utils import convert_size


class FileTreeComponent(QObject):
    """
    Show file paths (folders and subfolders up to 2 levels deep) with async size calculation.
    """
    tree_updated = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.root = None
        self.tree_widget = QTreeWidget()
        self.tree_widget.setStyleSheet(FILE_TREE)
        self.tree_widget.setHeaderLabels(["Folder", "Size"])
        self.thread_pool = QThreadPool()

        self.item_map = {}  # Map from folder path to QTreeWidgetItem
        self.total_root_size = 0  # Reset total
        self.pending_folder_count = 0
        self.top_folder_sizes = {}
        self.pending_top_folders = set()

    def build(self) -> QFrame:
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.addWidget(self.tree_widget)
        return frame

    @staticmethod
    def get_folder_size_limited(folder_path: Path, depth: int=1):
        """Return folder size limited to a given depth (relative to folder_path)."""
        folder_path = Path(folder_path).resolve()
        print(f"\nScanning: {folder_path}")
        total_size = 0
        base_depth = str(folder_path).rstrip(os.sep).count(os.sep)
        for root_dir, dirs, files in os.walk(folder_path):
            current_path = Path(root_dir).resolve()

            try:
                current_depth = str(root_dir).rstrip(os.sep).count(os.sep) - base_depth
            except ValueError:
                # Path not inside the folder_path
                print(f"Skipped (not relative): {current_path}")
                continue

            # print(f"  → At {current_path} (depth={relative_depth})")
            if current_depth > depth:
                # print(f"Skipping deeper level")
                dirs.clear()
                # continue

            for file in files:
                full_path = current_path / file
                try:
                    if full_path.is_file():
                        file_size = full_path.stat().st_size
                        total_size += file_size
                        # print(f"    + {file} ({file_size} bytes)")
                except Exception as e:
                    print(f"! Error reading file {file}: {e}")

        print(f"Total size for {folder_path}: {total_size} bytes\n")
        return total_size

    def clear_tree(self) -> None:
        self.pending_top_folders = set()
        self.top_folder_sizes = {}
        self.total_root_size = 0
        self.tree_widget.clear()
        self.item_map.clear()

    def populate_tree(self, folder_paths: set):
        """
        Populate the tree view (non-blocking) with folders and their sizes.
        """
        self.clear_tree()

        for folder in folder_paths:
            if not os.path.isdir(folder):
                continue

            folder_name = Path(folder).name
            folder_item = QTreeWidgetItem([folder_name, "Calculating..."])
            # self.root.addChild(folder_item)
            self.tree_widget.addTopLevelItem(folder_item)

            normalized_folder = os.path.normpath(folder)
            self.item_map[normalized_folder] = folder_item

            # Track pending top-level folder
            self.pending_folder_count += 1
            self.pending_top_folders.add(normalized_folder)

            self._start_size_worker(normalized_folder)

            # Immediate subfolders (1 level deep)
            for entry in os.scandir(normalized_folder):
                if entry.is_dir():
                    self.pending_folder_count += 1
                    sub_path = os.path.normpath(entry.path)
                    sub_item = QTreeWidgetItem([entry.name, "Calculating..."])
                    folder_item.addChild(sub_item)
                    self.item_map[sub_path] = sub_item
                    self._start_size_worker(sub_path)

        self.tree_widget.expandAll()

    def _start_size_worker(self, folder_path: Path):
        worker = FolderSizeWorker(folder_path)
        worker.signals.result.connect(self._update_folder_size)
        self.thread_pool.start(worker)

    def _update_folder_size(self, folder_path: Path, size_bytes: int):
        normalized = os.path.normpath(folder_path)
        item = self.item_map.get(normalized)
        if item:
            item.setText(1, convert_size(size_bytes))
            self.top_folder_sizes[folder_path] = size_bytes
            self.tree_widget.expandAll()

        self.pending_folder_count -= 1
        if self.pending_folder_count == 0:
            self.tree_updated.emit()


class FolderSizeWorkerSignals(QObject):
    result = pyqtSignal(str, int)  # folder path, size in bytes, is_top_level


class FolderSizeWorker(QRunnable):
    def __init__(self, folder_path):
        super().__init__()
        self.folder_path = folder_path
        self.signals = FolderSizeWorkerSignals()

    @pyqtSlot()
    def run(self) -> None:
        size = FileTreeComponent.get_folder_size_limited(self.folder_path, depth=1)
        self.signals.result.emit(self.folder_path, size)
