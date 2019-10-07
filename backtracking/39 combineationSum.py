def combine(candidates,target):
	# candidates = sorted(candidates)
	res = []
	def track(arr, aim, temp):
		summ = sum(temp)
		if summ == aim:
			res.append(temp)
		elif summ > aim:
			return
		else:
			for pos, num in enumerate(arr):
				if num + summ  <= aim:
					track(arr[pos:], aim, temp + [num])
				else:
					return 
	track(candidates, target, [])
	return res


candidates = [2,3,4]
target =7
print(combine(candidates, target))
		
