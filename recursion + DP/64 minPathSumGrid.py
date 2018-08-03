def createMat(rowCount,colCount):
	mat = []
	for i in range (rowCount):
		rowList = []
		for j in range (colCount):
			rowList.append(0)
		mat.append(rowList)
	return mat

def minPathSum(grid):
	m = len(grid)
	n = len(grid[0])
	S = createMat(m,n)
	for i in range(n):
		if i == 0:
			S[0][i] = grid[0][i]
		else:
			S[0][i] = grid[0][i] + S[0][i-1]
	for j in range(m):
		if j == 0:
			S[j][0] = grid[j][0]
		else:
			S[j][0] = grid[j][0] + S[j-1][0]
	for i in range(1,m):
		for j in range(1,n):
			S[i][j] = min(S[i-1][j],S[i][j-1])+ grid[i][j]
	return S[m-1][n-1]



def drvier(grid):
	return minPathSum(grid)

g = [[1,7,1],[1,5,1],[4,2,1],[39,74,7]]
print drvier(g)

