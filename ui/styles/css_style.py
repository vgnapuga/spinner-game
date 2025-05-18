from PyQt5.QtWidgets import QWidget

from typing import Union

class CssStyle:

    FONT_SIZE_STYLE: str = "font-size: 30px;"


    @classmethod
    def apply_font_size(cls, widgets: Union[QWidget, list[QWidget]]) -> None:
        if (isinstance(widgets, QWidget)):
            widgets.setStyleSheet(cls.FONT_SIZE_STYLE)
        else:
            for widget in widgets:
                widget.setStyleSheet(cls.FONT_SIZE_STYLE)