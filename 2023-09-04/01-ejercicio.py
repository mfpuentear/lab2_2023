# 8- Realizar una clase que represente una estructura de datos de tipo ‘Pila’ 
# con una lista como atributo. Incluir los siguientes métodos:
#• constructor: inicializa lista vacía.
#• agregar(): agrega un elementos al final de la lista.
#• quitar(): quita el ultimo elemento de la lista y lo devuelve.
#• estaVacia(): devuelve True si la lista esta vacía.
#• cantidad(): devuelve cantidad de elementos ingresados

class Pila():
  def __init__(self):
    self.lista = []
  
  def agregar(self, elemento):
    self.lista.append(elemento)

  def quitar(self):
    if not self.estaVacia():
      return self.lista.pop()
    else:
      print('Pila vacia')

  def estaVacia(self):
    return len(self.lista)==0
  
  def cantidad(self):
    return len(self.lista)

pila = Pila()


print('Se quito: ', pila.quitar())
pila.agregar(5)
pila.agregar(6)
print(pila.lista)
print('Se quito: ', pila.quitar())
print(pila.lista)

pila.agregar(2)
pila.agregar(8)
print(pila.lista)
print('Se quito: ', pila.quitar())
print(pila.lista)

