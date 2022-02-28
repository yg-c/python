# Recursion

# Fibonacci 1, 1, 2, 3, 5, 8, 13, 21 ...

def fib(n):
	if n <= 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)


fib(4)


# Memoization 

numbs = {}

def fibm(n):
	if n <= 2:
		return 1

	if n in numbs:
		return numbs[n]
	else:
		num = fibm(n-1) + fibm(n-2)
		numbs[n] = num
		return num


print(fibm(39))