from collections import deque
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = deque()
        for i in range(len(nums)):
            if (len(stack) + (len(nums) - i)) <= k:
                stack.appendleft(nums[i])
            while (stack[0] > nums[i]) and (len(stack) + (len(nums) - i)) > k:
                stack.popleft()
            stack.appendleft(nums[i])
        
        return stack
                

