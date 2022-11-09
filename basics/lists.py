# print indexed item of list
def print_item(items, index):
    print(f'item[{index}] = {items[index]:2}')

# the Fibonacci Series
fib_series = [0, 1, 1, 2, 3, 5, 8, 13, 21]

print('fibonacci series: ', end='')
for i in fib_series:
    print(i, ' ', end='')
print()

lgth = len(fib_series)      # lgth == 9
print(f'length = {lgth}\n') # prints 9

print_item(fib_series, 0)   # prints   0
print_item(fib_series, 4)   # prints   3
print_item(fib_series, 8)   # prints  21
print()

print('printed using for loop, range(), len()')
for i in range(len(fib_series)):
    print(fib_series[i], ' ', end='')
print('\n')                 # print 2 empty lines

# building a list
fib_2 = []                  # empty list
n1 = 0
n2 = 1
for i in range(9):
    fib_2.append(n1)        # append n1 to end of list
    next_val = n1 + n2
    n1 = n2
    n2 = next_val

print(f'built list = {fib_2}\n')

# a list containing lists
sublists = [['ints:', 1, 2, 3], ['floats:', 4.0, 5.0, 6.0], ['strings:', 'abc', 'def', 'ghi']]

print('sublists:', sublists)
for sublist in sublists:
    for item in sublist:
        print(str(item) + ' ', end='')
    print()

# altering the items of a list

def change_item(target_list, index, value):
    target_item = target_list[i]
    target_list[index] = value
    print(f'replaced {target_item} at index {index} with {value}')

cl = [1, 2, 3, 4, 5]
print('\nbefore:', cl)
for i in range(len(cl)):
    change_item(cl, i, 0)
print('after:', cl, '\n')

# list slicing
sl = ['a', 'b', 'c', 'd', 'e']
print('source list: ', sl)
sl_24 = sl[2:4]                     # [c, d]
print(f'slice [2:4] =', sl_24)
sl_3 = sl[3:]                       # [d, e]
print(f'slice [3:] = ', sl_3)
sl_m2 = sl[:-2]                     # [a, b, c]
print(f'slice [:-2] =', sl_m2)
sl[1:-2] = ['x', 'y']               # [a, x, y, d, e]
print('altered:     ', sl)