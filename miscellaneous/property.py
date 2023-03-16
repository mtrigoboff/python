class Battery:
    def __init__(self, volts):
        self.volts = volts

    @property
    def volts(self):
        return self._volts
    
    @volts.setter
    def volts(self, volts):
        self._volts = volts
    
    def __str__(self):
        return f'{self.volts} volts'

b = Battery(9)
print(b)
v = b.volts
print(v)
b.volts = 1.5
print(b)
