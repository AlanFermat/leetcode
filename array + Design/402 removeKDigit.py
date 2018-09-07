def removeKdigits(num, k):
	"""
	:type num: str
	:type k: int
	:rtype: str
	"""
	n = len(num)
	if n <= k:
		return "0"
	idx = 0
	stack = []
	res = ""
	while idx < n:
		while k > 0 and stack and int(stack[-1]) > int(num[idx]):
			stack.pop()
			k -= 1
		stack.append(num[idx])
		idx += 1
	while k > 0:
		stack.pop()
		k -= 1
	res = "".join(stack).lstrip("0")
	if not res:
		return "0"
	return res

num = "19349876"
k = 2


print (removeKdigits(num, k))



