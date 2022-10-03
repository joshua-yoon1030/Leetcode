class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1

        maxWater = (right - left) * min(height[left], height[right])

        while left < right:
            if height[left] < height[right]:
                heightNow = height[left]
                while (height[left] <= heightNow) and (left < right):
                    left += 1
            else:
                heightNow = height[right]
                while (height[right] <= heightNow) and (left < right):
                    right -= 1
            maxWater = max(maxWater, (right - left) * min(height[left], height[right]))
        return maxWater
            
            
mySol = Solution()
print(mySol.maxArea([1,8,6,2,5,4,8,3,7]))
print(mySol.maxArea([1,2,3,4,3,2,1]))