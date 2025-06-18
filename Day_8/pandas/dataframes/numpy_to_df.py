import numpy as np
import pandas as pd

arr = np.arange(100001, 1000000)
idx = np.arange(999999, 100000, -1)

df = pd.DataFrame(arr, columns=['Ids'], index=idx)

print(df)