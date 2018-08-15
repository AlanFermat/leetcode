def solveNQueens(n):
	"""
	:type n: int
	:rtype: List[List[str]]
	"""
	res = [["." for _ in range(n)] for _ in range(n)]
	ans = []
	def valid(res, row, col):
		# vertical and horizontal
		for j in range(n):
			if res[row][j] == "Q":
				return False
		for i in range(n):
			if res[i][col] == "Q":
				return False
		qx, qy = row, col
		# diagonal
		lx, ly = qx-1, qy-1
		while lx > -1 and ly > -1:
			if res[lx][ly] == "Q":
				return False
			lx -=1
			ly -=1
		rx, ry = qx + 1, qy+1
		while rx < n and ry < n:
			if res[rx][ry] == "Q":
				return False
			rx +=1
			ry +=1
		llx, lly = qx-1, qy +1
		while llx > -1 and lly < n:
			if res[llx][lly] == "Q":
				return False
			llx -=1
			lly +=1
		rrx, rry = qx+1, qy-1
		while rrx < n and rry > -1:
			if res[rrx][rry] == "Q":
				return False
			rrx +=1
			rry -=1 
		return True

	def backtrack(ans, res, row):
		if row == n:
			temp = []
			for idx in range(n):
				temp.append("".join(res[idx]))
			ans.append(temp)
			return 
		else:
			for col in range(n):
				if valid(res,row,col):
					res[row][col] = "Q"
					backtrack(ans, res, row+1)
					res[row][col] = "."		
	backtrack(ans, res, 0)
	return ans



n = 4
print (solveNQueens(n))
