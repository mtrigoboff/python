# recursion: a function that calls itself
def sum_of_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_recursion(n - 1)

def sum_of_formula(n):
    return int(n * (n + 1) / 2)

for i in range(1, 7):
    print(f'recursive: sum from 1 to {i} is {sum_of_recursion(i):2}')
    print(f'formula:   sum from 1 to {i} is {sum_of_formula(i):2}\n')
