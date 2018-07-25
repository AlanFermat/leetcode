from ListNode import *

def show(node):
	temp = []
	while node:
		temp.append(str(node.val))
		node = node.next
	print ("->".join(temp))

l1 = ListNode(1)
l1.next = ListNode(9)
l1.next.next = ListNode(8)

def reverseIte(l):
	if not l:
		return 
	prev, curr = None, l
	while curr:
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp
	return prev

def reverseRec(l, prev = None):
	if not l:
		return prev
	curr = l.next
	l.next = prev
	return reverseRec(curr, l)


show(reverseIte(l1))



