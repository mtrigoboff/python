import math

def is_prime(n):
	sqrt_n = int(math.sqrt(n))		# int() function truncates float to int
	print(f'is_prime({n})')
	print(f'sqrt({n}) truncated: {sqrt_n}')
	for i in range(2, sqrt_n + 1):
		if n % i == 0:
			print(f'{n} is not prime: {i} * {n // i}')
			return False
	print(f'{n} is prime')
	return True

tests = (2, 31, 36)

print('Primes')
print()
for t in tests:
	is_prime(t)
	print()