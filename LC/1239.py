#1239: Maximum Length of a Concat String with Unique Chars
#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
#My strategy: Use a set to keep track of what letters you used
#The max length is only 16 words, so you can recursively check every answer.
#make sure to deep copy all the bitmask sets.
class Solution(object):
    def dp(self, arr, letters):
        if len(arr) == 0:
            return len(letters)
        
        word = arr[0]
        if len(set(word)) != len(list(word)):
            return self.dp(arr[1:], letters)
        
        dontselect = self.dp(arr[1:], letters)

        wordmask = set(word)
        newletters = set()
        for i in letters:
            newletters.add(i)
        for letter in word:
            if letter in letters:
                return dontselect
            else:
                newletters.add(letter)
        return max(dontselect, self.dp(arr[1:], newletters))
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        letters = set()
        return self.dp(arr, letters)
        