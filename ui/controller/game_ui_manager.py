from typing import Callable

from PyQt5.QtWidgets import QStackedWidget

from ui.main_menu import MainMenu
from ui.settings import Settings


class GameUIManager(QStackedWidget):

    def __init__(self, quit_callback:Callable):
        super().__init__()

        self.menu = MainMenu(start_game_callback=self.start_game,
                             settings_callback=self.open_settings,
                             quit_callback=quit_callback)
        self.settings = Settings(back_callback=self.back_to_menu)

        self.addWidget(self.menu)
        self.addWidget(self.settings)

        self.setMinimumSize(900, 600)
        self.setMaximumSize(1920, 1080)
        self.setWindowTitle("Spinner game")


    def start_game(self) -> None:
        self.menu.hide()


    def open_settings(self) -> None:
        self.menu.hide()
        self.setCurrentWidget(self.settings)

    
    def back_to_menu(self) -> None:
        self.settings.hide()
        self.setCurrentWidget(self.menu)