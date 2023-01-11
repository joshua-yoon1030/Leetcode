#22: Generate Parentheses
#https://leetcode.com/problems/generate-parentheses/
#Strategy: Use recursion to generate all possible combinations
#Just check if its valid afterward
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dp(stack):
            if len(stack) == n * 2:
                if isvalid(stack):
                    ans.append(str.join("", stack))
            else:
                stack.append(")")
                dp(stack)
                stack.pop()
                stack.append("(")
                dp(stack)
                stack.pop()
                
                
        def isvalid(parens):
            score = 0
            for paren in parens:
                if paren == ")":
                    score -= 1
                    if score < 0:
                        return False
                if paren == "(":
                    score += 1
            return score == 0
        ans = []
        stack = []
        dp(stack)
        #print(possible)
        return ans
mySol = Solution()
print(mySol.generateParenthesis(1))
print(mySol.generateParenthesis(2))
print(mySol.generateParenthesis(3))

        