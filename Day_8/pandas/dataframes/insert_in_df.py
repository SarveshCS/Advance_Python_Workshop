import pandas as pd

a = pd.Series(['Ram', 'Raju', 'Rahul'])
b = pd.Series([101, 102, 103])
c = pd.Series([98, 99, 76])

x = {
    'Names': a, 'Roll No.': b, 'Marks': c
}

df = pd.DataFrame(x)

df['Address'] = ['India', 'Bhutan', 'Nepal']

df['pra_status'] = df['Marks'] > 80

# Insering a column as a given locatio

df.insert(1, 'Phone', [768372674, 6942473, 384627468])

print(df)