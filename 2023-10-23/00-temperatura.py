from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-23/00-temperatura.ui", self)
    self.calcular.clicked.connect(self.on_calcular)
    
  def on_calcular(self):
    temperatura = float(self.temperatura.text())

    if self.c_k.isChecked():
      resultado = temperatura + 273.15

    if self.k_c.isChecked():
      resultado = temperatura - 273.15
        
    if self.c_f.isChecked():
      resultado = temperatura * (9 / 5) + 32

    if self.f_c.isChecked():
      resultado = (temperatura - 32) * (5 / 9)
    
    self.resultado.setText(f'El resultado es: {resultado}')

app = QApplication([])

win = MiVentana()
win.show()

app.exec()
