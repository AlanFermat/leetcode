def solve(candidates, target):
	res = []
	candidates = sorted(candidates)
	def comboHelper(temp, arr, target):
		summ = sum(temp)
		if summ == target:
			res.append(temp)
		elif summ > target:
			return
		else:
			for i, num in enumerate(arr):
				if summ + num > target:
					return
				else:
					comboHelper(temp + [num], arr[i:], target)
	comboHelper([], candidates, target)
	return res



		

target = 7
candidates = [2,3,6,7]
print (solve(candidates, target))