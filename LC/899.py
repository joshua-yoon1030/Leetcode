#import string
from re import S


class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k > 1:
            return "".join(sorted(s))
        else:
            minS = s
            for i in range(len(s)):
                s = s[1:] + s[0]
                minS = min(minS, s[])

mySol = Solution()
print(mySol.orderlyQueue("asdfwef", 2))