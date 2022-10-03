import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m -= 1
        n -= 1
        sum = m + n

        a = math.factorial(sum)
        b = math.factorial(m)
        c = math.factorial(n)
        #print(a, b, c)
        return a// (b * c)
        
