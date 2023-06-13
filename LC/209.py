class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxl = -1
        running = nums[left]

        while right <= len(nums):
            if sum < target:
                if right == len(nums):
                    return max(maxl, 0)
                running += nums[right]
                right += 1
            else:
                #sum >= target, condition satisfied
                if right - left < maxl or maxl == -1:
                    maxl = right - left
                running -= nums[left]
                left += 1
