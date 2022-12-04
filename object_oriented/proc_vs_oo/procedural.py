unknown_animal_str = 'unknown animal '

def sound(animal):
	if animal == 'Bear':
		return 'Growl'
	elif animal == 'Bird':
		return 'Tweet'
	else:
		raise TypeError(unknown_animal_str + animal)

def n_feet(animal):
	if animal == 'Bear':
		return 4
	elif animal == 'Bird':
		return 2
	else:
		raise TypeError(unknown_animal_str + animal)

animals = ('Bear', 'Bird', 'Snake')

def main():
	print('Procedural')
	print('----------')
	for animal in animals:
		try:
			snd = sound(animal)
			nFt = n_feet(animal)
			print(f'species:{animal}, sound:{snd}, n_feet:{nFt}')
		except TypeError as err:
			print(f'error: {err}')

main()