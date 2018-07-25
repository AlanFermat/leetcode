def largestRectangleArea(heights):
	"""
	:type heights: List[int]
	:rtype: int
	"""
	if not heights:
		return None
	else:
		n = len(heights)
		i = 0
		s = []
		maxA = heights[0]
		while i < n:
			if not s:
				s.append(i)
				i += 1
			else:
				if heights[i] >= heights[s[len(s)-1]]:
					s.append(i)
					i += 1
				else:
					while s and heights[i] < heights[s[len(s)-1]]:
						top = s.pop()
						if not s:
							area = heights[top] * i
							maxA = max(maxA, area)
						else:
							area = heights[top] * (i-s[len(s)-1] - 1)
							maxA = max(maxA, area)
		while s:
			top = s.pop()
			if not s:
				area = heights[top] * i
				maxA = max(maxA, area)
			else:
				area = heights[top] * (i-s[len(s)-1] - 1)
				maxA = max(maxA, area)

		return maxA


heights = [2,1,4,3]
print largestRectangleArea(heights)


