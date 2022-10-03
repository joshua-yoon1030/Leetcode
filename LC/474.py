import collections

class Solution(object):
    def stringRead(self, text):        
        x, y = 0,0       
        for t in text:
            if t == '0':
                x += 1
            else:
                y += 1
        return (x,y)
        
    def dp(self, tups, m, n, ddict):
        if m == 0 and n == 0:
            return 0
        if len(tups) <= 0:
            return 0
        if m < 0 or n < 0:
            return -99999999
        if (str(tups), m, n) in ddict:
            return ddict[(str(tups), m, n)]
        
        maxRes = -1
        for i in range(len(tups)):
            removed = tups[:i] + tups[i+1:]
            (a,b) = tups[i]
            possible = self.dp(removed, m-a, n-b, ddict)
            if possible > maxRes:
                maxRes = possible
        ddict[(str(tups), m, n)] = maxRes + 1
        return maxRes + 1
    def keyfn(self, a):
        x,y = a
        a = str(x) + str(y)
        return int(a)

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ddict = collections.defaultdict(list)
        mapped = map((self.stringRead), strs)
        strs = list(mapped)
        strs = sorted(strs, key = self.keyfn)

        res = self.dp(strs, m, n, ddict)
        #print(ddict)
        return res
mySol = Solution()
#print(mySol.findMaxForm(["10","0","1"], 1, 1))
#print(mySol.findMaxForm(["10","0001","111001","1","0"], 5, 3))
#print(mySol.findMaxForm(["10","0001","111001","1","0"],4,3))