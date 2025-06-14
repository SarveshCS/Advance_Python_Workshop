A = [1, 2, 5, 6]
B = A.__iter__()
print(B)
print(dir(B))

x = [1, 2, 3, 4, 5, 6, 7, 8]
value = x.__iter__()
print(value)
print(dir(x))
print(dir(value))