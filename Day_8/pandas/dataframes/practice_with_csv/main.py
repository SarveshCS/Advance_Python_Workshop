import pandas as pd
import os

path = os.path.abspath(__file__)[::-1].partition('\\')[-1][::-1]+'\\data\\'
filename = 'data'
exts = ['csv'] + ['xlsx']
filepaths = {ext: filename+'.'+ext for ext in exts}

data = {
    "Names": ["Anurag", "Aditya", "Ashu"],
    "Roll No.": [101, 102, 103],
    "Marks": [8, 9, 8],
}

df = pd.DataFrame(data)

df.to_csv(filepaths['csv'])
df.to_excel(filepaths['xlsx'])

print(df)