class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 1000000007
        

        #example of digit dp
        def dp(memo, digits, pos, sum, flag):
            if pos >= len(digits):
                return 1 if (sum >= min_sum and sum <= max_sum) else 0
            
            if memo[pos][sum][flag] != -1:
                return memo[pos][sum][flag]

            limit = 9
            if flag:
                limit = digits[pos]
            
            ans = 0
            for i in range(limit + 1):
                new_flag = flag
                if flag == 1 and i == digits[pos]:
                    new_flag = 1
                else:
                    new_flag = 0
                
                ans += dp(digits, pos + 1, sum + i, new_flag)
                ans %= mod

            memo[pos][sum][flag] = ans
            return ans

        a = str(int(num1) - 1)
        a_digits = list(map(int, list(num1)))  
        b_digits = list(map(int, list(num2)))

        a_memo = [[[-1 for i in range(2)] for j in range(400) ] for k in range(len(a_digits))]
        b_memo = [[[-1 for i in range(2)] for j in range(400) ] for k in range(len(b_digits))]

        ans1 = dp(a_memo, a_digits, 0, 0, 1)
        ans2 = dp(b_memo, b_digits, 0, 0, 1)
        
        return (ans2 - ans1) % mod


            
