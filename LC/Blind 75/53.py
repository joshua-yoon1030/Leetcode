class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #the biggest factor we know is that our very minimum sum should always be 0
        #we go along and keep adding to our sum,
        #but if our sum is ever less than 0 we know we can just simply not include
        #that portion and just continue on

        sum = 0
        max = nums[0]
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            if sum > max:
                max = sum
        return max


mySol = Solution()
print(mySol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(mySol.maxSubArray([1]))
print(mySol.maxSubArray([-3,-2,-1]))