from collections import defaultdict
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = defaultdict(list)
        
        letters["2"] = ["a", "b", "c"]
        letters["3"] = ["d", "e", "f"]
        letters["4"] = ["g", "h", "i"]
        letters["5"] = ["j", "k", "l"]
        letters["6"] = ["m", "n", "o"]
        letters["7"] = ["p", "q", "r", "s"]
        letters["8"] = ["t", "u", "v"]
        letters["9"] = ["w", "x", "y", "z"]

        total = []
        def addDigit(j, ans):
            build = []
            for letter in letters[digits[j]]:
                temp = [list(i) for i in ans]
                for i in temp:
                    i.append(letter)
                build = build + temp
            return build
        
        for j in range(len(digits)):
            total = addDigit(j, total)
        return total

