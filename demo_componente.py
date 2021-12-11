import sys
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
from componente import Boton, Cuadro

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(50, 250)
        layoutCompleto = QVBoxLayout()
        layoutBotones = QHBoxLayout()

        self.boton1 = Boton("Transparente")
        self.boton2 = Boton("Opaco")
        self.cuadro = Cuadro()

        layoutBotones.addWidget(self.boton1)
        layoutBotones.addWidget(self.boton2)
        layoutCompleto.addWidget(self.cuadro)

        layoutCompleto.addLayout(layoutBotones)

        contenedor = QWidget()
        contenedor.setLayout(layoutCompleto)
        contenedor.resize(100, 100) #Tamaño inicial del contenedor.
        self.setCentralWidget(contenedor)
        
        self.cuadro.setStyleSheet("background-color:red;border-radius:15px;")
        self.cuadro.resize(100, 100)
        
        self.boton1.clicked.connect(self.cuadro.hacer_transparente)
        self.boton2.clicked.connect(self.cuadro.hacer_opaco)

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()
