from binaryTree import Node
from treeTraverse import *
node = Node(3)
node.left=Node(20)
node.right= Node(9)
node.left.left = Node(7)
node.left.right =Node(15)


node_list = preorderTraverse(node)
node_list.sort()
n = len(node_list)
print (node_list)


def arrToBST(arr,root):
	"""
		just apply sorted array to BST
	"""
	if not root:
		return 
	arrToBST(arr, root.left)
	root.val = arr[0]
	arr.pop(0)
	arrToBST(arr, root.right)

def binTreeToBST(root):
	if not root:
		return None
	arr = inorderTraverse(root)
	arr.sort()
	arrToBST(arr,root)

binTreeToBST(node)
print (inorderTraverse(node))