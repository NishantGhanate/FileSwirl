FOLDER_LIST_STYLE = """
    QListWidget {
        background-color: #1e1e2f;
        color: #dcdcdc;
        border: 1px solid #2e2e3e;
        border-radius: 8px;
        padding: 6px;
        font-size: 13px;
    }
    QListWidget::item {
        padding: 10px;
        margin: 4px;
        border-radius: 6px;
    }
    QListWidget::item:hover {
        background-color: #2d2d40;
        color: #ffffff;
    }
    QListWidget::item:selected {
        background-color: #4c8aff;
        color: white;
    }
    QScrollBar:vertical {
        background-color: #1e1e2f;
        width: 10px;
        margin: 0px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical {
        background-color: #3a3a5c;
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical:hover {
        background-color: #55558c;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
"""

ADD_BUTTON_STYLE = """
    QPushButton {
        background-color: rgba(75, 100, 140, 0.8);
        color: #e0e6ff;
        border: 1px solid rgba(120, 143, 184, 0.3);
        border-radius: 8px;
        padding: 8px;
        font-size: 12px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: rgba(85, 115, 160, 0.9);
        border-color: rgba(120, 143, 184, 0.5);
    }
    QPushButton:pressed {
        background-color: rgba(65, 85, 120, 0.9);
    }
"""

ADD_BUTTON_STYLE_PURPLE = """
    QPushButton {
        background-color: rgba(100, 100, 100, 0.2);  /* semi-transparent grey */
        color: #d0d0d0;
        border: 1px solid rgba(160, 160, 160, 0.3);
        border-radius: 8px;
        padding: 12px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: rgba(130, 130, 130, 0.25);
        border-color: rgba(200, 200, 200, 0.4);
    }
    QPushButton:pressed {
        background-color: rgba(80, 80, 80, 0.3);
    }
"""


REMOVE_BUTTON_STYLE = """
 QPushButton {
        background-color: rgba(200, 70, 70, 0.8);
        color: #fff;
        border: 1px solid rgba(255, 120, 120, 0.3);
        border-radius: 8px;
        padding: 12px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: rgba(220, 90, 90, 0.9);
        border-color: rgba(255, 150, 150, 0.5);
    }
    QPushButton:pressed {
        background-color: rgba(180, 50, 50, 0.9);
    }
"""

FILE_TREE = """
    QTreeWidget {
        background-color: #1e1e2f;
        color: #dcdcdc;
        border: 1px solid #2e2e3e;
        border-radius: 8px;
        font-size: 13px;
        padding: 6px;
    }

    QTreeView::item {
        padding: 8px;
        border-radius: 6px;
    }

    QTreeView::item:selected {
        background-color: #4c8aff;
        color: white;
    }

    QTreeView::item:hover {
        background-color: #2d2d40;
        color: white;
    }

    QHeaderView::section {
        background-color: #2a2a40;
        color: #9bb5ff;
        padding: 6px;
        border: none;
        font-weight: bold;
    }

    QScrollBar:vertical {
        background-color: #1e1e2f;
        width: 10px;
        margin: 0px;
        border-radius: 5px;
    }

    QScrollBar::handle:vertical {
        background-color: #3a3a5c;
        min-height: 20px;
        border-radius: 5px;
    }

    QScrollBar::handle:vertical:hover {
        background-color: #55558c;
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
"""

START_BUTTON = """
    QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #4a6cd4, stop:1 #6b8ce8);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 15px 30px;
        font-size: 16px;
        font-weight: bold;
        min-width: 200px;
    }
    QPushButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #5a7ce4, stop:1 #7b9cf8);
    }
    QPushButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #3a5cc4, stop:1 #5b7cd8);
    }
"""

START_BUTTON_STYLE_PURPLE = """
   QPushButton {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #6a0dad, stop:1 #9b4de0);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px 30px;
        font-size: 16px;
        font-weight: bold;
        min-width: 200px;
        letter-spacing: 0.5px;
    }
    QPushButton:hover {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #7e2fe0, stop:1 #b16eff);
    }
    QPushButton:pressed {
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #591c9e, stop:1 #8a3bd4);
    }
"""

