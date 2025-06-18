import pandas as pd

# Create a simple pandas series from a list data structure.

a = [10, 20, 30, 'Late', 'Punishment']

col = pd.Series(a)
print(col[1])


col2 = pd.Series(a, index=['x', 'y', 'z', 'a', 'b'])
print(col2)