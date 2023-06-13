class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = []

        while len(nums) > 0:
            temp = ans[::]
            next = nums.pop()
            for i in temp:
                i.append(next)
            ans += temp
        return ans