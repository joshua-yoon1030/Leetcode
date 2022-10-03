import numpy as np
class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = np.array(nums)       
        forward = np.copy(nums)
        backward = np.copy(nums)
        for i in range(1, n):
            forward[i] = forward[i-1] + nums[i]
        for i in range(n-2, -1, -1):
            backward[i] = backward[i+1] + nums[i]
        for i in range(n):
            forward[i] = forward[i] //(i+1)
        for i in range(n):
            backward[i] = backward[i] // (n-i-1)
        sums = abs(forward-backward)
        return min(sums)

        
        


