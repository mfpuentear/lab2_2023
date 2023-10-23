from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic

class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-10-23/01-message-box.ui", self)
    self.mostrar_mensaje.clicked.connect(self.on_mostrar)
  
  def on_mostrar(self):
    mensaje = QMessageBox()

    mensaje.setWindowTitle('Titulo del mensaje')
    mensaje.setText('Cuerpo del mensaje')

    #mensaje.setIcon(QMessageBox.Icon.Information)
    #mensaje.setIcon(QMessageBox.Icon.Question)
    #mensaje.setIcon(QMessageBox.Icon.Warning)
    mensaje.setIcon(QMessageBox.Icon.Critical)

    #mensaje.setStandardButtons( QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Close | QMessageBox.StandardButton.Save | QMessageBox.StandardButton.SaveAll | QMessageBox.StandardButton.Abort | QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.Ignore)
    mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)

    resultado = mensaje.exec()
    if (resultado == QMessageBox.StandardButton.Yes):
      print('usuario eligio SI')
    if (resultado == QMessageBox.StandardButton.No):
      print('usuario eligio NO')
    if (resultado == QMessageBox.StandardButton.Cancel):
      print('usuario eligio CANCELAR')





    

app = QApplication([])

win = MiVentana()
win.show()

app.exec()

