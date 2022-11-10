# Python code that demonstrates the inner mechanism of a Python dictionary

class KeyValuePair:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class HashTable:

	def __init__(self, arraySize):
		self.arraySize = arraySize
		self.array = [[] for n in range(arraySize)]

	# https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/lang/String.html#hashCode()
	@staticmethod
	def hashFn(word):
		hashCode = 0;
		pow31 = 1;
		for i in range(len(word) - 1, -1, -1):
			hashCode += ord(word[i]) * pow31;
			pow31 *= 31;
		return hashCode & 0xFFFFFFFF		# limit to range(0, 2^32)

	# get value for key, return None if key not present
	def get(self, key):
		hashCode = HashTable.hashFn(key)				# hash the key
		hashIndex = hashCode % self.arraySize			# limit to legal list index
		hashBucket = self.array[hashIndex]				# get list from array
		
		# see if we already have a Pair with this key
		for pair in hashBucket:
			if pair.key == key:
				return pair.value
		
		# we didn't
		return None

	# store value for key, return previous value for key, None if no previous value
	def put(self, key, value):
		hashCode = HashTable.hashFn(key)				# hash the key
		hashIndex = hashCode % self.arraySize			# limit to legal list index
		hashBucket = self.array[hashIndex]				# get list from array
		
		# see if we already have a Pair with this key
		for pair in hashBucket:
			if pair.key == key:
				oldValue = pair.value
				pair.value = value
				return oldValue
		
		# we didn't, so add new pair
		hashBucket.append(KeyValuePair(key, value))
		return None

def run():
	ht = HashTable(8)

	ht.put('alpha', 1)
	ht.put('bravo', 2)
	ht.put('charlie', 3)
	
	val = ht.get('charlie')
	
	val = ht.get('delta')
	pass

run()