from typing import Callable

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QCheckBox


class Settings(QWidget):

    def __init__(self, back_callback:Callable):
        super().__init__()

        self.setWindowTitle("Настройки")

        self.checkbox_time_limit = QCheckBox("Ограничение по времени")
        self.checkbox_turn_limit = QCheckBox("Ограничение по ходам")

        self.button_apply = QPushButton("Применить")
        self.button_back = QPushButton("Назад")

        self.button_apply.clicked.connect(self.apply_changes)
        self.button_back.clicked.connect(back_callback)

        self.lyt = QVBoxLayout()
        self.lyt.addWidget(self.checkbox_time_limit)
        self.lyt.addWidget(self.checkbox_turn_limit)
        self.lyt.addWidget(self.button_apply)
        self.lyt.addWidget(self.button_back)

        self.setLayout(self.lyt)


    def apply_changes(self) -> None:
        if (self.checkbox_time_limit.isChecked()):
            pass
        else:
            pass

        if (self.checkbox_turn_limit.isChecked()):
            pass
        else:
            pass