from binaryTree import Node
from treeTraverse import *
def sortedArrToBST(arr,start,end):
	"""
		The inorder traverse of BFS is 
		the same as the sorted array
	"""
	if start > end:
		return None
	if start == end:
		return Node(arr[start])
	mid = (start + end)/2 + 1
	root = Node(arr[mid])
	root.left = sortedArrToBST(arr,start, mid-1)
	root.right = sortedArrToBST(arr, mid+1 , end)
	return root



# arr =[2,7,9,15,20]
# n = len(arr)
# root =sortedArrToBST(arr,0,n-1)
# print (inorderTraverse(root))

