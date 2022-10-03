"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    #def cloneNeighbor(self, node):
     
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return
        d = {node: Node(node.val)}
        q = collections.deque([node])
        
        while q:
            cur_node = q.popleft()
            for nei in cur_node.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val)
                    q.append(nei)
                d[cur_node].neighbors.append(d[nei])
        return d[node]



        

