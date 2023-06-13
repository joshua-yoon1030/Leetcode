class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = [0] * len(graph)

        visited = set()
        def dfs(node, parity):
            #here, parity is defined by the color before it.
            #-1 = red, 1 = blue, 0 = undefined (not colored)
            if node in visited:
                if color[node] == parity:
                    return False
                return True
            
            color[node] = -parity
            visited.add(node)

            ans = True
            for neighbor in graph[node]:
                ans = ans and dfs(neighbor, -parity)
            return ans
        
        for i in range(len(graph)):
            if color[i] == 0:
                if(not dfs(i, -1)):
                    return False
        return True
            

            
        