import unittest
from modelo import calcular_desconto_dependente

# Contrua uma função (em python) que realize o cálculo do desconto por dependente. A função
# recebe um valor, e a idade do dependente. A idade do dependente deve estar restrita ao inter-
# valo [0..24]. O valor mínimo da compra deve ser 250,00 reais. Para dependentes até 12 anos
# (inclusive) o desconto é de 15%. Entre 13 e 18 (inclusive) o desconto é de 12%. Dos 19 aos 21
# (inclusive) o desconto é de 5% e dos 22 aos 24 de 3%.

class TesteDescontoDependente(unittest.TestCase):

    def test_valor_compra_minimo(self):
        with self.assertRaises(ValueError):
            calcular_desconto_dependente(100, 10)

    def test_idade_dependente_minima(self):
        self.assertEqual(calcular_desconto_dependente(300, 0), 45)

    def test_idade_dependente_maxima(self):
        self.assertEqual(calcular_desconto_dependente(300, 24), 9)

    def test_desconto_abaixo_limite_minimo_idade(self):
        self.assertEqual(calcular_desconto_dependente(300, 0), 45)

    def test_desconto_acima_limite_maximo_idade(self):
        self.assertEqual(calcular_desconto_dependente(300, 25), 9)

    def test_desconto_igual_limite_minimo_idade(self):
        self.assertEqual(calcular_desconto_dependente(300, 1), 45)

    def test_desconto_igual_limite_maximo_idade(self):
        self.assertEqual(calcular_desconto_dependente(300, 24), 9)

    def test_desconto_ate_12_anos(self):
        self.assertEqual(calcular_desconto_dependente(300, 12), 45)

    def test_desconto_13_a_18_anos(self):
        self.assertEqual(calcular_desconto_dependente(300, 15), 36)

    def test_desconto_19_a_21_anos(self):
        self.assertEqual(calcular_desconto_dependente(300, 20), 15)

    def test_desconto_22_a_24_anos(self):
        self.assertEqual(calcular_desconto_dependente(300, 22), 9)

    def test_valor_compra_igual_zero(self):
        with self.assertRaises(ValueError):
            calcular_desconto_dependente(0, 10)

    def test_valor_compra_negativo(self):
        with self.assertRaises(ValueError):
            calcular_desconto_dependente(-100, 10)

    def test_idade_dependente_igual_zero(self):
        self.assertEqual(calcular_desconto_dependente(300, 0), 45)

    def test_idade_dependente_negativa(self):
        with self.assertRaises(ValueError):
            calcular_desconto_dependente(300, -10)

if __name__ == '__main__':
    unittest.main()

