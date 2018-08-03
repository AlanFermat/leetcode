from binaryTree import *
from collections import defaultdict as df
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

def Kdist(root, target, K):
	"""
		bfs for K distance starting from target
	"""
	res = []
	neighbor = df(list)
	def neighborDict(root):
		if not root:
			return
		if root.left:
			neighbor[root.val] += [root.left.val]
			neighbor[root.left.val] += [root.val]
			neighborDict(root.left)
		if root.right:
			neighbor[root.val] += [root.right.val]
			neighbor[root.right.val] += [root.val]
			neighborDict(root.right)
	neighborDict(root)
	def bfs(neighbor, t, K):
		queue = [(t,0)]
		v = {}
		for key in neighbor:
			v[key] = False
		v[t] = True
		while queue:
			node, layer = queue.pop(0)
			if layer == K:
				res.append(node)
			for nval in neighbor[node]:
				if not v[nval]:
					v[nval] = True
					queue.append((nval, layer+1))
	bfs(neighbor, target.val, K)
	return res



K = 2
target = Node(5)
print Kdist(root, target, K)

