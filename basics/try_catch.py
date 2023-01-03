def count_down(n):
	print(n)
	if n == 1:
		raise RuntimeError('Blast off!')
	else:
		count_down(n - 1)

try:
	count_down(10)
except RuntimeError as e:
	print(e)
