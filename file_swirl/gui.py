import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

from file_swirl.ui_components.main_window import FolderSwirlUi


def main():
    """
    Main execution starts here
    """
    app = QApplication(sys.argv)

    # Set application style
    app.setStyle('Fusion')

    window = FolderSwirlUi()
    window.setWindowIcon(QIcon("assets/app_icon.png"))
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":

    main()
