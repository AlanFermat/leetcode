def bomb(grid):
	if not grid or not grid[0]:
		return 0
	m = len(grid)
	n = len(grid[0])
	
	temp = [[0 for _ in range(n)] for _ in range(m)]
	for i in range(m):
		count = 0 
		for j in range(n):
			if grid[i][j] == "E":
				count += 1
			elif grid[i][j] == "W":
				count = 0
			else:
				temp[i][j] =count

		count = 0 
		for j in range(n-1,-1,-1):
			if grid[i][j] == "E":
				count += 1
			elif grid[i][j] == "W":
				count = 0
			else:
				temp[i][j] += count

	for j in range(n):
		count =0 
		for i in range(m):
			if grid[i][j] == "E":
				count += 1
			elif grid[i][j] == "W":
				count = 0
			else:
				temp[i][j] += count
		count =0 
		for i in range(m-1,-1,-1):
			if grid[i][j] == "E":
				count += 1
			elif grid[i][j] == "W":
				count = 0
			else:
				temp[i][j] += count

	print (temp)
	# max_val = 0
	# for i in range(m):
	# 	for j in range(n):
	# 		max_val = max(temp[i][j], max_val)
	# return max_val


grid = [["0","E","E","0"],["E","0","W","E"],["0","E","E","E"],["E","0","0","0"]]
bomb(grid)




