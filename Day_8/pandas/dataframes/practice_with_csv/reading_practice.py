import pandas as pd
import numpy as np
import os

path = os.path.abspath(__file__)[::-1].partition('\\')[-1][::-1]+'\\data\\'
filename = "DETAILS(1-92).csv"
filepath = path + filename

data = pd.read_csv(filepath)

marks_columns = ["MARKS IN ENGLISH", "MARKS IN MATHS-1", "MARKS IN BEEE/PHYSICS", "MARKS IN DESIGN THINKING-1"]
for col in marks_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')

max_marks = {}
for subject in marks_columns:
    max_marks[subject] = data[subject].max()
    print(f"Max marks in {subject}: {max_marks[subject]}")
print()
min_marks = {}
for subject in marks_columns:
    min_marks[subject] = data[subject].min()
    print(f"Min marks in {subject}: {min_marks[subject]}")

print()

data['BRANCH'] = ['cse' if i.lower().strip() == 'computer science and engineering' or i.lower().strip() == 'cse core' else i.lower().strip() for i in data['BRANCH']]
branch_aggregation = data.groupby('BRANCH')[marks_columns].agg(['mean', 'max', 'min']).round(2)
print("Aggregation by BRANCH:")
print(branch_aggregation)

section_aggregation = data.groupby('SECTION')[marks_columns].agg(['mean', 'max', 'min']).round(2)
print("\nAggregation by SECTION:")
print(section_aggregation)

print("\nPerforming different types of joins")
df1 = data[['NAME OF STUDENT', 'ROLL NUMBER', 'MARKS IN ENGLISH', 'MARKS IN MATHS-1']].head(10)
df2 = data[['NAME OF STUDENT', 'ROLL NUMBER', 'MARKS IN BEEE/PHYSICS', 'MARKS IN DESIGN THINKING-1']].head(15)

inner_join = pd.merge(df1, df2, on=['NAME OF STUDENT', 'ROLL NUMBER'], how='inner')
print(f"Inner join result shape: {inner_join.shape}")
print("Inner join (first 5 rows):")
print(inner_join.head())

left_join = pd.merge(df1, df2, on=['NAME OF STUDENT', 'ROLL NUMBER'], how='left')
print(f"\nLeft join result shape: {left_join.shape}")

right_join = pd.merge(df1, df2, on=['NAME OF STUDENT', 'ROLL NUMBER'], how='right')
print(f"Right join result shape: {right_join.shape}")

outer_join = pd.merge(df1, df2, on=['NAME OF STUDENT', 'ROLL NUMBER'], how='outer')
print(f"Outer join result shape: {outer_join.shape}")

print()

math_high_scorers = data[data['MARKS IN MATHS-1'] > 80]['NAME OF STUDENT']
print(f"Students who scored more than 80% in Mathematics ({len(math_high_scorers)} students):")
print(*[name.strip() for name in math_high_scorers], sep=', ', end='\n\n')

physics_low_scorers = data[data['MARKS IN BEEE/PHYSICS'] < 75]['NAME OF STUDENT']
print(f"Students who scored less than 75% in Physics ({len(physics_low_scorers)} students):")
print(*[name.strip() for name in physics_low_scorers], sep=', ', end='\n\n')

data['TOTAL MARKS'] = pd.to_numeric(data['TOTAL MARKS'], errors='coerce')
data['SGPA'] = data['TOTAL MARKS'] / 10

def assign_grade(sgpa):
    if pd.isna(sgpa):
        return 'N/A'
    elif sgpa >= 90.0:
        return 'A'
    elif sgpa >= 80.0:
        return 'B'
    elif sgpa >= 70.0:
        return 'C'
    else:
        return 'D'

data['GRADE'] = data['SGPA'].apply(assign_grade)
print(data['GRADE'].value_counts())

output_filepath = path + "DETAILS_UPDATED.csv"
data.to_csv(output_filepath, index=False)
