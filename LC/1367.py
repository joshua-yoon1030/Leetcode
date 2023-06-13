# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        def check(node, llnode):
            #tree node, linked list node, linked list head
            if not llnode:
                return True
            if not node:
                #llnode must be true here (there is still more path to check)
                return False
            if llnode.val != node.val:
                return False
            a = check(node.left, llnode.next)
            b = check(node.right, llnode.next)
            
            return a or b

        def traverse(node):
            if check(node, head):
                return True
            if not node:
                return False
            return traverse(node.left) or traverse(node.right)

        return traverse(root)
                    
            