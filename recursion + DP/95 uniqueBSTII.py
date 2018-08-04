# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def generateTrees(self, n):
		"""
		:type n: int
		:rtype: List[TreeNode]
		"""
		if not n:
			return []
		def recursion(start, end):
			if start == end:
				return [TreeNode(start)]
			if start > end:
				return [None]
			res = []
			for i in range(start, end+1):
				left = recursion(start, i-1)
				right = recursion(i+1, end)
				for l in left:
					for r in right:
						root = TreeNode(i)
						root.left = l
						root.right = r
						res.append(root)
			return res
		return recursion(1, n)
		