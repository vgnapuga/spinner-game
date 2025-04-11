from logic.game_field import GameField
from typing import final


@final
class GameEngine:

    SCORE_COEFFICIENT = 10
    MIN_BALLS_TO_MATCH = 3
    MAX_BALLS_TO_MATCH = 7


    def __init__(self):
        self.__game_field = GameField()
        self.__score:int = 0


    @property
    def game_field(self) -> GameField:
        return self.__game_field.copy()


    @property
    def score(self) -> int:
        return self.__score
    

    def update_score(self) -> None:
        match_indexes:list[list[int]] = self.calculate_match_indexes(self.game_field.listed_field)
        self.__score += len(match_indexes) * self.SCORE_COEFFICIENT
    

    @staticmethod
    def calculate_match_indexes(game_field:list[list[int]]) -> list[list[int]]:
        match_indexes:list[list[int]] = []

        rows:int = GameField.HEIGHT - GameEngine.MIN_BALLS_TO_MATCH
        cols:int = GameField.WIDTH - GameEngine.MIN_BALLS_TO_MATCH

        for i in range(rows):
            for j in range(cols):
                current:int = game_field[i][j]

                vertical_matches:list[list[int]] = GameEngine.calculate_vertical_matches(game_field, i, j,
                                                                                         rows, current)
                if (vertical_matches):
                    match_indexes.append(match for match in vertical_matches)

                horizontal_matches:list[list[int]] = GameEngine.calculate_horizontal_matches(game_field, i, j,
                                                                                             cols, current)
                if (not horizontal_matches):
                    match_indexes.append(match for match in horizontal_matches)

        return match_indexes


    @staticmethod
    def calculate_vertical_matches(game_field:list[list[int]],
                                   row:int, col:int, rows:int, current:int) -> list[list[int]]:
        result:list[list[int]] = []

        if (row < rows - 1):
            for i in range(row, row + GameEngine.MAX_BALLS_TO_MATCH - 1):
                if (current == game_field[i][col]):
                    result.append(game_field[i][col])
                else:
                    return None
        else:
            for i in range(row, row + GameEngine.MIN_BALLS_TO_MATCH - 1):
                if (current == game_field[i][col]):
                    result.append(game_field[i][col])
                else:
                    return None
                
        return result
    

    @staticmethod
    def calculate_horizontal_matches(game_field:list[list[int]],
                                     row:int, col:int, cols:int, current:int) -> list[list[int]]:
        result:list[list[int]] = []

        if (col < cols - 1):
            for i in range(col, col + GameEngine.MAX_BALLS_TO_MATCH - 1):
                if (current == game_field[row][i]):
                    result.append(game_field[row][i])
                else:
                    return None
        else:
            for i in range(col, col + GameEngine.MIN_BALLS_TO_MATCH - 1):
                if (current == game_field[row][i]):
                    result.append(game_field[row][i])
                else:
                    return None
                
        return result