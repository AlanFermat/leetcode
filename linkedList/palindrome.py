from ListNode import *

def show(node):
	temp = []
	while node:
		temp.append(str(node.val))
		node = node.next
	print ("->".join(temp))

l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next= ListNode(1)


def isPalindrome(head):
	"""
	:type head: ListNode
	:rtype: bool
	"""
	curr = head
	res = reverseList(curr)
	show(res)
	show(head)
	while head:
		if head.val != res.val:
			return False
		head = head.next
		res = res.next
	return True
	
def reverseList(head):
	prev, curr = None, head
	while curr:
		temp = curr.next
		curr.next = prev
		prev = curr
		curr = temp 
	return prev

print (isPalindrome(l1))