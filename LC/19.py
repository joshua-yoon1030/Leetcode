# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        hare = head
        tortise = None
        while hare != None:
            if count < n + 1:
                count += 1
            elif count == n + 1:
                tortise = head
            else:
                tortise = tortise.next
            hare = hare.next

        if tortise:
            tortise.next = tortise.next.next
        else:
            head = head.next
        return head
        