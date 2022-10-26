# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#112 Path Sum
#https://leetcode.com/problems/path-sum/
#My Strategy: Traverse the tree and keep track of all sum paths
#at the end, check if the sum is in the path
class Solution(object):
    def traverse(self, node, total, sum):
        if not node:
            return 
        
        total = []
        if node.left:
            leftside = self.traverse(node.left)
            total += leftside
        if node.right:
            rightside = self.traverse(node.right)
            total += rightside
        for i in range(len(total)):
            total[i] += node.val
        return total

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        possible = self.traverse(root)
        return targetSum in possible
        