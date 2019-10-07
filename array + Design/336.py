def solve(words):
	def isPalindrome(word):
		start = 0
		end = len(word) - 1
		while start < end:
			if word[start] == word[end]:
				start += 1
				end -= 1
			else:
				return False
		return True
	res = set()
	d = {w:i for i, w in enumerate(words)}
	for i, word in enumerate(words): #n
		for j in range(len(word) + 1): #k
			w1 = word[:j]
			w2 = word[j:]
			w1_reverse = w1[::-1]
			w2_reverse = w2[::-1]
			if w1_reverse in d and isPalindrome(w2):
				if i != d[w1_reverse]:
					res.add((i, d[w1_reverse]))
			if w2_reverse in d and isPalindrome(w1):
				if i != d[w2_reverse]:
					res.add((d[w2_reverse], i))
	return list(res)



				
	

words = ["abcd","dcba","lls","s","sssll",""]
expected = [[0,1],[1,0],[3,2],[2,4]] 
print (solve(words))


