
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #start pos: (n - k) % k
        #end pos: 2n - k - 1
        n = len(nums)
        temp = nums[0]
        
        i = 0
        for j in range(n-1):
            newInd = (i + k) % n
            nums[i%n] = nums[newInd]
            i = i + k
        nums[-k] = temp

