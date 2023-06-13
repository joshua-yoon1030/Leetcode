from collections import deque
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {c: i for i, c in enumerate(s)}
        stack = deque()
        for i in range(len(s)):
            while len(stack) > 0 and stack[-1] > s[i] and i < last[stack[-1]]:
                stack.pop()
            stack.append(s[i])
        return stack
        