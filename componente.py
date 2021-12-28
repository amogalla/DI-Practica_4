from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGraphicsOpacityEffect, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Property, QPropertyAnimation, QSize

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        layoutCompleto = QVBoxLayout()
        layoutBotones = QHBoxLayout()

        self.botonTransparente = Boton("Transparente")
        self.botonOpaco = Boton("Opaco")
        self.cuadro = Cuadro()

        layoutBotones.addWidget(self.botonTransparente)
        layoutBotones.addWidget(self.botonOpaco)
        layoutCompleto.addWidget(self.cuadro)

        layoutCompleto.addLayout(layoutBotones)

        contenedor = QWidget()
        contenedor.setLayout(layoutCompleto)
        contenedor.resize(100, 100) #Tamaño inicial del contenedor.
        self.setCentralWidget(contenedor)
        
        self.cuadro.setStyleSheet("background-color:red;border-radius:15px;")
        self.cuadro.resize(100, 100)
        
        self.botonTransparente.clicked.connect(self.cuadro.hacer_transparente)
        self.botonOpaco.clicked.connect(self.cuadro.hacer_opaco)

class Boton(QtWidgets.QWidget):
    def __init__(self, texto = "Pulsa aquí", parent=None):
        super().__init__(parent)
        layout = QtWidgets.QHBoxLayout() # Establecemos un layout horizontal
        
        self.boton = QtWidgets.QPushButton() # Creamos el widget Boton
        self.boton.setText(texto)
        layout.addWidget(self.boton)
        self.setLayout(layout)

    def __getattr__(self, name):
        return getattr(self.boton, name)

    def sizeHint(self):
        return QSize(40, 40)

    def getTexto(self):
        return self.boton.text()

    def setTexto(self, texto):
        self.boton.setText(texto)

    texto = Property(str, getTexto, setTexto)

class Cuadro(QWidget):
    cambio_opacidad = QtCore.Signal(float)

    def __init__(self):
        super().__init__()
        self.resize(100, 100)
        self.cuadro = QWidget(self)
        self.cuadro.setStyleSheet("background-color:blue;border-radius:15px;")
        self.cuadro.resize(100, 100)
        self.opacidad = 1.0

        self.cambio_opacidad.connect(self.setOpacidad)

    def getOpacidad(self):
        return self.opacidad
    
    def setOpacidad(self, opacidad):
        if opacidad != self.opacidad:
            self.opacidad = opacidad

    value = Property(float, getOpacidad, setOpacidad)

    def cambiar_opacidad(self, valor):
        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)

        self.anim = QPropertyAnimation(effect, b"opacity")
        self.anim.setStartValue(self.getOpacidad())
        self.anim.setEndValue(valor)
        self.anim.setDuration(800)
        self.anim.start()

        #self.setOpacidad(valor)
        self.cambio_opacidad.emit(valor)  #Emitimos la señal


    def hacer_transparente(self):
        self.cambiar_opacidad(0.25)

    def hacer_opaco(self):
        self.cambiar_opacidad(1.0)

    def sizeHint(self):
        return QSize(100, 100)
