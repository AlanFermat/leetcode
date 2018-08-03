def maxArea(height):
	"""
	:type height: List[int]
	:rtype: int
	"""
	A = height
	n = len(height)
	i = 0
	j = n-1
	area = min(A[i],A[j]) * (j-i)
	while i < j:
		area = max(area, min(A[i],A[j]) * (j-i))
		if A[i] < A[j]:
			i += 1
			continue
		if A[i] >= A[j]:
			j -= 1
			continue
	return area

height = [2,1]
print maxArea(height)