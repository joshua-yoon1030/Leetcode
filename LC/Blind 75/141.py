# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        hare = head.next
        tortise = head

        while True:
            if hare:
                hare = hare.next
            else:
                return False
            if hare:
                hare = hare.next
            else:
                return False
            tortise = tortise.next
            if hare is tortise:
                return True
            
        