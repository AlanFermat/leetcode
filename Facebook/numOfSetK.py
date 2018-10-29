# def numOfSet(nums, target):
# 	nums = sorted(nums)
# 	res = []
# 	def backtrack(nums, path, target):
# 		if path:
# 			if len(path) == 1:
# 				if path[0] < target:
# 					if path not in res:
# 						res.append(path)
# 			else:
# 				if path[0] + path[-1] < target:
# 					if path not in res:
# 						res.append(path)
# 			if path[0] + path[-1] > target or not nums:
# 				return
# 			for i, num in enumerate(nums):
# 				if path[0] + num < target:
# 					backtrack(nums[i+1:], path+[num], target)
# 				else:
# 					return
# 		else:
# 			for i, num in enumerate(nums):
# 				backtrack(nums[i+1:], path+[num], target)
# 	backtrack(nums, [],target)
# 	return len(res)


def numberOfSet(nums, target):
	nums = list(set(nums))
	n = len(nums)
	i = 0
	nums = sorted(nums)
	cnt = 0
	for k in range(n):
		if target <= nums[k]:
			break
		cnt += 1
	while i < n:
		j = n-1
		while j > i:
			if nums[i] + nums[j] < target:
				cnt += 2**(j-i-1) 
				j -= 1
			elif nums[i] + nums[j] >= target:
				j -= 1
		i += 1
	return cnt

	




		



nums =[1,0,2,7,3,3,4,5]
target = 6
print (numberOfSet(nums, target))

