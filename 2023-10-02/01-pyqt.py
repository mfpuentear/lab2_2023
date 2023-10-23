from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication([])

window = QMainWindow()
window.setWindowTitle('Mi ventana')

label = QLabel('Hola mundo')

window.setCentralWidget(label)
window.show()

app.exec()