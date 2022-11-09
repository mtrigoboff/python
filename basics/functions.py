# demonstrates Python functions

# import pdb; pdb.set_trace()		# start debugger

# returns nothing
def fn(n):
	print(f'fn: called with {n}')

# returns 1 result
def add(x, y):
	result = x + y
	print(f'add: adding {x} and {y}')
	print(f'add: returning {result}')
	return result

# returns 2 results
def sum_and_diff(x, y):
	add_result = x + y
	sub_result = x - y
	return add_result, sub_result

# returns Boolean (True or False)
def greater_than(x, y):
	print(f'greaterThan: is {x} greater than {y}?')
	return x > y

fn(33)
print()					# skips a line

addRet = add(3, 4)
print(f'add function returned {addRet}')
print()					# skips a line

x = 12
y = 5
sum_of, diff_of = sum_and_diff(x, y)
print(f'sum of {x} and {y} is {sum_of}, diff of {x} and {y} is {diff_of}')

gt = greater_than(3, 4)
if gt:
	print('yes')
else:
	print('no')
print()					# skips a line
