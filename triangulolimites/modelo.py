class Triangulo:
  def __init__(self, lado1=None, lado2=None, lado3=None):
    self._lado1 = lado1
    self._lado2 = lado2
    self._lado3 = lado3

  def eh_valido(self):
    if self._lado1 > 0 and self._lado2 > 0 and self._lado3 > 0:
      if self._lado1 + self._lado2 > self._lado3: 
        if self._lado1 + self._lado3 > self._lado2:
          if self._lado2 + self._lado3 > self._lado1:
            return True
    return False

  def eh_equilatero(self):
    if self.eh_valido():
      if self._lado1 == self._lado2 and self._lado2 == self._lado3:
        return True
    return False

  def eh_isoceles(self):
    if self.eh_valido():
      if not self.eh_equilatero():
        if self._lado1 == self._lado2 or self._lado1 == self._lado3 or self._lado2 == self._lado3:
          return True
    return False

  def eh_escaleno(self):
    if self.eh_valido():
      if self._lado1 != self._lado2 and self._lado1 != self._lado3 and self._lado2 != self._lado3:
        return True
    return False
