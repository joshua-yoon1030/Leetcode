class Solution(object):
    #you can memoize this for a O(n) runtime
    def count(self, n, counter):
        if n == 0:
            return counter
        else:
            return self.count(n >> 1, counter + (n & 1))
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = [0] * (n + 1)
        for i in range(n+1):
            arr[i] = self.count(i, 0)
        return arr
mySol = Solution()
print(mySol.countBits(2))
print(mySol.countBits(5))
print(mySol.countBits(15))
        