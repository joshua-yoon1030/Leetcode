import collections
class Solution(object):
    def inRange(self, n, row, col, grid):
        return 0 <= row and row <= n-1 and 0 <= col and col <= n-1 and grid[row][col] == 0
    def isValid(self, grid, row, col, n, time):
        #disgusting check of 8 directions smh so long
        valid = list()
        if self.inRange(n, row + 1, col + 0, grid):
            valid.append((row + 1, col + 0, time))

        if self.inRange(n, row + 1, col + 1, grid):
            valid.append((row + 1, col + 1, time))

        if self.inRange(n, row + 0, col + 1, grid):
            valid.append((row + 0, col + 1, time))

        if self.inRange(n, row - 1, col + 1, grid):
            valid.append((row - 1, col + 1, time))

        if self.inRange(n, row - 1, col + 0, grid):
            valid.append((row - 1, col + 0, time))

        if self.inRange(n, row - 1, col - 1, grid):
            valid.append((row - 1, col - 1, time))

        if self.inRange(n, row + 0, col - 1, grid):
            valid.append((row + 0, col - 1, time))

        if self.inRange(n, row + 1, col - 1, grid):
            valid.append((row + 1, col - 1, time))
        return valid

    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #run bfs, some initial setup
        #the format for queue elemns: (row, col, dist)
        # start in top left corner at time 1
        if(grid[0][0] == 1): return -1
        queue = collections.deque([(0,0,1)])
        visited = set()
        n = len(grid)

        while queue:
            row, col, time = queue.popleft()
            #add all valid coords onto queue
            
            if((row, col) not in visited):
                visited.add((row, col))
                #print("travelled: ", row, col)
                if (row == n-1 and col == n-1):
                    return time
                #returns a list of neighbors
                neighbors = self.isValid(grid, row, col, n, time+1)
                for neighbor in neighbors:
                    queue.append(neighbor)
        return -1
mysol = Solution()
print(mysol.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))


