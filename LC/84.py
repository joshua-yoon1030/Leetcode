from collections import deque
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        right = [len(heights)] * len(heights)
        left = [0] * len(heights)
        stack = deque()

        for i in range(len(heights)):
            while len(stack) > 0 and stack[0][0] > heights[i]:
                height, index = stack.popleft()
                right[index] = i
            stack.appendleft([heights[i], i])
        stack = deque()
        for i in range(len(heights)-1, -1, -1):
            while len(stack) > 0 and stack[0][0] > heights[i]:
                height, index = stack.popleft()
                left[index] = i
            stack.appednleft([heights[i], i]) 
        
        area = 0
        for i in range(len(heights)):
            area = max(area, (right[i] - left[i] - 1) * heights[i])
        return area