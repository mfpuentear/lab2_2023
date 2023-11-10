from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic


class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-11-10/01-spinbox.ui", self)
    self.cantidadLibros.valueChanged.connect(self.on_cantidad_libros_changed)

  def on_cantidad_libros_changed(self):
    precioLibro = float(self.precioLibros.text())
    self.totalLibros.setText(f'{precioLibro * self.cantidadLibros.value()}')


app = QApplication([])

win = MiVentana()
win.show()

app.exec()
