class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        fn = lambda x: x[1]
        intervals.sort(key = fn)
        #print(intervals)

        counter = 0
        max_end = 0
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start >= max_end:
                counter += 1
                max_end = end
        return len(intervals) - counter

mySol = Solution()
print(mySol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))