from collections import defaultdict
#longest substring without repeating characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#My strategy: Use a two pointer approach, where the two pointers represent
#the start and end of our window
#We have a dictionary that stores the last seen index of that letter
#And if we meet all the conditions, we add the next letter in
#if we encounter a character we have already seen, we need to reduce our window until that point.
#runtime: O(n) because we do two passes through the array in the worst case.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        letters = defaultdict(lambda: -1)
        start = 0
        end = 0
        longest = 0
        while end < len(s):
            letter = s[end]
            #print(start, end)
            #print(letters.keys())
            if letters[letter] != -1:
                i = start
                while i <= letters[letter]:
                    letters.pop(s[i])
                    start += 1
                    i += 1
                    
            else:  
                letters[letter] = end
                end += 1
                longest = max(longest, end - start)
        return longest

        """
        :type s: str
        :rtype: int
        """
mySol = Solution()
print(mySol.lengthOfLongestSubstring("pwwkew"))
        