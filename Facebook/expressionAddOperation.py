def addOperators(self, num, target):
	"""
	:type num: str
	:type target: int
	:rtype: List[str]
	"""
	if not num:
		return []
	if len(num) == 1:
		if int(num) == target:
			return [num]
		return []
	def helper(num, target, start, last_item,summation, local, res):
		if len(num) == start and summation == target:
			res.append(local)
		for end in range(start+1, len(num) + 1):
			my_num = num[start:end]
			if len(my_num) > 1 and my_num[0] == "0":
				break
			cur = int(my_num)
			if start == 0:
				helper(num, target, end,cur,summation+cur, local+str(cur),res)
			else:
				helper(num, target, end, cur,summation+cur, local + "+" + str(cur), res)
				helper(num, target, end, -cur,summation-cur, local + "-" + str(cur), res)
				helper(num, target, end, last_item*cur,summation-last_item+(last_item*cur), local + "*" + str(cur), res)
				
		
	res = []
	local = ""
	summation = 0
	helper(num, target, 0, 0,summation, local, res)
	return res