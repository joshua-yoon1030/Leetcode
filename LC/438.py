from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        sdict = defaultdict(lambda: 0)
        pdict = defaultdict(lambda: 0)

        if len(p) > len(s):
            return []
        
        for i in range(len(p)):
            sdict[s[i]] += 1
            pdict[p[i]] += 1

        left = 0
        right = len(p)
        ans = []
        while right < len(s):
            if sdict == pdict:
                ans.append(left)
            sdict[s[left]] -= 1
            left += 1
            right += 1
            sdict[s[right]] += 1
        return ans
    

