#76: Minimum Window Substring:
#https://leetcode.com/problems/minimum-window-substring/
#My strategy: Setup, we have two dictionaries, a dictionary of the target word and current window
#We then apply a two pointer approach: If the condition is not satisfied add to the window
#If the condition is satisfied, remove from the window to get the minimum
#Runtime: O(n) for two pointer approach
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tdict = defaultdict(int)
        for letter in t:
            tdict[letter] += 1
        
        #checks to see if every char is included
        def checker(tdict, sdict):
            for (key, value) in tdict.items():
                if sdict[key] < value:
                    return False
            return True

        minlen = len(s)
        minstr = ""

        left = 0
        right = 0
        sdict = defaultdict(int)
        while(right < len(s)):
            #print("s: ", s[left : right])
            if not checker(tdict, sdict):
                sdict[s[right]] += 1
                right += 1
            
            
            while(checker(tdict, sdict)):
                if (right - left) <= minlen:
                    minlen = right - left
                    minstr = s[left: right]
                #minlen = min(right - left, minlen)
                #print("s: ", s[left : right])
                sdict[s[left]] -= 1
                left += 1
        return minstr