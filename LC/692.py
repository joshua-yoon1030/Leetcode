#692
#https://leetcode.com/problems/top-k-frequent-words/
#My Strategy:put everything into a dictionary and then take them out one by one
#runtime: O(nk) where n is the words and k is the kth frequent words
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        worddict = defaultdict(int)
        for word in words:
            worddict[word] += 1
        ans = []
        maxkey = ""
        maxval = 0
        for i in range(k):
            maxkey = ""
            maxval = 0
            for key, val in worddict.items():
                if val > maxval:
                    maxkey = key
                    maxval = val
                elif val == maxval:
                    maxkey = min(maxkey, key)
            ans.append(maxkey)
            worddict[maxkey] = 0
        return ans