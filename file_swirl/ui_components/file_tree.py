""""
File explorer

"""
import os
from collections import defaultdict
from pathlib import Path

from PyQt6.QtWidgets import QFrame, QTreeWidget, QTreeWidgetItem, QVBoxLayout

from file_swirl.ui_components.styles import FILE_TREE
from file_swirl.utils import categorize_file, convert_size, get_folder_size


class FileTreeComponent:
    """
    Show files paths
    """
    def __init__(self):
        self.tree_widget = QTreeWidget()
        self.tree_widget.setStyleSheet(FILE_TREE)
        self.tree_widget.setHeaderLabels(["Folder", "Metadata"])

    def build(self) -> QFrame:
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.addWidget(self.tree_widget)
        return frame

    def populate_tree(self, folder_paths: set):
        """
        Populate the tree view with dummy metadata for each folder path.
        """
        self.tree_widget.clear()
        root = QTreeWidgetItem(["Root",  ", ".join(folder_paths)])

        for folder in folder_paths:
            if not os.path.isdir(folder):
                continue

            folder_name = Path(folder).name
            size_bytes = get_folder_size(folder)
            size_readable = convert_size(size_bytes)

            node = QTreeWidgetItem([folder_name, f"Size: {size_readable}"])

            # Count file categories
            category_count = defaultdict(int)
            for root_dir, _, files in os.walk(folder):
                for file in files:
                    full_path = os.path.join(root_dir, file)
                    category = categorize_file(full_path)
                    category_count[category] += 1

            for category, count in category_count.items():
                node.addChild(QTreeWidgetItem([category, f"{count} items"]))

            root.addChild(node)

        self.tree_widget.addTopLevelItem(root)
        self.tree_widget.expandAll()

    def clear_tree(self):
        self.tree_widget.clear()
