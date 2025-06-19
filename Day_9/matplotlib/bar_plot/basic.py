import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'banana', 'mango', 'cherry']
counts = [234, 324, 122, 563]
bar_colors = ['tab:red', 'tab:orange', 'tab:green', 'tab:blue']

for i in range(len(fruits)):
    ax.bar(fruits[i], counts[i], color=bar_colors[i])

ax.set_ylabel('Count')
ax.set_xlabel('Fruits')
ax.set_title('Fruit Count Bar Graph')

plt.show()