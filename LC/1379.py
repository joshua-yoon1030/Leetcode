# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recurse(self, original, clone, target):
        if (original == None):
            return None
        if original is target:
            return clone
        else:
            return self.recurse(original.left, clone.left, target) or self.recurse(original.right, clone.right, target)

    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        return self.recurse(original, cloned, target)
        