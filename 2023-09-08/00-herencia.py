class Persona:
  def __init__(self, apellido, nombre):
    print('en constructor de persona')
    self.apellido = apellido
    self.nombre = nombre
  
  def __str__(self):
    print('en __str__ de persona')
    return f"{self.apellido}, {self.nombre}"

class Estudiante(Persona):
  def __init__(self, apellido, nombre, nota):
    print('en constructor de estudiante')
    super().__init__(apellido, nombre)
    self.nota = nota

  def __str__(self):
    print('en __str__ de estudiante')
    return super().__str__() + f', {self.nota}'
    #return f"{self.apellido}, {self.nombre}, {self.nota}"
  

estudiante = Estudiante('Sanchez', 'Pepe', 5)
print(estudiante)

persona = Persona('otra', 'persona')
print(persona)

  