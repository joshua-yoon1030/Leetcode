# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        left = deque()
        right = deque()

        def traverse(tort, hare):
            if not hare:
                return tort
            hare = hare.next
            if hare:
                hare = hare.next
            tort = tort.next
            return traverse(tort, hare)
        
        def assign(node, mid, truemid):
            if node == truemid:
                return
            left.appendleft(node)
            node = node.next
            if mid:
                right.appendright(mid)
                mid = mid.next
            assign(node, mid, truemid)
            
        mid = traverse(head, head)
        assign(head, mid, mid)

        head = left.pop()
        cur = head
        while len(left) > 0 or len(right) > 0:
            if len(left) > len(right):
                cur.next = left.pop()
            else:
                cur.next = right.pop()
            cur = cur.next
        return head