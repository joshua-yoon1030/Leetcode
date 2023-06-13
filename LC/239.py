from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def push(window, num):
            while len(window) > 0 and num[0] > window[-1][0]:
                window.pop()

            window.append(num)

        def findMax(window, i):
            while window[0][1] <= i:
                #can't ever pop till empty
                window.popleft()
            return window[0][0]
        
        window = deque()

        for i in range(k):
            push(window, (nums[i], i + k))
        
        ans = [findMax(window, 0)] * (len(nums) - k + 1)

        for i in range(k, len(nums)):
            push(window, (nums[i], i + k))
            ans[i - k + 1] = findMax(window, i)
        return ans
