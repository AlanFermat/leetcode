# Given two linked lists, the task is to check whether the first list is present in 2nd list or not.
#http://www.geeksforgeeks.org/sublist-search-search-a-linked-list-in-another-list/
from linkedList import Node, LinkedList

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

l2 = LinkedList()

l2.append(1)
l2.append(2)
l2.append(1)
l2.append(1)
l2.append(2)
l2.append(3)
l2.append(4)


# print l1.length()

# if l1.head:
# 	print 2


def subLinkedListSearch(l1, l2):
	# take the head nodes for both
	first = l1.head
	second = l2.head
	if l1.length() > l2.length():
		return False
	elif not l1.head and not l2.head:
		return True
	elif not l1.head:
		return False

	#when l2 is not null
	while l2.head:
		second = l2.head
		#iterate over l1 to see if the following linkedlist from this l2 can match l1
		while first:
			if not second:
				return False
			elif first.data == second.data:
				first = first.next
				second = second.next
			else:
				#if not match break
				break
		#if l1 is empty, every element is matched in the above process
		if not first:
			return True
		#otherwise, return to the first element of l1 and start over
		first = l1.head
		#refresh to the previous position of l2
		l2.head = l2.head.next
	return False

print subLinkedListSearch(l1, l2)




	
	




	