def fibonacci(length):
	"""
	length : int >=1 
	"""
	if length == 1:
		return [0]
	elif length == 2:
		return [0,1]
	else:
		ans = [0,1]
		for add in range(1,length):
			ans.append(ans[add]+ans[add-1])
		return ans

f = fibonacci(10)
# print f
g = list(map(lambda x: x % 2, f))
print g


