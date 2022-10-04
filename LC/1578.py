#1578 Minimum Time to Make Rope Colorful
#https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
#My strategy: Have a two pointer approach
#For every group of two balloons of the same color, we have to delete one of them
#repeat until done
from collections import defaultdict
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        sum = 0
        i = 0
        j = 1
        while(j < len(colors)):
            if colors[i] == colors[j]:
                if neededTime[i] > neededTime[j]:
                    #second balloon is faster
                    sum += neededTime[j]
                    j += 1
                else:
                    sum += neededTime[i]
                    j+= 1
                    i = j-1
            else:
                j += 1
                i = j -1

        return sum
        