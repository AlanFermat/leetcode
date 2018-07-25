def check24(nums):
	n = len(nums)
	if n == 1:
		return nums[0] == 24 or abs(nums[0] - 24.0) < 0.1
	else:
		for i in range(n):
			for j in range(n):
				if i == j:
					continue
				else:
					res = []
					indices = [_ for _ in range(n)]
					indices.remove(i)
					indices.remove(j)
					res.append(float(nums[i]) + float(nums[j]))
					res.append(float(nums[i]) - float(nums[j]))
					res.append(float(nums[i]) * float(nums[j]))
					res.append(float(nums[j]) - float(nums[i]))
					if float(nums[i]) != 0:
						res.append(float(nums[j]) / float(nums[i]))
					if float(nums[j]) != 0:
						res.append(float(nums[i]) / float(nums[j]))
					left = [nums[k] for k in indices]
					for x in res:
						if check24(left+[x]):
							return True
		return False


nums = [4,4,4,3]
print check24(nums)


