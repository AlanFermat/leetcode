class Node(object):
	"""docstring for Tree"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
def valid(root):
	if not root:
		return True
	if root.left and root.right:
		if root.left.val > root.val or root.right.val < root.val:
			return False
		else:
			return valid(root.left) and valid(root.right)
	if root.left:
		if root.left.val > root.val:
			return False
		else:
			return valid(root.left)
	if root.right:
		if root.right.val < root.val:
			return False
		else:
			return valid(root.right)
	return True

t =  Node(5)
t.left = Node(3)
t.left.left = Node(2)
t.left.right = Node(4)

print (valid(t))



	