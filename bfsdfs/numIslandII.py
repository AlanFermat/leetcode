def four_rotation(island):
	rotation = []
	d = sorted(island)
	rotation.append(d)
	upper_lower = sorted(island)
	left_right = sorted(island, key = lambda x:x[1])

	# left right reflection
	right_most = left_right[-1][1]
	left_most = left_right[0][1]
	a = []
	for i in range(len(island)):
		a.append([island[i][0], right_most - island[i][1] + left_most])
	# upper lower rotation
	upper_most = upper_lower[-1][0]
	lower_most = upper_lower[0][0]

	b = []
	for i in range(len(island)):
		b.append([upper_most - island[i][0] + lower_most, island[i][1]])


	# double rotation
	c = []
	b_left_right = sorted(b, key = lambda x:x[1])
	b_right_most = b_left_right[-1][1]
	b_left_most = b_left_right[0][1]
	for i in range(len(b)):
		c.append([b[i][0], b_right_most + b_left_most - b[i][1]])

	# reverse
	e = [[a[i][1], a[i][0]] for i in range(len(a))]
	f = [[b[i][1], b[i][0]] for i in range(len(b))]
	g = [[c[i][1], c[i][0]] for i in range(len(c))]
	h = [[d[i][1], d[i][0]] for i in range(len(d))]

	for item in [a,b,c,d,e,f,g,h]:
		if sorted(item) not in rotation:
			rotation.append(sorted(item))
	return rotation



def check(island1, island2):
	"""
		Check if island1 and island2 are distinct
	"""
	four_result = four_rotation(island1)
	island2 = sorted(island2)
	for item in four_result:
		if y_x_diff(item,island2):
			return False
	return True

def y_x_diff(island1, island2):
	if len(island1) != len(island2):
		return False
	horizontal = island2[0][0] - island1[0][0]
	vertical = island2[0][1] - island1[0][1]
	for i in range(len(island1)):
		if island2[i][0] - island1[i][0] !=  horizontal:
			return False
		if island2[i][1] - island1[i][1] != vertical:
			return False
	return True

def numDistinctIslands2(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	if not grid or not grid[0]:
		return 0
	visit = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
	res = []
	def getAllIslands(grid, i,j,visit, res):
		"""
			Use bfs to iterate over the grid
		"""
		temp = []
		qu = []
		temp.append([i,j])
		qu.append([i,j])
		visit[i][j]= True
		while qu:
			start = qu.pop(0)
			i, j = start[0], start[1]
			for p, q in (i+1, j), (i-1, j), (i,j+1), (i,j-1):
				if 0 <= p < len(grid) and 0<=q<len(grid[0]):
					if grid[p][q] == 1:
						if not visit[p][q]: 
							visit[p][q] = True
							qu.append([p,q])
							temp.append([p,q])

		res.append(temp)
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				if not visit[i][j]:
					getAllIslands(grid, i,j,visit, res)
	m = len(res)
	idx = 0
	while idx < m:
		k = idx + 1
		while k < m:
			if not check(res[idx], res[k]):
				del res[k]
				m -= 1
			else:
				k += 1
		idx += 1
	return len(res)

grid= [[1,0,1,1,1,0,1,0,1,0,0,0,1,1,0],[1,1,1,0,1,0,1,1,0,1,0,1,1,0,1],[1,0,1,1,0,0,0,1,0,1,0,0,0,0,0],[1,1,1,0,0,1,0,0,0,1,0,1,0,0,0],[0,0,0,1,1,0,1,0,0,0,1,0,1,0,1],[0,1,0,1,0,0,0,1,0,0,1,1,1,0,1],[1,1,1,0,0,0,0,0,0,0,0,0,1,0,1],[0,1,1,1,1,0,0,1,1,1,0,1,0,1,1],[1,1,1,1,0,0,1,0,1,0,1,1,1,0,0],[1,0,1,1,1,1,1,1,1,0,1,1,1,0,1]]
print (numDistinctIslands2(grid))







