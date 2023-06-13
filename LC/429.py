"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ans = []

        def traverse(node, depth):
            if not node:
                return
            
            for child in node.children:

                traverse(child, depth + 1)

            if depth >= len(ans):
                ans.append([])
            
            ans[depth].append(node.val)
        
        traverse(root, 0)
        return ans

