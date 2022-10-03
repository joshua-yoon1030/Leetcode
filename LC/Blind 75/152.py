class Solution(object):
    def mcss(self, nums):
        #return type:
        #[maxleft, maxright, mcss, total]
        if len(nums) == 0:
            return [(0,0),(0,0),0,0]
        if len(nums) == 1:
            return [(nums[0], nums[0]), (nums[0], nums[0]), nums[0], nums[0]]
        
        #divide and conquer
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        #print("calling mcss on ", left, right)
        
        [(l1MA, l1MI), (r1MA, r1MI), m1, t1] = self.mcss(left)
        [(l2MA, l2MI), (r2MA, r2MI), m2, t2] = self.mcss(right)
        l3MA = max(l1MA, t1 * l2MA, t1 * l2MI, t1 * t2)
        l3MI = min(l1MI, t1 * l2MA, t1 * l2MI, t1 * t2)
        r3MA = max(r2MA, t2 * r1MA, t2 * r1MI, t1 * t2)
        r3MI = min(r2MI, t2 * r1MA, t2 * r1MI, t1 * t2)
        m3 = max(m1, m2, r1MA * l2MA, r1MI * l2MI, r1MA * l2MI, r1MI * l2MA, t1 * t2)
        t3 = t1 * t2

        #print("for mcss on ", nums, "result was", [(l3MA, l3MI),(r3MA, r3MI), m3, t3])
        return [(l3MA, l3MI),(r3MA, r3MI), m3, t3]

    def maxProduct(self, nums):
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
#print(mySol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
#print(mySol.maxSubArray([1]))
print(mySol.maxSubArray([-3,-1,-1]))