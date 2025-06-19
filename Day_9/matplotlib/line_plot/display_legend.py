# Import libraries with aliases
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # Linear growth
y2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # Quadratic growth
y3 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]  # Exponential growth

# Create the plot
plt.figure(figsize=(10, 6))

# Plot multiple lines with different colors and styles
plt.plot(x, y1, color='green', marker='o', linestyle='-', linewidth=2, label='Linear (2x)')
plt.plot(x, y2, color='blue', marker='s', linestyle='--', linewidth=2, label='Quadratic (x²)')
plt.plot(x, y3, color='red', marker='^', linestyle='-.', linewidth=2, label='Exponential (2^x)')

# Add labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Multiple Lines with Legend Display')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Display legend with different positioning options
# You can customize the legend position using 'loc' parameter:
# 'upper right', 'upper left', 'lower left', 'lower right', 'center', etc.
plt.legend(loc='upper left', frameon=True, shadow=True, fontsize=10)

# Alternative legend customization (uncomment to try different styles):
# plt.legend(loc='best')  # Automatically finds best position
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Outside plot area
# plt.legend(ncol=3, loc='upper center')  # Horizontal legend with 3 columns

# Show the plot
plt.tight_layout()  # Adjusts spacing to prevent legend cutoff
plt.show()
