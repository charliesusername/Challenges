import numpy as np 
import random

n = 9
numbers = list(range(1, n + 1))

grid = np.zeros((n,n), dtype=int)

def build_grid(grid, i, j):
	value = random.choice(numbers)
	print(value)

	if value in grid[i]: return build_grid(grid, i, j)

	return grid

for i in range(9):
	for j in range(9):
		grid = build_grid(grid, i, j)

print(grid)
