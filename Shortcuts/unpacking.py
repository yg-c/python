# Unpacking

tup = (1, 2, 3, 4) 
a, b, c, d = tup # 1 2 3 4

lst = [1, 2, 3, 4]
e, f, g, h = lst # 1 2 3 4

dic = {'a':1, 'b':2}
i, j = dic
k, l = dic.values() # 1 2
m, n = dic.items() # ('a', 1) ('b', 2)

coords = [85447, 56961]
x, y = coords # 85447, 56961

print(e, f, g, h)