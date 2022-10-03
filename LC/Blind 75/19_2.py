# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def traverse(self, node, n):
        if not node:
            return (0,False)
        
        (count, finished) = self.traverse(node.next, n)

        if count == n:
            node.next = node.next.next
            return (count + 1, True)
        else:
            return (count + 1, finished)
        
        

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        (a, finished) = self.traverse(head, n)
        if finished:
            return head
        else:
            return head.next
        