class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        dp = [0] * (high + 1)

        dp[0] = 1
        ans = 0
        for i in range(high + 1):
            if (i - zero) >= 0:
                dp[i] += dp[i-zero]
            if (i - one) >= 0:
                dp[i] += dp[i-one]
                dp[i] %= 1000000007
            if i >= low:
                ans += dp[i]
                ans %= 1000000007
        #print(dp)
        return ans
            
        