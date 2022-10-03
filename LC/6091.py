class Solution(object):
    def helper(self, nums, k):
        if len(nums) == 1:
            return 1
        start = 0
        count = 1
        for i in range(len(nums)):
            if nums[i] - nums[start] > k:
                count += 1
                start = i
        return count
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return self.helper(nums, k)

        