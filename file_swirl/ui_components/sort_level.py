from copy import deepcopy

from PyQt6.QtCore import QPropertyAnimation, Qt
from PyQt6.QtWidgets import (
    QComboBox,
    QFrame,
    QGraphicsOpacityEffect,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from file_swirl.file_structs import NestedOrder
from file_swirl.ui_components.styles import (
    ADD_BUTTON_STYLE_PURPLE,
    KEY_BOX,
    LEVEL_PURPLE,
    SCROLL_AREA_STYLE,
    SORT_LEVEL_PURPLE,
)


class SortLevelWidget(QWidget):
    """
    Component to add nested level or organizing structure
    """
    def __init__(self, level=1, dop_down_items= ["Name", "Date", "Device", "Size"]):
        super().__init__()
        self.row_height = 32
        self.setStyleSheet(SORT_LEVEL_PURPLE)

        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(12)
        self.layout.setContentsMargins(8, 4, 8, 4)

        self.level_label = QLabel(f"Level {level}")
        self.level_label.setStyleSheet(LEVEL_PURPLE)
        self.level_label.setFixedHeight(self.row_height)
        self.level_label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.key_box = QComboBox()
        self.key_box.addItems(dop_down_items)
        self.key_box.setStyleSheet(KEY_BOX)
        self.key_box.setMinimumWidth(200)

        # self.key_box.setFixedSize(self.row_height)

        self.remove_level_button = QPushButton("✖")
        self.remove_level_button.setFixedSize(self.row_height, self.row_height)

        # Add widgets in a clean order
        self.layout.addWidget(self.level_label)
        self.layout.addWidget(self.key_box)

        self.layout.addStretch()
        self.layout.addWidget(self.remove_level_button)

    def get_config(self):
        return {
            "key": self.key_box.currentText()
        }

    @property
    def text(self) -> str:
        return self.key_box.currentText()

    def __str__(self):
        return f"SortLevel(key={self.key_box.currentText()})"

    def __repr__(self):
        return self.__str__()


class SortLevelComponent:

    def __init__(self) -> None:
        self.sort_levels = []
        self.sort_container = QVBoxLayout()

        self.dop_down_items = {e.value for e in NestedOrder}
        self.dop_down_set = deepcopy(self.dop_down_items)

    def build(self) -> QFrame:
        sort_frame = QFrame()
        outer_layout = QVBoxLayout(sort_frame)
        group_box = QGroupBox("Nested Sort Options")
        group_box.setStyleSheet("""
            QGroupBox {
                background-color: rgba(45, 55, 85, 0.4);
                border: 1px solid rgba(120, 143, 184, 0.3);
                border-radius: 8px;
                margin-top: 20px;
                padding: 12px;
            }

            QGroupBox:title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 6px;
                color: #9bb5ff;
                font-weight: bold;
                font-size: 13px;
                background-color: transparent;
            }
        """)
        self.group_layout = QVBoxLayout(group_box)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet(SCROLL_AREA_STYLE)
        scroll_area.setFixedHeight(230)

        scroll_widget = QWidget()
        scroll_widget.setLayout(self.sort_container)
        scroll_area.setWidget(scroll_widget)
        self.group_layout.addWidget(scroll_area)

        self.group_layout.addStretch()
        add_sort_button = QPushButton("+ Add Nested Level")
        add_sort_button.setStyleSheet(ADD_BUTTON_STYLE_PURPLE)
        add_sort_button.clicked.connect(self.add_sort_level)
        self.group_layout.addWidget(add_sort_button)

        outer_layout.addWidget(group_box)
        return sort_frame


    def add_sort_level(self) -> None:
        """
        Add the drop down row, remove the remove value to drop down
        """
        if not self.dop_down_set:
            return

        print(f"total: {self.dop_down_set}")
        level = len(self.sort_levels) + 1
        widget = SortLevelWidget(level= level, dop_down_items=self.dop_down_set)
        widget.remove_level_button.clicked.connect(lambda: self.remove_sort_level(widget))
        self.sort_levels.append(widget)
        print(f"Added : {widget.text}")
        self.dop_down_set.remove(widget.text)

        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        animation = QPropertyAnimation(effect, b"opacity")
        animation.setDuration(250)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start()

        widget._fade_in_animation = animation
        self.sort_container.addWidget(widget)

    def remove_sort_level(self, widget) -> None:
        """
        Remove the drop down row, add the remove value to drop down
        """
        def _finalize_removal():
            self.sort_container.removeWidget(widget)
            widget.deleteLater()
            self.reindex_sort_levels()

        # TODO: bug here
        index = self.sort_levels.index(widget)
        removed = self.sort_levels.pop(index)
        self.dop_down_set.add(removed.text)
        print(f"Adding back into set : {removed.text}")
        print(self.dop_down_set)

        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        animation = QPropertyAnimation(effect, b"opacity")
        animation.setDuration(200)
        animation.setStartValue(1.0)
        animation.setEndValue(0.0)
        animation.finished.connect(_finalize_removal)
        animation.start()



        widget._fade_out_animation = animation

    def reindex_sort_levels(self) -> None:
        """
        Update level labels after any removal
        """
        for i in range(self.sort_container.count()):
            item = self.sort_container.itemAt(i).widget()
            if item:
                label = item.findChild(QLabel)
                if label:
                    label.setText(f"Level {i + 1}")

    @property
    def selected_items(self):
        return  self.dop_down_items - self.dop_down_set
