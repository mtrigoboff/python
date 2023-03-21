from sys import argv

argv = [1, 2, 3, 4]

print(argv)

if len(argv) == 4:
	a1, a2, a3 = argv[1:]
	print(a1, a2, a3)
else:
	print('need 3 args')
