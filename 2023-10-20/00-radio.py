from PyQt6.QtWidgets import QApplication, QMainWindow 
from PyQt6 import uic

class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-20/00-radio.ui", self)

    self.opcion1.toggled.connect(self.on_opcion)
    self.opcion2.toggled.connect(self.on_opcion)
    self.opcion3.toggled.connect(self.on_opcion)
  
  def on_opcion(self):
    if self.opcion1.isChecked():
      self.etiqueta.setText('opcion 1 elegida')
    if self.opcion2.isChecked():
      self.etiqueta.setText('opcion 2 elegida')
    if self.opcion3.isChecked():
      self.etiqueta.setText('opcion 3 elegida')



app = QApplication([])

mi_ventana = MiVentana()
mi_ventana.show()

app.exec()