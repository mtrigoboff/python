class Battery:
    def __init__(self, volts):
        self.volts = volts				# calls setter
										# (does NOT use _volts)
    @property
    def volts(self):					# getter
        return self._volts
    
    @volts.setter						# setter
    def volts(self, volts):
        self._volts = volts
    
    def __str__(self):
        return f'{self.volts} volts'	# calls getter

b = Battery(9)
print(b)
v = b.volts
print(v, 'volts')
b.volts = 1.5
print(b)
