class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num == 1:
            return 1
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num//2)
        else:
            return 2 + self.numberOfSteps(num//2)
#mySol = Solution()
#print(mySol.numberOfSteps(123))