# Lambda fonction

# classic function
def func(x): 
	return x+5

# with lambda
fonc2 = lambda x: x+5

# multiple parameters
fonc3 = lambda x,y: x+y
fonc4 = lambda x,y=3: x+y

print(func(2)) # 7
print(fonc2(9)) # 14
print(fonc3(2,9)) # 11
print(fonc4(2)) # 5


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(map(lambda x: x+5, a)) # [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

new_list = list(filter(lambda x: x%2==0, a)) # [2, 4, 6, 8, 10]

print(new_list)