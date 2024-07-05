
import math

class Fracao:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError(  'Denominador deve ser diferente de zero')
        
    #     #reduzindo a fracao
    # def mdc(self, numerador, denominador):    
    #     mdc = 1
    #     for i in range(min(numerador,denominador), 1, -1):
    #         if numerador % i == 0 and denominador % i == 0:
    #             mdc = 1
    #             break
    #     return mdc

    @property
    def numerador(self):
        return self._numerador

    @property
    def denominador(self):
        return self._denominador
