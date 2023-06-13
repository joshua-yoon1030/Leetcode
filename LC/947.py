from collections import defaultdict
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
        graph = defaultdict(list)

        for (x1, y1) in stones:
            for (x2, y2) in stones:
                if x1 == x2 and y1 != y2:
                    graph[(x1, y1)].append((x2, y2))
                elif y1 == y2 and x1 != x2:
                    graph[(x1, y1)].append((x2, y2))
                
        
        def dfs(x,y):
            if (x,y) in visited:
                return

            visited.add((x,y)) 
            for (x2, y2) in graph[(x, y)]:
                dfs(x2, y2)
        
        visited = set()
        components = 0
        for (x, y) in stones:
            if (x,y) not in visited:
                components += 1
                dfs(x, y)
        return len(stones) - components