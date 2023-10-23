#Escribir un programa en Python que cree una clase representando un circulo.
#Incluir métodos para calcular su área y perímetro.

# Realizar un programa en Python que cree una clase que represente un triángulo. 
# Atributos: ladoA, ladoB y ladoC. 
# Métodos: 
#   perimetro() para calcular perímetro
#   esEquilatero(): Retorna True si los lado son iguales
#   esIsosceles(): Retorna True si dos lados son iguales y uno distinto
#   esEscaleno(): Retorna True si los tres lados son distintos

# Realizar una clase Contador con un atributo llamado 'cuenta'. Implementar los siguientes métodos:
#   + Constructor con cuenta inicial opcional iniciada en cero.
#   + mostrar(): Mostrar en pantalla la cuenta actual
#   + incrementar(valor): Incrementar la cuenta en valor o por defecto en 1 si no se especifica valor.
#   + decrementar(valor): Decrementar la cuenta en valor o por defecto en 1 si no se especifica valor.
#   + reiniciar(): Reinicar la cuenta a cero.

class Contador():
  def __init__(self, cuenta_inicial=10):
    self.cuenta = cuenta_inicial
   
  def incrementar(self, valor=1):
    self.cuenta = self.cuenta + valor

c = Contador(5)
print(c.cuenta)
c.incrementar()
print(c.cuenta)
c.incrementar(5)
print(c.cuenta)