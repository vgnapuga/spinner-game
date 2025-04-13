from typing import Callable

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class MainMenu(QWidget):
    
    def __init__(self, start_game_callback:Callable, settings_callback:Callable, quit_callback:Callable):
        super().__init__()

        self.setWindowTitle("Главное меню")

        self.start_button = QPushButton("Начать игру")
        self.settings_button = QPushButton("Настройки")
        self.quit_button = QPushButton("Выход")

        self.start_button.clicked.connect(start_game_callback)
        self.settings_button.clicked.connect(settings_callback)
        self.quit_button.clicked.connect(quit_callback)

        self.lyt = QVBoxLayout()
        self.lyt.addWidget(self.start_button)
        self.lyt.addWidget(self.settings_button)
        self.lyt.addWidget(self.quit_button)

        self.setLayout(self.lyt)