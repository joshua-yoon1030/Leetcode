class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        flag = False
        while not flag:
            flag = True
            for i in range(len(intervals)-1, 0, -1):
                [s1, e1] = intervals[i]
                [s2, e2] = intervals[i-1]
                if e2 >= s1:
                    intervals.remove([s1, e1])
                    intervals.remove([s2, e2])
                    intervals.insert(i-1, [s2,max(e2, e1)])
                    flag = False

        return intervals
mySol = Solution()
print(mySol.merge([[8,10],[15,18],[1,3],[2,6]]))
print(mySol.merge([[1,4],[2,3]]))