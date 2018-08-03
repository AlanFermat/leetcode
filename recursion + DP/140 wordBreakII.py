def wordBreak(s,wordDict):
	n = len(s)
	words = set(wordDict)
	dp = [[] for _ in range(n)]
	for end in range(n):
		for start in range(end+1):
			if s[start:end+1] in words and (start == 0 or dp[start-1]):
				dp[end].append(start)
	if not dp[-1]:
		return []
	print (dp)
	def backtracking(endIndex, current):
		if endIndex < 0:
			if current:
				yield " ".join(current)
			return 
		for start in dp[endIndex]:
			current.insert(0, s[start:endIndex+1])
			for solution in backtracking(start-1, current):
				yield solution
			current.pop(0)


	return list(backtracking(n-1, []))







					
				

w = ["apple", "pen", "applepen", "pine", "pineapple"]
s = "pineapplepenapple"
ww = ["a","b","aa"]
ss = "aab"
print (wordBreak(ss,ww))

