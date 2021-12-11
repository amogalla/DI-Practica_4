from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGraphicsOpacityEffect, QWidget
from PySide6.QtCore import Property, QPropertyAnimation

class Boton(QtWidgets.QWidget):
    def __init__(self, texto = "Pulsa aquí", parent=None):
        super().__init__(parent)
        
        layout = QtWidgets.QHBoxLayout() #Establecemos un layout horizontal
        
        self.boton = QtWidgets.QPushButton() # Creamos el widget Boton
        self.boton.setText(texto)
        
        layout.addWidget(self.boton)
        self.setLayout(layout)

    def __getattr__(self, name):
        return getattr(self.boton, name)

    def getTexto(self):
        return self.texto
    
    def setTexto(self, texto):
        self.texto = texto

    texto = Property(int, getTexto, setTexto)

class Cuadro(QWidget):
    cambio_opacidad = QtCore.Signal(float)

    def __init__(self):
        super().__init__()
        self.resize(100, 100)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:blue;border-radius:15px;")
        self.child.resize(100, 100)
        self.opacidad = 1.0

        self.cambio_opacidad.connect(self.setOpacidad)

    def getOpacidad(self):
        return self.opacidad
    
    def setOpacidad(self, opacidad):
        if opacidad != self.opacidad:
            self.opacidad = opacidad

    value = Property(int, getOpacidad, setOpacidad)

    def cambiar_opacidad(self, valor):
        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setStartValue(self.getOpacidad())

        self.cambio_opacidad.emit(valor)  #Emitimos la señal

        self.anim.setEndValue(valor)
        self.anim.setDuration(800)
        self.anim.start()

    def hacer_transparente(self):
        self.cambiar_opacidad(0.25)

    def hacer_opaco(self):
        self.cambiar_opacidad(1)
