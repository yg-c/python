# Generators

'''
Solved issiue memory RAM limitation 
Look at one value at the time and not store the entire sequence
'''

# Without Python generator

class Gen:
	def __init__(self, n):
		self.n = n
		self.last = 0

	def __next__(self):
		return self.next()

	def next(self):
		if self.last == self.n:
			raise StopIteration()

		rv = self.last ** 2 # we only keep the last variable
		self.last += 1
		return rv

g = Gen(100000000000)

while True:
	try:
		print(next(g))
	except StopIteration:
		break

# Python generator

def gen(n):
	for i in range(n):
		yield i**2 # pause de fonction

gen = gen(100000000000)

for i in g:
	print(i)
