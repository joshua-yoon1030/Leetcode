# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    maxDepth = 0
    def traverse(self, root, depth, vision):
        
        if not root:
            return
        #print("traversing", root.val, "depth", depth, "maxdepth", self.maxDepth)
        if depth > self.maxDepth:
            vision.append(root.val)
            self.maxDepth = depth
        self.traverse(root.right, depth + 1,  vision)
        self.traverse(root.left, depth + 1, vision)
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        vision = [root.val]
        self.traverse(root, 0, vision)
        return vision