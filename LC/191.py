class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif(n == 1):
            return 1
        if (n %2 == 1):
            return 1 + self.hammingWeight(n//2)
        return self.hammingWeight(n//2)