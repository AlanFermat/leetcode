def projection(grid):
	xy = 0
	n = len(grid)
	# xz = 0
	# yz = 0
	xz_max = []
	yz_max = []
	for i in range(n):
		m = 0
		for j in range(n):
			if grid[i][j]:
				xy += 1
			m = max(grid[i][j], m)
		xz_max.append(m)

	for col in range(n):
		r = 0
		for row in range(n):
			r = max(r, grid[row][col])
		yz_max.append(r)


	return xy + sum(yz_max) + sum(xz_max)

grid = [[2]]
print (projection(grid))