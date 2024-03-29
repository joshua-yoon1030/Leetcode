# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def traverse(node, depth):
            if not node:
                return
            if depth > len(ans)-1:
                ans.append(node.val)
            
            traverse(node.right, depth + 1)
            traverse(node.left, depth + 1)
        
        traverse(root, 0)
        return ans