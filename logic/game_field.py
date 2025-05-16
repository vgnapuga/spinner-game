import random

from typing import final


@final
class GameField:

    SIZE: int = 10
    COLOR_COUNT: int = 8


    def __init__(self):
        self._field = [
            [random.randint(1, GameField.COLOR_COUNT) for i in range(GameField.SIZE)]
            for j in range(GameField.SIZE)
        ]


    @property
    def listed_field(self) -> list[list[int]]:
        return [row[:] for row in self._field]
    

    def set_cell(
            self,
            row: int,
            col: int,
            value: int
            ) -> None:
        self._field[row][col] = value


    def update_field(self, match_indexes: set[tuple[int]]) -> None:
        if (not match_indexes):
            return

        for part_of_match in match_indexes:
            row: int = part_of_match[0]
            col: int = part_of_match[1]

            if (row != 0):
                for i in range(row, 0, -1):
                    self._field[i][col] = self._field[i - 1][col]

            self._field[0][col] = random.randint(1, self.COLOR_COUNT)