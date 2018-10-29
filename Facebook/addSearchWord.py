from collections import defaultdict as dd
class wordDictionary(object):
	"""docstring for wordDictionary"""
	def __init__(self):
		self.terminate = False
		self.child = dd(wordDictionary)

	def addWord(self, word):
		cur = self
		for c in word:
			cur = cur.child[c]
		cur.terminate = True

	def search(self, word):
		cur = self
		def helper(cur, word):
			if not word:
				return cur.terminate == True
			else:
				c = word[0]
				word = word[1:]
				if c != ".":
					if c not in cur.child:
						return False
					else:
						cur = cur.child[c]
						return helper(cur, word)
				else:
					for k in cur.child:
						if helper(cur.child[k],word):
							return True
					return False
		return helper(cur, word)

w = wordDictionary()
w.addWord("abcdf")
w.addWord("abcd")
print (w.search("abcd"))
