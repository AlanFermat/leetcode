from binaryTree import Node
from treeTraverse import *
from arrToBST import *
root = Node(5)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(9)
root.left.right.left = Node(7)
root.left.right.right = Node(11)
root.right = Node(13)

def BSTtoGT(root):
	node_list = inorderTraverse(root)
	summation = sum(node_list)
	idx = 0
	while idx < len(node_list):
		summation -= node_list[idx]
		node_list[idx] += summation
		idx +=1 
	return sortedArrToBST(node_list,0,len(node_list)-1)

root = BSTtoGT(root)
print (inorderTraverse(root))

summation = 0

# def BST2GT(root):
# 	convert(root)
# 	return root

# def convert(cur):
# 	global summation
# 	if cur == None:
# 		return 
# 	convert(cur.right)
# 	cur.val += summation
# 	summation = cur.val
# 	convert(cur.left)


# root = BST2GT(root)
# print (inorderTraverse(root))
