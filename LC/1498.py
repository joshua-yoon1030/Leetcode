class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        mod = 1000000007
        ans = 0

        def subseqs(i, j):
            #counts the number of subsequences where i and j must be included in it.
            return (1 << (j - i- 1)) % mod 
        
        while left < right:
            contender = nums[left] + nums[right]
            if contender <= target:
                ans += subseqs(left, right)
                left += 1
            else:
                right -= 1
        for i in range(len(nums)):
            if nums[i] * 2 <= target:
                ans += 1
        return ans % mod
