from logic.game_field import GameField

from typing import final


@final
class GameEngine:

    SCORE_COEFFICIENT: int = 10
    MIN_BALLS_TO_MATCH: int = 3
    MAX_BALLS_TO_MATCH: int = 5


    def __init__(self):
        self.__game_field: GameField = GameField()
        self.__score: int = 0
        self.__match_indexes: set[tuple[int, int]] = self.calculate_match_indexes()

        self.update_all()


    @property
    def game_field(self) -> list[list[int]]:
        return self.__game_field.listed_field


    @property
    def score(self) -> int:
        return self.__score


    @property
    def match_indexes(self) -> set[tuple[int, int]]:
        return self.__match_indexes.copy()


    def make_turn(self, row:int, col:int) -> None:
        if (not GameEngine.is_valid_turn(row, col)):
            return
        
        game_field: list[list[int]] = self.__game_field.listed_field

        temp_1: int = game_field[row - 1][col]
        temp_2: int = game_field[row + 1][col]

        self.__game_field.set_cell(row - 1, col, game_field[row][col - 1])
        self.__game_field.set_cell(row + 1, col, game_field[row][col + 1])

        self.__game_field.set_cell(row, col + 1, temp_1)
        self.__game_field.set_cell(row, col - 1, temp_2)

        self.update_all()


    @staticmethod
    def is_valid_turn(row: int, col: int) -> bool:
        return (0 < row < GameField.SIZE - 1 and
                0 < col < GameField.SIZE - 1)


    def update_all(self) -> None:
        self.update_match_indexes()

        while (self.__match_indexes):
            self.update_score()
            self.__game_field.update_field(self.__match_indexes)
            self.update_match_indexes()

        
    def update_match_indexes(self) -> None:
        self.__match_indexes = self.calculate_match_indexes()


    def update_score(self) -> None:
        if (not self.__match_indexes):
            return

        self.__score += len(self.__match_indexes) * self.SCORE_COEFFICIENT


    def calculate_match_indexes(self) -> set[tuple[int, int]]:
        field: list[list[int]] = self.game_field
        match_indexes: set[tuple[int]] = set()
        size: int = GameField.SIZE

        for i in range(size):
            match_indexes |= GameEngine.calculate_horizontal_matches(field, i, size)
            match_indexes |= GameEngine.calculate_vertical_matches(field, i, size)
            
        return match_indexes


    @staticmethod
    def calculate_horizontal_matches(field: list[list[int]],
                                     row: int, size: int) -> set[tuple[int, int]]:
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
    def calculate_vertical_matches(field: list[list[int]],
                                   col: int, size: int) -> set[tuple[int, int]]:
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