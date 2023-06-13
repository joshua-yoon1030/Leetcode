# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traverse(node, depth):
            if not node:
                return (0, True)
            (depth1, val1) = traverse(node.left, depth + 1)
            (depth2, val2) = traverse(node.right, depth + 1)
            return (depth, abs(depth1 - depth2) < 2 and val1 and val2)

        a, b = traverse(root, 0)
        return b
