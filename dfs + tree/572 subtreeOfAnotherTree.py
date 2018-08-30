def isSubtree(s, t):
	"""
	:type s: TreeNode
	:type t: TreeNode
	:rtype: bool
	"""
	if not t:
		return True
	def check(root_s,root_t):
		if not root_s and not root_t:
			return True
		if (not root_s and root_t) or  (root_s and not root_t):
			return False
		if root_s.val != root_t.val:
			return False
		return check(root_s.left,root_t.left) and check(root_s.right, root_t.right)
	
	def dfs(s,t):
		if not s and t:
			return False
		if check(s,t):
			return True
		return dfs(s.left, t) or dfs(s.right,t)
	return dfs(s,t)