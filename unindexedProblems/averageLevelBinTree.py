class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def averageLevelBinTree(root):
	if root == None:
		return []
	if root.left == None and root.right == None:
		return [root]
	aleft = self.averageOfLevels(root.left)
	aright = self.averageOfLevels(root.right)
	a = []
	i = 0
	while i < min(len(aleft), len(aright)):
		a[i] = (aleft[i] + aright[i] )/2.0
	if i < len(aleft):
		a.append(aleft[i:len(aleft)])
	if i < len(aright):
		a.append(aright[i:len(aright)])
	return a