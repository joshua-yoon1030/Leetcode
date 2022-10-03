import collections
class Solution(object):
    def dp(self, nums, x, numDict):
        if x == 0:
            return 0
        elif x < 0 or len(nums) == 0:
            return 99999999
        elif numDict[(tuple(nums), x)] != 0:
            return numDict[(tuple(nums), x)]
        else:
            left = nums[0]
            right = nums[-1]
            ans = min(self.dp(nums[1:], x - left, numDict), self.dp(nums[:-1], x - right, numDict))
            numDict[tuple((nums), x)] = ans + 1
            return ans + 1
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        numDict = collections.defaultdict(int)
        ans = self.dp(nums, x, numDict)
        if ans >= 99999999: return -1
        else: return ans

        