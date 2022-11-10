def sliceDemo(x, label):
	print(f'slicing a {label}')
	print(x)
	
	slc = x[1:6]			# second to fifth
	print(slc)
	
	slc = x[1:-1]			# second to next to last
	print(slc)
	
	slc = x[2:]				# third to end
	print(slc)
	
	slc = x[:6]				# first to fifth
	print(slc)
	
	slc = x[-4:]			# fourth from end to last
	print(slc)
	
	slc = x[::2]			# even numbered only
	print(slc)

	slc = x[::-1]			# reverse
	print(slc)

print()

# create list of numbers from 0 to 9
# (this syntax is called a 'list comprehension')
lst = [r for r in range(0, 10)]
sliceDemo(lst, 'list')
print()

rg = range(0, 10)
sliceDemo(rg, 'range')
print()

strg = 'abcdefghijklmnop'
sliceDemo(strg, 'string')
print()
