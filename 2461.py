#2461: Maximum Sum of Distinct Subarrays with length K
#https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
#my strat: You can check all the arrays, and keep track of the sum as a sliding window
#just keep a dictionary of everything you have so far
#One quick way to check if your thing is unique in O(1) time is to check the size == k
from collections import defaultdict
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #creation of window
        sum = 0
        numdict = defaultdict(int)
        for i in range(0, k):
            sum += nums[i]
            numdict[nums[i]] += 1
        def isValid(numdict, k):
            #print(numdict)
            return len(numdict) == k
        left = 0
        right = k
        maxSum = 0
        if isValid(numdict, k):
            maxSum = sum
        for i in range(k, len(nums)):
            sum += nums[right]
            sum -= nums[left]
            numdict[nums[right]] += 1
            numdict[nums[left]] -= 1
            if numdict[nums[left]] == 0:
                del numdict[nums[left]]
            if sum > maxSum and isValid(numdict, k):
                maxSum = sum
            right += 1
            left += 1
        return maxSum




        