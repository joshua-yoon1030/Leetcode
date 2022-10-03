class Solution(object):
    def permute_help(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            sum = []
            for i in range(len(nums)):
                sublists = self.permute_help(nums[:i] + nums[i+1:])
                #print(nums[:i] + nums[i+1:], sublists)
                for sublist in sublists:
                    sublist.append(nums[i])
                    sum.append(sublist)
                
                #print(nums[:i] + nums[i+1:], sublists)
            
            #print(nums, sum)
        return sum
                    

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute_help(nums)
mySol = Solution()
print(mySol.permute([0,1]))