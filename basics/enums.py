from enum import Enum

class Color(Enum):
	RED =	(255, 0, 0)
	GREEN =	(0, 255, 0)
	BLUE =	(0, 0, 255)

	def __str__(self):
		name_str = self.name + ':'
		return f'{name_str:8s}({self.value[0]:3d}, {self.value[1]:3d}, {self.value[2]:3d})'

for element in Color:
	print(element)
	