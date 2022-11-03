#5: Longest Palindromic Substring
#https://leetcode.com/problems/longest-palindromic-substring/
#My strat: Just brute force it
#if you start with an arbitrary character, you can check "build" a palindromic string by going in to out
#eg. aba -> xabax -> yxabaxy, stop if you reach end/it's bad
#remember there are two cases: aba or abba, plan accordingly.
#O(n^2 sol)
class Solution(object):
    def checkpalindrome(self, s, start, end):
        #palindrome is s[start:end]
        while end < len(s) and start > 0:
            if s[end] == s[start-1]:
                end += 1
                start -= 1
            else:
                break
        return (end- start, s[start: end])
            
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxl = 0
        maxpali = ""
        for i in range(len(s)):
            (contender, palindrome) = self.checkpalindrome(s, i, i+1)
            if maxl < contender:
                maxpali = palindrome
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                (contender, palindrome) = self.checkpalindrome(s, i, i+2)
            if maxl < contender:
                maxpali = palindrome
        return maxpali
            


        