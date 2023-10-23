# Escribir una clase Persona con los siguientes atributos y métodos:
# Atributos: apellido, nombre, edad, altura y peso.
# Métodos: constructor, nombreCompleto() string con formato "apellido, nombre", esMayor(), imc() y __str__()

class Persona():
  def __init__(self, apellido, nombre, edad, altura, peso):
    self.apellido = apellido
    self.nombre = nombre
    self.edad = edad
    self.altura = altura
    self.peso = peso
  
  def nombreCompleto(self):
    return f"{self.apellido}, {self.nombre}"
  
  def esMayor(self):
    return self.edad >= 18

  def imc(self):
    return self.peso / (self.altura * self.altura)
  
  def __str__(self):
    return f"{self.apellido}, {self.nombre}, {self.edad}, {self.altura:.2f}, {self.peso:.3f}"
  

persona = Persona("Sanchez", "Pepe", 25, 1.85, 78)
print(persona.nombreCompleto())
print(persona.esMayor())
print(f"{persona.imc():.2f}")
print(persona)
