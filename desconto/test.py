import unittest
from desconto import calcular_desconto

class TestTriangulo(unittest.TestCase):
  # Testa limite de valores de Valor para cálculo de desconto
  def test_valor_invalido_limite_inferior(self):
    self.assertEqual(calcular_desconto(249.99, 5), 0)
  def test_valor_valido_limite_superior(self):
    self.assertNotEqual(calcular_desconto(250, 5), 0)
  def test_valor_valido_acima_limite_superior (self):
    self.assertNotEqual(calcular_desconto(250.01, 5), 0)

  # Testa limite de valores de Idade inválidos para cálculo de desconto
  def test_idade_invalida_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, -1), 0) 
  def test_idade_invalida_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 25), 0)

  # Testa limite de valores de Idade entre 0 e 12 para cálculo de desconto
  def test_faixa_idade_0_a_12_invalida_limite_inferior(self):
    self.assertNotEqual(calcular_desconto(250, -1), 250*0.15)
  def test_faixa_idade_0_a_12_valida_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, 0), 250*0.15)
  def test_faixa_idade_0_a_12_valida_acima_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, 1), 250*0.15)
  def test_faixa_idade_0_a_12_valida_abaixo_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 11), 250*0.15)
  def test_faixa_idade_0_a_12_valida_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 12), 250*0.15)
  def test_faixa_idade_0_a_12_invalida_acima_limite_superior(self):
    self.assertNotEqual(calcular_desconto(250, 13), 250*0.15)

  # Testa limite de valores de Idade entre 13 e 18 para cálculo de desconto
  def test_faixa_idade_13_a_18_invalida_limite_inferior(self):
    self.assertNotEqual(calcular_desconto(250, 12), 250*0.12)
  def test_faixa_idade_13_a_18_valida_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, 13), 250*0.12)
  def test_faixa_idade_13_a_18_valida_acima_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, 14), 250*0.12)
  def test_faixa_idade_13_a_18_valida_abaixo_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 17), 250*0.12)
  def test_faixa_idade_13_a_18_valida_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 18), 250*0.12)
  def test_faixa_idade_13_a_18_invalida_acima_limite_superior(self):
    self.assertNotEqual(calcular_desconto(250, 19), 250*0.12)

  # Testa limite de valores de Idade entre 19 e 21 para cálculo de desconto
  def test_faixa_idade_19_a_21_invalida_limite_inferior(self):
    self.assertNotEqual(calcular_desconto(250, 18), 250*0.05)
  def test_faixa_idade_19_a_21_valida_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, 19), 250*0.05)
  def test_faixa_idade_19_a_21_valida_acima_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, 20), 250*0.05)
  def test_faixa_idade_19_a_21_valida_abaixo_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 20), 250*0.05)
  def test_faixa_idade_19_a_21_valida_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 21), 250*0.05)
  def test_faixa_idade_19_a_21_invalida_acima_limite_superior(self):
    self.assertNotEqual(calcular_desconto(250, 22), 250*0.05)

  # Testa limite de valores de Idade entre 22 e 24 para cálculo de desconto
  def test_faixa_idade_22_a_24_invalida_limite_inferior(self):
    self.assertNotEqual(calcular_desconto(250, 21), 250*0.03)
  def test_faixa_idade_22_a_24_valida_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, 22), 250*0.03)
  def test_faixa_idade_22_a_24_valida_acima_limite_inferior(self):
    self.assertEqual(calcular_desconto(250, 23), 250*0.03)
  def test_faixa_idade_22_a_24_valida_abaixo_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 23), 250*0.03)
  def test_faixa_idade_22_a_24_valida_limite_superior(self):
    self.assertEqual(calcular_desconto(250, 24), 250*0.03)
  def test_faixa_idade_22_a_24_invalida_acima_limite_superior(self):
    self.assertNotEqual(calcular_desconto(250, 25), 250*0.03)
    
if __name__ == '__main__':
  unittest.main()
