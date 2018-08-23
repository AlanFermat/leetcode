def reversePairs(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if not nums or len(nums) == 1:
		return 0
	def helper(arr):
		if len(arr) == 2 or len(arr) == 3:
			res = 0
			for i in range(len(arr)-1):
				for j in range(i+1,len(arr)):
					if arr[i] > 2 * arr[j]:
						res += 1
			return res
		left = arr[:len(arr)//2]
		right = arr[len(arr)//2:]
		lll = helper(left)    
		rrr = helper(right)
		ans= lll + rrr
		left =sorted(left)[::-1]
		right = sorted(right)[::-1]
		# print (left, right, ans)
		l_idx = 0
		r_idx = 0
		while l_idx < len(left):
			num = left[l_idx]
			while r_idx < len(right):
				if 2 * right[r_idx] < num:
					ans += len(right) - r_idx
					break
				else:
					r_idx += 1
			l_idx += 1
		return ans
	return helper(nums)

nums = [1,3,2,3,1]
print (reversePairs(nums))


