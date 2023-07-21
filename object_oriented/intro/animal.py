class Animal:

	# used for implementing a unique id number for each instance
	_next_id = 1								# class variable

	def __init__(self, kind, skin_type):
		self._kind = kind
		self._skin_type = skin_type
		self._instance_id = Animal._next_id		# store id number
		Animal._next_id += 1					# next id number

	def __str__(self):
		return f'and is covered in {self._skin_type} (id: {self._instance_id}).'
