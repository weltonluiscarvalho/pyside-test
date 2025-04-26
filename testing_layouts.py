from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QApplication

class myLabel(QLabel):
    def __init__(self, parent):
        self.adjustSize()
        super().__init__(parent)

    def set_size(self):
        # self.setMinimumWidth(int(widget.width() / 3))
        # self.setMaximumWidth(int(widget.width() / 3))
        # self.setMinimumHeight(int(widget.height() / 3))
        # self.setMaximumHeight(int(widget.height() / 3))
        self.adjustSize()


class myWidget(QWidget):

    signal_resize = Signal(int)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def resizeEvent(self, event):
        self.signal_resize.emit(event)
        return super().resizeEvent(event)

app = QApplication()
widget = myWidget()
layout_principal = QVBoxLayout()
layout_topo = QHBoxLayout()
layout_baixo = QHBoxLayout()

layout_velocidade = QVBoxLayout()
layout_erros = QVBoxLayout()

label_velocidade_nome = myLabel("velocidade")
label_velocidade_valor = myLabel("placeholder valor")
layout_velocidade.addWidget(label_velocidade_nome)
layout_velocidade.addWidget(label_velocidade_valor)


label_erros_nome = myLabel("erros")
label_erros_valor = myLabel("placeholder valor")
layout_erros.addWidget(label_erros_nome)
layout_erros.addWidget(label_erros_valor)

layout_topo.addLayout(layout_velocidade)
layout_topo.addLayout(layout_erros)

label_frase_principal = QLabel("placeholder frase principal")

botao_reiniciar = QPushButton("Reiniciar")
botao_alterar_frase = QPushButton("Alterar frase")
botao_finalizar = QPushButton("Finalizar")

# botao_reiniciar.clicked.connect(lambda x: print(label_velocidade_nome.size()))
# botao_reiniciar.clicked.connect(lambda x: print(label_velocidade_nome.maximumSize()))
# botao_reiniciar.clicked.connect(lambda x: print(label_velocidade_nome.minimumSize()))

def print_stretch():
    for i in range(0, layout_principal.count()):
        print(layout_principal.stretch(i))

botao_reiniciar.clicked.connect(lambda x: label_velocidade_nome.hide() if not label_velocidade_nome.isHidden() else label_velocidade_nome.show())
# widget.signal_resize.connect(label_velocidade_nome.set_size)
# widget.signal_resize.connect(label_velocidade_valor.set_size)
# widget.signal_resize.connect(label_erros_nome.set_size)
# widget.signal_resize.connect(label_erros_valor.set_size)
widget.signal_resize.connect(lambda x: print("signal emited!"))

layout_baixo.addWidget(botao_reiniciar)
layout_baixo.addWidget(botao_alterar_frase)
layout_baixo.addWidget(botao_finalizar)

layout_principal.addLayout(layout_topo)
layout_principal.addWidget(label_frase_principal)
layout_principal.addLayout(layout_baixo)

widget.setLayout(layout_principal)

widget.setStyleSheet("QLabel { border: 1px solid black }")
widget.show()

app.exec()
