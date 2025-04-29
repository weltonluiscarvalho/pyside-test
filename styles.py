from PySide6.QtGui import QPainter, QPalette
from PySide6.QtWidgets import QStyle, QStyleOptionFocusRect, QWidget

class myWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)

        option = QStyleOptionFocusRect(1)
        option.init(self)
        option.backgroundColor = palette().color(QPalette.Window)
        style().drawPrimitive(QStyle.PE_FrameFocusRect, option, painter, self)


print('bunda')
