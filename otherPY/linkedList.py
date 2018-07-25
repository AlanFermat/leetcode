# Node class
class Node:
  
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize 
                          # next as null
  
# Linked List class
class LinkedList:
    
    # Function to initialize the Linked 
    # List object
    def __init__(self): 
        self.head = None 

    def printList(self):
    	temp = self.head
    	while temp:
    		print temp.data
    		temp = temp.next

    def push(self, new_data):
    	new = Node(new_data)
    	new.next = self.head
    	self.head = new


    def insertAfter(self, prev_node, new_data):
    	if not prev_node:
    		print "Not feasible"
    		return 
    	new = Node(new_data)
    	new.next = prev_node.next
    	prev_node.next = new

    def append(self, new_data):
     	new = Node(new_data)
     	if self.head is None:
     		self.head = new
     		return
     	curr = self.head
     	while curr.next:
     		curr = curr.next
     	curr.next = new

    def getCount(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length


# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
 
    # Insert 6.  So linked list becomes 6->None
    llist.append(6)
 
    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);
 
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);
 
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)
 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)
 
    print 'Created linked list is:',
    llist.printList()
    print "Count of nodes is :",llist.getCount()
 
# This code is contributed by Manikantan Narasimhan


