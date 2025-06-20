# Advanced Python Workshop - Library Reference Guide

This comprehensive guide covers the most important libraries, functions, and methods covered in Days 6-9 of the Advanced Python Workshop.

## Table of Contents

1. [Tkinter (GUI Programming)](#tkinter-gui-programming)
2. [PIL/Pillow (Image Processing)](#pilpillow-image-processing)
3. [NumPy (Numerical Computing)](#numpy-numerical-computing)
4. [Pandas (Data Analysis)](#pandas-data-analysis)
5. [Matplotlib (Data Visualization)](#matplotlib-data-visualization)
6. [Quick Reference](#quick-reference)

---

## Tkinter (GUI Programming)

Tkinter is Python's standard GUI toolkit for creating desktop applications.

### Basic Setup and Window Creation

```python
from tkinter import Tk, Label, Button, Menu, Frame
import tkinter as tk

# Basic window setup
root = Tk()
root.title("Window Title")
root.geometry("600x500+300+150")  # width x height + x_offset + y_offset
root.configure(background='#5b5b5b')
```

### Essential Tkinter Widgets

#### 1. **Label Widget**

```python
# Basic Label
label = Label(root, text="Welcome to workshop")
label.pack()

# Styled Label
label = Label(root, text="Styled Text", 
              font=('Times new roman', 33, 'italic bold'),
              foreground='#f7f7f7',
              background="#9a9999")
label.pack(pady=10, ipadx=0, side='top')
```

#### 2. **Button Widget**

```python
# Simple Button
btn = Button(root, text='EXIT', command=root.destroy)
btn.pack()

# Button with Custom Function
def mycallback():
    print("Button clicked")

msgbtn = Button(root, text="Click here", command=mycallback)
msgbtn.pack()
```

#### 3. **Menu Bar**

```python
# Create Menu Bar
menubar = Menu(root)

# Create File Menu
fileMenu = Menu(root, tearoff=0)
fileMenu.add_command(label="Stop", command=root.destroy)
fileMenu.add_command(label="Kill", command=root.destroy)
fileMenu.add_command(label="Exit", command=root.destroy)

# Add Menu to MenuBar
menubar.add_cascade(label='File', menu=fileMenu)
root.config(menu=menubar)
```

### Window Management Functions

```python
# Get screen dimensions
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

# Window positioning and sizing
root.geometry("600x500+300+150")
root.resizable(width=True, height=True)
```

### Layout Management

#### Pack Layout

```python
label.pack()                    # Default packing
label.pack(side='top')         # Specific side
label.pack(pady=10, ipadx=0)   # Padding options
```

#### Grid Layout

```python
label.grid(row=0, column=0)
button.grid(row=1, column=1, sticky='nsew')
```

#### Place Layout

```python
frame.place(anchor='center', relx=0.5, rely=0.5)
```

### Main Event Loop

```python
root.mainloop()  # Must be called at the end
```

---

## PIL/Pillow (Image Processing)

PIL (Python Imaging Library) / Pillow is used for image processing and integration with Tkinter.

### Basic Image Operations

```python
from PIL import ImageTk, Image
from tkinter import Tk, Frame, Label

# Load and display image in Tkinter
root = Tk()
frame = Frame(root, width=400, height=400)
frame.pack()

# Load image
img_path = "path/to/your/image.ico"
img = ImageTk.PhotoImage(Image.open(img_path))

# Display in Label
label = Label(frame, image=img)
label.pack()
```

### Common PIL/Pillow Functions

```python
from PIL import Image

# Open image
image = Image.open("image.jpg")

# Basic operations
image.show()                    # Display image
image.save("output.jpg")        # Save image
image.resize((width, height))   # Resize image
image.rotate(90)               # Rotate image
image.crop((left, top, right, bottom))  # Crop image

# Image properties
print(image.size)              # Get dimensions
print(image.format)            # Get format
print(image.mode)              # Get color mode
```

---

## NumPy (Numerical Computing)

NumPy is the fundamental package for scientific computing in Python.

### Array Creation

```python
import numpy as np

# Basic array creation
arr = np.array([1, 3, 4, 5, 2])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Array with mixed data types (converts to string)
mixed = np.array([1, 2, 3.5, 'rohit'])
```

### Common Matrix Creation Functions

```python
# Zero matrices
zeros = np.zeros((3, 4), dtype='int16')

# Ones matrices
ones = np.ones((3, 4), dtype='int16')

# Fill with specific value
full = np.full((3, 4), 5)

# Fill with NaN
nan_array = np.full((3, 4), np.nan)

# Diagonal matrix
diag = np.diag([10, 20, 30, 40, 50])

# Identity matrix
identity = np.eye(5, dtype='int16')

# Range arrays
range_arr = np.arange(10, 30)
```

### Random Arrays

```python
# Random floats between 0 and 1
rand_arr = np.random.rand(3, 4)

# Random integers
rand_int = np.random.randint(-4, 10, size=(2, 4))

# Random normal distribution
normal = np.random.randn(3, 4)
```

### Array Properties and Information

```python
print(arr.dtype)      # Data type
print(arr.shape)      # Shape/dimensions
print(arr.size)       # Total elements
print(arr.ndim)       # Number of dimensions
```

### Array Manipulation

```python
# Reshaping
reshaped = arr.reshape(2, 4)

# Flattening
flat1 = arr.ravel()     # Returns view if possible
flat2 = arr.flatten()   # Always returns copy

# Transposing
transposed = arr.transpose()
# or
transposed = arr.T
```

### Mathematical Operations

```python
# Trigonometric functions
angles = np.array([0, 30, 45, 60, 90, 180])
sin_vals = np.sin(angles)
cos_vals = np.cos(angles)
tan_vals = np.tan(angles)

# Matrix operations
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[5, 9, 1], [6, 8, 3], [7, 4, 5]])

# Addition/Subtraction
result = matrix_a + matrix_b

# Matrix multiplication
dot_product = matrix_a.dot(matrix_b)
# or
dot_product = matrix_a @ matrix_b
# or
dot_product = np.matmul(matrix_a, matrix_b)

# Matrix properties
trace = np.trace(matrix_a)           # Trace (sum of diagonal)
determinant = np.linalg.det(matrix_b)  # Determinant
inverse = np.linalg.inv(matrix_b)    # Inverse matrix
```

### Array Indexing and Slicing

```python
# Basic indexing
element = arr[0]        # First element
row = arr_2d[0]        # First row
element_2d = arr_2d[0, 1]  # Element at row 0, column 1

# Slicing
slice_arr = arr[1:4]    # Elements from index 1 to 3
slice_2d = arr_2d[0:2, 1:3]  # Subarray
```

---

## Pandas (Data Analysis)

Pandas provides high-performance data structures and analysis tools.

### Series Creation and Operations

```python
import pandas as pd

# Create Series from list
data = [10, 20, 30, 'Late', 'Punishment']
series1 = pd.Series(data)

# Series with custom index
series2 = pd.Series(data, index=['x', 'y', 'z', 'a', 'b'])

# Accessing elements
print(series1[1])      # By position
print(series2['x'])    # By label
```

### Series from Different Data Types

```python
# From dictionary
dict_data = {'a': 10, 'b': 20, 'c': 30}
series_dict = pd.Series(dict_data)

# From scalar value
scalar_series = pd.Series(5, index=[0, 1, 2, 3])

# From NumPy array
import numpy as np
np_array = np.array([1, 2, 3, 4, 5])
series_np = pd.Series(np_array)
```

### DataFrame Creation and Operations

```python
# Create DataFrame from dictionary
data = {
    "Names": ["Anurag", "Aditya", "Ashu"],
    "Roll No.": [101, 102, 103],
    "Marks": [8, 9, 8],
}
df = pd.DataFrame(data)

# From NumPy array
arr = np.arange(100001, 1000000)
idx = np.arange(999999, 100000, -1)
df_np = pd.DataFrame(arr, columns=['Ids'], index=idx)
```

### File I/O Operations

```python
# Reading CSV files
df = pd.read_csv("filename.csv")
df = pd.read_csv("path/to/file.csv", index_col=0)

# Writing CSV files
df.to_csv("output.csv")
df.to_csv("output.csv", index=False)

# Other file formats
df = pd.read_excel("file.xlsx")
df = pd.read_json("file.json")
```

### DataFrame Inspection

```python
# Basic info
print(df.head())        # First 5 rows
print(df.tail())        # Last 5 rows
print(df.info())        # DataFrame info
print(df.describe())    # Statistical summary
print(df.shape)         # Dimensions
print(df.columns)       # Column names
print(df.index)         # Index
```

### Data Selection and Filtering

```python
# Column selection
column = df['column_name']
columns = df[['col1', 'col2']]

# Row selection
row = df.loc[0]         # By label
row = df.iloc[0]        # By position

# Conditional filtering
filtered = df[df['Marks'] > 5]
filtered = df[(df['Marks'] > 5) & (df['Roll No.'] < 103)]
```

### Data Manipulation

```python
# Adding columns
df['New_Column'] = df['Marks'] * 2

# Removing columns
df.drop('column_name', axis=1, inplace=True)
df.drop(['col1', 'col2'], axis=1, inplace=True)

# Removing rows
df.drop(0, axis=0, inplace=True)  # Remove row at index 0

# Inserting data
df.insert(1, 'New_Col', [1, 2, 3])  # Insert at position 1
```

### Statistical Operations

```python
# Basic statistics
print(df['Marks'].mean())     # Mean
print(df['Marks'].median())   # Median
print(df['Marks'].std())      # Standard deviation
print(df['Marks'].sum())      # Sum
print(df['Marks'].count())    # Count non-null values
print(df['Marks'].min())      # Minimum
print(df['Marks'].max())      # Maximum
```

---

## Matplotlib (Data Visualization)

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations.

### Basic Setup and Imports

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

### Line Plots

```python
# Basic line plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

plt.plot(x, y)
plt.show()

# Styled line plot
plt.plot(x, y, color='green', marker='o', linewidth=2, markersize=6, label='Line 1')

# Multiple lines
y2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
plt.plot(x, y2, color='blue', marker='s', linewidth=2, markersize=6, label='Line 2')
```

### Plot Customization

```python
# Labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Graph with Two Lines')

# Legend
plt.legend()

# Grid
plt.grid(True, alpha=0.3)

# Show plot
plt.show()
```

### Bar Plots

```python
# Basic bar plot
fig, ax = plt.subplots()

fruits = ['apple', 'banana', 'mango', 'cherry']
counts = [234, 324, 122, 563]
bar_colors = ['tab:red', 'tab:orange', 'tab:green', 'tab:blue']

# Individual bars with colors
for i in range(len(fruits)):
    ax.bar(fruits[i], counts[i], color=bar_colors[i])

# Alternative: all bars at once
ax.bar(fruits, counts, color=bar_colors)

ax.set_ylabel('Count')
ax.set_xlabel('Fruits')
ax.set_title('Fruit Count Bar Graph')

plt.show()
```

### Plot Styles and Colors

```python
# Color options
colors = ['red', 'blue', 'green', 'orange', 'purple']
colors = ['#FF0000', '#0000FF', '#00FF00']  # Hex colors
colors = ['tab:red', 'tab:blue', 'tab:green']  # Tab colors

# Marker styles
markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']

# Line styles
linestyles = ['-', '--', '-.', ':']

# Example with styles
plt.plot(x, y, color='red', marker='o', linestyle='--', 
         linewidth=2, markersize=8, alpha=0.7)
```

### Figure and Subplots

```python
# Create figure and axes
fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(10, 6))

# Multiple subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, y)
ax2.bar(fruits, counts)

# Subplot grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y)
axes[0, 1].bar(fruits, counts)
```

### Saving Plots

```python
# Save plot
plt.savefig('plot.png')
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.savefig('plot.pdf')  # Different formats
```

### Advanced Features

```python
# Annotations
plt.annotate('Important Point', xy=(5, 10), xytext=(6, 12),
             arrowprops=dict(arrowstyle='->'))

# Text
plt.text(5, 10, 'Sample Text', fontsize=12)

# Limits
plt.xlim(0, 10)
plt.ylim(0, 20)

# Ticks
plt.xticks([1, 2, 3, 4, 5])
plt.yticks(range(0, 21, 5))
```

---

## Quick Reference

### Most Common Operations by Library

#### Tkinter Essentials

```python
from tkinter import Tk, Label, Button, Menu
root = Tk()
root.geometry("width x height + x + y")
widget.pack() / .grid() / .place()
root.mainloop()
```

#### NumPy Essentials

```python
import numpy as np
np.array(), np.zeros(), np.ones(), np.random.rand()
arr.reshape(), arr.T, arr.dot(), np.linalg.det()
```

#### Pandas Essentials

```python
import pandas as pd
pd.Series(), pd.DataFrame(), pd.read_csv()
df.head(), df.info(), df['column'], df.loc[], df.iloc[]
```

#### Matplotlib Essentials

```python
import matplotlib.pyplot as plt
plt.plot(), plt.bar(), plt.xlabel(), plt.ylabel()
plt.title(), plt.legend(), plt.grid(), plt.show()
```

### Data Type Conversion Chain

```python
# List → NumPy → Pandas → Matplotlib
list_data = [1, 2, 3, 4, 5]
np_array = np.array(list_data)
pd_series = pd.Series(np_array)
plt.plot(pd_series)
```

### File Handling Best Practices

```python
# Always use proper paths
import os
path = os.path.abspath(__file__)
file_path = os.path.join(path, 'data', 'file.csv')

# Handle exceptions
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found")
```

### Performance Tips

- Use NumPy arrays for numerical computations
- Use Pandas for data manipulation and analysis
- Use vectorized operations instead of loops
- Cache frequently accessed data
- Use appropriate data types (int16 vs int64)

This guide covers the fundamental concepts and most commonly used functions from the Advanced Python Workshop. Each library builds upon the others to create a powerful toolkit for data science and GUI development.
