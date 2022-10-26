#523: Continuous Subarray Sum
#https://leetcode.com/problems/continuous-subarray-sum/
#Strategy: I first compute the prefix sum of all the elements
#I then store a hashmap of what the mod value is
#Note the numbers need to be two apart, so as long as the prefix entries are 2 apart
#I just need to match something that has the same mod:
#eg. a + b + c == 6 mod 7, a == 6 mod 7, so b + c is a multiple of 7
#Time O(n) for the prefix/hashmap/iteration

from collections import defaultdict
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        moddict = defaultdict(lambda:-1)
        prefix = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            if prefix[i] % k == 0:
                return True
        
        for i in range(len(prefix)-1, -1, -1):
            moddict[prefix[i]%k] = i
        for i in range(2, len(prefix)):
            modnum = prefix[i]%k
            if moddict[modnum] <= i-2:
                return True
        return False

        