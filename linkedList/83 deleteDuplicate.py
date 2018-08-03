from ListNode import *

def show(node):
	temp = []
	while node:
		temp.append(str(node.val))
		node = node.next
	print ("->".join(temp))

l1 = ListNode(1)
l1.next= ListNode(8)
l1.next.next = ListNode(9)

def deleteDuplicates(head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	dummy = ListNode(-1)
	dummy.next = head
	prev, curr = dummy, dummy.next
	while curr:
		if curr.next and curr.next.val == curr.val:
			value = curr.val
			while curr.val == value:
				curr = curr.next
			prev.next = curr # skip the repeated items
		else:
			prev = curr
			curr = curr.next 
	return dummy.next

show(deleteDuplicates(l1))