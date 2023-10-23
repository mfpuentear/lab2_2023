class Objeto():
  def __init__(self, atributo):
    self.atributo = atributo
    
  def mostrar(self):
    print(self.atributo)

obj = Objeto(5)
obj2 = Objeto(5)

obj.mostrar()
obj2.mostrar()

obj.atributo = 6

obj.mostrar()
obj2.mostrar()
