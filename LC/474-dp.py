class Solution(object):
    def stringRead(self, text):        
        x, y = 0,0       
        for t in text:
            if t == '0':
                x += 1
            else:
                y += 1
        return (x,y)
        
    def dp(self, strs, index, m, n, matrix):
        if index == len(strs):
            return 0
        elif(m == 0 and n == 0):
            return 0
        #check dictionary
        if (matrix[index][m][n] != -1):
            return matrix[index][m][n]
        
        #not in dictionary -> proceed as normal
        (numZ, numO) = strs[index]
        if (m - numZ < 0 or n - numO < 0):
            return self.dp(strs, index + 1, m, n, matrix)
       
        used = 1 + self.dp(strs, index + 1, m - numZ, n - numO, matrix)
        unused = 0 + self.dp(strs, index + 1, m, n, matrix)

        ans = max(used, unused)
        #make sure to put in dictionary
        matrix[index][m][n] = ans
        return ans

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        l = len(strs)
        matrix=[[[-1 for col in range(n+1)] for col in range(m+1)] for row in range(l)]
        #matrix[i][m][n] is the dictionary entry for (index, m, n)
        mapped = map((self.stringRead), strs)
        strs = list(mapped)
        res = self.dp(strs,0, m, n, matrix)
        return res
#mySol = Solution()
#print(mySol.findMaxForm(["10","0","1"], 1, 1))
#print(mySol.findMaxForm(["10","0001","111001","1","0"], 5, 3))
#print(mySol.findMaxForm(["10","0001","111001","1","0"],4,3))
#print(mySol.findMaxForm(["011111","001","001"], 4, 5))