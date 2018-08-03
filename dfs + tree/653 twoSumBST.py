from binaryTree import Node
from treeTraverse import *
node = Node(5)
node.left=Node(3)
node.right= Node(6)
node.left.left = Node(2)
node.left.right =Node(4)
node.right.right = Node(7)
target = 10

# use two sum in array
node_list = inorderTraverse(node)
def twoSum(arr,target):
	"""
		O(n) solution for two sum
	"""
	maxVal = max(arr)
	help_list= [0] * (maxVal +1)
	for j in range(len(arr)):
		need = target - arr[j]
		if need < maxVal:
			if help_list[need] == 1:
				return True
			help_list[arr[j]] += 1
	return False


print (twoSum(node_list, target))


# Do not use two sum in array
def driver(root, target):
	if not root :
		return False
	return findComplement(root,set([]), target)

def findComplement(root,nodes,target):
	if root == None:
		return False
	complement  = target - root.val
	if complement in nodes:
		return True
	nodes.add(root.val)
	return findComplement(root.left, nodes,target) or findComplement(root.right, nodes, target)

print (driver(node,target))
