import os.path

data = [[1, 2, 3],
		[4, 5, 6]]

csv_file = open(os.path.join('csv_file', 'data.csv'), 'w')
for row in data:

	# 'pythonic' code
	csv_file.write(''.join([str(item) + ',' for item in row])[:-1] + '\n')

	# more straightforward (but probably slower) code
	'''
	line = ''

	for item in row:
		line += str(item) + ','
	csv_file.write(line[:-1] + '\n')
	'''

csv_file.close()
