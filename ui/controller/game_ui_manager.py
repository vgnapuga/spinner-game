from typing import Callable

from PyQt5.QtWidgets import QStackedWidget

from ui.main_menu import MainMenu
from ui.game_view import GameView
from ui.settings import Settings


class GameUIManager(QStackedWidget):

    def __init__(self, quit_callback:Callable):
        super().__init__()

        self.setFixedSize(1920, 1080)
        self.setWindowTitle("Spinner game")

        self.menu = MainMenu(start_game_callback=self.start_game,
                             settings_callback=self.open_settings,
                             quit_callback=quit_callback)
        self.game = GameView(back_callback=self.back_to_menu)
        self.settings = Settings(back_callback=self.back_to_menu)

        self.addWidget(self.menu)
        self.addWidget(self.game)
        self.addWidget(self.settings)


    def start_game(self) -> None:
        self.menu.hide()
        self.setCurrentWidget(self.game)


    def open_settings(self) -> None:
        self.menu.hide()
        self.setCurrentWidget(self.settings)

    
    def back_to_menu(self) -> None:
        self.currentWidget().hide()
        self.setCurrentWidget(self.menu)