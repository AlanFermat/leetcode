from heapq import *

def removeKDigit(num, k):
	if not num:
		return "0"
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

num = "16003405"
k = 2
print (removeKDigit(num, k))
				
	


			