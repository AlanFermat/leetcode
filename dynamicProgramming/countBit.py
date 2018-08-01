def countBits(num):
	"""
	:type num: int
	:rtype: List[int]
	"""
	if not num:
		return [0]
	if num == 1:
		return [0,1]
	if num ==2:
		return [0,1,1]
	ans = [0 for _ in range(num+1)]
	def checkPower(num):
		for idx in range(num):
			if 2 ** idx > num:
				return idx
	
	
	# fill the entries whose index is power of 2
	# by 1
	p = checkPower(num)
	for power in range(p):
		ans[2 ** power] = 1
	
	# now look at the rest of the numbers
	count = 3
	curr_p = 1
	
	while count < num+1:
		if not ans[count]:
			
			ans[count] = 1 + ans[count-2**curr_p]
			count += 1
		else:
			curr_p += 1
			count += 1
	print (ans)
	return ans

num = 10

countBits(num)