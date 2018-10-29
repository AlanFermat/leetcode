class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		

def inorderTraversal(root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	if not root:
		return []
	stack = []
	res = []
	while True:
		while root:
			stack.append(root)
			root = root.left
		if not stack:
			return res
		node = stack.pop()
		res.append(node.val)
		root = node.right

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.left.right.right.right = TreeNode(8)

print (inorderTraversal(root))





	