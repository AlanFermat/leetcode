class Point(object):
	"""docstring for Point"""
	def __init__(self, a = 0, b= 0 ):
		self.x = a
		self.y = b
		

def maxPoints(points):
	"""
	:type points: List[Point]
	:rtype: int
	"""
	# note that we have two cases one from left_bottom to top_right, the
	# other from left_top to right_bottom
	if not points:
		return 0
	uniq = {}
	for p in points:
		uniq[(p.x,p.y)] = uniq.get((p.x,p.y),0) + 1
	P = uniq.keys()
	if len(P) == 1:
		return uniq[P[0]]
	maxP = 0
	for i in range(len(P)-1):
		slopes = {}
		for j in range(i+1,len(P)):
			x1, y1 = P[i][0], P[i][1]
			x2, y2 = P[j][0], P[j][1]
			dx = x2 - x1
			dy = y2 - y1
			if not dx:
				slope = "%"
			elif not dy:
				slope = 0
			else:
				slope = 1.0 * dy / dx
			slopes[slope] = slopes.get(slope, 0) + uniq[P[j]]
			
		maxP = max(maxP, max(slopes.values()) + uniq[P[i]])
	return maxP

l = [[0,0],[0,0],[0,0]]
temp = []
for item in l:
	temp += [Point(item[0], item[1])]

print (maxPoints(temp))





