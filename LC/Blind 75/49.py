#49. Group Anagrams:
#https://leetcode.com/problems/group-anagrams/
#My Strategy: Build your list of anagrams as you go
#The anagrams will be all the same if you sort them
#so have the key of your dictionary be the sorted word
# and the entry be the actual word
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        wordDict = collections.defaultdict(list)
        for word in strs:
            sortW = "".join(sorted(word))
            wordDict[sortW].append(word)
        return wordDict.values()

        