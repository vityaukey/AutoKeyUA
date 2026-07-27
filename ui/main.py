import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

from src.config import create_directories, load_config


def main():

    create_directories()

    load_config()

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()