#424. Longest Repeating Character Replacement
#https://leetcode.com/problems/longest-repeating-character-replacement/
#my strategy: start with an increasing window, only increasing it for the same letter
#if the letter changes, mark that index in a queue and use one of the "k" as leeway
#if we run out of k to use, restart from one of the other indexes in our queue
#stop if we reach the end
#why this doesn't work: we miss the cases where we can release letters from the end
#eg. fails ABBBA
class Solution(object):
    def checkside(self, s, k):
        changes = []
        match = s[0]
        prev = s[0]
        start = 0
        end = 1
        count = k
        longest = 0
        while(end < len(s)):
            #queue appends first
            if s[end] != prev:
                changes.append(end)
            prev = s[end]

            if s[end] != match and count == 0:
                #worst case, we gotta reset everything
                count = k
                start = changes.pop(0)
                end = start
                match = s[start]
                pass
            elif s[end] != match:
                #we use up one of our "k"s
                count -= 1
            longest = max(longest, end - start+1)
            end += 1
        return longest
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return max(self.checkside(s,k), self.checkside(s[::-1], k))


        
        