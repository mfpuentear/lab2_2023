from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6 import uic

class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-09/ejercicio3.ui", self)
    #self.mostrar.clicked.connect(self.on_mostrar)
    self.nombre.textChanged.connect(self.on_cambio_nombre)
  
  #def on_mostrar(self):
  #  nombre = self.nombre.text()
  #  self.nombre_completo.setText(f'{nombre}')
  
  def on_cambio_nombre(self, nombre):
    self.nombre_completo.setText(nombre)
  

app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()