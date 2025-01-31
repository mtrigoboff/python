class Battery:
    def __init__(self, volts):
        self._volts = volts				# calls setter as it should
										# (no direct use of  _volts)
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
v = b.volts								# calls getter
print(v, 'volts')
b.volts = 1.5							# calls setter
print(b)
