from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6 import uic

class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-20/01-check.ui", self)

    self.opcion1.toggled.connect(self.on_opcion)
    self.opcion2.toggled.connect(self.on_opcion)
    self.opcion3.toggled.connect(self.on_opcion)
  
  def on_opcion(self):
    seleccion = ''
    if self.opcion1.isChecked():
      seleccion += 'opcion 1 '
    if self.opcion2.isChecked():
      seleccion += 'opcion 2 '
    if self.opcion3.isChecked():
      seleccion += 'opcion 3'
    self.etiqueta.setText(seleccion)



app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()