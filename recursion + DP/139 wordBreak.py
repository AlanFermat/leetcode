def wordBreak(s,wordDict):
	if not s:
		return False
	else:
		s = "-" + s
		n = len(s)
		d = [0] * n
		d[0] = True
		for i in range(n):
			for j in range(i):
				if d[j] == True and s[j+1:i+1] in wordDict:
					d[i] = True
				if d[i] == True:
					break
			print d
		if d[n-1] == True:
			return True
		else:
			return False
				

w = []
s = "a"
print wordBreak(s,w)