# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#237: Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/
#My strategy:
#We can only look at the nodes after the node we have to delete
#So we "rebuild" the linked list but we just don't put in the first node
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        while cur:
            after = cur.next
            cur.val = after.val
            if not after.next:
                cur.next = None
            cur = cur.next
            
        cur = None