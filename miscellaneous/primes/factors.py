import math

def factors(n):
	print(f'factors of {n}')
	prime = True
	sqrt_n = math.sqrt(n)
	print(f'square root of {n}: {sqrt_n:.2f}')
	tsqrt_n = int(sqrt_n)						# truncated square root
	for i in range(2, int(tsqrt_n) + 1):		# +1 to include sqrt_n
		if n % i == 0:
			prime = False
			print(f'factor pair: {i} and {n // i}')
	if prime:
		print(f'{n} is prime')
	print()

numbers = (1, 2, 24, 31, 36)

print('Factors')
print()
print('* Note that for each factor pair,')
print('* one is below the square root and')
print('* the other is above the square root,')
print('* or both are equal to the truncated')
print('* square root.')
print()
for i in numbers:
	factors(i)