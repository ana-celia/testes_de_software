'''
Questão: Contrua uma função (em python) que realize o cálculo do desconto por dependente. A função
recebe um valor, e a idade do dependente. A idade do dependente deve estar restrita ao inter-
valo [0..24]. O valor mínimo da compra deve ser 250,00 reais. Para dependentes até 12 anos
(inclusive) o desconto é de 15%. Entre 13 e 18 (inclusive) o desconto é de 12%. Dos 19 aos 21
(inclusive) o desconto é de 5% e dos 22 aos 24 de 3%.'''

def calcular_desconto(valor, idade):
  if valor < 250:
    return 0
  elif idade >= 0 and idade <= 12:
    return valor * 0.15
  elif idade >= 13 and idade <= 18:
    return valor * 0.12
  elif idade >= 19 and idade <= 21:
    return valor * 0.05
  elif idade >= 22 and idade <= 24:
    return valor * 0.03
  else:
    return 0
