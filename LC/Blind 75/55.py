class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxJump = 0
        for i in range(len(nums)):
            if maxJump >= i:
                maxJump = max(maxJump, i + nums[i])
            #print("read", i, "maxJump: ", maxJump)

        return maxJump >= len(nums) -1 
mySol = Solution()
print(mySol.canJump([2,3,1,1,4]))
print(mySol.canJump([3,2,1,0,4]))