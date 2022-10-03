import collections
class Solution(object):
    #bottom up dp method
    #Time: O(N^2) beacause you loop whole remaining array for every arr
    #Space: O(N) because one array
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        LIS = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)

mySol = Solution()
print(mySol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(mySol.lengthOfLIS([0,1,0,3,2,3]))
print(mySol.lengthOfLIS([7,7,7,7,7,7,7]))
print(mySol.lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))