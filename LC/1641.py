class Solution(object):
    def vowelHelper(self, n, vowels):
        if n == 1:
            return vowels
        else:
            sum = 0
            for i in range(1, vowels + 1):
                sum = sum + self.vowelHelper(n-1, i)
            return sum

    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.vowelHelper(n, 5)

