class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def serialize(root):
	if not root:
		return "[]"
	temp = [root]
	res = []
	while temp:
		node = temp.pop(0)
		if not node:
			res.append(None)
		else:
			res.append(node.val)
			temp.append(node.left)
			temp.append(node.right)
	idx = len(res) - 1
	while idx > -1:
		if res[idx] == None:
			res.pop()
			idx -= 1
		else:
			break

	print (str(res))
	return str(res)

def deserialize(data):
	if data == "[]":
		return None
	tree = data.split(",")
	if len(tree) == 1:
		return TreeNode(int(tree[0][1:-1]))
	tree[0] = tree[0][1:]
	tree[-1] = tree[-1][:-1]
	root = TreeNode(int(tree[0]))
	node_list = [root]
	i, j = 0, 1
	n = len(tree)
	for i in range(len(tree)):
		tree[i] = tree[i].replace(' ', "")
	while j < n and node_list:
		node = node_list.pop(0)
		if node:
			if tree[j] != "None":
				node.left = TreeNode(int(tree[j]))
			else:
				node.left = None
			node_list.append(node.left)
			j += 1
			if j < n:
				if tree[j] != "None":
					node.right = TreeNode(int(tree[j]))
				else:
					node.right = None
				node_list.append(node.right)
			j += 1
	return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

root1 = TreeNode(3)
res1 = serialize(root)
print (deserialize(res1).left.val)


