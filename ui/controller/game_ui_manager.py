from typing import Callable

from enum import IntEnum

from PyQt5.QtWidgets import QStackedWidget, QWidget

from ui.main_menu import MainMenu
from ui.game_view import GameView
from ui.settings import Settings
from ui.pause_view import PauseView


class ScreenIndex(IntEnum):

    MAIN_MENU = 0
    SETTINGS = 1
    GAME_VIEW = 2
    PAUSE_VIEW = 3


class GameUIManager(QStackedWidget):

    def __init__(
            self,
            quit_callback: Callable,
            ):
        super().__init__()

        self.setFixedSize(1920, 1080)
        self.setWindowTitle("Spinner game")

        self._widgets: list[QWidget] = []

        self.setup_main_menu(quit_callback)
        self.setup_settings()
        self.setup_game_view()
        self.setup_pause_view()

        for widget in self._widgets:
            self.addWidget(widget)


    def setup_main_menu(self, quit_callback: Callable) -> None:
        menu = MainMenu(
            start_game_callback=self.start_game,
            settings_callback=self.open_settings,
            quit_callback=quit_callback
            )
        
        self._widgets.append(menu)


    def setup_settings(self,) -> None:
        settings = Settings(menu_callback=self.back_to_menu)

        self._widgets.append(settings)


    def setup_game_view(self) -> None:
        game = GameView(
            pause_callback=self.open_pause,
            is_time_limit=self._widgets[ScreenIndex.SETTINGS].is_time_limit,
            is_turn_limit=self._widgets[ScreenIndex.SETTINGS].is_turn_limit,
            )
        
        self._widgets.append(game)


    def setup_pause_view(self) -> None:
        pause = PauseView(
            back=self.back_to_game,
            menu_callback=self.back_to_menu,
            )
        
        self._widgets.append(pause)


    def start_game(self) -> None:
        settings: QWidget = self._widgets[ScreenIndex.SETTINGS]

        if (self._widgets[ScreenIndex.GAME_VIEW] == None):
            game = GameView(
                pause_callback=self.open_pause,
                is_time_limit=settings.is_time_limit,
                is_turn_limit=settings.is_turn_limit,
            )

            self._widgets[ScreenIndex.GAME_VIEW] = game
            self.addWidget(game)

        self.setCurrentWidget(self._widgets[ScreenIndex.GAME_VIEW])


    def open_settings(self) -> None:
        settings: QWidget = self._widgets[ScreenIndex.SETTINGS]

        self.setCurrentWidget(settings)


    def back_to_menu(self) -> None:
        if (not self._widgets[ScreenIndex.GAME_VIEW] == None):
            self.removeWidget(self._widgets[ScreenIndex.GAME_VIEW])
            self._widgets[ScreenIndex.GAME_VIEW].deleteLater()
            self._widgets[ScreenIndex.GAME_VIEW] = None

        self.setCurrentWidget(self._widgets[ScreenIndex.MAIN_MENU])


    def open_pause(self) -> None:
        pause: QWidget = self._widgets[ScreenIndex.PAUSE_VIEW]

        self.setCurrentWidget(pause)


    def back_to_game(self) -> None:
        game: QWidget = self._widgets[ScreenIndex.GAME_VIEW]

        self.setCurrentWidget(game)