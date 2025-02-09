class queue:

	def __init__(self):
		self._list = []
	
	def enqueue(self, item):
		self._list.append(item)

	def peek(self):
		return self._list[0]
	
	def dequeue(self):
		item = self._list[0]
		self._list = self._list[1:]
		return item
	
q = queue()

for i in range(5):
	q.enqueue(i)

for i in range(5):
	print(q.dequeue()) 
