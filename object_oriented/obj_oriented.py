class Animal:

	# class (static) variable
	kingdomName = 'Animal'

	@staticmethod
	def kingdom():
		return Animal.kingdomName

	def species(self):
		raise NotImplementedError(f'{type(self).__name__} does not implement species()')

	def sound(self):
		raise NotImplementedError(f'{type(self).__name__} does not implement sound()')

	def nFeet(self):
		raise NotImplementedError(f'{type(self).__name__} does not implement nFeet()')
	
	def __str__(self):
		return 'kingdom:' + Animal.kingdomName

class Bear(Animal):
	
	def species(self):
		return 'Bear'

	def sound(self):
		return 'Growl'

	def nFeet(self):
		return 4

	def __str__(self):
		return f'species:{self.species()}, sound:{self.sound()}, nFeet:{self.nFeet()}, {super().__str__()}'
	
class Bird(Animal):

	def species(self):
		return 'Bird'

	def sound(self):
		return 'Tweet'

	def nFeet(self):
		return 2

	def __str__(self):
		return f'species:{self.species()}, sound:{self.sound()}, nFeet:{self.nFeet()}, {super().__str__()}'

class Snake(Animal):

	def species(self):
		return 'Snake'
	
	def sound(self):
		return 'Hiss'

	def __str__(self):
		return f'species:{self.species()}, sound:{self.sound()}, nFeet:{self.nFeet()}, {super().__str__()}'

animals = (Bear(), Bird(), Snake())

def main():
	print('Object Oriented')
	print('---------------')
	for animal in animals:
		try:
			species = animal.species()
			sound = animal.sound()
			nFeet = animal.nFeet()
			kingdom = animal.kingdom()
			print(f'species:{species}, sound:{sound}, nFeet:{nFeet}, kingdom:{kingdom}')
			print(f'__str__: {animal}')
		except NotImplementedError as err:
			print(f'error: {err}')
		print()

main()