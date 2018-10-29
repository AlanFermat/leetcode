def multiply(s1,s2):
	res = [0] * (len(s1) + len(s2)+1)
	pos = len(res) - 1
	for n1 in reversed(s1):
		tempPos = pos
		for n2 in reversed(s2):
			temp = int(n1) * int(n2)
			res[tempPos] += temp
			res[tempPos-1] += res[tempPos] // 10
			res[tempPos] %= 10
			tempPos -= 1
		pos -= 1
	pt = 0 
	while pt < len(res) and res[pt] == 0:
		pt += 1
	return "".join(map(str, res[pt:]))

s1 = "392"
s2 = "233"
print (392 * 233)
print (multiply(s1,s2))