data = [[1, 2, 3],
		[4, 5, 6]]

csv_file = open('data.csv', 'w')
for row in data:
	line = ''
	for item in row:
		line += str(item) + ','
	csv_file.write(line[:-1] + '\n')
csv_file.close()
