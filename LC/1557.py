from collections import defaultdict
class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #edges are directed
        graph = defaultdict(list)
        for x, y in edges:
            graph[y].append(x)

        
        return [i for i in range(n) if len(graph[i]) == 0]