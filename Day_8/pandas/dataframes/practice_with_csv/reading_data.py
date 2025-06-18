import pandas as pd
import os

path = os.path.abspath(__file__)[::-1].partition('\\')[-1][::-1]+'\\data\\'
filename = "economic-survey-of-manufacturing-march-2025-quarter.csv"
filepath = path + filename

data = pd.read_csv(filepath)
# print(data)

print(data.Data_value.count())