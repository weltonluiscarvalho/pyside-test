from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QApplication

app = QApplication()

widget = QWidget()

layout = QVBoxLayout()

line_edit = QLineEdit("teste")
label = QLabel("www.google.com")
label.setTextFormat(Qt.MarkdownText)
label.linkHovered.connect(lambda x: print("teste signal"))

layout.addWidget(line_edit)
layout.addWidget(label)

widget.setLayout(layout)


widget.show()

app.exec()
