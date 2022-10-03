class Solution(object):
    def dfs(self, grid, x,y , visited):
        if visited[x][y] == 1 or grid[x][y] == "0":
            return
        
        #mark current node as visited
        visited[x][y] = 1

        #up
        self.dfs(grid, max(0, x-1), y, visited)

        #down
        self.dfs(grid, min(x+1, len(grid) - 1), y, visited)

        #left
        self.dfs(grid, x, max(0, y-1), visited)

        #right
        self.dfs(grid, x, min(y+1, len(grid[0]) - 1), visited)


        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        #a graph of which nodes we have visited:
        #key: 0 -> unvisited
        #   : 1 -> visited

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #i, j == row, col
                #we want to see if the node we are on is part of an unvisited island
                #if it is, we add it to our island count
                #we then run dfs on it and mark the rest of the island as visited
                #print(visited[i][j], grid[i][j])
                if visited[i][j] == 0 and grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j, visited)
        return islands
mySol = Solution()
print(mySol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

        