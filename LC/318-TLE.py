class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        biggest = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                #compare words[i] and words[j]
                first = list(words[i])
                second = list(words[j])
                if len(set(first).intersection(set(second))) == 0:
                    if biggest < len(first) * len(second):
                        biggest = len(first) * len(second)
        return biggest
mySol = Solution()
print(mySol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(mySol.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(mySol.maxProduct([["a","aa","aaa","aaaa"]]))
        