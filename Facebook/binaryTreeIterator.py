class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BSTIterator(object):
	"""docstring for bSTIterator"""
	
	def __init__(self, root):
		self.stack = []
		self.operation(root)

	def operation(self, root):
		while root:
			self.stack.append(root)
			root = root.left

	def hasNext(self):
		return len(self.stack) >= 1

	def next(self):
		if not self.hasNext():
			return None
		else:
			node = self.stack.pop()
			if node.right:
				self.operation(node.right)
			return node.val



root = TreeNode(7)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

it = BSTIterator(root)
print (it.next())
print (it.next())
print (it.next())
print (it.next())
print (0%(-1))
