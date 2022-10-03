class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg = 0
        end = 0
        #the sum you get by adding all the numbers in your sliding window
        sum = 0
        #the set for checking uniqueness
        S = set()
        ans = 0

        while end < len(nums):
            #if we have a unique element, we should add it to the set
            if nums[end] not in S:
                S.add(nums[end])
                sum += nums[end]
                ans = max(ans, sum)
                end += 1
            #if we have a repeat, we should keep removing until we don't
            else:
                S.remove(nums[beg])
                sum -= nums[beg]
                beg += 1
        return ans