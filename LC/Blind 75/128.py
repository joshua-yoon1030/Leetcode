class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = set(nums)

        longest = 1
        while nums:
            num = nums.pop()
            counter = 1
            up = num + 1
            while up in nums:
                nums.remove(up)
                counter += 1
                up += 1
            down = num - 1
            while down in nums:
                nums.remove(down)
                counter += 1
                down -= 1

            longest = max(longest, counter)
            counter = 1
        return longest

mySol = Solution()
print(mySol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
            
