import unittest
from modelo import Triangulo

# Resposta a) Condições: 
# 1- É triangulo: precisa ter três lados a, b, c em que o valor de cada lado deve ser menor que a soma dos outros 2 lados
# 2- É equilátero: precisa ser triângulo + 3 lados iguais
# 3- É isosceles: precisa ser triângulo + apenas 2 lados iguais
# 4- É escaleno: precisa ser triângulo + todos os 3 lados diferentes
# Respostas b) e c) Para cada condição, classes válidas e inválidas para cada entrada de a, b e de c, logo:
# 1- É triangulo: 
# válidos: entradas para cada lado que sejam valores positivos, diferentes de zero e menor que a soma dos outros dois lados; 
# inválidos: valores negativos, iguais a zero e maiores ou iguais a soma dos outros dois lados.
# 2- É equilátero: 
# válidos: cada entrada precisa ser igual às outras duas; 
# inválidos: qualquer entrada ser diferente das outras duas.
# 3- É isosceles: 
# válidos: testar se uma das entradas é diferente e as outras duas iguais; 
# inválidos: testar se mais de uma entrada de lado é diferente e se é equilátero.
# 4- É escaleno: 
# válidos: ver se cada entrada é diferente da outra;
# inválidos: checar se existem lados iguais.
# d) ver no código


#Inicialmente se certificar que é um triângulo
class TrianguloTeste (unittest.TestCase):
   
    def test_eh_triangulo (self):
        a, b, c = 8, 9, 10
        t = Triangulo(a, b, c)
        self.assertTrue(t.validarForma())

#testar as classes inválidas que em que os valores de a, b, e c são maiores e/ou menores às condições válidas de triângulo em modelo.py
    def test_todos_zeros (self): #inválidos valores = zero 
        a, b, c = 0, 0, 0
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    def test_todos_menor (self): #inválidos valores negativos
        a, b, c = -5, -6, -7 
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    def test_a_igual_soma (self): #inválidos valores de a=b+c
        a, b, c = 7, 3, 4
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())
    
    def test_a_maior_soma (self): #inválidos valores de a>b+c
        a, b, c = 8, 3, 4
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    def test_b_igual_soma (self): #inválidos valores de b=a+c
        a, b, c = 3, 7, 4
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())
      
    def test_b_maior_soma (self): #inválidos valores de b>a+c
        a, b, c = 4, 8, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    def test_c_igual_soma (self): #inválidos valores de c=b+a
        a, b, c = 3, 4, 7
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

    def test_c_maior_soma (self): #inválidos valores de c>b+a
        a, b, c = 3, 4, 8
        t = Triangulo(a, b, c)
        self.assertFalse(t.validarForma())

class TesteTrianguloEquilatero (unittest.TestCase): 

    def test_ehEquilatero (self): #válidos valores de a, b, c
        a, b, c = 3, 3, 3
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehEquilatero())
      
    def test_a_diferente (self): #inválido valor de a
        a, b, c = 4, 3, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEquilatero())

    def test_b_diferente (self): #inválido valor de b
        a, b, c = 3, 4, 3
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEquilatero())

    def test_c_diferente (self): #inválido valor de c
        a, b, c = 3, 3, 4
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEquilatero())

class TesteTrianguloIsosceles (unittest.TestCase):
    def test_ehIsoscelesAB (self): #válidos valores de a, b, c - sendo um lado diferente e dois lados iguais
        a, b, c = 5, 5, 6
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehIsosceles())

    def test_ehIsoscelesAC (self):
        a, b, c = 5, 6, 5
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehIsosceles())

    def test_ehIsoscelesBC (self):
        a, b, c = 6, 5, 5
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehIsosceles())

    def test_ehIsoscelesiguais (self): #inválidos valores de a, b, c
        a, b, c = 5, 5, 5
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehIsosceles())

    def test_ehIsoscelesdiferentes (self): #inválidos valores de a, b, c
        a, b, c = 5, 6, 7
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehIsosceles())

class TesteTrianguloEscaleno (unittest.TestCase): #válidos valores de a, b, c - todos diferentes entre si

    def test_ehEscaleno (self):
        a, b, c = 5, 6, 7
        t = Triangulo(a, b, c)
        self.assertTrue(t.ehEscaleno())

    def test_ehEscaleno_AB (self):
        a, b, c = 5, 5, 6   #inválidos valores de a e b
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEscaleno())

    def test_ehEscaleno_AC (self):
        a, b, c = 5, 6, 5   #inválidos valores de a e c
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEscaleno())
       
    def test_ehEscaleno_BC (self):
        a, b, c = 5, 6, 6   #inválidos valores de b e c
        t = Triangulo(a, b, c)
        self.assertFalse(t.ehEscaleno())

if __name__ == "__main__":
    unittest.main()
