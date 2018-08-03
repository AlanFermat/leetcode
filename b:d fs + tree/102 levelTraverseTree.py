# this is equivalent to the BFS of Tree
from binaryTree import Node
def height(t):
	"""
		input: root node
		output: height of the tree
	"""
	if t == None:
		return 0
	hl = height(t.left)
	hr = height(t.right)
	return max(hl,hr) + 1

def levelConcat(t,d):
	if t == None:
		return []
	if d == 1:
		return [t.val]
	if d > 1:
		return levelConcat(t.left, d-1) + levelConcat(t.right, d-1)


def bfsTree(t):
	n = height(t)
	result = []
	for i in range(1,n+1):
		result += levelConcat(t,i)
	return result

# node = Node(3)
# node.left=Node(9)
# node.right= Node(20)
# node.right.left = Node(15)
# node.right.left.right =Node(7)
# node.right.left.left =Node(7)
# print (bfsTree(node))