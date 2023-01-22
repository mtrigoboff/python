class Animal:

	# used for implementing a unique id number for each instance
	instance_id = 0		# class variable

	def __init__(self, kind, skin_type):
		self.kind = kind
		self.skin_type = skin_type
		Animal.instance_id += 1					# next id number
		self.instance_id = Animal.instance_id	# store id number

	def __str__(self):
		return f'and is covered in {self.skin_type} (id: {self.instance_id}).'
