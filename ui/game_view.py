from typing import Callable
from enum import IntEnum

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView, QPushButton, QHBoxLayout, QLabel, QVBoxLayout

from logic import GameEngine
from logic import GameField
from ui.styles import CssStyle


class FieldIndex(IntEnum):

    SCORE_FIELD = 0
    TIME_FIELD = 1
    TURNS_FIELD = 2


class GameView(QWidget):


    def __init__(
            self,
            pause_callback: Callable,
            is_time_limit: bool,
            is_turn_limit: bool,
            ):
        super().__init__()

        self.engine: GameEngine = GameEngine(is_time_limit, is_turn_limit)
        self._widgets: list[QWidget] = []
        self._fields: list[QLabel] = []

        self.setup_table()
        self.render_field()

        self.setup_pause_button(pause_callback)

        self.setup_fields(is_time_limit, is_turn_limit)

        CssStyle.apply_font_size(self._widgets)
        CssStyle.apply_font_size(self._fields)

        layout_h = QHBoxLayout()
        layout_h.setContentsMargins(380, 0, 380, 0)

        for widget in self._widgets: 
            layout_h.addWidget(widget)

        layout_v = QVBoxLayout()
        layout_v.setContentsMargins(0, 300, 0, 300)

        for field in self._fields:
            layout_v.addWidget(field)

        layout_h.addLayout(layout_v)

        self.setLayout(layout_h)


    def setup_table(self) -> None:
        size: int = GameField.SIZE
        table: QTableWidget = QTableWidget(size, size)

        table.setFixedSize(900, 900)

        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)

        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for i in range(size): 
            table.setColumnWidth(i, 90)
            table.setRowHeight(i, 90)

        table.setSelectionMode(QAbstractItemView.NoSelection)
        table.cellClicked.connect(self.handle_cell_click)

        self._widgets.append(table)


    def render_field(self) -> None:
        colors: dict[int, str] = {
            0: "#FFFFFF",
            1: "#FF0000",
            2: "#00FF00",
            3: "#0000FF",
            4: "#FFFF00",
            5: "#FF00FF",
            6: "#00FFFF",
            7: "#FFA500",
            8: "#800080",
        }

        table: QTableWidget = self._widgets[0]
        game_field: list[list[int]] = self.engine.game_field

        for i in range(GameField.SIZE): 
            for j in range(GameField.SIZE): 
                item: QTableWidgetItem = QTableWidgetItem()

                item.setBackground(QColor(colors[game_field[i][j]]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

                table.setItem(i, j, item)


    def handle_cell_click(self, row: int, col: int) -> None:
        self.engine.make_turn(row, col)
        self.update_turn_field()
        self.update_score_field()
        self.render_field()


    def setup_pause_button(self, pause_callback: Callable) -> None:
        button_pause: QPushButton = QPushButton("П\nа\nу\nз\nа")
        button_pause.clicked.connect(pause_callback)

        button_pause.setFixedHeight(900)
        button_pause.setFixedWidth(80)

        self._widgets.append(button_pause)


    def setup_fields(
            self,
            is_time_limit: bool,
            is_turn_limit: bool,
            ) -> None:
        self.setup_score_field()
        self.setup_time_field(is_time_limit)
        self.setup_turn_field(is_turn_limit)

    
    def setup_score_field(self) -> None:
        score_field: QLabel = QLabel()
        score_field.setText(f"Счёт: {str(self.engine.score)}")

        self._fields.append(score_field)


    def update_score_field(self) -> None:
        self._fields[FieldIndex.SCORE_FIELD].setText(f"Счёт: {str(self.engine.score)}")


    def setup_time_field(self, is_time_limit: bool) -> None:
        time_field: QLabel = QLabel()

        if (not is_time_limit):
            time_field.setText("Время: inf")
        else:
            time_field.setText(f"Время: {str(self.engine.TIME_LIMIT)}")

        self._fields.append(time_field)


    #TODO: realization    
    def update_time_field(self) -> None:
        pass


    def setup_turn_field(self, is_turn_limit: bool) -> None:
        turn_field: QLabel = QLabel()

        if (not is_turn_limit):
            turn_field.setText("Ходы: inf")
        else:
            turn_field.setText(f"Ходы: {str(self.engine.TURN_LIMIT)}")

        self._fields.append(turn_field)


    def update_turn_field(self) -> None:
        self._fields[FieldIndex.TURNS_FIELD].setText(f"Ходы: {self.engine.turns_left}")