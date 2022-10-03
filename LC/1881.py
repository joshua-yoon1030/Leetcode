class Solution(object):
    def maxPos(self, n, x):
        for i in range(len(n)):
            if n[i] < x:
                return n[:i] + x + n[i:]
        return n + x

    def maxNeg(self, n, x):
        for i in range(len(n)):
            if n[i] > x:
                return n[:i] + x + n[i:]
        return n + x


    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        x = str(x)
        if n[0] == "-":
            return "-" + self.maxNeg(n[1:], x)
        else:
            return self.maxPos(n,x)

mySol = Solution()
print(mySol.maxValue("-132", 3))
print(mySol.maxValue("-648468153646", 5))
