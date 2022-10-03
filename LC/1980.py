class Solution(object):
    def help(self, char):
        if char == "1":
            return "0"
        else:
            return "1"
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        #reconstruct a binary string using a diagonalization argument
        unique = ""
        for i in range(len(nums)):
            num = nums[i]
            unique += (self.help(num[i]))
        return unique
    