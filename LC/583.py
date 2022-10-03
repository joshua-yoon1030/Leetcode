# import collections
# class Solution(object):
#     def dp(self, word1, word2, wordDict):
#         if(word1 == word2):
#             print(wordDict)
#             return 0
#         elif len(word1) == 0:
#             return len(word2)
#         elif(len(word2) == 0):
#             return len(word1)
#         elif(wordDict[(word1, word2)] < 9999999):
#             return wordDict[(word1, word2)]
#         else:
#             moves = 9999999
#             for i in range(len(word1)):
#                 new_word = word1[:i] + word1[i+1:]
#                 moves = min(self.dp(new_word, word2, wordDict), moves)
#             for i in range(len(word2)):
#                 new_word = word2[:i] + word2[i+1:]
#                 moves = min(self.dp(word1, new_word, wordDict), moves)
#             wordDict[(word1, word2)] = moves + 1
#             return moves + 1
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         wordDict = collections.defaultdict(lambda: 9999999999)
#         return self.dp(word1, word2, wordDict)
# mySol = Solution()
# print(mySol.minDistance("sea", "eat"))
# #print(mySol.minDistance("leetcode", "etco"))
# #print(mySol.minDistance("prosperity", "properties"))

print(set("hello"))