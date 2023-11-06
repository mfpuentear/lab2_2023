from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QTableWidgetItem, QMessageBox
from PyQt6 import uic

class Persona():
  def __init__(self, apellido, nombre, email):
    self.apellido = apellido
    self.nombre = nombre
    self.email = email
  
  def __str__(self):
    return f'{self.apellido}, {self.nombre}, {self.email}'


class DialogoPersona(QDialog):
  def __init__(self, persona=None):
    super().__init__()
    uic.loadUi("2023-11-06/00-dialogo-persona.ui", self)

    if (persona != None):
      self.apellido.setText(persona.apellido)
      self.nombre.setText(persona.nombre)
      self.email.setText(persona.email)

  #def setPersona(self, persona):
  #  self.apellido.setText(persona.apellido)
  #  self.nombre.setText(persona.nombre)
  #  self.email.setText(persona.email)

  def getPersona(self):
    apellido = self.apellido.text()
    nombre = self.nombre.text()
    email = self.email.text()
    return Persona(apellido, nombre, email)


class MiVentana(QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi("2023-11-06/00-tabla.ui", self)

    self.agregar.clicked.connect(self.on_agregar)
    self.editar.clicked.connect(self.on_editar)
    self.eliminar.clicked.connect(self.on_eliminar)
    self.tabla.currentItemChanged.connect(self.on_current_item_changed)

  def on_agregar(self):
    dialogo = DialogoPersona()
    if (dialogo.exec()):
      persona = dialogo.getPersona()

      # Cantidad de filas
      filas = self.tabla.rowCount()

      # Insertar fila en tabla
      self.tabla.insertRow(filas)
      self.tabla.setItem(filas, 0, QTableWidgetItem(persona.apellido))
      self.tabla.setItem(filas, 1, QTableWidgetItem(persona.nombre))
      self.tabla.setItem(filas, 2, QTableWidgetItem(persona.email))

  def on_editar(self):
    # Verificar que este elegido un item de la tabla
    item = self.tabla.currentItem()
    if (item == None):
      return

    # Obtener apellido, nombre y email de la tabla
    fila = item.row()
    apellido = self.tabla.item(fila, 0).text()
    nombre = self.tabla.item(fila, 1).text()
    email = self.tabla.item(fila, 2).text()

    persona = Persona(apellido, nombre, email)

    # Abrir dialogo con apellido, nombre y email elegido
    dialogo = DialogoPersona(persona)
    #dialogo = DialogoPersona()
    #dialogo.setPersona(persona)
    if (dialogo.exec()):
      persona = dialogo.getPersona()

      # Editar filas
      self.tabla.setItem(fila, 0, QTableWidgetItem(persona.apellido))
      self.tabla.setItem(fila, 1, QTableWidgetItem(persona.nombre))
      self.tabla.setItem(fila, 2, QTableWidgetItem(persona.email))
  
  def on_eliminar(self):
    # Verificar que este elegido un item de la tabla
    item = self.tabla.currentItem()
    if (item == None):
      return

    mensaje = QMessageBox()

    mensaje.setWindowTitle('Eliminar fila')
    mensaje.setText('¿Desea eliminar fila?')
    mensaje.setIcon(QMessageBox.Icon.Warning)
    mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    resultado = mensaje.exec()
    if (resultado == QMessageBox.StandardButton.Yes):
      # Quitar fila
      fila = item.row()
      self.tabla.removeRow(fila)
  
  def on_current_item_changed(self, item):
    print(item.text())


app = QApplication([])

win = MiVentana()
win.show()

app.exec()
