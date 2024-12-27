def safe_divide(fn):
	def decorator_fn(num, den):
		if den == 0:
			raise ValueError('zero divide!')
		return fn(num, den)
	return decorator_fn

@safe_divide
def divide(num, den):
	return num/den

print(divide(5, 4))

try:
	print(divide(5, 0))
except ValueError as e:
	print(e)
