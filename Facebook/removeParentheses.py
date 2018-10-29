class solution(object):
	"""docstring for solution"""
		
	def removeParentheses(self, s):
		if not s:
			return [""]
		
		self.flag = False
		self.res = set()
		self.visit = dict()
		self.bfs(s)
		return list(self.res)

	def bfs(self, s):
		
		q = [s]
		while q:
			ss = q.pop(0)
			n = len(ss)
			idx = 0
			if self.isValid(ss):
				self.res.add(ss)
				self.flag = True
				continue
			if self.flag:
				continue 
			while idx < n:
				c = ss[idx]
				if self.isParenthesis(c):
					new_s = ss[:idx] + ss[idx+1:]
					if not self.visit.get(new_s, 0):
						self.visit[new_s] = 1
						q.append(new_s)
				idx += 1
		
	def isParenthesis(self, c):
		return c in ["(", ")"]

	def isValid(self, s):
		s_l = list(s)
		score = 0
		while s_l:
			if s_l[-1] == ")":
				score += 1
				s_l.pop()
			elif s_l[-1] == "(":
				score -= 1
				if score < 0 :
					return False
				s_l.pop()
			else:
				s_l.pop()
		return score == 0


a = solution()
s = "((a()"
print (a.removeParentheses(s))



