class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        return self.merge(intervals)
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i = len(intervals) - 1
        while i > 0:
            [s1, e1] = intervals[i-1]
            [s2, e2] = intervals[i]
            if e1 >= s2:
                intervals.remove([s1, e1])
                intervals.remove([s2, e2])
                intervals.insert(i-1, [s1,max(e2, e1)])
                i += 1
            i -= 1

        return intervals
mySol = Solution()
print(mySol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))


