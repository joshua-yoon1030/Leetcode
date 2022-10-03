import collections
class Solution(object):
    def DFS(self, graph, node, visited, stack):
        if node in visited:
            #cycle encountered
            #print("cycle deteced")
            if node in stack:
                return False
        stack.append(node)
        visited.add(node)
        for neighbor in graph[node]:
            if self.DFS(graph, neighbor, visited, stack) == False:
                return False
        stack.pop()
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
        visited = set()
        for i in range(numCourses):
            #print("run dfs on ", i)
            if self.DFS(graph, i, visited, []) == False:
                return False
        return True

mySol = Solution()

#print(mySol.canFinish(1,[[1,0],[0,1]]))
#print(mySol.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))