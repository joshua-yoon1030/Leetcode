# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.ans = 0
        def findsum(node, total):
            if not node:
                return
            
            total += node.val
            if total == targetSum:
                #print("here")
                self.ans += 1
            findsum(node.left, total)
            findsum(node.right, total)
        
        def traverse(node):
            if not node:
                return
            
            findsum(node, 0)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return self.ans
            