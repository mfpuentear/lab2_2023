# Desarrollar una clase Cafetera con:
# Atributos: 
#  + capacidadMaxima: Cantidad maxima de cafe que puede contener la cafetera en CC
#  + cantidadActual: Cantidad actual de cafe que hay en la cafetera en CC
# Metodos:
#  + Constructor: Considerar por defecto capacidad maxima de 1000 CC y cantidad actual en cero
#  + llenar(): Llena cafetera a la capacidad maxima
#  + servir(cantidad): sirve una cantidad de cafe (Verificar que cantidad sea positivo y no servir mas del actual)
#  + vaciar(): Vaciar cafetera 
#  + agregar(cantidad): añade una cantidad de cafe (Verificar que cantidad sea positivo y no supere el maximo)

# Escribir una clase Persona con los siguientes atributos y métodos:
# Atributos: apellido, nombre, edad, altura y peso.
# Métodos: constructor, nombreCompleto() string con formato "apellido, nombre", esMayor(), imc() y __str__()

class Cafetera():
  def __init__(self, cantidadActual=0, capacidadMaxima=1000):
    self.cantidadActual = cantidadActual
    self.capacidadMaxima = capacidadMaxima
  
  def __str__(self):
    return f"{self.cantidadActual} de {self.capacidadMaxima}"

  def llenar(self):
    self.cantidadActual = self.capacidadMaxima
  
  def vaciar(self):
    self.cantidadActual = 0
  
  def servir(self, cantidad):
    if cantidad > 0 and cantidad <= self.cantidadActual:
      self.cantidadActual = self.cantidadActual - cantidad
    else:
      print("cantidad menor o igual a cero o no se puede servir mas de la cantidad actual")
  

c = Cafetera()
print(c)
c.llenar()
print(c)
c.servir(200)
print(c)
c.servir(-200)
c.servir(10000)
c.servir(800)
print(c)
