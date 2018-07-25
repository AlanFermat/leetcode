def sortingMethod(seq, num):
	"""
	find (the position of )a pair of numbers in arr such that their sum is equal to num
	O(n log n)
	"""
	arr = list(seq)
	arr.sort()
	start = 0
	end = len(arr) -1
	while start < end:
		if arr[start] + arr[end] == num:
			return seq.index(arr[start]), seq.index(arr[end])
		elif arr[start] + arr[end] > num:
			end -= 1
		else:
			start += 1
	return -1, -1


MAX = 1000000
def hashMethod(seq, num):
	"""
	O(n) if the range of the numbers is known
	"""
	mapp = [0] * MAX
	for temp in seq:
		if mapp[num - temp] == 1:
			return temp, num- temp
		mapp[temp] = 1
	return -1,-1



seq = range(1000000) + range(10000)
num = 50600

print hashMethod(seq, num)
