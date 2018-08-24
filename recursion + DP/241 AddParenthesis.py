def diffWatCompute(input):
	temp = []
	if not input:
		return []
	n = len(input)
	idx = 0
	num = 0
	factor = 1
	while idx < n:
		c = input[idx]
		if c.isdigit():
			num = int(c) + num * factor
			factor *= 10
			idx += 1
		else:
			temp.append(num)
			temp.append(c)
			factor = 1
			num = 0
			idx  += 1
	temp.append(num)
	def helper(arr):
		if len(arr) == 1:
			return [arr[0]]
		if len(arr) == 3:
			if arr[1] == "*":
				return [arr[0] * arr[2]]
			if arr[1] =="-":
				return [arr[0] - arr[2]]
			if arr[1] == "+":
				return [arr[0] + arr[2]]
		n = len(arr)
		m = (n-1)//2
		res = []
		for i in range(m):
			operation = arr[2*i+1]
			left = helper(arr[:2*i+1])
			right = helper(arr[2*i+2:])
			if operation == "*":
				for l in left:
					for r in right:
						res.append(l * r)
			elif operation == "+":
				for l in left:
					for r in right:
						res.append(l + r)
			else:
				for l in left:
					for r in right:
						res.append(l - r)
		return res
	return helper(temp)

		

input = "11"
print (diffWatCompute(input))
