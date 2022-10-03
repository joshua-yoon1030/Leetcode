#1155. Number of Dice Rolls with Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# My strategy: For each dice you can only roll from 1-k, so we can recurse
#the number of dice has to be 0 when you are at 0, or else we are stuck
#runtime: hopefully not too long, something like O(2^n) but n is 30
from collections import defaultdict
class Solution(object):
    def dp(self, n, k, target, rollDict):
        mod = 1000000007
        if n == 0:
            if target == 0:
                return 1
            else:
                return 0
        if (n,k) in rollDict:
            return rollDict[(n,k)]
        #rolling the nth (n = 0 -> n)dice
        sum = 0
        for i in range(1, k+1):
            sum += self.dp(n-1, k, target - i)
        rollDict[(n,k)] = sum % mod
        return sum % mod
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        rollDict = defaultdict(int)
        return self.dp(n, k, target, rollDict)
