class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #generate prefix sum matrix
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        ans = [0] * len(nums)
        ans[0] = prefix[len(nums) - 1] - len(nums) * nums[0]
        ans[len(nums) -1] = abs(prefix[len(nums) - 1] - len(nums) * nums[len(nums) - 1])
        for split in range(1,len(nums)-1):
            sum1 = abs((prefix[len(nums) - 1] - prefix[split]) - (len(nums) - 1 - split) * nums[split])
            sum2 = abs(prefix[split] - (split + 1) * nums[split])
            ans[split] = sum1 + sum2
        return ans

