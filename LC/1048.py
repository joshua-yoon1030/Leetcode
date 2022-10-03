import collections
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        hashtable = collections.defaultdict(list)
        for word in words:
            hashtable[len(word)].append(word)
        #print(hashtable)
        
        dp = {}


        
        for i in range(1,17):
            len_i_words = hashtable[i]
            for word in len_i_words:
                if len(word) == 1:
                    dp[word] = 1
                else:
                    chain = 1
                    #print("word:", word)
                    for index in range(len(word)):
                        check = word[:index] + word[index+1:]
                        #print(check)
                        if check in dp.keys():
                            chain = max(chain, dp[check] + 1)
                    dp[word] = chain
        return max(dp.values())
                        


mySol = Solution()
print(mySol.longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(mySol.longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
