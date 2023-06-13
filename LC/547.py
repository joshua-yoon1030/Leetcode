class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        def dfs(vertex, visited):
            if vertex in visited:
                return
            visited.add(vertex)

            for i in range(len(isConnected[vertex])):
                if isConnected[vertex][i] == 1:
                    dfs(i, visited)
        
        visited = set()
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i, visited)
        return provinces
            

