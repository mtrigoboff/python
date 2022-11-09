# Python Debugger (pdb) Demo

import pdb; pdb.set_trace()		# start debugger

numerator = 17
denominator = 5

integer_quotient = numerator // denominator
float_quotient = numerator / denominator
remainder = numerator % denominator

fstr = f'integer quotient: {integer_quotient}, float quotient = {float_quotient}'
print(fstr)