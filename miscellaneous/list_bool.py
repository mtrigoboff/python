# demo that a list can function as a boolean:
# empty list -> false
# non empty list -> true

empty = []
not_empty = [1, 2, 3]

if empty:
	print('empty: true')
else:
	print('empty: false')

if not_empty:
	print('not_empty: true')
else:
	print('not_empty: false')