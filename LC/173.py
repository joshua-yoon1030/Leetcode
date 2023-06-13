# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = deque()
        node = root
        self.root = root
        while node:
            self.stack.append(node)
            node = node.left
        self.pointer = None
        

    def next(self):
        """
        :rtype: int
        """
        if not self.pointer or not self.pointer.right:
            self.pointer = self.stack.pop()
            return self.pointer.val
        
        self.pointer = self.pointer.right
        node = self.pointer
        while node:
            self.stack.append(node)
            node = node.left
        self.pointer = self.stack.pop()
        return self.pointer.val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.pointer:
            return True
        
        return not (self.pointer.right == None and len(self.stack) == 0)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()