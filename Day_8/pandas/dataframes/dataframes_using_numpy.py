import numpy as np
import pandas as pd

arr = np.array([['a', 'b', 'c'], [101, 102, 103], [92, 98, 91]])

df = pd.DataFrame(arr, index=['id1', 'id2', 'id3'], columns=['Names', 'Roll no.', 'Marks'])

print(df)