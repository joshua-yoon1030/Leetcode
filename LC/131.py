#131: Palindrome Partitioning
#https://leetcode.com/problems/palindrome-partitioning/
#Strategy: Just brute force it, and then check if every partition is a palindrome
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def dp(word):
            if len(word) == 1:
                return [[word]]
            
            subcase = dp(word[1:])

            newlist = []
            for case in subcase:
                together = word[0] + case[0]
                case1 = [together] + case[1:]  
                case2 = [word[0]] + case
                newlist.append(case1)
                newlist.append(case2)
            return newlist
        possible = dp(s)
        ans = []

        def ispalindrome(word):
            for partition in word:
                if partition != partition[::-1]:
                    return False
            return True
        for access in possible:
            if ispalindrome(access):
                ans.append(access)
            
        return ans

word = input()
mySol = Solution()
mySol.partition(word)
        