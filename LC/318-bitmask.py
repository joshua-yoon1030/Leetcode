from itertools import combinations
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = [0] * len(words)
        for i in range(len(words)):
            mask = 0
            #print(words[i])
            for letter in words[i]:
                mask |= 1<<ord(letter) - ord('a')
            masks[i] = mask
        
        maximum = 0
        for i,j in combinations(range(len(words)), 2):
            if masks[i] & masks[j] == 0:
                maximum = max(maximum, len(words[i])* len(words[j]))


        return maximum
mySol = Solution()
print(mySol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(mySol.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(mySol.maxProduct(["a","aa","aaa","aaaa"]))