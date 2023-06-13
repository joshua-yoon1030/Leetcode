import heapq
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        sd = [[float('inf') for i in range(len(grid[0]))] for j in range(len(grid))]

        def dijkstras(row, col):
            visited = set()
            pqueue = []

            heapq.heappush(pqueue, (0, row, col))

            while pqueue:
                (dist, row, col) = heapq.heappop(pqueue)
                sd[row][col] = min(sd[row][col], dist)

                if (row, col) in visited:
                    continue

                visited.add((row, col))

                if row > 0 and grid[row - 1][col] == 1:
                    heapq.heappush(pqueue, (dist + 1, row - 1, col))
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    heapq.heappush(pqueue, (dist + 1, row - 1, col))
                if col > 0 and grid[row][col - 1] == 1:
                    heapq.heappush(pqueue, (dist + 1, row, col - 1))
                if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                    heapq.heappush(pqueue, (dist + 1, row, col + 1))
        
        for i in len(grid):
            for j in len(grid):
                if grid[i][j] == 2:
                    dijkstras(i, j)
        
        ans = -1
        for i in len(sd):
            for j in len(sd):
                if grid[i][j] == 1:
                    ans = max(ans, sd[i][j])
        if ans == float('inf'):
            return -1
        return ans


