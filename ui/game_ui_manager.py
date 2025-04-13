from typing import Callable

from PyQt5.QtWidgets import QStackedWidget

from ui.main_menu import MainMenu
from ui.settings import Settings


class GameUIManager(QStackedWidget):

    def __init__(self, start_game_callback:Callable, settings_callback:Callable,
                 quit_callback:Callable, back_callback:Callable):
        super().__init__()

        self.menu = MainMenu(start_game_callback, settings_callback, quit_callback)
        self.settings = Settings(back_callback)

        self.addWidget(self.menu)
        self.addWidget(self.settings)

        self.setFixedSize(900, 600)
        self.setWindowTitle("Spinner game")