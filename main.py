import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")

        label.setStyleSheet("border: 1px solid black")
        label2.setStyleSheet("border: 1px solid black")
        label3.setStyleSheet("border: 1px solid black")
        
        size = QSize(15,15)
        label.setMaximumHeight(20)        
        label2.setMaximumHeight(20)        
        label3.setMaximumHeight(20)        
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)

        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()
    sys.exit(app.exec())
