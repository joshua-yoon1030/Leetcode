from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        self.found = -1
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            graph[a].append((b, val))
            graph[b].append((a,  1.0 / val))
        
        def dfs(node, product, visited, target):
            if node in visited:
                return
            if node == target:
                self.found = product
                return
            
            visited.add(node)

            for neighbor, weight in graph[node]:
                dfs(neighbor, product * weight, visited, target)
        
        ans = []
        for start, end in queries:
            self.found = -1
            if start not in graph or end not in graph:
                ans.append(-1)
                continue
            dfs(start, 1.0, set(), end)
            ans.append(self.found)
        return ans

