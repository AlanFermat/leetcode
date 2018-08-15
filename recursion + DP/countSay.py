def countSay(n):
	if not n:
		return ""
	s = "1"
	for i in range(n-1):
		res = ""
		temp = s[0]
		count = 0
		for char in s:
			if char != temp:
				res += str(count) + temp 
				count = 1
				temp = char
			else:
				count += 1
		res += str(count) + temp
		s = res
	return s

n = 7
print (countSay(n))