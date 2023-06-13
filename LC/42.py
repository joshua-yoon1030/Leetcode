class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        fromLeft = [0] * len(height)
        fromRight = [0] * len(height)

        for i in range(1, len(height)):
            fromLeft[i] = max(fromLeft[i-1], height[i])
        for i in range(len(height)-2 , -1, -1):
            fromRight[i] = max(fromRight[i+1], height[i])
        
        rain = 0
        for i in range(1, len(height) - 1):
            rain += min(fromLeft[i], fromRight[i]) - height[i]
        return rain
