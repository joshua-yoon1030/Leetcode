class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or maxPts + k - 1 <= n:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1.0

        window = 1.0
        for i in range(1, n + 1):

            dp[i] = window / maxPts

            if i < k:
                window += dp[i]
            if i - maxPts >= 0:
                window -= dp[i - maxPts]
        return sum(dp[k:])