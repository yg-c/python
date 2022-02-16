# A list is a collection which is ordered and changeable. Allows duplicate members.

""" Create """
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(list)


""" Access """
# Specific item
print(list[2])

# Last item
print(list[-1])

# Range
print(list[2:5])

# In the list
if 'cherry' in list :
	print('yes')


""" Change """
list[1] = 'raspberry'
list[3:4] = ["blackcurrant", "watermelon"]

""" Insert """
list.insert(2, 'watermelon') # insert in indelist 2

list.append('bueberry')

tropical = ["mango", "pineapple", "papaya"]
list.extend(tropical)


""" Remove """
list.remove('kiwi') # remove item

list.pop(1) # remove indelist 1

del list[0] # remove indelist 0

del list # delete the list


""" Iterate """
list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

for l in list :
	print(l)

for i in range(len(list)):
	print(list[i])

[print(x) for x in list] 


""" Sort """
list.sort()
list.sort(reverse = True)


""" Copy """
newlist = list.copy()


""" Join """
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2
list4 = list1.extend(list2)