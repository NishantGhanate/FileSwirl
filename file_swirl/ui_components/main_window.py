"""
Main code where it calls cli code
"""
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from file_swirl.file_sorter import FileSorter
from file_swirl.file_structs import ProcessType, ShiftType
from file_swirl.ui_components import (
    FileTreeComponent,
    ProgressComponent,
    SortLevelComponent,
)
from file_swirl.ui_components.file_add import FileAddComponent
from file_swirl.ui_components.styles import (
    MAIN_WINDOW_PURPLE,
    START_BUTTON_STYLE_PURPLE,
)


class FolderSwirlUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("\ud83d\udcc1 Folder Swirl")
        self.setGeometry(100, 100, 1400, 800)
        self.setStyleSheet(MAIN_WINDOW_PURPLE)

        self.file_add_component = FileAddComponent()
        self.sort_level_component = SortLevelComponent()
        self.file_tree_component = FileTreeComponent()
        self.progress_component = ProgressComponent()

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
        right_column.addWidget(self.progress_component.build())
        content_layout.addLayout(right_column, 2)

        main_layout.addLayout(content_layout)

        # Optional: add a Start button here to test
        # e.g., QPushButton("Start Swirl") connected to dummy slot
        start_button = QPushButton("▶ Start Swirl")
        start_button.setStyleSheet(START_BUTTON_STYLE_PURPLE)
        start_button.clicked.connect(self.run_file_swirl)  # Define this method

        main_layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def update_after_swirl(self):
        """
        Example method you can call after file swirl starts
        """
        self.progress_component.update_status("Swirl started...")
        self.progress_component.update_progress(0)
        self.file_tree_component.populate_tree(self.file_add_component.folder_paths)

    def reset_ui(self):
        self.progress_component.reset()
        self.file_tree_component.clear_tree()


    def run_file_swirl(self):
        """
        Triggered by 'Start Swirl' button.
        Simulate the process or connect your actual logic here.
        """

        # prepare cli
        print(self.file_add_component.folder_paths)
        print(self.file_add_component.output_folder_path)
        print(self.sort_level_component.selected_items)

        # file_sorter = FileSorter(
        #     input_folders=args.input_paths,
        #     output_folder=args.output_path,
        #     shift_type= args.shift_type,
        #     file_extensions= args.file_extensions,
        #     location=args.location,
        #     nested_order=args.nested_order,
        #     dry_run=True
        # )
        # file_sorter.process_files(
        #     process_type=ProcessType(args.process_type)
        # )


        self.progress_component.reset()
        self.progress_component.update_status("Swirling started...")
        self.progress_component.update_progress(25)

        # Simulate tree output
        self.file_tree_component.populate_tree(self.file_add_component.folder_paths)

        self.progress_component.update_progress(100)
        self.progress_component.update_status("Swirl complete!")
