#1328: Break a palindrome
#https://leetcode.com/problems/break-a-palindrome/
#My strategy: Just search the first half of the string until you get something that isn't an "a"
#If the string was all As, turn the last character to a B
#Also in the case we can't break the palindrome, just return empty string(only len(0,1))
#runtime: O(n) where n is the length of the string
class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) < 2:
            return ""
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b"
        