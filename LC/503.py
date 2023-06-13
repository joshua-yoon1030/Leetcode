from collections import deque
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = deque()
        n = len(nums)
        double = nums + nums
        ans = [0] * n

        for i in range(len(double)):
            while len(stack) > 0 and double[i] > stack[0][0]:
                (num, index) = stack.popleft()
                if index < n:
                    ans[index] = double[i]
            stack.appendleft(double[i], i)
        return ans
                