class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def sortedListToBST(head):
	"""
	:type head: ListNode
	:rtype: TreeNode
	"""
	l = []
	while head:
		l.append(head.val)
		head = head.next
	node = listConvertBST(l)
	return node

def listConvertBST(l):
	if not l:
		return None
	n = len(l)
	mid = l[n/2]
	root = TreeNode(mid)
	root.left = listConvertBST(l[:mid])
	root.right = listConvertBST(l[mid+1:])
	return root
head = ListNode(10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
print sortedListToBST(head)

