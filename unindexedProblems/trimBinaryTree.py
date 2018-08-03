class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t = TreeNode(3)
t.left = TreeNode(0)
t.right = TreeNode(4)
t.left.left  = TreeNode(2)
t.left.right  = TreeNode(2)
t.left.right.left = TreeNode(1)
t.left.right.right = TreeNode(1)

def trimTree(root,lower,upper):
	if root == None:
		return root
	if root.val > upper:
		return trimTree(root.left, lower, upper)
	if root.val < lower:
		return trimTree(root.right, lower, upper)
	root.left = trimTree(root.left, lower, upper)
	root.right = trimTree(root.right, lower, upper)
	return root

t = trimTree(t,1,2)
print t.val
print t.left.val
print t.right.val



	