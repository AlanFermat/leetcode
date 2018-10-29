class ListNode(object):
	"""docstring for ListNode"""
	def __init__(self, arg):
		self.val = arg
		self.next = None

def visualization(node):
	if not node:
		return ""
	else:
		return str(node.val) + "->" + visualization(node.next) if visualization(node.next) else str(node.val)

from heapq import *
def merge(lists):
	dummy = ListNode(0)
	cur = dummy
	p = []
	for root in lists:
		heappush(p,[root.val, root])
	while p:
		val, node = heappop(p)
		cur.next = ListNode(val)
		if node.next:
			heappush(p,[node.next.val, node.next])
		cur = cur.next
	print visualization(dummy.next)
	return dummy.next




	


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1, l2, l3]
merge(lists)
		