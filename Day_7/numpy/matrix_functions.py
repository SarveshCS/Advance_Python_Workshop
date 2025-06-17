import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([
    [5, 9, 1],
    [6, 8, 3],
    [7, 4, 5]
])

a = a.transpose()

print(a)

print(np.trace(a))
print(a+b)

print(a.dot(b))

print(a@b)
print(np.matmul(a, b))

print(np.linalg.det(b))

print(np.linalg.inv(b))