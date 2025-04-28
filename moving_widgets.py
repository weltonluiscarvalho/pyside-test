from PySide6.QtCore import QTimeLine
from PySide6.QtWidgets import QApplication, QPushButton, QWidget

x_direction = 1
y_direction = 1

def move_widget():
    global x_direction, y_direction
    if widget_filho.x() + widget_filho.width() > widget_pai.width():
        x_direction = -1
    if widget_filho.y() + widget_filho.height() > widget_pai.height():
        y_direction = -1
    if widget_filho.x() < 0:
        x_direction = 1
    if widget_filho.y() < 0:
        y_direction = 1

    widget_filho.move(widget_filho.x() + (5 * x_direction), widget_filho.y() + (5 * y_direction))

app = QApplication()
widget_pai = QWidget()
widget_filho = QWidget()
widget_filho.setParent(widget_pai)
widget_filho.setStyleSheet("QWidget { border: 1px solid black }")
widget_filho.setFixedSize(100, 100)
widget_pai.show()

timeline = QTimeLine(100000)
timeline.setFrameRange(0, 1000)
timeline.frameChanged.connect(move_widget)
timeline.start()

app.exec()
