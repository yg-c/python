# Comprehensions

# A way to initialize or create some type of collections in one line

x = [0 for i in range(100)] # fill a list with 100 zeros

y = [i for i in range(100)] # fill with 0 to 99

z = [i for i in range(100) if i % 2 == 0] # fill with even numbers

a = [i*j for i in range(100) for j in range(10)]

b = [[0 for _ in range(5)] for _ in range(5)] # _  can be use instead of a variable if we're not using it 

tup = (i for i in 'hello')


sentence = 'hello my name is Yann'
dic = {char: sentence.count(char) for char in set(sentence)} # char frequence

print(dic)