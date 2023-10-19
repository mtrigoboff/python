# strings are immutable, so act as though they are not passed by reference
# (see object_oriented/binary_search_tree.py)

def fn(strg):
	strg += ' xyz'
	print(strg)

str1 = 'abc'
fn(str1)
print(str1)