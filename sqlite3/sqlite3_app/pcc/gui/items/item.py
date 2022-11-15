class Item(object):		# must explicitly inherit from object to enable use of super() in subclasses

	def __init__(self, window, name):
		self.wn = window
		self.name = name
		self.wn.items[name] = self
		self.padding = 4

	def getValue(self):
		raise NotImplementedError("'{}' has no getValue() function".format(self.name))

	def setValue(self, name, value):
		raise NotImplementedError("'{}' has no setValue() function".format(self.name))

	def setEnabled(self, enabled):
		raise NotImplementedError("'{}' has no setEnabled() function".format(self.name))

	def grid(self, row, col):
		raise NotImplementedError("'{}' has no grid() function".format(self.name))
