import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print(type(arr))
print(arr.ndim)

print(arr[2][1])

r1 = arr[:2, :2]
print(r1)