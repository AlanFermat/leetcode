def numIslands(grid):
	"""
	:type grid: List[List[str]]
	:rtype: int
	"""
	
	def dfs(x,y,m,n,g):
		if x<0 or y <0 or x > m-1 or y >n-1 or g[x][y] != 1:
			return 
		g[x][y] = "#"
		dfs(x+1,y,m,n,g)
		dfs(x-1,y,m,n,g)
		dfs(x,y+1,m,n,g)
		dfs(x,y-1,m,n,g)
		
	
	if not grid:
		return 0
	m, n = len(grid), len(grid[0])
	res = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				dfs(i,j,m,n,grid)
				res += 1
	print (grid)
	return res



grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
print (numIslands(grid))

