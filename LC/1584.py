class Solution(object):
    

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum = 0 
        for point in points:
            mindist = self.greedy(point, points)
            sum += mindist
        
        return sum

    def greedy(self, target, points):
        dist = 99999999999
        for point in points:
            x = abs(point[0] - target[0])
            y = abs(point[1] - target[1])
            if((x + y ) < dist and ((x + y) != 0)):
                dist = x + y
        return dist

        