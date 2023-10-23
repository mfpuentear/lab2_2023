#Realizar una clase CuentaBancaria con los siguientes atributos y metodos:
#Atributos: nombre y apellido del titular, saldo de la cuenta
#Métodos:
#  + constructor: 
#  + __str__(): devolver todos los atributos.
#  + saldo(): mostrar el saldo de la cuenta
#  + ingresar(monto): ingresar un monto a la cuenta (verificar monto positivo)
#  + retirar(monto): retirar un monto de la cuenta no superior al saldo (verificar monto positivo)

class CuentaBancaria():
  def __init__(self, apellido, nombre, saldo):
    self.apellido = apellido
    self.nombre = nombre
    self.saldo = saldo
  
  def __str__(self):
    return f'{self.apellido}, {self.nombre}, {self.saldo}'

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
    
#Las clases CuentaAhorro y CuentaCorriente heredan los atributos y metodos de CuentaBancaria.

#La clase CuentaAhorro tiene además un atributo para determinar si la cuenta esta inactiva si el saldo es menor a 10000 y 
#activa si es mayor. Tiene los siguientes metodos:
#  + ingresar(monto): Se puede ingresar dinero invocando al método heredado cuando esta activa la cuenta.
#  + retirar(monto): Se puede retirar si la cuenta esta activa. Debe invocar al metodo heredado.
#  + __str__(): devolver todos los atributos incluyendo si esta activa.

#La clase CuentaCorriente tiene además un atributo de sobregiro inicializada en cero. Además los siguientes métodos:
#  + ingresar(monto): Se puede ingresar, pero si hay sobregiro se reduce la cantidad agregada.
#  + retirar(monto): Se puede retirar un monto superior al saldo, el dinero que se debe queda como sobregiro. Invocar al 
#    metodo heredado.
#  + __str__(): devolver todos los atributos incluyendo el sobregiro. Invocar al metodo heredado.

Realizar las siguientes clases:

Clase Inmueble:
Atributos:
  + identificador inmobiliario (numero)
  + cantidadHabitaciones (numero)
  + area (numero) en metros cuadrados
  + direccion (texto)
  + precioVenta (numero)
Metodos:
  + calcularPrecio(valorArea): calcular y devolver precioVenta = area * valorArea
  + __str__(): devolver todos los atributos.

Clase Casa, hereda de Inmueble:
Atributos:
  + cantidadPisos (numero)
Metodos:
  + __str__(): devolver todos los atributos.

Clase Departamento, hereda de Inmueble:
Atributos:
  + numeroPiso (numero)
Metodos:
  + __str__(): devolver todos los atributos.

Clase CasaRural, hereda de Casa:
Atributos:
  + distancia (numero) a la municipalidad mas cercana
  + altitud (numero)
Metodos:
  + __str__(): devolver todos los atributos.

Clase CasaUrbana, hereda de Casa:
Atributos:
  + tienePileta (boolean)
Metodos:
  + __str__(): devolver todos los atributos.

Clase DepartamentoFamiliar, hereda de Departamento:
atributos:
  + cantidadFamiliares (numero)
Metodos:
  + __str__(): devolver todos los atributos.

Clase DepartamentoEstudio, hereda de Departamento:
atributos:
  + cantidadEmpleados (boolean)
Metodos:
  + __str__(): devolver todos los atributos.

