class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.left.left = TreeNode(5)
t1.right = TreeNode(2)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.left.right = TreeNode(4)
t2.right = TreeNode(3)
t2.right.right = TreeNode(7)

def mergeTree(t1,t2):
	"""
		input:  t1: TreeNode
				t2: TreeNode
		rtype: TreeNode
	"""
	if t1 == None:
		return t2
	if t2 == None:
		return t1
	t1.val += t2.val
	t1.left = mergeTree(t1.left, t2.left)
	t1.right = mergeTree(t1.right, t2.right) 
	return t1
	

t = mergeTree(t1,t2)
print t.left.right.val
