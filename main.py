import sys
import os

from PyQt5.QtWidgets import QApplication

from logic.game_engine import GameEngine
from ui.controller.game_ui_manager import GameUIManager


def main() -> None:
    app: QApplication = QApplication(sys.argv)
    window: GameUIManager = GameUIManager(quit_callback=quit_application)
    window.show()
    sys.exit(app.exec_())


def quit_application() -> None:
    QApplication.quit()


if (__name__ == "__main__"):
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = ".venv/lib/python3.12/site-packages/PyQt5/Qt5/plugins"
    main()