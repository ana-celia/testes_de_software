import unittest
from triangulo import Triangulo

class TestTriangulo(unittest.TestCase):
  # Testa triângulos válidos
  def test_eh_valido(self):
    self.assertTrue(Triangulo(3, 4, 5).eh_valido())

  # Testa triângulos inválidos
  def test_invalido_lado_igual_a_zero(self):
    self.assertFalse(Triangulo(0, 1, 2).eh_valido())
    self.assertFalse(Triangulo(1, 0, 2).eh_valido())
    self.assertFalse(Triangulo(1, 2, 0).eh_valido())

  def test_invalido_lado_menor_que_zero(self):
    self.assertFalse(Triangulo(-1, 2, 3).eh_valido())
    self.assertFalse(Triangulo(1, -2, 3).eh_valido())
    self.assertFalse(Triangulo(1, 2, -3).eh_valido())

  def test_invalido_soma_dos_lados_igual_ao_terceiro_lado(self):
    self.assertFalse(Triangulo(1, 1, 2).eh_valido())
    self.assertFalse(Triangulo(1, 2, 1).eh_valido())
    self.assertFalse(Triangulo(2, 1, 1).eh_valido())

  def test_invalido_soma_dos_lados_menor_que_terceiro_lado(self):
    self.assertFalse(Triangulo(1, 1, 3).eh_valido())
    self.assertFalse(Triangulo(1, 3, 1).eh_valido())
    self.assertFalse(Triangulo(1, 1, 3).eh_valido())

  # Testa triângulos equiláteros
  def test_eh_equilatero(self):
    self.assertTrue(Triangulo(5, 5, 5).eh_equilatero())

  # Testa triângulos que não são equiláteros
  def test_nao_eh_equilatero(self):
    self.assertFalse(Triangulo(0, 4, 5).eh_equilatero())
    self.assertFalse(Triangulo(5, -1, 5).eh_equilatero())
    self.assertFalse(Triangulo(5, 4, -2).eh_equilatero())
    self.assertFalse(Triangulo(5, 12, 12).eh_equilatero())
    self.assertFalse(Triangulo(8, 8, 9).eh_equilatero())
    self.assertFalse(Triangulo(4, 4, 3).eh_equilatero())

  # Testa triângulos isósceles
  def test_eh_isoceles(self):
    self.assertTrue(Triangulo(4, 3, 3).eh_isoceles())
    self.assertTrue(Triangulo(2, 1, 2).eh_isoceles())
    self.assertTrue(Triangulo(5, 5, 7).eh_isoceles())
    self.assertTrue(Triangulo(4, 4, 2).eh_isoceles())

  # Testa triângulos que não são isósceles
  def test_nao_eh_isoceles(self):
    self.assertFalse(Triangulo(0, 1, 2).eh_isoceles())
    self.assertFalse(Triangulo(1, 0, 1).eh_isoceles())
    self.assertFalse(Triangulo(1, 1, 0).eh_isoceles())
    
  def test_nao_eh_isoceles_lados_diferentes(self):
    self.assertFalse(Triangulo(4, 2, 3).eh_isoceles())
    self.assertFalse(Triangulo(5, 4, 8).eh_isoceles())

  def test_nao_eh_isoceles_lados_iguais(self):
    self.assertFalse(Triangulo(1, 1, 1).eh_isoceles())

  # Testa triângulos escalenos
  def test_eh_escaleno(self):
    self.assertTrue(Triangulo(3, 4, 5).eh_escaleno())

  # Testa triângulos que não são escalenos
  def test_nao_eh_escaleno(self):
    self.assertFalse(Triangulo(-3, 4, 5).eh_escaleno())
    self.assertFalse(Triangulo(7, -2, 10).eh_escaleno())
    self.assertFalse(Triangulo(3, 4, -1).eh_escaleno())
    self.assertFalse(Triangulo(5, 4, 5).eh_escaleno())
    self.assertFalse(Triangulo(7, 7, 10).eh_escaleno())
    self.assertFalse(Triangulo(3, 4, 4).eh_escaleno())

if __name__ == '__main__':
  unittest.main()
