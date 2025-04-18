from typing import Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout

from logic.game_engine import GameEngine
from logic.game_field import GameField


class GameView(QWidget):

    def __init__(self, pause_callback:Callable):
        super().__init__()

        self.engine:GameEngine = GameEngine()
        self.__widgets:list[QWidget] = []

        self.setup_table()
        self.setup_buttons(pause_callback)

        layout = QHBoxLayout()
        layout.setContentsMargins(500, 0, 420, 8)

        for widget in self.__widgets:
            widget.setStyleSheet("font-size: 30px;")

            layout.addWidget(widget)

        self.setLayout(layout)
        

    def setup_table(self) -> None:
        size:int = GameField.SIZE
        table:QTableWidget = QTableWidget(size, size)

        table.setFixedSize(900, 900)

        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)

        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for i in range(size):
            table.setColumnWidth(i, 90)
            table.setRowHeight(i, 90)

        self.__widgets.append(table)

    def setup_buttons(self, pause_callback:Callable) -> None:
        button_pause:QPushButton = QPushButton("П\nа\nу\nз\nа")
        button_pause.clicked.connect(pause_callback)
        
        button_pause.setFixedHeight(900)
        button_pause.setFixedWidth(80)

        self.__widgets.append(button_pause)