import os

start_day = 1
end_day = 15
fold_name_base = "Day_"

days = range(start_day, end_day+1)

for day in days:
    filepath = fold_name_base+str(day)

    if not os.path.exists(filepath):
        os.mkdir(filepath)
        print(f"Folder '{filepath}' created successfully.")
    else:
        print(f"Folder '{filepath}' already exists.")
