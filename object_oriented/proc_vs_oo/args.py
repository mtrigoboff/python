def fn_a(a, b, *args):
	print(a, b, end=' ')
	if len(args) > 0:
		for arg in args:
			print(arg, end=' ')
	print()

print('args')
fn_a(1, 2)
fn_a(1, 2, 3, 4)
print()

def fn_k(a, b, **kwargs):
	print(a, b, end=' ')
	if kwargs is not None:
		for item in kwargs.items():
			print(f'{item[0]}={item[1]}', end=' ')
	print()

print('kwargs')
fn_k(1, 2)
fn_k(1, 2, x=5, y=6)

print()
def fn_ak(a, b, *args, **kwargs):
	print(a, b, end=' ')
	if len(args) > 0:
		for arg in args:
			print(arg, end=' ')
	if kwargs is not None:
		for item in kwargs.items():
			print(f'{item[0]}={item[1]}', end=' ')
	print()

print('args + kwargs')
fn_ak(1, 2)
fn_ak(1, 2, 3, 4)
fn_ak(1, 2, x=5, y=6)
fn_ak(1, 2, 3, 4, x=5, y=6)
print()
