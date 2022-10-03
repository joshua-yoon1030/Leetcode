class Solution(object):

    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        arr = [0] * (n//2)
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] = min(nums[2*i], nums[2*i + 1])
            else:
                arr[i] = max(nums[2*i], nums[2*i + 1])
        return self.minMaxGame(arr)
        