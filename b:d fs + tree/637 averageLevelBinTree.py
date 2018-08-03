from binaryTree import Node

node = Node(3)
node.left=Node(9)
node.right= Node(20)
node.left.left = Node(3)
node.left.left.right = Node(34)
node.left.left.left = Node(13)
node.right.left = Node(15)
node.right.right =Node(7)

# do a BFS so that we can do average
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
	"""
		concat the nodes of tree
		on level d
	"""
	if t == None:
		return []
	if d == 1:
		return [t.val]
	if d > 1:
		return levelConcat(t.left, d-1) + levelConcat(t.right, d-1)


def bfsTree(t):
	n = height(t)
	result = {}
	for i in range(1,n+1):
		result[i] = levelConcat(t,i)
	return result

levelVal = bfsTree(node)
averageVal = []
for key in levelVal.keys():
	averageVal.append(sum(levelVal[key]) * 1.0/len(levelVal[key]))
print (averageVal)




