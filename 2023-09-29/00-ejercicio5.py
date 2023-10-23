class Cancion():
  def __init__(self, titulo, autor, duracion):
    self.titulo = titulo
    self.autor = autor
    self.duracion = duracion
  
  def __str__(self):
    return f'Titulo: {self.titulo}, autor: {self.autor}, duracion: {self.duracion}'

class Album():
  def __init__(self, titulo):
    self.titulo = titulo
    # Atributo privado
    self.__canciones = []
  
  def agregar_cancion(self, cancion):
    self.__canciones.append(cancion)
  
  def numero_canciones(self):
    return len(self.__canciones)
  
  def eliminar_cancion(self, indice):
    self.__canciones.pop(indice)
  
  def duracion_total(self):
    total = 0
    for cancion in self.__canciones:
      total += cancion.duracion
    return total
  
  def __str__(self):
    str = ''
    for i in range(len(self.__canciones)):
      str += f'Pista: {i+1} => {self.canciones[i]}\n'
    return str

cancion0 = Cancion('Titulo 0', 'Autor 0', 150)
cancion1 = Cancion('Titulo 1', 'Autor 1', 250)
cancion2 = Cancion('Titulo 2', 'Autor 2', 350)

album = Album('El album del siglo')
album.agregar_cancion(cancion0)
album.agregar_cancion(cancion1)
album.agregar_cancion(cancion2)

#print(album.numero_canciones())
#print(album.canciones[1])
print(album.duracion_total())