class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mincost = [0] * len(cost)

        mincost[0] = cost[0]
        mincost[1] = cost[1]

        for i in range(2, len(cost)):
            mincost[i] = cost[i] + min(mincost[i-1], mincost[i-2])
        return min(mincost[-1], mincost[-2])
mySol = Solution()
print(mySol.minCostClimbingStairs([10,15,20]))
print(mySol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))