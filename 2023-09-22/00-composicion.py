# Composicion

class Punto():
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __str__(self):
    return f'({self.x}, {self.y})'

class Linea():
  def __init__(self, xa, ya, xb, yb):
    self.punto_a = Punto(xa, ya)
    self.punto_b = Punto(xb, yb)

  def __str__(self):
    return f'({self.punto_a}, {self.punto_b})'


linea = Linea(10, 10, 10, 5)

print(linea.punto_a)
print(linea.punto_b)
print(linea)