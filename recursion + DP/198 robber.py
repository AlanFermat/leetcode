def maxRob(arr):
	"""
		argument: arr ---- a list of numbers representing amount of money
		return: result ---- best robbery result in terms of total money
	"""
	prevMax = 0
	currMax = 0
	for i in range(len(arr)):
		temp = currMax
		currMax = max(prevMax+arr[i], currMax)
		prevMax = temp

	result= currMax
	return result



arr = [2,3,0]
print (maxRob(arr))