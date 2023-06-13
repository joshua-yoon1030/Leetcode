from functools import cache
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        @cache
        def dp(total, i):
            #i is the index of the number we're looking at
            if total == 0:
                return True
            if i >= len(nums):
                return False
            return dp(total, i + 1) or dp(total - nums[i], i + 1)
        
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        return dp(total_sum// 2, 0)
