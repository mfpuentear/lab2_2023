# Realizar una clase CuentaBancaria con los siguientes atributos y metodos:
# Atributos: apellido del titular, nombre del titular, numero de cuenta, 
#            saldo de la cuenta.
# Métodos:
#  + constructor: con saldo inicial en cero.
#  + __str__(): devolver un string con todos los atributos.
#  + saldo(): mostrar el saldo de la cuenta
#  + ingresar(monto): ingresar un monto a la cuenta 
#                     (verificar monto positivo)
#  + retirar(monto): retirar un monto a la cuenta 
#                    (verificar monto positivo y saldo suficiente)

# Incorporar a la clase anterior una lista con el historial de ingresos 
# y retiros de la cuenta. Agregar tambien el metodo verHistorial que 
# muestre los movimientos.

class CuentaBancaria():
  def __init__(self, apellido, nombre, cuenta):
    self.apellido = apellido
    self.nombre = nombre
    self.cuenta = cuenta
    self.saldo = 0
    self.historial =[]
  
  def __str__(self):
    return f'{self.apellido}, {self.nombre}, {self.cuenta}, {self.saldo}'

  def verSaldo(self):
    print(f'El saldo actual es: {self.saldo}')

  def ingresar(self, monto):
    if monto>0:
      self.saldo += monto
      self.historial.append(f'Ingreso de {monto}, saldo actual: {self.saldo}')
    else:
      print('Monto negativo o cero')
  
  def retirar(self, monto):
    if monto > 0 and monto <= self.saldo:
      self.saldo -= monto
      self.historial.append(f'Retiro de {monto}, saldo actual: {self.saldo}')
    else:
      print('Monto negativo, cero o saldo insuficiente')
    
  def verHistorial(self):
    return self.historial

cuenta = CuentaBancaria('Sanchez', 'Pepe', '1213')

cuenta.verSaldo()
cuenta.ingresar(100)
cuenta.retirar(50)
cuenta.ingresar(150)
cuenta.retirar(10)
cuenta.verSaldo()
print(cuenta)
print(cuenta.verHistorial())
