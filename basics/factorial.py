# iterative and recursive implementations of the factorial function

def fact_i(n):					# iterative implementation
	fi = 1
	for i in range(2, n + 1):
		fi *= i
	return fi

def fact_r(n):					# recursive implementation
	if n == 1:
		return 1
	else:
		return n * fact_r(n - 1)

start_n = 5
fact_value_i = fact_i(start_n)
fact_value_r = fact_r(start_n)
print(f'factorial of {start_n} is {fact_value_i}, {fact_value_r}')
