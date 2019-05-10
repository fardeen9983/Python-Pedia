"""
matplotlib is a popular plotting library aka used for data visualization
pyplot is the python version for Matlab's plotting features
Like plotting numbers, graphs, points, visualising them,etc
"""

import matplotlib.pyplot as plt
import numpy as np

# Plot a simple graph

# Only provide y axis values
# x axis will be automatically generated like 0,1,2,...
plt.plot([2, 4, 6, 1, 3])

# Place axis labels
plt.xlabel("Indices")
plt.ylabel("Numbers")

# Set graph title
plt.title("Demo")

# Plot the graph
plt.show()

# Plot numbers and there squares with grid
a = np.arange(1, 6)
# Plot numbers on x axis and squares on y
plt.plot(a, a ** 2)
# Put labels on the axis
plt.xlabel("Number")
plt.ylabel("Squares")
# Show the grid
plt.grid()
# Plot the graph
plt.show()

# Display colored points rather than lines
plt.plot(a, a ** 2, "ro")
# r - red color, 0 - dots instead of curve
plt.grid()
plt.show()

# red squares, blue triangles and green dashes
# r,g,b : red,blue,green
# s,^,-- : square, triangle, dash
a = np.arange(0., 5., 0.2)
plt.plot(a, a ** 2, "rs", label="^2")
plt.plot(a, a ** 2.25, "b^", label="^2.2")
plt.plot(a, a ** 2.5, "g--", label="^2.5")
# Show legend
plt.legend()
plt.grid()
plt.show()

# Specify Linewidth
