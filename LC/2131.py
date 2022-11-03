#2131: Longest Palindrome by Concating Two letter words
#https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
#Strategy: This seems like a dp problem or smth but it's actually a counting problem
#The words.length  <= 10^5 is a good hint
#for a given word it's either a palindrome or it's going to have a counterpart to match
#Just like twosum 
from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        worddict = defaultdict(int)
        count = 0
        for word in words:
                worddict[word] += 1
        for word in words:
            rev = word[::-1]
            if word == rev:
                #palindrome case
                if worddict[word] > 1:
                    count += 2
                    worddict[word] -= 2
            elif worddict[rev] > 0 and worddict[word] > 0:
                #regular twosum case
                worddict[word] -=1
                worddict[rev] -=1
                count += 2
        #in the end, if we have a natural palindrome, we can put it in the middle
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        for letter in alphabet:
            letter = letter + letter
            if worddict[letter] > 0:
                return count * 2 + 2
        return count * 2
                
        