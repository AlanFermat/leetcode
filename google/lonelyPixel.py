def findLonelyPixel(picture):
	"""
	:type picture: List[List[str]]
	:rtype: int
	"""
	row = [0] * len(picture)
	col = [0] * len(picture[-1])
	
	for i in range(len(picture)):
		for j in range(len(picture[-1])):
			if picture[i][j] == 'B':
				row[i] += 1
				col[j] += 1
	row_1 = sum([1 for i in row if i == 1])
	col_1 = sum([1 for i in col if i == 1])
	return min(row_1, col_1)

input = [['B', 'B', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

print (findLonelyPixel(input))