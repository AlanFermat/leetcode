def maximalRectangle(matrix):
	"""
	:type matrix: List[List[str]]
	:rtype: int
	"""
	if not matrix:
		return 0
	if not matrix[0]:
		return 0
	m,n = len(matrix), len(matrix[0])
	h = [[0 for _ in range(n)] for _ in range(m)] # height of the maximal rect at (i,j)
	w = [[0 for _ in range(n)] for _ in range(m)] # weight of the maximal rect at (i,j)
	pos = [[[0,0] for _ in range(n)] for _ in range(m)] # position for left upper corner with
	# lower right corner at (i,j) in the matrix
	ans = 0
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == '1':
				if i == 0 and j == 0:
					h[i][j] = 1
					w[i][j] = 1
					pos[i][j] = [0,0]
				elif i == 0:
					h[i][j] = 1
					w[i][j] = w[i][j-1] + 1
					pos[i][j] = [0, j - w[i][j] + 1]
				elif j == 0:
					w[i][j] = 1
					h[i][j] = h[i-1][j] + 1
					pos[i][j] = [i - h[i][j] + 1,0]
				else: 
					h[i][j] = h[i-1][j] + 1
					w[i][j] = w[i][j-1] + 1
					y = i - h[i][j] + 1
					x = j - w[i][j] + 1
					if matrix[i-1][j] == '0':
						pos[i][j] = [i,x]
					elif matrix[i][j-1] == '0':
						pos[i][j] = [y,j]
					else:
						A1 = 0
						if matrix[i-1][j-1] == '1':
							A1 = (i - max(pos[i-1][j-1][0] , y) + 1) * ( j - max(pos[i-1][j-1][1], x) + 1)
						A2 = (i - max(pos[i-1][j][0] , y) + 1) * ( j - max(pos[i][j-1][1], x) + 1)
						A3 = (i - max(pos[i][j-1][0] , y) + 1) * ( j - max(pos[i][j-1][1], x) + 1)
						A = max(A1,A2,A3)
						if A == A1:
							pos[i][j] = [max(pos[i-1][j-1][0] , y) , max(pos[i-1][j-1][1], x)]
						if A == A2:
							pos[i][j] = [max(pos[i-1][j][0] , y) , max(pos[i-1][j][1], x)]
						if A == A3:
							pos[i][j] = [max(pos[i][j-1][0] , y) , max(pos[i][j-1][1], x)]
				ans = max(ans, (i - pos[i][j][0] + 1) * (j - pos[i][j][1] + 1))
	return ans

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
maximalRectangle(matrix)
					