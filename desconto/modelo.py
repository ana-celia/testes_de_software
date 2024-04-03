import datetime

class Desconto_idade_dependente:
    def __init__(self, valor_compra, idade_dependente):
        self.valor_compra = valor_compra
        self.idade_dependente = idade_dependente
        
    def calcular_desconto_dependente(valor_compra, idade_dependente):
        if valor_compra < 250:
            raise ValueError("O valor mínimo da compra deve ser de R$ 250,00")
        if idade_dependente < 0 or idade_dependente > 24:
            raise ValueError("A idade do dependente deve estar no intervalo de 0 a 24 anos")
        if idade_dependente <= 12:
            return valor_compra * 0.15
        elif idade_dependente <= 18:
            return valor_compra * 0.12
        elif idade_dependente <= 21:
            return valor_compra * 0.05
        else:
            return valor_compra * 0.03
