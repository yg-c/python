# A list is a collection which is ordered and changeable. Allows duplicate members.

""" Create """
a_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


""" Access """
a_list[2] # Specific item

a_list[-1] # Last item

a_list[2:5] # Range

if 'cherry' in a_list : # In the list
	print('yes')


""" Change """
a_list[1] = 'raspberry'
a_list[3:4] = ["blackcurrant", "watermelon"]

""" Insert """
a_list.insert(2, 'watermelon') # insert in indelist 2

a_list.append('bueberry')

tropical = ["mango", "pineapple", "papaya"]
a_list.extend(tropical)


""" Remove """
a_list.remove('kiwi') # remove item

a_list.pop(1) # remove indelist 1

del a_list[0] # remove indelist 0

del a_list # delete the list


""" Iterate """
a_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

for l in a_list :
	print(l)

for i in range(len(a_list)):
	print(a_list[i])

[print(x) for x in a_list] 


""" Sort """
a_list.sort()
a_list.sort(reverse = True)


""" Copy """
newlist = a_list.copy()


""" Join """
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2
list4 = list1.extend(list2)