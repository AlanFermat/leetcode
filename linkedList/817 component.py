from ListNode import *

def numComponents(head, G):
	"""
	:type head: ListNode
	:type G: List[int]
	:rtype: int
	"""
	G_set = set(G)
	component = len(G)
	while head:
		flag = 1
		while head and (head.val in G_set):
			flag = 0
			head = head.next
			component -= 1
		if flag:
			head = head.next
		if not flag:
			component += 1
	return component

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
G = [1,2,3]

print numComponents(head, G)
