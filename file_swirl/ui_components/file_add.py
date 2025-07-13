# file_add_component.py

from PyQt6.QtWidgets import (
    QFileDialog,
    QFrame,
    QGraphicsBlurEffect,
    QHBoxLayout,
    QLineEdit,
    QListWidget,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
)

from file_swirl.ui_components.styles import (
    ADD_BUTTON_STYLE,
    ADD_BUTTON_STYLE_PURPLE,
    FOLDER_LIST_STYLE,
    REMOVE_BUTTON_STYLE,
    SUB_WINDOW_PURPLE,
)


class FileAddComponent:
    """
    File dialog box
    """
    def __init__(self):
        self.folder_paths = set()
        self.folder_list = QListWidget()
        self.output_folder_path = ''
        self.output_folder_label = QLineEdit("Select a output folder")
        self.output_folder_label.setReadOnly(True)
        self.output_folder_label.setFixedHeight(35)
        self.output_folder_label.setStyleSheet("""
            QLineEdit {
                color: #9bb5ff;
                font-size: 14px;
                font-weight: bold;
                background: transparent;
                border: none;
            }"""
        )
        self.folders_count = QLineEdit("input folders: 0")
        self.folders_count.setStyleSheet("""
            QLineEdit {
                color: #9bb5ff;
                font-size: 14px;
                font-weight: bold;
                background: transparent;
                border: none;
            }"""
        )

    def build_old(self) -> QFrame:
        frame = QFrame()

        frame.setStyleSheet(SUB_WINDOW_PURPLE)
        frame.setFixedHeight(350)
        layout = QVBoxLayout(frame)

        header = QHBoxLayout()
        header.setSpacing(10)  # Add consistent spacing
        output_folder_button = QPushButton("📁 Swirl files to")
        output_folder_button.setFixedHeight(35)
        output_folder_button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        # output_folder_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        output_folder_button.setStyleSheet(ADD_BUTTON_STYLE)
        output_folder_button.clicked.connect(self.select_output_folder)

        header.addWidget(output_folder_button)
        header.addWidget(self.output_folder_label)
        # header.addStretch()

        layout.addLayout(header)

        self.folder_list.setFixedHeight(150)
        self.folder_list.setStyleSheet(FOLDER_LIST_STYLE)
        layout.addWidget(self.folders_count)
        layout.addWidget(self.folder_list)

        buttons = QHBoxLayout()

        add_button = QPushButton("+ Add Folder")
        # add_button.setFixedHeight(35)  # Set consistent height
        add_button.setStyleSheet(ADD_BUTTON_STYLE_PURPLE)
        add_button.clicked.connect(self.add_folder)
        buttons.addWidget(add_button)

        remove_button = QPushButton("🗑 Remove Selected")
        # remove_button.setFixedHeight(35)  # Set consistent height
        remove_button.setStyleSheet(REMOVE_BUTTON_STYLE)
        remove_button.clicked.connect(self.remove_selected_folder)
        buttons.addWidget(remove_button)

        layout.addLayout(buttons)


        return frame

    def build(self) -> QFrame:
        # Outer frame to hold blur + content
        outer_frame = QFrame()
        outer_frame.setFixedHeight(350)

        # Use absolute positioning to overlay content on background
        outer_frame.setStyleSheet("QFrame { background-color: transparent; }")

        # Blurred background frame
        blurred_bg = QFrame(outer_frame)
        blurred_bg.setGeometry(0, 0, outer_frame.width(), outer_frame.height())
        blurred_bg.setStyleSheet("""
            QFrame {
                background-color: rgba(45, 55, 85, 0.5);
                border: 2px dashed rgba(120, 143, 184, 0.2);
                border-radius: 10px;
            }
        """)
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(10)
        blurred_bg.setGraphicsEffect(blur)

        # Main content frame with transparent background
        content_frame = QFrame(outer_frame)
        content_frame.setGeometry(0, 0, outer_frame.width(), outer_frame.height())
        content_frame.setStyleSheet("""
            QFrame {
                background-color: transparent;
            }
        """)

        content_layout = QVBoxLayout(content_frame)
        content_layout.setContentsMargins(15, 15, 15, 15)

        # Header row
        header = QHBoxLayout()
        output_folder_button = QPushButton("📁 Swirl files to")
        output_folder_button.setFixedHeight(35)
        output_folder_button.setStyleSheet(ADD_BUTTON_STYLE_PURPLE)
        output_folder_button.clicked.connect(self.select_output_folder)

        header.addWidget(output_folder_button)
        header.addWidget(self.output_folder_label)
        content_layout.addLayout(header)

        # Folder list
        self.folder_list.setFixedHeight(150)
        self.folder_list.setStyleSheet(FOLDER_LIST_STYLE)
        content_layout.addWidget(self.folders_count)
        content_layout.addWidget(self.folder_list)

        # Action buttons
        buttons = QHBoxLayout()
        add_button = QPushButton("+ Add Folder")
        add_button.setStyleSheet(ADD_BUTTON_STYLE_PURPLE)
        add_button.clicked.connect(self.add_folder)

        remove_button = QPushButton("🗑 Remove Selected")
        remove_button.setStyleSheet(REMOVE_BUTTON_STYLE)
        remove_button.clicked.connect(self.remove_selected_folder)

        buttons.addWidget(add_button)
        buttons.addWidget(remove_button)
        content_layout.addLayout(buttons)

        # Handle resize events to keep frames aligned
        def resizeEvent(event):
            blurred_bg.setGeometry(0, 0, outer_frame.width(), outer_frame.height())
            content_frame.setGeometry(0, 0, outer_frame.width(), outer_frame.height())

        outer_frame.resizeEvent = resizeEvent

        return outer_frame


    def add_folder(self):
        """
        Open folder dialog to select folder
        """
        folder = QFileDialog.getExistingDirectory()
        if folder and folder not in self.folder_paths:
            self.folder_paths.add(folder)
            self.folder_list.addItem(folder)
            self.folders_count.setText(f"Selected: {len(self.folder_paths)}")

    def remove_selected_folder(self):
        for item in self.folder_list.selectedItems():
            path = item.text()
            if path in self.folder_paths:
                self.folder_paths.remove(path)
            self.folder_list.takeItem(self.folder_list.row(item))
        self.folders_count.setText(f"Selected: {len(self.folder_paths)}  ")

    def select_output_folder(self):
        self.output_folder_path = QFileDialog.getExistingDirectory()
        self.output_folder_label.setText(f"{self.output_folder_path[:50]}...")
