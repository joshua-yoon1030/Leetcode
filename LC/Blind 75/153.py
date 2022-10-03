class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Binary search with indicies of 2
        nums = nums + [nums[0]]

        bot = 0
        max = len(nums) - 2

        boundary = nums[0]

        while(bot <= max):
            mid = bot + (max - bot)//2
            before = nums[mid]
            after = nums[mid + 1]
            #print("checking", nums[bot], nums[max])

            if(after < before):
                return after
            elif(before < boundary):
                max = mid - 1
            else:
                bot = mid + 1
            
        return min(nums[0], nums[-2])
mySol = Solution()
print(mySol.findMin([3,4,5,1,2]))
print(mySol.findMin([4,5,6,7,0,1,2]))
print(mySol.findMin([11,13,15,17]))
print(mySol.findMin([3,2,1]))
print(mySol.findMin([1]))
print(mySol.findMin([3,1,2]))

