"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
"""
from ListNode import *

class MyLinkedList(object):
	"""docstring for myLinkedList"""
	def __init__(self):
		self.size = 0
		self.head = None

	def get(self, index):
		if index >= self.size:
			return -1
		temp = self.head
		while index:
			temp = temp.next
			index -= 1
		return temp.val

	def addAtHead(self, val):
		new = ListNode(val)
		new.next = self.head
		self.head = new
		self.size += 1

	def addAtTail(self, val):
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = ListNode(val)
		self.size += 1

	def addAtIndex(self, index, val):
		count = 0
		temp = self.head
		if self.size >= index:
			if index == 0:
				self.addAtHead(val)
			elif index == self.size:
				self.addAtTail(val)
			# locate that position
			else:
				while count < index-1:
					temp = temp.next
					count += 1
				# swap the value
				new = ListNode(val)
				new.next = temp.next
				temp.next = new
				self.size += 1

	def deleteAtIndex(self, index):
		temp = self.head
		if index == 0:
			self.head = self.head.next
			self.size -= 1
		else:
			if self.size > index:
				while index-1:
					temp = temp.next
					index -= 1
				if temp.next:
					temp.next = temp.next.next
				self.size -= 1

g = MyLinkedList()
g.addAtHead(0)
g.addAtIndex(1,9)
g.addAtIndex(1,5)

g.addAtTail(7)
g.addAtHead(1)
g.addAtIndex(5,8)
show(g.head)
g.addAtIndex(5,2)

g.addAtIndex(3,0)
g.addAtTail(1)
g.addAtTail(0)
show(g.head)
g.deleteAtIndex(6)
show(g.head)
			









		

