def maxSubArray(arr):
	"""
		O(n) solution for finding max subarray
	"""
	n = len(arr)
	if n ==0:
		return 0
	maxSum = max(arr)
	curSum = arr[0]
	start = 0
	end = 0
	idx = 0
	max_end_here = arr[0]
	if len(arr) > 1:
		for i in range(1,len(arr)):
			num = arr[i]
			max_end_here += arr[i]
			if max_end_here > maxSum:
				maxSum = max_end_here
				end = i
				start = idx+1
			if max_end_here < 0 :
				idx = i
				max_end_here = 0
	return start, end, maxSum



arr = [1,2,-3,4,5,5,-100,4,-9,5,31,3]
print maxSubArray(arr)