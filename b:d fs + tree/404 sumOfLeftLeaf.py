from binaryTree import Node
from treeTraverse import *
node = Node(3)
node.left=Node(9)
node.right = Node(20)
node.right.left = Node(15)
node.right.right = Node(7)

def getLeaf(root):
	if not root:
		return 0
	flag = root.left and (not root.left.left) and (not root.left.right)
	if flag:
		return root.left.val+getLeaf(root.left) + getLeaf(root.right)
	return getLeaf(root.left) + getLeaf(root.right)

print (getLeaf(node))