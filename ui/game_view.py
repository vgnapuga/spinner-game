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

        self.render_field()

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

        table.cellClicked.connect(self.handle_cell_click)

        self.__widgets.append(table)


    def render_field(self) -> None:
        table:QTableWidget = self.__widgets[0]
        game_field:list[list[int]] = self.engine.game_field.listed_field

        for i in range(GameField.SIZE):
            for j in range(GameField.SIZE):
                item:QTableWidgetItem = QTableWidgetItem(str(game_field[i][j]))

                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

                table.setItem(i, j, item)


    def handle_cell_click(self, row:int, col:int) -> None:
        self.engine.make_turn(row, col)
        self.engine.update_all()
        self.render_field()


    def setup_buttons(self, pause_callback:Callable) -> None:
        button_pause:QPushButton = QPushButton("П\nа\nу\nз\nа")
        button_pause.clicked.connect(pause_callback)
        
        button_pause.setFixedHeight(900)
        button_pause.setFixedWidth(80)

        self.__widgets.append(button_pause)