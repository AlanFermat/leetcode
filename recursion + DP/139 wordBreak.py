# def wordBreak(s,wordDict):
# 	if not s:
# 		return False
# 	else:
# 		s = "-" + s
# 		n = len(s)
# 		d = [0] * n
# 		d[0] = True
# 		for i in range(n):
# 			for j in range(i):
# 				if d[j] == True and s[j+1:i+1] in wordDict:
# 					d[i] = True
# 				if d[i] == True:
# 					break
# 		return d[n-1]
	
def sol(s, wordDict):
	n = len(s)
	for j in range(1, len(s)+1):
		if helper(s, wordDict, 0, j, n):
			return True
	return False


def helper(s, wordDict, i, j, n):
	if i >= j:
		return True
	if s[i:j] in wordDict:
		if j >= n :
			return True
		for k in range(j+1, len(s)+1):
			if helper(s, wordDict, j, k, n):
				return True
	return False


w = ["aaaa","aa"]
s = "aaaaaaa"
print (sol(s,w))




# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# print (sol(s,wordDict))
