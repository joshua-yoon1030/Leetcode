from collections import defaultdict
import math
class Solution:
    
    def maximumDetonation(self, bombs) -> int:

        def blowsUp(x1, y1, x2, y2, r):
            #determines if blowing up bomb 1 with radius r will also ignite bomb 2.
            return r >= math.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) **2)

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and blowsUp(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1], bombs[i][2]):
                    graph[i].append(j)
        
        self.visited = set()
        maxbombs = 0
        def dfs(node):
            if node in self.visited:
                return
            
            self.visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)
        
        for i in range(len(bombs)):
            self.visited = set()
            dfs(i)
            maxbombs = max(maxbombs, len(self.visited))
        return maxbombs
                    
    
    
