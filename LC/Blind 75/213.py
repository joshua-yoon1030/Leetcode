class Solution(object):
    def rob1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxRob = [0] * len(nums)
        if len(nums) < 3:
            return max(nums)
        maxRob[0] = nums[0]
        maxRob[1] = nums[1]
    
        for i in range(2, len(nums)):
            #best: best rob assuming we rob the current house
            best = max(maxRob[:i-1])
            #get the best rob so far or just don't rob either
            maxRob[i] = max(best + nums[i], maxRob[i-1])
        #print (maxRob)
        return maxRob[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        first = nums[:len(nums)-1]
        sec = nums[1:]
        #print(first)
        #print(sec)
        ans1 = self.rob1(first)
        ans2 = self.rob1(sec)
        return max(ans1, ans2)

mySol = Solution()
print(mySol.rob([2,3,2]))