from collections import defaultdict
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        #graph construction
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        stops = defaultdict(lambda: (-1, k))
        
        pqueue = []
        #heapq elements are: (dist, vertex, hops)
        heapq.heappush(pqueue, (0, src, 0))
        visited = set()
        while pqueue:
            (dist, node, hop) = heapq.heappop(pqueue)
            if stops[node] != -1 or hop > stops[node]:
                continue

            stops[node] = hop

            if node == dst:
                return dist

            for (neighbor, weight) in graph[node]:
                heapq.heappush(pqueue, (weight + dist, neighbor, hop + 1))
            
        return -1


