class Animal:

	# class (static) variable
	_kingdom_name = 'Animal'

	@staticmethod
	def kingdom():
		return Animal._kingdom_name

	def species(self):
		raise NotImplementedError(f'{type(self).__name__} does not implement species()')

	def sound(self):
		raise NotImplementedError(f'{type(self).__name__} does not implement sound()')

	def n_feet(self):
		raise NotImplementedError(f'{type(self).__name__} does not implement n_feet()')
	
	def __str__(self):
		return 'kingdom:' + Animal._kingdom_name

class Bear(Animal):
	
	def species(self):
		return 'Bear'

	def sound(self):
		return 'Growl'

	def n_feet(self):
		return 4

	def __str__(self):
		return f'species:{self.species()}, sound:{self.sound()}, n_feet:{self.n_feet()}, {super().__str__()}'
	
class Bird(Animal):

	def species(self):
		return 'Bird'

	def sound(self):
		return 'Tweet'

	def n_feet(self):
		return 2

	def __str__(self):
		return f'species:{self.species()}, sound:{self.sound()}, n_feet:{self.n_feet()}, {super().__str__()}'

class Snake(Animal):

	def species(self):
		return 'Snake'
	
	def sound(self):
		return 'Hiss'

	def __str__(self):
		return f'species:{self.species()}, sound:{self.sound()}, n_feet:{self.n_feet()}, {super().__str__()}'

animals = (Bear(), Bird(), Snake(), Animal())

def main():
	print('Object Oriented')
	print('---------------')
	for animal in animals:
		try:
			species = animal.species()
			sound = animal.sound()
			n_feet = animal.n_feet()
			kingdom = animal.kingdom()
			print(f'species:{species}, sound:{sound}, n_feet:{n_feet}, kingdom:{kingdom}')
			print(f'__str__: {animal}')
		except NotImplementedError as err:
			print(f'error: {err}')
		print()

main()