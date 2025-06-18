import pandas as pd

a = pd.Series(['Ram', 'Raju', 'Rahul'])
b = pd.Series([101, 102, 103])
c = pd.Series([98, 99, 97])

x = {
    'Names': a, 'Roll No.': b, 'Marks': c
}

df = pd.DataFrame(x)

print(df)
