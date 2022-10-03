# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursion(self, root, depth):
        if(root.left == None and root.right == None):
            return (root.val, depth)
        elif(root.left == None):
            return self.recursion(root.right, depth + 1)
        elif(root.right == None):
            return self.recursion(root.left, depth + 1)
        else:
            (leftV, leftD) = self.recursion(root.left, depth + 1)
            (rightV, rightD) = self.recursion(root.right, depth + 1)
            if (leftD > rightD):
                return (leftV, leftD)
            elif(rightD > leftD):
                return (rightV, rightD)
            else:
                return (leftV + rightV, leftD)
        
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        (val, depth) =  self.recursion(root, 0)
        return val
        