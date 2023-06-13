from collections import deque
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = deque()
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[0][0]:
                bad = stack.popleft()
                temperatures[bad[1]] = i - bad[1]
            stack.appendleft([temperatures[i], i])
        return ans

