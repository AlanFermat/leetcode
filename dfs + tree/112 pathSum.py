from binaryTree import *
def pathSum(root,summation):
	if not root:
		return False
	if not root.left and not root.right:
		return (root.val == summation)
	return pathSum(root.left, summation - root.val) or pathSum(root.right, summation - root.val)


root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right  = Node(1)
summation = 18
print pathSum(root, summation)