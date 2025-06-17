import numpy as np

a = np.zeros((3, 4), dtype='int16')

print(a)

b = np.ones((3, 4), dtype='int16')
print(b)

c = np.full((3, 4), 5)
print(c)

d = np.full((3, 4), np.nan)
print(d)

e = np.diag([10, 20, 30, 40, 50])
print(e)

f = np.eye(5, dtype='int16')
print(f)