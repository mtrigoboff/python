listDict = [['alpha', 1], ['bravo', 2], ['charlie', 3]]

pythonDict = {'alpha':1, 'bravo':2, 'charlie':3}		# initialize with 3 key-value pairs

print(pythonDict)
print()

# get value for key 'bravo'
key = 'bravo'
value = pythonDict[key]
print(f'pythonDict[{key}] = {value}')
print()

# print the pairs the default way
for pair in pythonDict.items():
	print(pair)
print()

pythonDict['delta'] = 4									# add new pair

# print the pairs with full control
for key in pythonDict:
	print(key, pythonDict[key])
print()

keys = pythonDict.keys()
print(keys)												# print the keys
print()

values = pythonDict.values()
print(values)											# print the values
print()
