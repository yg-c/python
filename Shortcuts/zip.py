# Zip

names = ['tim', 'joe', 'billy', 'sally']
ages = [21, 19, 18, 43]
eye_colors = ['blue', 'brown', 'brown', 'green']

print(list(zip(names, eye_colors))) # [('tim', 'blue'), ('joe', 'brown'), ('billy', 'brown'), ('sally', 'green')]

for name, age, eye_color in zip(names, ages, eye_colors):
	if age > 20 :
		print(name) # tim, sally