from typing import Callable

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from ui.styles import CssStyle


class MainMenu(QWidget):

    def __init__(
            self,
            start_game_callback: Callable,
            settings_callback: Callable,
            quit_callback: Callable,
            ):
        super().__init__()

        self._widgets: list[QWidget] = []

        self.setup_buttons(
            start_game_callback,
            settings_callback,
            quit_callback,
            )

        layout: QVBoxLayout = QVBoxLayout()
        layout.setContentsMargins(200, 200, 200, 200)

        for widget in self._widgets:
            widget.setFixedHeight(80)
            CssStyle.apply_font_size(widget)

            layout.addWidget(widget)

        self.setLayout(layout)

    def setup_buttons(
            self,
            start_game_callback: Callable,
            settings_callback: Callable,
            quit_callback: Callable
            ) -> None:
        start_button: QPushButton = QPushButton("Начать игру")
        settings_button: QPushButton = QPushButton("Настройки")
        quit_button: QPushButton = QPushButton("Выход")

        start_button.clicked.connect(start_game_callback)
        settings_button.clicked.connect(settings_callback)
        quit_button.clicked.connect(quit_callback)

        self._widgets.append(start_button)
        self._widgets.append(settings_button)
        self._widgets.append(quit_button)