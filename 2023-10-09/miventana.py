from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6 import uic

class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-09/miventana.ui", self)
    self.cambiar.clicked.connect(self.on_cambiar_saludo)
  
  def on_cambiar_saludo(self):
    self.etiqueta.setText('Chau mundo!')


app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()