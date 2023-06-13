class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        tally = 0
        left = 0
        right = 1
        product = nums[left]

        while left < len(nums):
            while right < len(nums) and product < k:
                product = product * nums[right]
                right += 1
            tally += right - left - 1
            product = product // nums[left]
            left += 1

                
        return tally