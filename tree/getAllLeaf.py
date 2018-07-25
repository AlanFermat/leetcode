from binaryTree import Node
def getLeaf(root):
	if not root:
		return []
	if not root.right and not root.left:
		return [root.val]
	return getLeaf(root.left) + getLeaf(root.right)

node = Node(3)
node.left=Node(20)
node.right= Node(9)
node.left.left = Node(7)
node.left.right =Node(15)
node.right.right= Node(19)