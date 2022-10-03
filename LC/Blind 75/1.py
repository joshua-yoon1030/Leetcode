class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        subtract = dict()
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in subtract:
                return [subtract[ans], i]
            else:
                subtract[nums[i]] = i
        return -1

        