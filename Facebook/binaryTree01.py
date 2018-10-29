class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None



root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)

# bottom up 
# until parent does not change or reach the root
