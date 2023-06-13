class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 999999999
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                contender = nums[i] + nums[left] + nums[right]
                ans = min(ans, abs(contender - target))
                if ans == 0:
                    return 0
                if contender < target:
                    left += 1
                elif contender > target:
                    right -= 1
        return ans