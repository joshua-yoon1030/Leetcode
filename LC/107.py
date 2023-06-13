# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def traverse(node, depth, nodeDict):
            if not node:
                return

            if node.left:
                traverse(node.left, depth + 1, nodeDict)
            
            nodeDict[depth].append(node.val)

            if node.right:
                traverse(node.right, depth + 1, nodeDict)
        
        nodeDict = defaultdict(lambda: [])

        traverse(root, 0, nodeDict)

        ans = []
        for (depth, nodes) in nodeDict.items():
            print(depth)
            ans.append(nodes)
        list.reverse(ans)
        return ans