MAIN_WINDOW = """
    QMainWindow {
        background: qlineargradient(
            x1:0, y1:0, x2:1, y2:1,
            stop:0 #1a1a2e, stop:0.5 #16213e, stop:1 #0f3460
        );
    }
"""
MAIN_WINDOW_PURPLE = """
    QMainWindow {
        background-color: qlineargradient(
            x1:0, y1:0, x2:1, y2:1,
            stop:0 #2e005f, stop:0.5 #4b0082, stop:1 #6a0dad
        );
    }
"""

SUB_WINDOW_PURPLE = """
    QFrame {
        background-color: rgba(30, 30, 60, 0.5); /* darker, more neutral base */
        border: 1.5px dashed rgba(180, 200, 255, 0.15); /* softer dashed border */
        border-radius: 12px;
        padding: 16px;
    }
"""

SUB_WINDOW_BLUE  ="""
    QFrame {
        background-color: rgba(45, 55, 85, 0.6);
        border: 2px dashed rgba(120, 143, 184, 0.3);
        border-radius: 10px;
        padding: 20px;
    }
"""

SCROLL_AREA_STYLE = """
QScrollArea {
    background-color: transparent;
    border: none;
}

QScrollBar:vertical {
    background: rgba(30, 30, 47, 0.4);
    width: 10px;
    margin: 2px;
    border-radius: 5px;
}

QScrollBar::handle:vertical {
    background: rgba(100, 100, 140, 0.6);
    border-radius: 5px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background: rgba(130, 130, 170, 0.8);
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
    background: none;
    border: none;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: none;
}
"""

SORT_LEVEL_BLUE = """
    QLabel {
        color: white;
        font-size: 14px;
    }
    QComboBox {
        background-color: #2b2d42;
        color: #f0f0f0;
        border-radius: 6px;
        padding: 6px;
        min-width: 120px;
    }
    QPushButton {
        background-color: rgba(200, 70, 70, 0.8);
        color: #fff;
        border: 1px solid rgba(255, 120, 120, 0.3);
        border-radius: 6px;
        font-size: 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: rgba(220, 90, 90, 0.9);
        border-color: rgba(255, 150, 150, 0.5);
    }
    QPushButton:pressed {
        background-color: rgba(180, 50, 50, 0.9);
    }
"""

SORT_LEVEL_PURPLE = """
    QLabel {
        color: #d0d0d0;
        font-size: 13px;
    }

    QComboBox {
        background-color: rgba(60, 65, 90, 0.8);
        color: #f0f0f0;
        border-radius: 6px;
        padding: 4px 10px;
        font-size: 13px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    QPushButton {
        background-color: rgba(200, 70, 70, 0.8);
        color: #fff;
        border: 1px solid rgba(255, 120, 120, 0.3);
        border-radius: 6px;
        font-size: 14px;
        font-weight: bold;
    }

    QPushButton:hover {
        background-color: rgba(220, 90, 90, 0.9);
        border-color: rgba(255, 150, 150, 0.5);
    }

    QPushButton:pressed {
        background-color: rgba(180, 50, 50, 0.9);
    }
"""

LEVEL_PURPLE = """
QLabel {
    color: #e0e0e0;
    font-size: 13px;
    font-weight: bold;
    padding: 6px 12px;
    background-color: rgba(90, 100, 120, 0.2);  /* Slight bluish-grey tint */
    border: 1px solid rgba(200, 200, 255, 0.08);
    border-radius: 6px;
}
"""

KEY_BOX = """
    QComboBox {
        background-color: rgba(40, 45, 65, 0.8);
        color: #f0f0f0;
        border-radius: 6px;
        padding: 6px 12px;
        font-size: 13px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 20px;
        border-left: 1px solid rgba(255, 255, 255, 0.05);
    }

    QComboBox::down-arrow {
        /* image: url(:/icons/chevron-down.svg);   Optional: custom arrow */
        width: 12px;
        height: 12px;
    }

    QComboBox QAbstractItemView {
        background-color: #1e1e2e;
        color: #ffffff;
        selection-background-color: #4c8aff;
        border: none;
        padding: 4px;
    }
"""
