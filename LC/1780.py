class Solution(object):

    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if (n%3 == 2):
            return False
        else:
            return self.checkPowersOfThree(n//3)

#mySol = Solution()
#print(mySol.checkPowersOfThree(12))
#print(mySol.checkPowersOfThree(91))
#print(mySol.checkPowersOfThree(21))