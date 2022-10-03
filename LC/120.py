class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        dp = []
        for i in triangle:
            dp.append([0] * len(i))
        dp[len(dp) - 1] = triangle[len(dp)-1]
        for i in range(len(dp)-2, -1, -1):
            for j in range(len(dp[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]



mySol = Solution()
print(mySol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
