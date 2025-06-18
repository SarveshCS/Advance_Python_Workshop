import pandas as pd

a = pd.Series([11, 12, 13, 14, 15])

b = dict(a)

print(b)

a = pd.Series(b)

print(a)