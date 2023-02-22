class Animal:

    def __init__(self, name, species, skin_type):
        self._name = name
        self._species = species
        self._skin_type = skin_type
    
    def __str__(self):
        return f'species: {self._species}, skin: {self._skin_type}, name: {self._name}'

class Mammal(Animal):

    def __init__(self, name, species, sound):
        super().__init__(name, species, 'fur')
        self._sound = sound

    def __str__(self):
        return f'sound: {self._sound}, {super().__str__()}'

class Bird(Animal):

    def __init__(self, name, species):
        super().__init__(name, 'bird', 'feathers')
        self._sound = 'tweet'

    def __str__(self):
        return f'sound: {self._sound}, {super().__str__()}'

class Fish(Animal):

    def __init__(self, name, species):
        super().__init__(name, species, 'scales')

teddy = Mammal('Teddy', 'bear', 'growl')
tweety = Bird('Tweety', 'canary')
goldy = Fish('Goldy', 'goldfish')

print(teddy)
print(tweety)
print(goldy)

pass
