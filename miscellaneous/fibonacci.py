fib_series = []            # empty list

n1 = 1
n2 = 1

for i in range(8):
    fib_series.append(n1)
    sum = n1 + n2
    n1 = n2
    n2 = sum

print(fib_series)
print()
