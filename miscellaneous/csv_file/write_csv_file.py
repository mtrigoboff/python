import os.path

data = [[1, 2, 3],
		[4, 5, 6]]

csv_file = open(os.path.join('csv_file', 'data.csv'), 'w')
for row in data:

	# 'pythonic' code
	print(''.join([str(item) + ',' for item in row])[:-1], file=csv_file)

	# more straightforward (but probably slower) code
	'''
	line = ''

	for item in row:
		line += str(item) + ','
	print(line[:-1], file=csv_file)
	'''

csv_file.close()
