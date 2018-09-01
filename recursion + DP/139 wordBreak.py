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
		return d[n-1]
				

w = ["leet","code"]
s = "leetcode"
print wordBreak(s,w)