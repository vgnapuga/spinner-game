from logic.game_field import GameField

from typing import final
from copy import deepcopy


@final
class GameEngine:

    SCORE_COEFFICIENT: int = 10
    MIN_BALLS_TO_MATCH: int = 3
    MAX_BALLS_TO_MATCH: int = 5


    def __init__(self):
        self.__game_field: GameField = GameField()
        self.__score: int = 0
        self.__match_indexes: set[tuple[int]] = self.calculate_match_indexes()

        self.update_all()


    @property
    def game_field(self) -> GameField:
        return self.__game_field.listed_field


    @property
    def score(self) -> int:
        return self.__score


    @property
    def match_indexes(self) -> set[tuple[int]]:
        return deepcopy(self.__match_indexes)


    def make_turn(self, row:int, col:int) -> None:
        if (not GameEngine.is_valid_turn(row, col)):
            return

        game_field: list[list[int]] = self.game_field

        temp_1: int = game_field[row - 1][col]
        temp_2: int = game_field[row + 1][col]

        game_field[row - 1][col] = game_field[row][col - 1]
        game_field[row + 1][col] = game_field[row][col + 1]

        game_field[row][col + 1] = temp_1
        game_field[row][col - 1] = temp_2

        self.update_all()


    @staticmethod
    def is_valid_turn(row: int, col: int) -> bool:
        return ((row and col) < GameField.SIZE - 1) and ((row and col) > 0)


    def update_all(self) -> None:
        while (self.__match_indexes):
            self.update_score()
            self.__game_field.update_field(self.__match_indexes)
            self.update_match_indexes()


    def update_score(self) -> None:
        if (not self.__match_indexes):
            return

        self.__score += len(self.__match_indexes) * self.SCORE_COEFFICIENT


    def update_match_indexes(self) -> None:
        self.__match_indexes = self.calculate_match_indexes()


    def calculate_match_indexes(self) -> set[tuple[int]]:
        match_indexes: set[tuple[int]] = set()
        game_field: list[list[int]] = self.game_field

        rows: int = GameField.SIZE - GameEngine.MIN_BALLS_TO_MATCH
        cols: int = GameField.SIZE - GameEngine.MIN_BALLS_TO_MATCH

        for i in range(rows):
            for j in range(cols):
                current: int = game_field[i][j]

                vertical_matches: list[list[int]] = GameEngine.calculate_vertical_matches(game_field, i, j,
                                                                                         rows, current)
                if (vertical_matches):
                    for match in vertical_matches:
                        match_indexes.add((match[0], match[1]))

                horizontal_matches: list[list[int]] = GameEngine.calculate_horizontal_matches(game_field, i, j,
                                                                                             cols, current)
                if (horizontal_matches):
                    for match in horizontal_matches:
                        match_indexes.add((match[0], match[1]))

        return match_indexes


    @staticmethod
    def calculate_vertical_matches(game_field: list[list[int]],
                                   row: int, col: int,
                                   rows: int, current: int) -> list[list[int]]:
        result: list[list[int]] = []

        if (row < rows - 1):
            for i in range(row, row + GameEngine.MAX_BALLS_TO_MATCH):
                if (current == game_field[i][col]):
                    result.append([i, col])
                else:
                    return []
        else:
            for i in range(row, row + GameEngine.MIN_BALLS_TO_MATCH):
                if (current == game_field[i][col]):
                    result.append([i, col])
                else:
                    return []

        return result


    @staticmethod
    def calculate_horizontal_matches(game_field: list[list[int]],
                                     row: int, col: int,
                                     cols: int, current: int) -> list[list[int]]:
        result: list[list[int]] = []

        if (col < cols - 1):
            for i in range(col, col + GameEngine.MAX_BALLS_TO_MATCH):
                if (current == game_field[row][i]):
                    result.append([row, i])
                else:
                    return []
        else:
            for i in range(col, col + GameEngine.MIN_BALLS_TO_MATCH):
                if (current == game_field[row][i]):
                    result.append([row, i])
                else:
                    return []

        return result