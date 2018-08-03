def findWords(board, words):
	ans = []
	if not board:
		return []
	if not board[0]:
		return []
		# construct the trie
	trie = {}
	trie[0] = {}
	depth = 1
	m, n = len(board), len(board[0])
	visit = [[False for _ in range(n)] for _ in range(m)]
	for w in words:
		curr_node = trie[0]
		for c in w:
			if c not in curr_node:
				curr_node[c] = depth 
				trie[depth] = {}
				depth += 1
			curr_node = trie[curr_node[c]]
		curr_node['$'] = w # mark the end of a word chain
	
	def explore(board, i, j, layer):
		visit[i][j] = True
		if '$' in layer:
			if layer['$'] not in ans:
				ans.append(layer['$'])
		for x, y in (i+1, j),  (i-1, j), (i, j+1), (i, j-1):
			if 0 <= x < m and 0 <= y < n and board[x][y] in layer and not visit[x][y]:
				explore(board, x, y, trie[layer[board[x][y]]])
		visit[i][j] = False



	for i in range(m):
		for j in range(n):
			if board[i][j] in trie[0]:
				explore(board, i, j, trie[trie[0][board[i][j]]])

	return ans

board =[['o','a','a','n'],['e','t','a','e'],['i','h','k','p'],['i','f','l','v']]
words = ["oath","pea","eat","rain"]

print (findWords(board,words))



