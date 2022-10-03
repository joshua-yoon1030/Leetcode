class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ranges = set()
        for i in nums:
            ranges.add(i)
        for i in range(n+1):
            if i not in ranges:
                return i

        