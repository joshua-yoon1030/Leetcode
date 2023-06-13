import heapq
import math
class Solution(object):
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def getDist(x, y):
            return math.sqrt(x ** 2 + y ** 2)

        distanceQ = []
        i = 0
        for point in points:
            heapq.heappush(distanceQ, (getDist(point[0], point[1]), i))
            i += 1
        
        ans = []
        for j in range(k):
            (a, b) = heapq.heappop(distanceQ)
            ans.append(points[b])
        return ans
        



