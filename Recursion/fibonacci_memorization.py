# Fibonacci memorization 

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