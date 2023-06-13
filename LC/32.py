from collections import deque
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dictionary in the form of (i, l),
        #indicating there is a valid paren seq ending at index i with length l
        valid = dict()
        stack = deque()

        for i in range(len(s)):
            if s == "(":
                stack.appendleft(i)
            elif len(stack) > 0:
                left = stack.popleft()
                dist = i - left
                if left-1 in valid:
                    dist += valid[left-1]
                valid[i] = dist
        return max(valid.values())


        