# Realizar un programa en Python que cree una clase 
# que represente un triángulo. 
# Atributos: ladoA, ladoB y ladoC. 
# Métodos: 
#   perimetro() para calcular perímetro
#   esEquilatero(): Retorna True si los lado son 
#   iguales
#   esIsosceles(): Retorna True si dos lados son 
#   iguales y uno distinto
#   esEscaleno(): Retorna True si los tres lados son 
#   distintos

class Triangulo():
  def __init__(self, ladoA, ladoB, ladoC):
    self.ladoA = ladoA
    self.ladoB = ladoB
    self.ladoC = ladoC
  
  def perimetro(self):
    return self.ladoA + self.ladoB + self.ladoC
  
  def esEquilatero(self):
    return self.ladoA == self.ladoB and self.ladoA == self.ladoC
  
  def esEscaleno(self):
    return self.ladoA != self.ladoB and self.ladoA != self.ladoC and self.ladoB != self.ladoC
  
  def esIsosceles(self):
    return not self.esEquilatero() and not self.esEscaleno()

triangulo = Triangulo(3,2,3)
print(triangulo.perimetro())
print(triangulo.esEquilatero())
print(triangulo.esEscaleno())
print(triangulo.esIsosceles())
