try:
	strg = 'abcdefg'
	strg[1] = 'x'
	print(strg)
except:
	print('can\'t modify a string') 

byte_array = b'\xFA'
byte_array += b'\xFF'
print(f'len = {len(byte_array)}')
# byte_array[1] = 'x'		cannot do this
byte_array += b'\xFA'
print(byte_array)
print(len(byte_array))