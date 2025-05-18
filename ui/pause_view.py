from typing import Callable

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

from ui.styles.css_style import CssStyle


class PauseView(QWidget):

    def __init__(
            self,
            back: Callable,
            menu_callback: Callable,
            ):
        super().__init__()

        self._widgets: list[QWidget] = []

        self.setup_buttons(back, menu_callback)

        layout: QVBoxLayout = QVBoxLayout()
        layout.setContentsMargins(200, 200, 200, 200)

        for widget in self._widgets: 
            widget.setFixedHeight(80)
            CssStyle.apply_font_size(widget)

            layout.addWidget(widget)

        self.setLayout(layout)


    def setup_buttons(self, back: Callable, menu_callback: Callable) -> None:
        button_back: QPushButton = QPushButton("Назад")
        button_menu: QPushButton = QPushButton("В меню")

        button_back.clicked.connect(back)
        button_menu.clicked.connect(menu_callback)

        self._widgets.append(button_back)
        self._widgets.append(button_menu)