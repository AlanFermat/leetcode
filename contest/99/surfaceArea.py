def surfaceArea(grid):
	if not grid or not grid[0]:
		return 0
	surface = 0
	total = 0
	m,n = len(grid), len(grid[0])
	for i in range(m):
		for j in range(n):
			total += 6 * grid[i][j]
	for i in range(1,m):
		for j in range(n):
			if grid[i][j] and grid[i-1][j]:
				total -= min(grid[i][j],grid[i-1][j]) * 2
	for j in range(1,n):
		for i in range(m):
			if grid[i][j] and grid[i][j-1]:
				total -= min(grid[i][j],grid[i][j-1]) * 2
	for i in range(m):
		for j in range(n):
			if grid[i][j] > 1:
				total -= 2 * (grid[i][j] - 1)

	return total

grid = [[2,2,2],[2,1,2],[2,2,2]]
print (surfaceArea(grid))
