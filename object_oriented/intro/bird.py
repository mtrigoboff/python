from animal import Animal

class Bird(Animal):

	# constructor
	def __init__(self, species, can_fly):
		super().__init__('bird', 'feathers')
		self.species = species
		self.can_fly = can_fly
	
	def __str__(self):
		if self.can_fly:
			not_str = ''
		else:
			not_str = 'not'
		return f'The {self.species} can{not_str} fly {super().__str__()}'

