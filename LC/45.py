class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [99999] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(nums[i] + 1):
                dp[i+j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]

