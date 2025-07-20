

from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout

from file_swirl.ui_components.buttons import ToggleButton
from file_swirl.ui_components.drop_down import MultiSelectComboBox


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
        toggles = QHBoxLayout()
        self.dry_run_toggle = ToggleButton("Dry Run: ON", "Dry Run: OFF", initial=False)
        self.parallel_toggle = ToggleButton("Execution: Parallel", "Execution: Linear", initial=False)
        self.shift_toggle = ToggleButton("Shift by: Cut", "Shift by: Copy", initial=False)
        toggles.addWidget(self.dry_run_toggle)
        toggles.addWidget(self.parallel_toggle)
        toggles.addWidget(self.shift_toggle)

        layout.addLayout(toggles)


        # Multi-select dropdown
        self.multi_select = MultiSelectComboBox(multi_select_items)
        layout.addWidget(QLabel("Fiter Extensions:", self))
        layout.addWidget(self.multi_select)


    def toggle(self):
        self.setVisible(not self.isVisible())
