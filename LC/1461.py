class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        hashmap = set()
        for i in range(n-k+1):
            entry = s[i:i+k]
            hashmap.add(entry)
        return len(hashmap) == pow(2, k)
            

mySol = Solution()
print(mySol.hasAllCodes("00110110", 2))
print(mySol.hasAllCodes("0110", 1))
print(mySol.hasAllCodes("0110", 2))
        