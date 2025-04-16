from typing import Callable

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class MainMenu(QWidget):
    
    def __init__(self, start_game_callback:Callable,
                 settings_callback:Callable, quit_callback:Callable):
        super().__init__()

        self.__widgets:list[QWidget] = []

        self.setup_buttons(start_game_callback, settings_callback, quit_callback)

        self.lyt:QVBoxLayout = QVBoxLayout()
        self.lyt.setSpacing(10)
        self.lyt.setContentsMargins(200, 200, 200, 200)

        for widget in self.__widgets:
            widget.setFixedHeight(80)
            widget.setStyleSheet("font-size: 30px;")
            
            self.lyt.addWidget(widget)

        self.setLayout(self.lyt)

    def setup_buttons(self, start_game_callback:Callable,
                         settings_callback:Callable, quit_callback:Callable) -> None:
        self.start_button:QPushButton = QPushButton("Начать игру")
        self.settings_button:QPushButton = QPushButton("Настройки")
        self.quit_button:QPushButton = QPushButton("Выход")

        self.start_button.clicked.connect(start_game_callback)
        self.settings_button.clicked.connect(settings_callback)
        self.quit_button.clicked.connect(quit_callback)

        self.__widgets.append(self.start_button)
        self.__widgets.append(self.settings_button)
        self.__widgets.append(self.quit_button)