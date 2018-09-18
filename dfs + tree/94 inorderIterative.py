def inorder(root):
	if not root:
		return []
	stack, res =[], []
	while True:
		while root:
			stack.append(root)
			root = root.left
		if not stack:
			return res
		node = stack.pop()
		res.append(node.val)
		root = node.right
		