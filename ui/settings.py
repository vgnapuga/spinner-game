from typing import Callable

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QCheckBox


class Settings(QWidget):

    SETTINGS_FILE_PATH:str = "settings.txt"

    def __init__(self, back_callback:Callable):
        super().__init__()

        self.__widgets:list[QWidget] = []

        self.__is_time_limit:bool = Settings.get_parameter_from_file("time_limit")
        self.__is_turn_limit:bool = Settings.get_parameter_from_file("turn_limit")
        self.initiate_check_boxes()

        self.initiate_buttons(back_callback)

        self.lyt:QVBoxLayout = QVBoxLayout()
        for widget in self.__widgets:
            self.lyt.addWidget(widget)

        self.setLayout(self.lyt)


    @property
    def is_time_limit(self) -> bool:
        return self.__is_time_limit
    

    @property
    def is_turn_limit(self) -> bool:
        return self.__is_turn_limit


    def initiate_check_boxes(self) -> None:
        self.check_box_time_limit:QCheckBox = QCheckBox("Ограничение по времени")
        self.check_box_turn_limit:QCheckBox = QCheckBox("Ограничение по ходам")

        self.check_box_time_limit.setChecked(self.__is_time_limit)
        self.check_box_turn_limit.setChecked(self.__is_turn_limit)

        self.__widgets.append(self.check_box_time_limit)
        self.__widgets.append(self.check_box_turn_limit)


    def initiate_buttons(self, back_callback:Callable) -> None:
        self.button_apply:QPushButton = QPushButton("Применить")
        self.button_back:QPushButton = QPushButton("Назад")

        self.button_apply.clicked.connect(self.apply_changes)
        self.button_back.clicked.connect(back_callback)

        self.__widgets.append(self.button_apply)
        self.__widgets.append(self.button_back)


    def apply_changes(self) -> None:
        self.__is_time_limit = self.check_box_time_limit.isChecked()
        self.__is_turn_limit = self.check_box_turn_limit.isChecked()

        self.update_settings_file()


    @staticmethod
    def get_parameter_from_file(parameter:str) -> bool:
        settings:set[tuple[str, bool]] = Settings.read_settings_from_file()
        return settings[parameter]


    @staticmethod
    def read_settings_from_file() -> dict[str, bool]:
        settings:dict[str, bool] = {}

        try:
            with open(Settings.SETTINGS_FILE_PATH, "r") as file:
                for line in file:
                    parameter, state = line.strip().split(":", 1)
                    settings[parameter] = state.lower() == "true"
        except FileNotFoundError:
            with open(Settings.SETTINGS_FILE_PATH, "x") as file:
                file.write(f"time_limit:False\nturn_limit:False")
                settings = {"time_limit":False, "turn_limit":False}

        return settings


    def update_settings_file(self) -> None:
        with open(Settings.SETTINGS_FILE_PATH, "w") as file:
            file.write(f"time_limit:{self.__is_time_limit}\nturn_limit:{self.__is_turn_limit}")