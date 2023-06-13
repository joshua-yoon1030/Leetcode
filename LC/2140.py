from collections import defaultdict
class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """

        def dp(i, memo, questions):
            #dp[i] is the best solution you can get by starting on the ith problem
            if i >= len(questions):
                return 0
            
            if memo[i] > 0:
                return memo[i]
            
            ans = max(dp(i+1, memo, questions), questions[i][0] + dp(i + questions[i][1] + 1, memo, questions))
            memo[i] = ans
            return ans

        memo = defaultdict(lambda: 0)

        ans = dp(0,memo, questions)
        #print(memo)
        return ans

