
class Celsius:
    def __init__(self, celsius):
        self._celsius = celsius

    @property 
    def celsius(self):
        return 5
    
    def convert_celsius_to_fahrenheit(celsius):
        f = (celsius*9/5) + 32
        return f