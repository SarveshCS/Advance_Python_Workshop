import matplotlib.pyplot as plt

species = ['Abelian', 'cinstrap', 'gentop']
species_count = [120, 85, 95]

sex_count = {
    'male': 3422,
    'female': 6585
}

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 180, 220, 170, 250]

plt.figure(figsize=(10, 6))

for i in range(len(species)):
    plt.bar(species[i], species_count[i])

plt.title('Species Count')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 5))

keys = list(sex_count.keys())
values = list(sex_count.values())

for i in range(len(keys)):
    plt.bar(keys[i], values[i])

plt.title('Sex Count')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12, 6))

for i in range(len(months)):
    plt.bar(months[i], sales[i])

plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

