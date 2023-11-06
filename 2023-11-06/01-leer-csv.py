import csv

# Abrir archivo
archivo = open('2023-11-06/01-datos.csv')
#archivo = open('2023-11-06/01-datos2.csv')
filas = csv.reader(archivo, delimiter=',', quotechar='"')

# Leer filas
for fila in filas:
  print(fila[0], ' ', fila[1], ' ', fila[2])

# cerrar archivo
archivo.close()