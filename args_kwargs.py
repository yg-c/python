# *args **kwargs

""" args """
def add_item(*args): # allows any number of positional arguments
	print(args)
	result = sum(args)
	print(result)

add_item(1, 1, 3)
add_item(1, 4, 8, 3)
add_item(7, 10, 15, 4, 8, 3)

""" kwargs """
def add_item(*args, **kwargs): # allows any number of key words arguments
	print(args, kwargs)
	result = sum(args) + kwargs["a"]
	print(result)

add_item(1, 4, a=3, b=5)


def my_function(**kwargs):
  print("His last name is " + kwargs["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 