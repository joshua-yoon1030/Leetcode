# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(node):
            if not node:
                return
            
            temp = node.left
            node.left = node.right
            node.right = temp
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return root