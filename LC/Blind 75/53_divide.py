class Solution(object):
    def mcss(self, nums):
        #return type:
        #[maxleft, maxright, mcss, total]
        if len(nums) == 0:
            return [0,0,0,0]
        if len(nums) == 1:
            return [nums[0], nums[0], nums[0], nums[0]]
        
        #divide and conquer
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        
        [l1, r1, m1, t1] = self.mcss(left)
        [l2, r2, m2, t2] = self.mcss(right)
        l3 = max(l1, t1 + l2, t1 + t2)
        r3 = max(r2, t2 + r1, t1 + t2)
        m3 = max(m1, m2, r1 + l2, t1 + t2)
        t3 = t1 + t2

        return [l3, r3, m3, t3]

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #divide and conquer method:
        #
        #The maximum subarray can either be in 
        #the first half of the array
        #the second half of the array 
        #some middle half (part of left, part of right) of the array


        [a,b,c,d] = self.mcss(nums)
        return c

mySol = Solution()
print(mySol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(mySol.maxSubArray([1]))
print(mySol.maxSubArray([-3,-2,-1]))