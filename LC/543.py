# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(node, depth):
            if not node:
                #diameter, depth, 
                return (0, depth)
            
            (dia1, depth1) = traverse(node.left, depth + 1)
            (dia2, depth2) = traverse(node.right, depth + 1)

            return (max(dia1, dia2, depth1 + depth2), depth)

        (a, d) = traverse(root, 0)
        return a