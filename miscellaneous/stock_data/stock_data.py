import os.path

data = {'AAPL' : {'price' : 500, 'shares' : 10000}, 'IBM' : {'price' : 200, 'shares' : 20000}}

csv_file = open(os.path.join('stock_data', 'stock_data.csv'), 'w')

# column headers
line = 'stock,'
val = list(data.values())[0]
for key in val.keys():
	line += key + ','
csv_file.write(line[:-1] + '\n')

# stock data
for key in data.keys():
	line = key + ','
	attrs = data[key]
	for attr in attrs.keys():
		line += str(attrs[attr]) + ','
	csv_file.write(line[:-1] + '\n')

csv_file.close()

