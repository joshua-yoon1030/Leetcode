#452: Minimum Number of Arrows to Burst Balloons
#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
#Strategy: You can greedily remove points from the array, just you have to keep track of the smallest interval
#you can put the dart in for a specific group. That way, you maintain the invariant that 
#the dart can actually go through everything you remove.
#note that you can do it greedily bc you don't actually optimize anything if you get rid of
#multiple darts in one shot, for every group you will have to use 1 dart anyway. 
#eg. if you pop 2-2 or 1-3, you still require 2 darts.
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        points.sort()
    
        darts = 0
        i = 0
        while i < len(points):
            darts += 1
            end = points[i][1]
            while i + 1 < len(points):
                #need new dart check
                if points[i+1][0] > end:
                    break
                end = min(end, points[i+1][1])
                i += 1
            #move on to new group
            i += 1
        return darts


mySol = Solution()
print(mySol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))