from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6 import uic

class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-06/miventana.ui", self)
    self.etiqueta.setText('Nuevo mensaje')


app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()