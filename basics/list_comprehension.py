# build a list of squares using a for loop
numbers = []
for i in range(1, 11):
    numbers.append(i ** 2)
print(numbers)

# build a list of squares using a list comprehension
numbers = [i ** 2 for i in range(1, 11)]
print(numbers)

# build a list of 5 False values
false_vals = [False for _ in range(5)]
print(false_vals)

# list comprehension with a condition
odd_vals = [n for n in range(9) if n % 2 == 1]
print(odd_vals)