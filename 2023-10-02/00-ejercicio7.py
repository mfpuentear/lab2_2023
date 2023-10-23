class Vehiculo():
  def __init__(self, placa, valor_peaje):
    self.placa = placa
    self.valor_peaje = valor_peaje 

class Moto(Vehiculo):
  def __init__(self, placa):
    super().__init__(placa, 150)

class Auto(Vehiculo):
  def __init__(self, placa):
    super().__init__(placa, 300)

class Camion(Vehiculo):
  def __init__(self, placa, cantidad_ejes):
    super().__init__(placa, cantidad_ejes * 500)
    self.cantidad_ejes = cantidad_ejes

class Peaje():
  def __init__(self, nombre, departamento):
    self.nombre = nombre
    self.departamento = departamento
    self.vehiculos = []

  def agregar_vehiculo(self, vehiculo):
    self.vehiculos.append(vehiculo)

  def calcular_total_peaje(self):
    total = 0
    for vehiculo in self.vehiculos:
      total += vehiculo.valor_peaje
    return total

  def cantidad_vehiculos(self):
    return len(self.vehiculos)


peaje = Peaje('autopista', 'Rosario')

peaje.agregar_vehiculo(Moto('ABC'))
peaje.agregar_vehiculo(Moto('CBA'))
peaje.agregar_vehiculo(Auto('DBA'))
peaje.agregar_vehiculo(Auto('JIK'))
peaje.agregar_vehiculo(Camion('LOY', 3))

print('Cantidas vehiculos', peaje.cantidad_vehiculos())
print('Total peaje', peaje.calcular_total_peaje())

