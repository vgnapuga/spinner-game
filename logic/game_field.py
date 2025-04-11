import random

from typing import final


@final
class GameField:

    HEIGHT:int = 10
    WIDTH:int = 10
    COLOR_COUNT:int = 8


    def __init__(self):
        self.__field = [
            [random.randint(1, GameField.COLOR_COUNT) for i in range(GameField.HEIGHT)]
            for j in range(GameField.WIDTH)
        ]


    @property
    def height(self) -> int:
        return self.HEIGHT


    @property
    def width(self) -> int:
        return self.WIDTH


    @property
    def listed_field(self) -> list[list[int]]:
        return self.__field.copy()

    
    def update_field(self, indexes:list[list[int]]) -> None:
        pass