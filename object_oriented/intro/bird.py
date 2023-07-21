from animal import Animal

class Bird(Animal):

	# constructor
	def __init__(self, species, can_fly):
		super().__init__('bird', 'feathers')
		self._species = species
		self._can_fly = can_fly
	
	def __str__(self):
		if self._can_fly:
			not_str = ''
		else:
			not_str = 'not'
		return f'The {self._species} can{not_str} fly {super().__str__()}'

