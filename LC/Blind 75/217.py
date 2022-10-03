class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print(set(nums))
        return not len(set(nums)) == len(nums)
mySol = Solution()
print(mySol.containsDuplicate([1,2,3,1]))