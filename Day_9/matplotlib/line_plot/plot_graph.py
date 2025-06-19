# Import libraries with aliases
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create simple lists for x and y variables
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Plot a green color graph
plt.plot(x, y, color='green', marker='o', linewidth=2, markersize=6, label='Line 1')

# Plot a second line with blue color
plt.plot(x, y2, color='blue', marker='s', linewidth=2, markersize=6, label='Line 2')

# Add labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Graph with Two Lines')

# Add legend to show both lines
plt.legend()

# Add grid for better visibility
plt.grid(True, alpha=0.3)

# Display the plot
plt.show()