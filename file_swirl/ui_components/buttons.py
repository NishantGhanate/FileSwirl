from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QListView,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ToggleButton(QPushButton):
    toggled_state = pyqtSignal(bool)

    def __init__(self, label_a: str, label_b: str, initial: bool = True):
        super().__init__()
        self.label_a = label_a
        self.label_b = label_b
        self.setCheckable(True)
        self.setChecked(initial)
        self.update_text()
        self.clicked.connect(self.toggle)

        self.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                font-weight: bold;
                font-size: 13px;
                color: white;
                background-color: #5a5a7a;
                border-radius: 6px;
            }
            QPushButton:checked {
                background-color: #7a7aff;
            }
        """)

    def toggle(self):
        self.update_text()
        self.toggled_state.emit(self.isChecked())

    def update_text(self):
        self.setText(f"{self.label_a if self.isChecked() else self.label_b}")


class MultiSelectCombo(QComboBox):
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


class ControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        toggles = QHBoxLayout()
        self.dry_run_toggle = ToggleButton("Dry Run: ON", "Dry Run: OFF", initial=True)
        self.parallel_toggle = ToggleButton("Execution: Parallel", "Execution: Linear", initial=True)
        toggles.addWidget(self.dry_run_toggle)
        toggles.addWidget(self.parallel_toggle)

        self.multi_select = MultiSelectCombo(["Name", "Date", "Size", "Device"])

        layout.addLayout(toggles)
        layout.addWidget(self.multi_select)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = ControlPanel()
    win.setWindowTitle("PyQt6 Toggle + Multi-Select")
    win.resize(400, 180)
    win.show()
    sys.exit(app.exec())
