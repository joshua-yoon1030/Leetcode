# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A_dict = set()
        cur = headA
        while(cur != None):
            A_dict.add(cur)
            cur = cur.next
        cur = headB
        while(cur != None):
            if cur in A_dict:
                return cur
            else:
                cur = cur.next
        return None

        