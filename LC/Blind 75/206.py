# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        linklist = []
        cur = head
        while cur != None:
            linklist.append(cur.val)
            cur = cur.next
        linklist.reverse()
        head = ListNode(val = linklist[0])
        cur = head
        for i in range(1, len(linklist)):
            cur.next = ListNode(val = linklist[i])
            cur = cur.next
        return head
        
        