import collections
class Solution(object):
    def DFS (self, graph, node, visited, ocean):
        if node in visited:
            return
        ocean.add(node)
        visited.add(node)
        for nbh in graph[node]:
            self.DFS(graph, nbh, visited, ocean)

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(list)
        """
        setup graph:
        our setup is as follows:
        an adj list where (m,n) -> [list of neighbors for coord (m,n)]
        edges will be directed edges from coor a -> b, where height(a) <= height(b).
        note: that means if height(a) == height(b), the edge will be undirected.
        """
        #doing the left right coords graph setup
        for i in range(0, len(heights)):
            for j in range(1, len(heights[i])):
                #(row, col) == (i,j)
                left = heights[i][j]
                right = heights[i][j-1]
                if left >= right:
                    graph[(i,j-1)].append((i, j))
                if right >= left:
                    graph[(i,j)].append((i,j-1))
                    

        #doing top down coords graph setup
        for j in range(0, len(heights[0])):
            for i in range(1, len(heights)):
                #(row, col) == (i,j)
                up = heights[i][j]
                down = heights[i-1][j]
                if up >= down:
                    graph[(i-1,j)].append((i, j))
                if down >= up:
    
                    graph[(i,j)].append((i-1,j))
        #return graph
        #we run dfs on each atlantic side and pacific side to see what square can reach
        atlantic = set()
        pacific = set()
        
        visitedP = set()
        visitedA = set()
        #pacfic side, then atlantic side for each loop
        for i in range(len(heights)):
            self.DFS(graph, (i,0), visitedP, pacific)
            self.DFS(graph, (i, len(heights[i])-1), visitedA, atlantic)
        for i in range(len(heights[0])):
            self.DFS(graph, (0,i), visitedP, pacific)
            self.DFS(graph, (len(heights)-1, i), visitedA, atlantic)
        

        both = visitedA.intersection(visitedP)
        return list(both)
        


mySol = Solution()
print(mySol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
#print(mySol.pacificAtlantic([[2,1],[1,2]]))
        
        
        