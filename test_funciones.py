import unittest, pytest, sys
from PySide6 import QtCore
from PySide6.QtCore import QSize
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget

from componente import Boton, Cuadro, Ventana

#OK
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


#Constructor inicial de un botón
@pytest.fixture
def boton(qtbot):
    botonInicial = Boton()
    qtbot.addWidget(botonInicial)

    return botonInicial

def test_texto_boton_inicial(boton):
    assert boton.getTexto() == "Pulsa aquí"

#Botón transparente
@pytest.fixture
def transparente(qtbot):
    botonTransparente = Boton("Transparente")
    qtbot.addWidget(botonTransparente)

    return botonTransparente

def test_texto_boton_transparente(transparente):
    assert transparente.getTexto() == "Transparente"


#Botón opaco
@pytest.fixture
def opaco(qtbot):
    botonOpaco = Boton("Opaco")
    qtbot.addWidget(botonOpaco)

    return botonOpaco

def test_texto_boton_opaco(opaco):
    assert opaco.getTexto() == "Opaco"

#OK
@pytest.fixture
def app2(qtbot):
    test_componente = Ventana()
    qtbot.addWidget(test_componente)

    return test_componente

def test_opacidad_inicial(app2):
    assert app2.cuadro.getOpacidad() == 1.0



@pytest.fixture
def app3(qtbot):
    test_ventana = Ventana()
    qtbot.addWidget(test_ventana)

    return test_ventana


def test_opacidad_tras_click_opaco(app3, qtbot):
    qtbot.mouseClick(app3.botonOpaco, QtCore.Qt.LeftButton)
    assert app3.cuadro.getOpacidad() == 1.0


if __name__ == '__main__':
    unittest.main()