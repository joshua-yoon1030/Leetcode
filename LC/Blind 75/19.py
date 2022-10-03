# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def traverse(self, node, n):
        i = 1
        ans = False
        if node.next:
            (i, ans) = self.traverse(node.next, n)
        if i == n:
            return (i+1, True)
        elif ans:
            node.next = node.next.next
            return (i+1, False)
        else:
            return (i+1, ans)
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        (i, ans) = self.traverse(head, n)
        if ans:
            return head.next
        return head