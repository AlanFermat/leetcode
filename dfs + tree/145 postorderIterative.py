def postorder(root):
	stack = []
	res = []
	if not root:
		return res
	while True:
		while root:
			stack.append(root)
			res.append(root.val)
			root = root.right
		if not stack:
			return res[::-1]
		node = stack.pop()
		root = node.left
		
