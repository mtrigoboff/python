HDR_WIDTH = 15

def compute_pay(hours, rate):
	pay = hours * rate
	if hours > 40:		# time + 1/2 for overtime
		pay += (hours - 40) * rate * 0.5
	return pay

def run():
	print("Enter negative hours or rate to exit.\n")
	while True:

		# get hours, rate from user
		try:
			hours = float(input(f'{"enter hours:":{HDR_WIDTH}s}'))
			if (hours < 0):
				break
			rate =  float(input(f'{"enter rate:":{HDR_WIDTH}s}'))
			if (rate < 0):
				break

		# handle non-numeric user input
		except ValueError:
			print(f'{"error:":{HDR_WIDTH}s}number required\n')
			continue

		# print computed pay
		print(f'{"pay":{HDR_WIDTH}s}${compute_pay(hours, rate):,.2f}\n')

	print('\nbye...\n')

if __name__ == '__main__':
	run()
