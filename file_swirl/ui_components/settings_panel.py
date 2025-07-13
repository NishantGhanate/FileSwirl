from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QListView,
    QRadioButton,
    QVBoxLayout,
)


class MultiSelectComboBox(QComboBox):
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

class SettingsPanelComponent(QFrame):
    def __init__(self, multi_select_items: list[str]):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: rgba(40, 40, 60, 0.85);
                border-radius: 8px;
                padding: 10px;
            }
        """)
        self.setVisible(False)  # Hidden initially

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # Dry run checkbox
        self.dry_run_checkbox = QCheckBox("Dry Run")
        self.dry_run_checkbox.setChecked(False)
        layout.addWidget(self.dry_run_checkbox)

        # Execution mode: Linear / Parallel
        mode_label = QLabel("Execution Mode:")
        mode_label.setStyleSheet("color: white;")
        layout.addWidget(mode_label)

        self.linear_button = QRadioButton("Linear")
        self.parallel_button = QRadioButton("Parallel")
        self.linear_button.setChecked(True)

        mode_group = QHBoxLayout()
        mode_group.addWidget(self.linear_button)
        mode_group.addWidget(self.parallel_button)
        layout.addLayout(mode_group)

        # Multi-select dropdown
        self.multi_select = MultiSelectComboBox(multi_select_items)
        layout.addWidget(QLabel("Filter Keys:", self))
        layout.addWidget(self.multi_select)

    def toggle(self):
        self.setVisible(not self.isVisible())
