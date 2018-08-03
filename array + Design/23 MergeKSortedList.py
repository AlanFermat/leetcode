from Queue import PriorityQueue as pq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        p = pq()
        for root in lists:
            if root:
                p.put((root.val,root))
        dummy = ListNode(0)
        iterate = dummy
        
        while not p.empty():
            last_val = p.get()
            iterate.next = ListNode(last_val[0])
            change = last_val[1]
            if change.next:
                p.put((change.next.val,change.next))
            iterate = iterate.next
        return dummy.next
        