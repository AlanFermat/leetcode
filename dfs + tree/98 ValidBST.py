def isValidBST(root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	def helper(node,minval, maxval):
		if not node:
			return True
		if minval >= node.val or maxval <= node.val:
			return False
		return helper(node.left, minval, node.val) and helper(node.right, node.val, maxval)
		
	if not root:
		return True
	else:
		return helper(root,-float("inf"), float("inf"))