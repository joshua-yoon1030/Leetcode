# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pqueue = []
        for list1 in lists:
            cur = list1
            while cur:
                heapq.heappush(pqueue,(cur.val))
                cur = cur.next
        if len(pqueue) < 1:
            return None

        head = ListNode(heapq.heappop(pqueue))
        cur = head

        while len(pqueue) > 0:
            next = ListNode(heapq.heappop(pqueue))
            cur.next = next
            cur = next
        

