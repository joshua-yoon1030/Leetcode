import collections
class Solution(object):
    def soup(self, a, b, soupDict):
        if a == 0 and b == 0:
            return 0.5
        elif a == 0:
            return 1
        elif b == 0:
            return 0
        elif soupDict[(a,b)] != -999:
            return soupDict[(a,b)]
        else:
            f1 = self.soup(max(a-100, 0), b, soupDict)
            f2 = self.soup(max(a-75, 0), max(b-25, 0), soupDict)
            f3 = self.soup(max(a-50, 0), max(b-50, 0), soupDict)
            f4 = self.soup(max(a-25, 0), max(b-75, 0), soupDict)
            prob = 0.25 * (f1 + f2 + f3 + f4)
            soupDict[(a,b)] = prob
            return prob
            
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n >= 4800:
            return 1
        soupDict = collections.defaultdict(lambda: -999)
        prob = self.soup(float(n), float(n), soupDict)
        return prob
mySol = Solution()
print(mySol.soupServings(50))
print(mySol.soupServings(100))