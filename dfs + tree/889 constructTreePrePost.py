def constructFromPrePost(pre, post):
	"""
	:type pre: List[int]
	:type post: List[int]
	:rtype: TreeNode
	"""
	if not pre:
		return None
	root = TreeNode(pre[0])
	if len(pre) == 1 or len(post) == 1:
		return root
	right_sub = pre.index(post[-2]) 
	root.left = self.constructFromPrePost(pre[1:right_sub], post[:right_sub-1])
	root.right = self.constructFromPrePost(pre[right_sub:], post[right_sub-1:-1])
	return root