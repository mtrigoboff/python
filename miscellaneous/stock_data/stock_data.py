import os
from os.path import join
from time import sleep

import copy			# only needed for fake data production

# fake data for testing purposes
fake_data = {'AAPL' : {'price' : 500, 'shares' : 10000}, 'IBM' : {'price' : 200, 'shares' : 20000}}

def get_stock_data(stocks):

	# replace with code that actually gets stock data from brokerage
	
	# generate different fake data each time
	fake_data['AAPL']['price'] += 1
	fake_data['AAPL']['shares'] += 10
	fake_data['IBM']['price'] += 1
	fake_data['IBM']['shares'] += 10

	return copy.deepcopy(fake_data)

def write_csv_file(stock_symbols, file_name, csv_data):
	
	csv_file = open(os.path.join('stock_data', file_name), 'w')
	
	# column headers
	line = 'stock,'
	val = list(csv_data.values())[0][0]
	for key in val.keys():
		line += key + ','
	csv_file.write(line[:-1] + '\n')

	# stock data
	for stock_symbol in stock_symbols:
		for stock_data in csv_data[stock_symbol]:
			line = stock_symbol + ','
			attrs = stock_data.keys()
			for attr in attrs:
				line += str(stock_data[attr]) + ','
			csv_file.write(line[:-1] + '\n')

	csv_file.close()

def run(interval_secs, file_name):
	
	stock_symbols = ['AAPL', 'IBM']				# list of stock symbols
	csv_data = dict([[stock_symbol, []] for stock_symbol in stock_symbols])

	for rep in range(0, 3):						# loop runs 3 times
		stock_data = get_stock_data(stock_symbols)
		for stock_symbol in stock_symbols:
			csv_data[stock_symbol].append(stock_data[stock_symbol])
		sleep(interval_secs)					# sleep for designated seconds

	write_csv_file(stock_symbols, file_name, csv_data)

run(1, 'stock_data.csv')

