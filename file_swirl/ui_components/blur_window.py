from typing import List, Optional, Union

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGraphicsBlurEffect
from PyQt5.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class BlurContainer(QFrame):
    """
    A reusable container component with blur background effect that can hold any widgets.
    """

    def __init__(self,
                 height: int = 350,
                 background_color: str = "rgba(45, 55, 85, 0.5)",
                 border_color: str = "rgba(120, 143, 184, 0.2)",
                 border_radius: int = 10,
                 blur_radius: int = 10,
                 content_padding: int = 15,
                 use_blur: bool = True):
        """
        Initialize the blur container.

        Args:
            height: Fixed height of the container
            background_color: Background color (supports rgba)
            border_color: Border color (supports rgba)
            border_radius: Corner radius in pixels
            blur_radius: Blur effect radius
            content_padding: Internal padding for content
            use_blur: Whether to apply blur effect
        """
        super().__init__()
        self.height = height
        self.background_color = background_color
        self.border_color = border_color
        self.border_radius = border_radius
        self.blur_radius = blur_radius
        self.content_padding = content_padding
        self.use_blur = use_blur

        self.content_layout = None
        self._setup_container()

    def _setup_container(self):
        """Setup the container structure."""
        self.setFixedHeight(self.height)

        if self.use_blur:
            self._setup_blur_container()
        else:
            self._setup_simple_container()

    def _setup_blur_container(self):
        """Setup container with blur effect."""
        self.setStyleSheet("QFrame { background-color: transparent; }")

        # Blurred background frame
        self.blurred_bg = QFrame(self)
        self.blurred_bg.setGeometry(0, 0, self.width(), self.height())
        self.blurred_bg.setStyleSheet(f"""
            QFrame {{
                background-color: {self.background_color};
                border: 2px dashed {self.border_color};
                border-radius: {self.border_radius}px;
            }}
        """)

        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(self.blur_radius)
        self.blurred_bg.setGraphicsEffect(blur)

        # Content frame
        self.content_frame = QFrame(self)
        self.content_frame.setGeometry(0, 0, self.width(), self.height())
        self.content_frame.setStyleSheet("QFrame { background-color: transparent; }")

        self.content_layout = QVBoxLayout(self.content_frame)
        self.content_layout.setContentsMargins(self.content_padding, self.content_padding,
                                              self.content_padding, self.content_padding)

    def _setup_simple_container(self):
        """Setup container without blur effect."""
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {self.background_color.replace('0.5', '0.8')};
                border: 2px dashed {self.border_color.replace('0.2', '0.4')};
                border-radius: {self.border_radius}px;
            }}
        """)

        self.content_layout = QVBoxLayout(self)
        self.content_layout.setContentsMargins(self.content_padding, self.content_padding,
                                              self.content_padding, self.content_padding)

    def add_widget(self, widget: QWidget):
        """Add a widget to the container."""
        if self.content_layout:
            self.content_layout.addWidget(widget)

    def add_layout(self, layout):
        """Add a layout to the container."""
        if self.content_layout:
            self.content_layout.addLayout(layout)

    def add_widgets(self, widgets: List[QWidget]):
        """Add multiple widgets to the container."""
        for widget in widgets:
            self.add_widget(widget)

    def add_stretch(self, stretch: int = 0):
        """Add stretch to the container layout."""
        if self.content_layout:
            self.content_layout.addStretch(stretch)

    def set_spacing(self, spacing: int):
        """Set spacing between widgets."""
        if self.content_layout:
            self.content_layout.setSpacing(spacing)

    def clear_content(self):
        """Clear all content from the container."""
        if self.content_layout:
            while self.content_layout.count():
                child = self.content_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    def resizeEvent(self, event):
        """Handle resize events to keep frames aligned."""
        super().resizeEvent(event)
        if self.use_blur and hasattr(self, 'blurred_bg') and hasattr(self, 'content_frame'):
            self.blurred_bg.setGeometry(0, 0, self.width(), self.height())
            self.content_frame.setGeometry(0, 0, self.width(), self.height())


# Example usage and factory functions
class BlurContainerFactory:
    """Factory class for creating common blur container variants."""

    @staticmethod
    def create_folder_selector(output_folder_label, folders_count, folder_list,
                             select_output_folder_callback, add_folder_callback,
                             remove_selected_folder_callback,
                             add_button_style, remove_button_style):
        """Create a folder selector blur container."""
        container = BlurContainer(height=350)

        # Header row
        header = QHBoxLayout()
        output_folder_button = QPushButton("📁 Swirl files to")
        output_folder_button.setFixedHeight(35)
        output_folder_button.setStyleSheet(add_button_style)
        output_folder_button.clicked.connect(select_output_folder_callback)

        header.addWidget(output_folder_button)
        header.addWidget(output_folder_label)
        container.add_layout(header)

        # Folder list
        folder_list.setFixedHeight(150)
        container.add_widget(folders_count)
        container.add_widget(folder_list)

        # Action buttons
        buttons = QHBoxLayout()
        add_button = QPushButton("+ Add Folder")
        add_button.setStyleSheet(add_button_style)
        add_button.clicked.connect(add_folder_callback)

        remove_button = QPushButton("🗑 Remove Selected")
        remove_button.setStyleSheet(remove_button_style)
        remove_button.clicked.connect(remove_selected_folder_callback)

        buttons.addWidget(add_button)
        buttons.addWidget(remove_button)
        container.add_layout(buttons)

        return container

    @staticmethod
    def create_simple_card(title: str = "", height: int = 200):
        """Create a simple card container."""
        container = BlurContainer(height=height, use_blur=False)

        if title:
            title_label = QLabel(title)
            title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")
            container.add_widget(title_label)

        return container

    @staticmethod
    def create_button_group(buttons_config: List[dict], height: int = 100):
        """
        Create a container with a horizontal group of buttons.

        Args:
            buttons_config: List of dicts with keys: 'text', 'style', 'callback'
            height: Container height
        """
        container = BlurContainer(height=height)

        buttons_layout = QHBoxLayout()
        for config in buttons_config:
            button = QPushButton(config['text'])
            button.setStyleSheet(config.get('style', ''))
            if 'callback' in config:
                button.clicked.connect(config['callback'])
            buttons_layout.addWidget(button)

        container.add_layout(buttons_layout)
        return container

if __name__ == "__man__":

    # Usage examples:

    # Example 1: Simple usage with individual widgets
    container = BlurContainer(height=300)
    container.add_widget(QPushButton("Click me"))
    container.add_widget(QLabel("Some text"))

    # Example 2: Using factory for folder selector
    # folder_container = BlurContainerFactory.create_folder_selector(
    #     output_folder_label, folders_count, folder_list,
    #     self.select_output_folder, self.add_folder, self.remove_selected_folder,
    #     ADD_BUTTON_STYLE_PURPLE, REMOVE_BUTTON_STYLE
    # )

    # Example 3: Custom styled container
    custom_container = BlurContainer(
        height=400,
        background_color="rgba(20, 30, 40, 0.7)",
        border_color="rgba(100, 150, 200, 0.3)",
        blur_radius=15,
        use_blur=True
    )
    custom_container.add_widget(QLabel("Custom Container"))

    # Example 4: Button group
    buttons_config = [
        {'text': 'Save', 'style': 'background-color: green;', 'callback': save_function},
        {'text': 'Cancel', 'style': 'background-color: red;', 'callback': cancel_function},
    ]
    button_container = BlurContainerFactory.create_button_group(buttons_config)

    # Example 5: Simple card without blur
    card = BlurContainerFactory.create_simple_card("My Card Title", height=250)
    card.add_widget(QLabel("Card content here"))
