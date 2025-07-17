from typing import List

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QComboBox, QListView


class MultiSelectComboBox(QComboBox):
    """
    As name suggests
    """
    def __init__(self, items):
        super().__init__()
        self.setView(QListView())
        self.setModel(QStandardItemModel(self))
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setPlaceholderText("Select options...")
        self.setStyleSheet("QComboBox { padding: 8px; font-size: 13px; }")
        self.populate(items)
        self.model().itemChanged.connect(self.update_display)

    def populate(self, items):
        for item in items:
            std_item = QStandardItem(item)
            std_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            std_item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
            self.model().appendRow(std_item)

    def update_display(self):
        checked = [self.model().item(i).text()
                   for i in range(self.model().rowCount())
                   if self.model().item(i).checkState() == Qt.CheckState.Checked]
        self.lineEdit().setText(", ".join(checked))

    def selected_items(self):
        return [
            self.model().item(i).text()
            for i in range(self.model().rowCount())
            if self.model().item(i).checkState() == Qt.CheckState.Checked
        ]
