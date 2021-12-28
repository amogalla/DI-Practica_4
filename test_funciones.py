import unittest, pytest, sys
from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget

from componente import Boton, Cuadro, Ventana

class BotonTestCase(unittest.TestCase):
    def test_sizeHintCuadro(self):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()

        result = Cuadro().sizeHint()
        self.assertEqual(result, QSize(100, 100))

    def test_sizeHintBoton(self):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()
        
        result = Boton().sizeHint()
        self.assertEqual(result, QSize(40, 40))

    def test_textoBotonInicial(self):
        result = Boton().getTexto()
        self.assertEqual(result, "Pulsa aquí")

    def test_textoBotonTransparente(self):
        result = Boton("Transparente").getTexto()
        self.assertEqual(result, "Transparente")

    def test_textoBotonOpaco(self):
        result = Boton("Opaco").getTexto()
        self.assertEqual(result, "Opaco")
    
    def test_opacidadInicial(self):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()
        result = Cuadro().getOpacidad()
        print(result)
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()
