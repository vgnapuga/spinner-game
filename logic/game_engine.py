from typing import final

from logic import GameField


@final
class GameEngine:

    SCORE_COEFFICIENT: int = 10

    MIN_BALLS_TO_MATCH: int = 3

    TIME_LIMIT: int = 60
    TURN_LIMIT: int = 50
    NO_LIMIT: int = 1_000_000


    def __init__(
            self,
            is_time_left: bool,
            is_turns_left: bool,
            ):
        self._game_field: GameField = GameField()
        self._match_indexes: set[tuple[int, int]] = self.calculate_match_indexes()

        self._score: int = 0

        self._time_left: int = GameEngine.TIME_LIMIT if (is_time_left) else GameEngine.NO_LIMIT
        self._turns_left: int = GameEngine.TURN_LIMIT if (is_turns_left) else GameEngine.NO_LIMIT

        self.update_all()


    @property
    def game_field(self) -> list[list[int]]:
        return self._game_field.listed_field


    @property
    def match_indexes(self) -> set[tuple[int, int]]:
        return self._match_indexes.copy()
    

    @property
    def score(self) -> int:
        return self._score
    

    @property
    def turns_left(self) -> int:
        return self._turns_left


    def make_turn(self, row:int, col:int) -> None:
        if (not GameEngine.is_valid_turn(row, col)):
            return
        
        if (self._turns_left < GameEngine.NO_LIMIT):
            self._turns_left -= 1
        
        game_field: list[list[int]] = self._game_field.listed_field

        temp_1: int = game_field[row - 1][col]
        temp_2: int = game_field[row + 1][col]

        self._game_field.set_cell(row - 1, col, game_field[row][col - 1])
        self._game_field.set_cell(row + 1, col, game_field[row][col + 1])

        self._game_field.set_cell(row, col + 1, temp_1)
        self._game_field.set_cell(row, col - 1, temp_2)

        self.update_all()


    @staticmethod
    def is_valid_turn(row: int, col: int) -> bool:
        return (0 < row < GameField.SIZE - 1 and
                0 < col < GameField.SIZE - 1)


    def update_all(self) -> None:
        self.update_match_indexes()

        while (self._match_indexes):
            self.update_score()
            self._game_field.update_field(self._match_indexes)
            self.update_match_indexes()

        
    def update_match_indexes(self) -> None:
        self._match_indexes = self.calculate_match_indexes()


    def update_score(self) -> None:
        if (not self._match_indexes):
            return

        self._score += len(self._match_indexes) * self.SCORE_COEFFICIENT


    def calculate_match_indexes(self) -> set[tuple[int, int]]:
        field: list[list[int]] = self.game_field
        match_indexes: set[tuple[int]] = set()
        size: int = GameField.SIZE

        for i in range(size):
            match_indexes |= GameEngine.calculate_horizontal_matches(field, i, size)
            match_indexes |= GameEngine.calculate_vertical_matches(field, i, size)
            
        return match_indexes


    @staticmethod
    def calculate_horizontal_matches(
            field: list[list[int]],
            row: int,
            size: int
            ) -> set[tuple[int, int]]:
        matches: set[tuple[int, int]] = set()
        count: int = 1

        for i in range(1, size):
            if (field[row][i] == field[row][i - 1]):
                count += 1
            else:
                if (count >= GameEngine.MIN_BALLS_TO_MATCH):
                    for j in range(i - count, i):
                        matches.add((row, j))

                count = 1

        if (count >= GameEngine.MIN_BALLS_TO_MATCH):
            for j in range(size - count, size):
                matches.add((row, j))

        return matches


    @staticmethod
    def calculate_vertical_matches(
            field: list[list[int]],
            col: int,
            size: int
            ) -> set[tuple[int, int]]:
        matches: set[tuple[int, int]] = set()
        count: int = 1

        for i in range(1, size):
            if (field[i][col] == field[i - 1][col]):
                count += 1
            else:
                if (count >= GameEngine.MIN_BALLS_TO_MATCH):
                    for j in range(i - count, i):
                        matches.add((j, col))

                count = 1

        if (count >= GameEngine.MIN_BALLS_TO_MATCH):
            for j in range(size - count, size):
                matches.add((j, col))

        return matches
    

    def is_game_over(self) -> bool:
        if (
            self._time_left == 0 or
            self._turns_left == 0
            ):
            return True
        
        return False