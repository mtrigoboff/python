from animal import Animal

class Fish(Animal):

	# constructor
	def __init__(self, species, is_carniverous):
		super().__init__('fish', 'scales')
		self._species = species
		self._is_carniverous = is_carniverous
	
	def __str__(self):
		if self._is_carniverous:
			not_str = ''
		else:
			not_str = 'not '
		return f'The {self._species} is {not_str}carniverous {super().__str__()}'


