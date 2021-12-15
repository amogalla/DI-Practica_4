import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from componente import Ventana

app = QApplication(sys.argv)
w = QWidget()

ventana = Ventana()
w.setLayout(QVBoxLayout())
w.layout().addWidget(ventana)

w.show()
app.exec()
