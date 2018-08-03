from binaryTree import Node
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

# these are dfs of the tree
def inorderTraverse(tree):
	"""
		left root right
	"""
	if not tree:
		return []
	return inorderTraverse(tree.left) + [tree.val] + inorderTraverse(tree.right)


def preorderTraverse(tree):
	"""
		root left right
	"""
	if not tree:
		return []
	return [tree.val] + preorderTraverse(tree.left) + preorderTraverse(tree.right)


def postorderTraverse(tree):
	"""
		left right root
	"""
	if not tree:
		return []
	return  postorderTraverse(tree.left) + postorderTraverse(tree.right) + [tree.val]

print inorderTraverse(root)

a = [None, None]

# print preorderTraverse(root)

# print postorderTraverse(root)