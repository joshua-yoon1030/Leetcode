# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def remove(prev2, prev, cur):
            #Only enter this case in the event that prev == cur
            while cur and prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            
            #At the end, we also need to remove the first duplicate node
            prev2.next = cur
            prev = prev.next
            if cur:
                cur = cur.next
        
        #preprocessing
        prev2 = head
        if not prev2:
            return head
        prev = prev2.next
        if not prev:
            return head
        cur = prev.next
        if not cur:
            if prev2.val == prev.val:
                return None
            return head
        
        while cur:
            if cur.val == prev.val:
                remove(prev2, prev, cur)
            else:
                prev2 = prev
                prev = cur
                cur = cur.next

        return head