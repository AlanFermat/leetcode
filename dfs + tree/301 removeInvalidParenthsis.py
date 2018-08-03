class Solution(object):    
	def removeInvalidParentheses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		if not s:
			return [""]
		self.result = set()
		self.flag = False
		self.visit = set()
		self.bfs(s)
		return list(self.result)
	
		
		
	def bfs(self, s):
		q = [s]
		while q:
			curr = q.pop(0)
			if self.isValid(curr):
				self.result.add(curr)
				self.flag = True
				continue
			if self.flag == True:
				continue
			for i in range(len(curr)):
				if self.isParenthesis(curr[i]):
					candidate = curr[:i] + curr[i+1:]
					if candidate not in self.visit:
						self.visit.add(candidate)
						q.append(candidate)
		return 
			
	
	
	def isParenthesis(self,c):
		if c in ["(",")"]:
			return True
		return False
	
	def isValid(self, curr):
		idx = 0
		val = 0
		while idx < len(curr):
			if curr[idx] == "(":
				val += 1
			if curr[idx] == ")":
				val -= 1
				if val < 0:
					return False
			idx += 1
		return val == 0


s = "(1)()(a"
p = Solution()
print (p.removeInvalidParentheses(s))


