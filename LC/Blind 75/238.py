class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rightSide = [1] * len(nums)
        leftSide = [1] * len(nums)

        #doing left side prefix product first
        product = nums[0]
        for i in range(1, len(nums)):
            leftSide[i] = product
            product = product * nums[i]
        product = nums[len(nums)-1]

        for i in range(len(nums)-2, -1, -1):
            rightSide[i] = product
            product = product * nums[i]
        
        ans = [leftSide[i] * rightSide[i] for i in range(len(nums))]
        return ans 
