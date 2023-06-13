# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return ans[k-1]