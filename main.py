import sys

from PyQt5.QtWidgets import QApplication

from logic.game_engine import GameEngine
from ui.game_ui_manager import GameUIManager


def start_game() -> None:
    print("game")


def open_settings() -> None:
    print("settings")


def quit_application() -> None:
    QApplication.quit()


def return_to_menu() -> None:
    print("back")


def main() -> None:
    engine:GameEngine = GameEngine()

    app = QApplication(sys.argv)
    window = GameUIManager(start_game_callback=start_game,
                           settings_callback=open_settings,
                           quit_callback=quit_application,
                           back_callback=return_to_menu)
    window.show()
    sys.exit(app.exec_())


if (__name__ == "__main__"):
    main()