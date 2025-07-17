"""
Component for cli view
"""

from PyQt6.QtCore import QProcess
from PyQt6.QtWidgets import QFrame, QTextEdit, QVBoxLayout, QWidget

from file_swirl.ui_components.styles import CONSOLE_VIEW


class CLIOutputViewer(QWidget):
    """
    console window
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CLI Output Console")
        self.resize(600, 400)


        self.console = QTextEdit()
        self.console.setStyleSheet(CONSOLE_VIEW)
        self.console.setReadOnly(True)

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

    def run_cli_script(self):
        self.console.clear()
        # Python interpreter and CLI script


    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.console.append(data)

    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        self.console.append(f"<span style='color:red;'>{data}</span>")

    def process_finished(self):
        self.console.append("✅ CLI process finished.")

    def build(self) -> QFrame:
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.addWidget(self.console)
        return frame
