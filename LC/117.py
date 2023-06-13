"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        nextptr = [None] * 6000
        def traverse(node, depth):
            if not node:
                return
            node.next = nextptr[depth]
            nextptr[depth] = node
            traverse(node.right, depth + 1)
            traverse(node.left, depth + 1)
        
        traverse(root, 0)
        return root
