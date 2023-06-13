from collections import defaultdict
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        graph = defaultdict(list)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row > 0:
                    graph[(row, col)].append((row-1, col))
                if row < len(grid) - 1:
                    graph[(row, col)].append((row + 1, col))
                if col > 0:
                    graph[(row, col)].append((row, col - 1))
                if col < len(grid[0]) - 1:
                    graph[(row, col)].append((row, col + 1))
        
        
        def dfs(row, col, visited):
            if (row, col) in visited or grid[row][col] == "0":
                return
            
            visited.add((row, col))

            for nr, nc in graph[(row, col)]:
                dfs(nr, nc, visited)
        

        visited = set()
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    dfs(row, col, visited)
        return islands
                           


            
        