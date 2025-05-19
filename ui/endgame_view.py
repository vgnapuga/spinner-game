from typing import Callable
from enum import IntEnum

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

from ui.styles import CssStyle


class WidgetIndex(IntEnum):

    SCORE_FIELD = 0
    BUTTON_MENU = 1


class EndgameView(QWidget):

    
    def __init__(
            self,
            menu_callback: Callable,
            score: int,
            ):
        super().__init__()

        self._widgets: list[QWidget] = []

        self.setup_score_field(score)
        self.setup_menu_button(menu_callback)

        CssStyle.apply_font_size(self._widgets)

        layout: QVBoxLayout = QVBoxLayout()
        layout.setContentsMargins(500, 400, 500, 400)

        for widget in self._widgets:
            layout.addWidget(widget)

        self.setLayout(layout)


    def setup_score_field(self, score: int) -> None:
        score_field: QLabel = QLabel()
        score_field.setText(f"Счёт: {score}")

        self._widgets.append(score_field)


    def setup_menu_button(self, menu_callback: Callable) -> None:
        button_menu: QPushButton = QPushButton("Меню")
        button_menu.clicked.connect(menu_callback)

        button_menu.setFixedHeight(80)

        self._widgets.append(button_menu)