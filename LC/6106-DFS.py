import collections
class Solution(object):
    def dfs(self, n, graph, visited):
        visited.add(n)
        diff = graph[n].difference(visited)
        if diff == set():
            return
        for neighbor in diff:
            self.dfs(neighbor, graph, visited)


    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #generate graph
        graph = collections.defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start) 
        missed_edges = 0
        for i in range(n):
            visited = set()
            #run dfs on node i, updated visited
            #print("running on node ", i)
            self.dfs(i, graph, visited)
            #print("missed edges ", missed_edges)
            missed_edges += n - len(visited)
        return missed_edges //2

mySol = Solution()
print(mySol.countPairs(7,[[0,2],[0,5],[2,4],[1,6],[5,4]]))
        