def minCut(s):
	"""
	:type s: str
	:rtype: int
	"""
	pal = checkPal(s)
	cutMin = []
	for i in range(len(s)):
		cutMin.append(i+1)
	for i in range(len(s)):
		for j in range(i+1):
			if pal[j][i]:
				if j == 0:
					cutMin[i] = 0
				else:
					cutMin[i] = min(cutMin[i], cutMin[j-1] + 1)

	return cutMin[len(s)-1]
					
			
		
def checkPal(s):
	pal = [[False for _ in range(len(s))] for _ in range(len(s))]
	
	for i in range(len(s)):
		pal[i][i] = True
	for i in range(1,len(s)):
		pal[0][i] = True if s[:i+1] == s[i::-1] else False
	
	for k in range(len(s)-1):
		pal[k][k+1] = True if s[k] == s[k+1] else False
		
	for diff in range(2, len(s)-1):
		for idx in range(len(s)-2):
			if idx + diff < len(s):
				if s[idx] == s[diff + idx] and pal[idx+1][idx+diff-1] == True:
					pal[idx][idx+diff] = True
	return pal
s = "aabaacdcfc"
print (s)
print (minCut(s))