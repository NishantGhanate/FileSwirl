""""
File explorer

"""
from PyQt6.QtWidgets import QFrame, QTreeWidget, QTreeWidgetItem, QVBoxLayout

from file_swirl.ui_components.styles import FILE_TREE


class FileTreeComponent:
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
        root = QTreeWidgetItem(["Root", ""])

        for folder in folder_paths:
            name = folder.split("/")[-1] or folder.split("\\")[-1]
            node = QTreeWidgetItem([name, "Size: 1.2GB"])
            node.addChild(QTreeWidgetItem(["Photos", "12 items"]))
            node.addChild(QTreeWidgetItem(["Docs", "8 items"]))
            root.addChild(node)

        self.tree_widget.addTopLevelItem(root)
        self.tree_widget.expandAll()

    def clear_tree(self):
        self.tree_widget.clear()
