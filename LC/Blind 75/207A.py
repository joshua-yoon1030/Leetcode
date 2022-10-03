import collections
class Solution(object):
    def DFS(self, graph, node, visited):
        if visited[node] == -1:
            #-1 means that its already cleared
            return True
        elif visited[node] == 1:
            #1 means we were in the process of checking it,
            #hence cycle deteced
            return False
        #else we are visiting it right now
        visited[node] = 1
        for neighbor in graph[node]:
            if self.DFS(graph, neighbor, visited) == False:
                return False
        visited[node] = -1
        return True

        

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)

        for [start, end] in prerequisites:
            graph[start].append(end)
        #print(graph)
        
        #checking, run dfs on everything
        visited = collections.defaultdict(lambda: 0)
        for i in range(numCourses):
            #print("run dfs on ", i)
            if self.DFS(graph, i, visited) == False:
                return False
        return True

mySol = Solution()

print(mySol.canFinish(1,[[1,0],[0,1]]))
print(mySol.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))