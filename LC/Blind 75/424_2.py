#424. Longest Repeating Character Replacement
#https://leetcode.com/problems/longest-repeating-character-replacement/
#My strategy: In our window, we keep track of what the most frequent letter is
#for the window to be valid, the rest of the letters has to be <= k
#if this is true, we add the next letter and go again
#if all of a sudden, the window becomes invalid, we decrease the window and go again
#runtime: O(n). At every iteration, we do constant operations, 
# and our two pointers run max once through the array
from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        letters = defaultdict(int)
        start = 0
        end = 0
        longest = 0
        while end < len(s):
            #add a letter in
            letters[s[end]] += 1
            end += 1
            maxLetter = max(letters.values())
            
            #make sure window is valid
            while end - start - maxLetter <= k:
                letters[s[start]] -= 1
                start += 1
                maxLetter = max(letters.values())
            longest = max(longest, end - start)
        return longest   

        