class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        numdict = dict()
        for i in range(len(nums)):
            numdict[nums[i]] = i
        for op in operations:
            numdict[op[1]] = numdict.pop(op[0])
        for (key,val) in numdict.items():
            nums[val] = key
        return nums
        