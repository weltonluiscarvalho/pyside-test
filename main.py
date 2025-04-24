import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QComboBox, QLabel, QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        central_widget = QWidget()
        layout = QVBoxLayout()
        label = QLabel("Mais vale um passaro na mao do que 2 voando")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")

        style_sheet = """
            QLabel {
                border: 2px solid black;
                background-image: url(gato.png);
                background-position: right;
                background-clip: content;
                background-size: contain;
            }
        """
        central_widget.setStyleSheet(style_sheet)
        label.setStyleSheet("QLabel { border: 1px solid black }")

        
        
        # label2.setStyleSheet(style_sheet)

        # label.setStyleSheet("border: 1px solid black; font-family: JetBrainsMonoNerdFont; font-size: 5.5em")
        # label2.setStyleSheet("border: 1px solid black")
        # label3.setStyleSheet("border: 1px solid black")
        
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
