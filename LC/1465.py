class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        mod = 1000000007
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        
        last = 0
        maxH = 0
        for horiz in horizontalCuts:
            if (horiz - last > maxH):
                maxH = horiz-last
            last = horiz
        last = 0
        maxV = 0
        for vert in verticalCuts:
            if(vert - last > maxV):
                maxV = vert-last
            last = vert
        return (maxH * maxV) % mod