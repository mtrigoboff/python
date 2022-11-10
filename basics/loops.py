# demo of python loops

print()
print('characters in string: ', end='')
for char in 'abcd':
	print(f'{char} ', end='')
print('\n')

print('elements of list:     ', end='')
for element in ['abd', 'def', 'ghi']:
	print(f'{element} ', end='')
print('\n')

print('numeric for loop:     ', end='')
for i in range(0, 5):
	print(f'{i} ', end='')
print('\n')

print('numeric while loop:   ', end='')
i = 0
while i < 5:
	print(f'{i} ', end='')
	i = i + 1
print('\n')

print('continue, break:      ', end='')
for i in range(0, 20):
	if i == 3 or i == 5:
		continue
	elif i == 7:
		break
	else:
		print(f'{i} ', end='')
print('\n')

print('nested loops')
for i in range(1, 4):
	for j in range(1, 4):
		print(f'({i}, {j}) ', end='')
print('\n')

