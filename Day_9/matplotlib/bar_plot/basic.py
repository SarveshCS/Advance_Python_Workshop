import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'banana', 'mango', 'cherry']
counts = [234, 324, 122, 563]
bar_labels = ['red', 'yellow', 'yellow', '_red']
bar_colors = ['tab:red', 'tab:orange', 'tab:green', 'tab:blue']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Count')
ax.set_xlabel('Fruits')
ax.set_title('Fruit Count Bar Graph')
ax.legend(title='Colors')

plt.show()