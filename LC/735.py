from collections import deque
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        right = deque()
        left = deque()

        free = []

        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                #positive case, moving right
                right.appendleft(asteroids[i])
            else:
                left.appendleft(asteroids[i])

            #collision check
            while len(right) > 0 and len(left) > 0:
                rightA = right.popleft()
                leftA = left.popleft()
                if rightA > -leftA:
                    #right side wins
                    right.appendleft(rightA)
                elif -leftA > rightA:
                    #left side wins
                    left.appendleft(leftA)
            if len(right) == 0 and len(left) > 0:
                #left moving asteroids shouldn't be affected anymore
                free.append(leftA)
        
        right.reverse()
        return free + list(right)