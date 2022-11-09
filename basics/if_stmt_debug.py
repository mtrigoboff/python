# demo of debugging the Python if statement

import pdb; pdb.set_trace()		# start debugger

# boolean variable
bool_var = True
if bool_var:
    dbg = 'yes'
else:
    dbg = 'no'

# questions about numbers
x = 3
if x > 3:
    dbg = 'yes'
else:
    dbg = 'no'
bool_var = x > 3
if bool_var:
    dbg = 'yes'
else:
    dbg = 'no'

# combining questions
y = 4
if x == 3 and y == 4:
    dbg = 'yes'
else:
    dbg = 'no'

if x == 5 or y == 4:
    dbg = 'yes'
else:
    dbg = 'no'

# questions about strings
strg = 'abc'
if strg == 'def':
    dbg = 'yes 1'
else:
    dbg = 'no'
if len(strg) == 3:
    dbg = 'yes'
else:
    dbg = 'no'

# 3 alternatives
if strg == 'aaa':
    dbg = 'yes 1'
elif strg == 'abc':
    dbg = 'yes 2'
else:
    dbg = 'no'
