#1706: Where will the ball fall
#https://leetcode.com/problems/where-will-the-ball-fall/
#Strategy: Simulate each ball going down the graph using dfs
#Runtime: O(m) for each ball (m rows in grid), O(n) for each ball, O(mn)
class Solution(object):
    
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        def dfs(grid, row,col):
            #end check
            if row >= len(grid):
                return col
            #right edge check
            if grid[row][col] == 1:
                #stuck on right wall
                if col + 1 >= len(grid[0]):
                    return -1
                #stuck in basin
                if grid[row][col + 1] == -1:
                    return -1
                return dfs(grid, row + 1, col + 1)
            #left edge check
            else:
                #stuck on left wall
                if col - 1 < 0:
                    return -1
                #stuck in basin
                if grid[row][col - 1] == 1:
                    return -1
                return dfs(grid, row + 1, col - 1)
        ans = [0] * len(grid[0])
        for i in range(len(grid[0])):
            ans[i] = dfs(grid, 0, i)
        return ans
                

        