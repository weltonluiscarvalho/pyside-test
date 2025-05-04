from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtGui import (QBrush, QPainter, QColor,
                           QPainterPath, QPalette, QPen,
                           QPixmap, QPolygon)
from PySide6.QtWidgets import (QApplication,QGridLayout, QWidget)

import basicdrawing_rc  # noqa: F401


class RenderArea(QWidget):
    points = QPolygon([
        QPoint(10, 80),
        QPoint(20, 10),
        QPoint(80, 30),
        QPoint(90, 70)
    ])

    (Line, Points, Polyline, Polygon, Rect, RoundedRect, Ellipse,
     Arc, Chord, Pie, Path, Text, Pixmap) = range(13)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.pen = QPen()
        self.brush = QBrush()
        self.pixmap = QPixmap()

        self.shape = RenderArea.Polygon
        self.antialiased = False
        self.transformed = False
        self.pixmap.load(':/images/qt-logo.png')

        self.setBackgroundRole(QPalette.ColorRole.Base)
        self.setAutoFillBackground(True)
    
    def paintEvent(self, event):
        rect = QRect(10, 20, 80, 60)

        path = QPainterPath()
        path.moveTo(20, 80)
        path.lineTo(20, 30)
        path.cubicTo(80, 0, 50, 50, 80, 80)

        with QPainter(self) as painter:
            painter.setPen(self.pen)
            painter.setBrush(self.brush)
            if self.antialiased:
                painter.setRenderHint(QPainter.RenderHint.Antialiasing)

            # for x in range(0, self.width(), 100):
            #     for y in range(0, self.height(), 100):
            #         with QPainterStateGuard(painter):
            #             painter.translate(x, y)
            #
            #             painter.drawPath(path)
            painter.drawPath(path)

            painter.setPen(self.palette().dark().color())
            painter.setBrush(Qt.BrushStyle.HorPattern)
            painter.drawRect(QRect(0, 0, self.width() - 1, self.height() - 1))
            path = QPainterPath()
            path.addRect(20, 20, 60, 60)
            path.moveTo(0, 0)
            path.cubicTo(99, 0, 50, 50, 99, 99)
            path.cubicTo(0, 99, 50, 50, 0, 0)
            painter = QPainter(self)
            painter.fillRect(0, 0, 100, 100, Qt.GlobalColor.white)
            painter.setPen(QPen(QColor(79, 106, 25), 1, Qt.SolidLine, Qt.FlatCap, Qt.MiterJoin))
            painter.setBrush(QColor(122, 163, 39))
            painter.drawPath(path)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self._render_area = RenderArea()
        main_layout = QGridLayout()
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(3, 1)
        main_layout.addWidget(self._render_area, 0, 0, 1, 4)
        self.setLayout(main_layout)
        self.setWindowTitle("Basic Drawing")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
