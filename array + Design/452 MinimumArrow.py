def findMinArrowShots(points):
	"""
	:type points: List[List[int]]
	:rtype: int
	"""
	if not points:
		return 0
	n = len(points)
	points = sorted(points)
	idx = 1
	res = 1
	least_end = points[0][1]
	print ( points)
	while idx < n:
		if points[idx][0] > least_end:
			res += 1
			least_end = points[idx][1]
		else:
			least_end = min(least_end, points[idx][1])
			idx += 1
	return res

points = [[10,16],[2,8],[1,6],[7,12]]
print (findMinArrowShots(points))		
			
			
		
		