# Decorators

def func(f):
	def wrapper(*args, **kwargs): # to pass arguments
		print('Started')
		rv = f(*args, **kwargs) # to be able to return a variable
		print('Ended')
		return rv

	return wrapper

@func
def func2(x):
	print('i am func2', x)
	return x

@func
def func3():
	print('i am func3')

x = func2(5)
print(x)

func3()

''' Timer decorator '''
import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		rv = func()
		total = time.time() - start
		print('Time:', total)
		return rv
	return wrapper

@timer
def test():
	for _ in range(10000000):
		# print(_)
		pass

@timer
def test2():
	time.sleep(2)

test()

test2()