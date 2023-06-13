# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def traverse(node1, node2):
            if not (node1 and node2):
                return False
            if node1.val != node2.val:
                return False
            else:
                return traverse(node1.left, node2.left) and traverse(node1.right, node2.right)
        
        if not root:
            return False
        if traverse(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)