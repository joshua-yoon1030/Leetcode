import collections
class Solution(object):
    def dp(self, alphabet,dictionary, s):
        if not s:
            return 1
        if dictionary[s] > 0:
            return dictionary[s]
        if len(s) == 1:
            return 1 if s in alphabet else 0
        else:
            sum = 0
            try1a = s[:1]
            try1b = s[1:]
            try2a = s[:2]
            try2b = s[2:]

            if try1a in alphabet:
                sum += self.dp(alphabet, dictionary, try1b)
                #sum += 1
            if try2a in alphabet:
                sum += self.dp(alphabet, dictionary, try2b)
                #sum += 1
            dictionary[s] = sum
            return sum


    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = set()
        dictionary = collections.defaultdict(lambda: -9999)
        for i in range(1,27):
            decode = str(i)
            alphabet.add(decode)
        return self.dp(alphabet, dictionary, s)

mySol = Solution()
print(mySol.numDecodings("12"))
print(mySol.numDecodings("226"))
print(mySol.numDecodings("06"))
        