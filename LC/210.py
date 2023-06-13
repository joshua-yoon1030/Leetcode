from collections import defaultdict
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        incoming = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1
        topological = []

        while 0 in incoming:
            new = [i for i in range(numCourses) if incoming[i] == 0]
            for vertex in new:
                for out in graph[vertex]:
                    incoming[out] -= 1
                topological.append(vertex)
                incoming[vertex] -= 1
            
        if len(topological) == numCourses:
            return topological
        return []

            

