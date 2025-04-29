from PySide6.QtCore import QPoint
from PySide6.QtGui import QPainter, QPalette, QPolygon
from PySide6.QtWidgets import QProxyStyle, QStyle, QStyleOptionFocusRect, QWidget

class myWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)

        option = QStyleOptionFocusRect(1)
        option.init(self)
        option.backgroundColor = palette().color(QPalette.Window)
        style().drawPrimitive(QStyle.PE_FrameFocusRect, option, painter, self)


class CustomStyle(QProxyStyle):

    def drawPrimitive(element, option, painter, widget):
        if element == PE_IndicatorSpinUp or element == PE_IndicatorSpinDown:
            points = QPolygon(3)
            x = option.rect.x()
            y = option.rect.y()
            w = option.rect.width() / 2
            h = option.rect.height() / 2
            x += (option.rect.width() - w) / 2
            y += (option.rect.height() - h) / 2
            if element == PE_IndicatorSpinUp:
                points[0] = QPoint(x, y + h)
                points[1] = QPoint(x + w, y + h)
                points[2] = QPoint(x + w / 2, y + h)

            else:
                points[0] = QPoint(x, y)
                points[1] = QPoint(x + w, y)
                points[2] = QPoint(x + w / 2, y + h)


            if option.state == State_Enabled:
                painter.setPen(option.palette.mid().color())
                painter.setBrush(option.palette.buttonText())
            else:
                painter.setPen(option.palette.buttonText().color())
                painter.setBrush(option.palette.mid())

            painter.drawPolygon(points)

        else:
            QProxyStyle.drawPrimitive(element, option, painter, widget)
