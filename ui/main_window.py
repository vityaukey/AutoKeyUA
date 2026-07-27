from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "AutoKeyUA"
        )

        self.resize(
            600,
            500
        )

        self.create_ui()


    def create_ui(self):

        central = QWidget()

        layout = QVBoxLayout()


        title = QLabel(
            "AutoKeyUA\nМайстерня ключів"
        )

        title.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(title)


        buttons = [
            "🔑 Каталог ключів",
            "👥 Клієнти",
            "🚗 Автомобілі",
            "📦 Склад",
            "📋 Замовлення",
            "💰 Каса",
            "⚙ Налаштування"
        ]


        for text in buttons:

            button = QPushButton(text)

            button.setMinimumHeight(
                40
            )

            layout.addWidget(button)


        central.setLayout(
            layout
        )

        self.setCentralWidget(
            central
        )