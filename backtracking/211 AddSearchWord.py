from collections import defaultdict as dd
class WordDictionary(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.child = dd(WordDictionary)
		self.isleaf = False
		
		

	def addWord(self, word):
		"""
		Adds a word into the data structure.
		:type word: str
		:rtype: void
		"""
		curr = self
		for c in word:
			curr = curr.child[c]
		curr.isleaf = True
		
		
		

	def search(self, word):
		"""
		Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
		:type word: str
		:rtype: bool
		"""
		def helper(level, w, curr):
			if level == len(w):
				return curr.isleaf
			else:
				if w[level] == ".":
					candidate = curr.child.keys()
					for letter in candidate:
						if helper(level+1, w, curr.child[letter]):
							return True
					return False
				else:
					if curr.child.get(word[level]):
						return helper(level+1, w, curr.child[w[level]])
					else:
						return False
					
			
			
		return helper(0,word, self)