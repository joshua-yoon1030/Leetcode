class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if you xor a number with itself, it will become 0
        #eg. 3 ^ 3 == 0
        #also if you have 0 xor something, it will stay
        #eg. 0 ^ 3 == 3
        #so what we can do is have all the 0 -> n xored
        #and then xor all the numbers in the array
        #and the only thing left would be the missing number
        xor = 0
        for i in range(len(nums)):
            xor ^= i
            xor ^= nums[i]
        xor ^= len(nums)
        return xor
mySol = Solution()
print(mySol.missingNumber([3,0,1]))
print(mySol.missingNumber([9,6,4,2,3,5,7,0,1]))
        