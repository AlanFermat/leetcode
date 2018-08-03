def findWords(board, words):
	"""
	:type board: List[List[str]]
	:type words: List[str]
	:rtype: List[str]
	"""
	if not words:
		return []
	if not board:
		return []
	if not board[0]:
		return []
	res = []
	for word in words:
		cp = copy(board)
		if canFind(cp, word):
			res.append(word)
	return res

def copy(board):
	temp = []
	for i in range(len(board)):
		store = []
		for j in range(len(board[0])):
			store.append(board[i][j])
		temp.append(store)
	return temp

def canFind(board, word):
	if not word:
		return True
	m = len(board)
	n = len(board[0])
	for i in range(m):
		for j in range(n):
			if exist(board, word, i, j, m, n):
				return True
	return False

def exist(board, word, i, j, m, n):
	if board[i][j] == word[0]:
		board[i][j] = ""
		if not word[1:]:
			return True
		else:
			if i + 1 < m and  exist(board, word[1:], i+1, j, m, n):
				return True
			if j + 1 < n and  exist(board, word[1:], i, j+1, m, n):
				return True
			if i - 1 > -1 and  exist(board, word[1:], i-1, j, m, n):
				return True
			if j - 1 > -1 and  exist(board, word[1:], i, j-1, m, n):
				return True
		board[i][j] = word[0]
	else:
		return False


input = ["oath","eat"]
board =[['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
print (findWords(board,input))
