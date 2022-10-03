class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(text2))] for i in range(len(text1))]

        #setup sides
        if text1[0] == text2[0]:
            dp[0][0] = 1
        for i in range(1 , len(text2)):
            if text1[0] == text2[i]:
                dp[0][i] = max(1,dp[0][i-1])
            else:
                dp[0][i] =  dp[0][i-1]
        for i in range(1,len(text1)):
            if text2[0] == text1[i]:
                dp[i][0] = max(1, dp[i-1][0])
            else:
                dp[i][0] = dp[i-1][0]
        
        #setup middle block
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], )
        print(dp)
        return dp[-1][-1]

mySol = Solution()
print(mySol.longestCommonSubsequence("abcde", "ace"))
print(mySol.longestCommonSubsequence("abc", "abc"))

    