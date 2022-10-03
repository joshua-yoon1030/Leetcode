class Solution(object):
    def wb(self, s, wordDict, dp):
        if not s:
            return True
        if s in dp:
            return dp[s]

        possible = False
        for word in wordDict:
            if word in s:
                k = s.replace(word, "@", 1)
                splits = k.split("@")
                #print(splits)
                possible = possible or (self.wb(splits[0], wordDict, dp) and self.wb(splits[1], wordDict, dp))
        dp[s] = possible 
        return possible
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = dict()
        return self.wb(s, wordDict, dp)

mySol = Solution()
#k = "leetcode"
#k = k.replace("leet","@",1 )
#print(k)
#print(mySol.wordBreak("leetcode", ["leet", "code"]))
#print(mySol.wordBreak("applepenapple", ["apple", "pen"])) 
#print(mySol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(mySol.wordBreak("a", ["b"]))
            


