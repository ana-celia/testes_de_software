import unittest 
from TP4.ex1.modelo1 import Celsius

class TestTemperatureConversion(unittest.TestCase):
    def test_construtor_1(self):
        c = Celsius(23)
        f = c.convert_celsius_to_fahrenheit
        self.assertNotEqual(c,f)
        