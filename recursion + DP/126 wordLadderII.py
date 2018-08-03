def ladderLength(beginWord, endWord, wordList):
	"""
	:type beginWord: str
	:type endWord: str
	:type wordList: List[str]
	:rtype: int
	"""
	wordList = set(wordList)
	if endWord not in wordList:
		return 0
	q = []
	q.append([beginWord,1])
	storage = "abcdefghijklmnopqrstuvwxyz"
	while q:
		w, length = q.pop(0)
		if w == endWord:
			return length
		for i in range(len(w)):
			for c in storage:
				cat = w[:i] + c + w[i+1:]
				if cat in wordList:
					q.append([cat, length+1])
					wordList.remove(cat)
	return 0

def findLadders(beginWord, endWord, wordList):
	"""
	:type beginWord: str
	:type endWord: str
	:type wordList: List[str]
	:rtype: List[List[str]]
	"""
	min_length = ladderLength(beginWord, endWord, wordList)
	wordList = set(wordList)
	ans = []
	if min_length == 0:
		return ans
	q = [(beginWord, 1)]

	storage = "absdefghijklmnopqrstuvwxyz"
	def find(qu, li,temp):
		if qu:
			w, l = qu.pop(0)
			if l == min_length and w != endWord:
				return          
			if l == min_length and w == endWord:
				ans.append(temp)
			for i in range(len(w)):
				for c in storage:
					candidate = w[:i]+c+w[i+1:]
					if candidate in li:	
						li.remove(candidate)
						find(qu+[(candidate, l+1)], li, temp+[candidate])
	find(q, wordList,[beginWord])
	return ans

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print (findLadders(beginWord, endWord, wordList))

