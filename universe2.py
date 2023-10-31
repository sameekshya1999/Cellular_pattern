import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
GRID_SIZE = 50  # Size of the grid (square)
GENERATIONS = 50

# Create the initial grid with a simple pattern
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
grid[45:55, 45:55] = 1  # Create a simple block pattern

# Function to apply a custom rule for pattern generation
def apply_custom_rule(x, y, grid, generation):
    # Adjust for grid boundaries and wrap around
    x = x % GRID_SIZE
    y = y % GRID_SIZE
    return (grid[x, y] + grid[x - 1, y] + grid[x, y - 1] + grid[(x + 1) % GRID_SIZE, y] + grid[x, (y + 1) % GRID_SIZE]) % 2

# Function to update the grid for each generation
def update(frameNum, img, grid):
    newGrid = np.zeros_like(grid)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            newGrid[x, y] = apply_custom_rule(x, y, grid, frameNum)
    img.set_data(newGrid)
    grid[:] = newGrid
    return img

# Create the figure and axis for the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')

# Adjust the interval to control animation speed (e.g., 200 milliseconds for a slower speed)
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=GENERATIONS, interval=1600)

# Display the animation
plt.show()
