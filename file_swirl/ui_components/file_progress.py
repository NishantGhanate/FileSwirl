# progress_component.py
from PyQt6.QtWidgets import QFrame, QLabel, QProgressBar, QVBoxLayout


class ProgressComponent:

    def __init__(self):
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #2e2e3e;
                border-radius: 8px;
                text-align: center;
                color: white;
                background-color: #1e1e2f;
                height: 20px;
            }
            QProgressBar::chunk {
                background-color: #4c8aff;
                border-radius: 8px;
            }
        """)

        self.status_label = QLabel("Ready")
        self.status_label.setStyleSheet("color: #888; font-size: 12px;")

    def build(self) -> QFrame:
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label)
        return frame

    def update_progress(self, percent: int):
        self.progress_bar.setValue(percent)

    def update_status(self, message: str):
        self.status_label.setText(message)

    def reset(self):
        self.progress_bar.setValue(0)
        self.status_label.setText("Ready")
