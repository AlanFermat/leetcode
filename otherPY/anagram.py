def isAnagram(s,t):
	compare = list(t)
	temp = list(s)
	if len(temp) != len(compare):
		return False
	else:
		temp.sort() 
		compare.sort()
		print temp, compare
		return temp == compare


s = "a"
t = "b"
print isAnagram(s,t)