from collections import defaultdict
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern = list(pattern)
        s = s.split(" ")
        patterndict = defaultdict(lambda x: "")
        
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if pattern[i] in patterndict:
                if patterndict[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in patterndict.values():
                    return False
                patterndict[pattern[i]] = s[i]
        return True


