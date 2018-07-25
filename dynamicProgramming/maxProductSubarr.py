def maxProductArr(arr):
	n = len(arr)
	maxPro = max(arr)
	curMin = arr[0]
	curMax = arr[0]
	i = 1
	while i < n:
		if arr[i] < 0:
			curMax, curMin = curMin, curMax
		curMax = max(curMax*arr[i],arr[i])
		curMin = min(curMin*arr[i],arr[i])
		maxPro = max(maxPro, curMax)
		i += 1
	return maxPro


	


def drvier(arr):
	return maxProductArr(arr)

arr = [-2,-5,-4,-6]
print drvier(arr)