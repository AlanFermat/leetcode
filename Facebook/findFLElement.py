def find(nums, target):	
	def search(nums, target):
		lo = 0
		hi = len(nums) - 1
		while lo <= hi:
			mid = (lo + hi) >>1 
			if nums[mid] == target:
				return True
			else:
				if nums[mid] > target:
					hi = mid - 1
				else:
					lo = mid + 1
		return False

	def left(nums, target):
		lo = 0
		hi = len(nums) - 1
		while lo <= hi:
			mid = (lo + hi) >>1 
			if nums[mid] < target:
				lo = mid + 1
			else:
				hi = mid - 1
		return lo

	def right(nums, target):
		lo = 0
		hi = len(nums) - 1
		while lo <= hi:
			mid = (lo + hi) >>1 
			if nums[mid] > target:
				hi = mid - 1
			else:
				lo = mid + 1
		return hi

	if search(nums, target):
		return [left(nums, target), right(nums, target)]
	return [-1, -1]


nums = [1,4,4,4,7,8]
target = 4
print (find(nums, target))

