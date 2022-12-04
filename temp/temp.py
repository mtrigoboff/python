meals = [10, 20]
total_meals = [100, 200]

d = {}
for i in range(0, len(meals)):
	d[i + 1] = total_meals[i]

print(d)
