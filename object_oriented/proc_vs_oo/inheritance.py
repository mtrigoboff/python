class Animal:

    def __init__(self, species, skin_type):
        self._species = species
        self._skin_type = skin_type
    
    def __str__(self):
        return f'species: {self._species}, skin: {self._skin_type}'

class LandAnimal(Animal):

    def __init__(self, species, sound, skin_type):
        super().__init__(species, skin_type)
        self._sound = sound
        self._n_feet = 4

    def __str__(self):
        return f'sound: {self._sound}, n_feet: {self._n_feet}, {super().__str__()}'

class FlyingAnimal(Animal):

    def __init__(self, species, sound, skin_type, n_feet):
        super().__init__(species, skin_type)
        self._sound = sound
        self._n_feet = n_feet

    def __str__(self):
        return f'sound: {self._sound}, n_feet: {self._n_feet}, {super().__str__()}'

class Bear(LandAnimal):

    def __init__(self, name):
        self.name = name
        super().__init__('bear', 'growl', 'fur')

    def __str__(self):
        return f'name: {self.name}, {super().__str__()}'

class Armadillo(LandAnimal):

    def __init__(self, name):
        self.name = name
        super().__init__('armadillo', None, 'scales')

    def __str__(self):
        return f'name: {self.name}, {super().__str__()}'

class Bird(FlyingAnimal):

    def __init__(self, name):
        self.name = name
        super().__init__('bird', 'tweet', 'feathers', 2)

    def __str__(self):
        return f'name: {self.name}, {super().__str__()}'


bear = Bear('Teddy')
armadillo = Armadillo('Scaly')
bird = Bird('Tweety')

print(bear)
print(armadillo)
print(bird)

pass
