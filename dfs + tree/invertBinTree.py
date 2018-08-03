from binaryTree import Node

def invertTree(root):
	if root == None:
		return None
	tl = invertTree(root.left)
	tr = invertTree(root.right)
	root.right = tl
	root.left = tr
	return root



node = Node(3)
node.left=Node(9)
node.right= Node(20)
node.right.left = Node(15)
node.right.left.right =Node(7)
node.right.left.left =Node(7)

node = invertTree(node)
print (node.left.val)