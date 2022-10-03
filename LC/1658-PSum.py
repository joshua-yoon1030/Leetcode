class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        #instead of finding min operations, let's just find max subarray
        #create a prefixsum and apply a twopointer strategy
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        #indexes
        #start: start of prefix sum (right side)
        #end: end of prefix sum (left side)
        #invariant: start >= end
        start = 0
        end = 0
        target = prefix[-1] - x
        bestanswer = 99999999
        while(start >= end):
            if start >= len(prefix):
                break
            subarray = prefix[start] - prefix[end]
            if subarray == target:
                bestanswer = min((len(nums) - (start - end)), bestanswer)
                if start < len(prefix) - 1:
                    start += 1
                else:
                    end += 1
            elif subarray < target:
                start += 1
            else:
                end += 1
        if bestanswer > 9999999:
            return -1
        return bestanswer


mySol = Solution()
print(mySol.minOperations([1,1,4,2,3], 5) )  
print(mySol.minOperations([5,2,3,1,1], 5) ) 