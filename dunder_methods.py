# Dunder methods

# __method__

# https://docs.python.org/3/reference/datamodel.html


class Person:

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'Person({self.name})'

	def __mul__(self, x) : # multiplication

		if type(x) is not int:
			raise Exception('Invalid argument, must be int')

		self.name = salf.name * x

	def __call__(self, y):
		print('called __call__ function', y)

	def __len__(self):
		return len(self.name)

p = Person('yann')

print(p) 
# without __repr__ : <__main__.Person object at 0x00000245507A2080>
# with __repr__ : Person(yann)

p(4) # called __call__ function 4

print(len(p)) # 4


from queue import Queue as q
import inspect

print(inspect.getsource(q)) # to get documentation about Queue including dunder methods

class Queue(q):
	def __repr__(self):
		return f'Queue({self.qsize()})' # qsize() present in inspect

	def __add__(self, item):
		self.put(item)

	def __sub__(self, item):
		self.get(item)

qu = Queue()
print(qu) # Queue(0)

qu + 9
qu + 3
print(qu) # Queue(2)

qu - 3
print(qu) # Queue(1)
