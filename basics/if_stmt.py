# demo of the Python if statement

# import pdb; pdb.set_trace()		# start debugger

if True:
    print('True')
else:
    print('False')

# boolean variable
bool_var = True
print('bool_var == ', end='')
if bool_var:
    print('True')
else:
    print('False')
print(f'bool_var == {bool_var}')

# questions about numbers
x = 3
if x > 3:
    print('greater')
else:
    print('not greater')
bool_var = x > 3
if bool_var:
    print('greater')
else:
    print('not greater')

# combining questions
y = 4
if x == 3 and y == 4:
    print('both')
else:
    print('not both')

if x == 5 or y == 4:
    print('one')
else:
    print('none')

# questions about strings
strg = 'abc'
if strg == 'def':
    print('equal')
else:
    print('not equal')
if len(strg) == 3:
    print('length is 3')
else:
    print('length is not 3')

# 3 alternatives
if strg == 'aaa':
    print('aaa')
elif strg == 'abc':
    print('abc')
else:
    print('neither')
