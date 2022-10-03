# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def traverse (self, node, traversal, depth):
        if not node:
            return
        
        traversal.append((node.val, depth))
        self.traverse(node.left, traversal, depth + 1)
        self.traverse(node.right, traversal, depth + 1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        traversal = []
        self.traverse(root, traversal, 0)
        tree_dict = collections.defaultdict(list)
        for (node, depth) in traversal:
            tree_dict[depth].append(node)
        
        ans = []
        for val in tree_dict.values():
            ans += [val]
        return ans