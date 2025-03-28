import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = np.sin(x)

# Create a figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# Plot the first function
ax1.plot(x, y1, color='r', label='y = x^2')
ax1.set_title('Quadratic Function')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend()
ax1.grid(True)

# Plot the second function
ax2.plot(x, y2, color='b', label='y = sin(x)')
ax2.set_title('Sine Function')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.legend()
ax2.grid(True)

# Adjust spacing between subplots
plt.subplots_adjust(hspace=0.5)

# Show the plot
plt.show()