"""
Main code where it calls cli code
"""
import sys

from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from file_swirl.constants import FILE_EXTENSIONS
from file_swirl.file_sorter import FileSorter
from file_swirl.ui_components import (
    CLIOutputViewer,
    FileTreeComponent,
    ProgressComponent,
    SettingsPanelComponent,
    SortLevelComponent,
)
from file_swirl.ui_components.file_add import FileAddComponent
from file_swirl.ui_components.styles import (
    MAIN_WINDOW_PURPLE,
    START_BUTTON_STYLE_PURPLE,
)
from file_swirl.utils import convert_size


class FolderSwirlUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("\ud83d\udcc1 Folder Swirl")
        self.setGeometry(100, 100, 1400, 800)
        self.setStyleSheet(MAIN_WINDOW_PURPLE)

        self.file_add_component = FileAddComponent()
        self.sort_level_component = SortLevelComponent()
        self.file_tree_component = FileTreeComponent()
        self.file_tree_component.tree_updated.connect(self.on_tree_updated)
        self.progress_component = ProgressComponent()
        self.settings_panel = SettingsPanelComponent(multi_select_items=sorted(FILE_EXTENSIONS))
        self.console_view = CLIOutputViewer()

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(20)

        title = QLabel("\ud83d\udcc1 Folder Swirl - A fast, flexible file organizer")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #9bb5ff;
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        """)
        main_layout.addWidget(title)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(30)

        # Left Column (Folder Add + Sort Levels)
        left_column = QVBoxLayout()
        left_column.setSpacing(20)
        left_column.addWidget(self.file_add_component.build())
        left_column.addWidget(self.sort_level_component.build())
        content_layout.addLayout(left_column, 1)

        # Right Column (Tree + Progress)
        right_column = QVBoxLayout()
        right_column.setSpacing(20)
        right_column.addWidget(self.file_tree_component.build())
        # right_column.addWidget(self.progress_component.build())
        right_column.addWidget(self.console_view.build())
        content_layout.addLayout(right_column, 2)

        main_layout.addLayout(content_layout)

        # Horizontal layout for Start and Settings buttons
        button_row = QHBoxLayout()

        # Start Button
        self.start_button = QPushButton("▶ Start Swirl")
        self.start_button.setStyleSheet(START_BUTTON_STYLE_PURPLE)
        self.start_button.clicked.connect(self.run_file_swirl)
        button_row.addWidget(self.start_button)

        # Add spacing between Start and Settings if desired
        button_row.addSpacing(50)

        # Settings Button
        self.settings_button = QPushButton("⚙")
        # self.settings_button.setStyleSheet("padding: 8px 16px;")
        self.settings_button.setFixedSize(40, 40)  # Equal width and height
        self.settings_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(130, 130, 130, 0.2);
                color: white;
                border: 2px solid rgba(180, 180, 180, 0.4);
                border-radius: 20px;  /* Half of width/height for perfect circle */
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(160, 160, 160, 0.3);
                border-color: rgba(200, 200, 200, 0.5);
            }
            QPushButton:pressed {
                background-color: rgba(100, 100, 100, 0.3);
                border-color: rgba(150, 150, 150, 0.6);
            }
        """)
        self.settings_button.clicked.connect(self.settings_panel.toggle)
        button_row.addWidget(self.settings_button)

        # Optional: Align the button group to center or right
        button_row.addStretch()  # Push buttons to the left
        # or use: button_row.setAlignment(Qt.AlignmentFlag.AlignRight) if you want both on right

        # Add the row to main layout
        main_layout.addLayout(button_row)



    def reset_ui(self):
        self.console_view.console.clear()
        self.file_tree_component.clear_tree()

    @pyqtSlot()
    def on_tree_updated(self):
        print("Tree completed")
        total_size_bytes = sum(self.file_tree_component.top_folder_sizes.values())
        item = self.file_tree_component.tree_widget.topLevelItem(0)
        item.setText(1, convert_size(total_size_bytes))

    def run_file_swirl(self):
        """
        Triggered by 'Start Swirl' button.
        Simulate the process or connect your actual logic here.
        """

        # prepare cli
        self.reset_ui()
        self.start_button.setEnabled(False)

        args = [
            "-m", "file_swirl.cli",
            "--input_paths", *self.file_add_component.folder_paths,
            "--output_path", self.file_add_component.output_folder_path,
        ]
        if self.sort_level_component.selected_items:
            args += ['--nested_order', *self.sort_level_component.selected_items]


        if self.settings_panel.parallel_toggle.isChecked():
            args += ['--process_type', 'parallel']

        # Shift Type
        shift_type = self.settings_panel.shift_toggle.isChecked() # e.g., "copy", "move"
        if shift_type:
            args += ['--shift_type', "move"]

        if self.settings_panel.dry_run_toggle.isChecked():
            args += ['--dry_run', "True"]

        items = self.settings_panel.multi_select.selected_items()
        if items:
            args += ['--file_extensions', *items]

        self.console_view.process.start(sys.executable, args)

        # Simulate tree output
        self.file_tree_component.populate_tree(folder_paths=[self.file_add_component.output_folder_path])
        self.start_button.setEnabled(True)
