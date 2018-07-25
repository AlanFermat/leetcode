from binaryTree import Node
from treeTraverse import *
from levelTraverseTree import *

def pathSum(root, target):
	if not root:
		return []
	if not root.left and not root.right and root.val == target:
		return [[root.val]]
	temp = pathSum(root.left, target-root.val) + pathSum(root.right, target-root.val)
	return [[root.val] + i for i in temp]

target = 22
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)
root.right.right.left = Node(5)

print (pathSum(root, target))
