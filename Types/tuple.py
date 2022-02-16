# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.

""" Create """
a_tuple = ("apple", "banana", "cherry", "apple", "cherry")


""" Access """
a_tuple[2] # Specific item

a_tuple[-1] # Last item

a_tuple[2:5] # Range

if 'cherry' in a_tuple : # In the list
	print('yes')


""" Iterate """
for t in a_tuple :
	print(t)

for i in range(len(a_tuple)):
	print(a_tuple[i])


""" Join """
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2