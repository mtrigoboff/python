from animal import Animal

class Fish(Animal):

	# constructor
	def __init__(self, species, is_carniverous):
		super().__init__('fish', 'scales')
		self.species = species
		self.is_carniverous = is_carniverous
	
	def __str__(self):
		if self.is_carniverous:
			not_str = ''
		else:
			not_str = 'not '
		return f'The {self.species} is {not_str}carniverous {super().__str__()}'


