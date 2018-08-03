from binaryTree import *
from levelTraverseTree import *
from treeTraverse import *
def construct(start,end,nums):
	if len(nums) == 0:
		return None
	elif len(nums) == 1:
		return Node(nums[0])	
	else:
		m = max(nums)
		root = Node(m)
		idx = nums.index(m)
		root.left = construct(0, idx, nums[start:idx])
		root.right = construct(0, end - idx + 1, nums[idx+1:end])
		return root

	


def constructMAX(nums):
	n = len(nums)
	r = construct(0,n,nums)
	return r

nums = [3,4,2,1,6,0,5]
r= constructMAX(nums)
print inorderTraverse(r)
print bfsTree(r)