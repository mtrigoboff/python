unknownAnimalStr = 'unknown animal '

def sound(animal):
	if animal == 'Bear':
		return 'Growl'
	elif animal == 'Bird':
		return 'Tweet'
	else:
		raise TypeError(unknownAnimalStr + animal)

def nFeet(animal):
	if animal == 'Bear':
		return 4
	elif animal == 'Bird':
		return 2
	else:
		raise TypeError(unknownAnimalStr + animal)

animals = ('Bear', 'Bird', 'Snake')

def main():
	print('Procedural')
	print('----------')
	for animal in animals:
		try:
			snd = sound(animal)
			nFt = nFeet(animal)
			print(f'species:{animal}, sound:{snd}, nFeet:{nFt}')
		except TypeError as err:
			print(f'error: {err}')

main()