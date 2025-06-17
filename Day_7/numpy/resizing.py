import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
a.resize(2, 3)

print(a)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.nbytes)