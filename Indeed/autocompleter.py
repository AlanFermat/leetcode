from collections import defaultdict as dd
class wordDict(object):
	"""docstring for word"""
	def __init__(self):
		self.terminate = False
		self.child = dd(wordDict)


	def add(self, word):
		cur = self
		for c in word:
			cur = cur.child[c]
			# print (cur.child)
		cur.terminate = True

	def autocompleter(self, word):
		l = list(word)
		n = len(l)
		idx = 0
		while idx < n:
			if l[idx].istitle() and idx > 0:
				l.insert(idx, "*")
				idx += 2
				n += 1
			else:
				idx += 1
		# print (l)
		res = []
		self.helper(l, "", res)
		return res

	def helper(self, l, path, res):
		cur = self
		if not l:
			cur.backtrack(path,res)
			return
		top = l[0]
		if top != "*":
			l.pop(0)
			if top not in cur.child:
				return
			cur = cur.child[top]
			cur.helper(l, path + top, res)
		else:
			for letter in cur.child:
				if letter.istitle():
					if letter != l[1]:
						return 
					else:
						if cur.terminate and l[2:]:
							return
						cur2 = cur.child[letter]
						l1 = l[2:]
						# print (l1,path + letter, cur.child[letter])
						cur2.helper(l1, path + letter, res)
				else:				
					cur1 = cur.child[letter]
					cur1.helper(l, path + letter, res)

			

	def backtrack(self, path, res):
		cur = self
		if cur.terminate:
			res.append(path)
		for key in cur.child:
			path += key
			cur1 = cur.child[key]
			cur1.backtrack(path, res)
			path = path[:-1]
		return 






wordlist = ["GraphView", "DataGraphView","DGV","DotGrap","DiscoveryGraph","DataScienceGraph","DataGeography","DataGrip","DataController","DGViii","DGrrVi","DataScienceView","GraphViewController"]
# wl = ["DGV","DGVi"]
q = wordDict()
for word in wordlist:
	q.add(word)

print (q.autocompleter("DGrVi"))


# q.helper(['i'],"DGV",[])

# print ("A".istitle())

# "D*G*Vi"
# "*G*Vi"
# ""

#"G", "a"
#  G "*Vi" GV
#  a  "*G*Vi"


		

